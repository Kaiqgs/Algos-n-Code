using Plugin.BLE;
using Plugin.BLE.Abstractions.Contracts;
using Plugin.BLE.Abstractions.EventArgs;
using Plugin.BLE.Abstractions.Exceptions;
using SmartLock.Models;
using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;

namespace SmartLock.Services
{
    public class DoorConnection : IDoorConnection
    {
        private Guid deviceid = new Guid("00000000-0000-0000-0000-587a62143d30");
        private Guid charid = new Guid("0000ffe1-0000-1000-8000-00805f9b34fb");
        private Guid servid = new Guid("0000ffe0-0000-1000-8000-00805f9b34fb");

        private IDoorProtocol<ProtocolType> WaitingProtocol;
        private IDevice ConnectedDevice;
        private IService ConnectedService;
        private ICharacteristic ConnectedCharacteristic;

        public bool IsConnected { get; set; }
        public bool CanConnect { get => CrossBluetoothLE.Current != null && CrossBluetoothLE.Current.IsOn; }
        public async Task<bool> AttemptSignInAsync(SignIn signIn)
        {
            if (!IsConnected) return false;
            var EmailProt = await SendProtocol(new DoorProtocol(ProtocolType.SignInEmail, signIn.Email));
            var PasswordProt = await SendProtocol(new DoorProtocol(ProtocolType.SignInPassword, signIn.Password));
            return EmailProt.ID == ProtocolType.Acknowledge && PasswordProt.ID == ProtocolType.Acknowledge;
        }

        public async Task<bool> AttemptSignUpAsync(SignUp signUp)
        {
            if (!IsConnected) return false;
            var EmailProt = await SendProtocol(new DoorProtocol(ProtocolType.SignUpEmail, signUp.Email));
            var PasswordProt = await SendProtocol(new DoorProtocol(ProtocolType.SignUpPassword, signUp.Password));
            return EmailProt.QuerySuccess && PasswordProt.QuerySuccess;
        }

        public async Task ConnectAsync()
        {
            var ble = CrossBluetoothLE.Current;
            var adapter = CrossBluetoothLE.Current.Adapter;
            
            ConnectedDevice = await adapter.ConnectToKnownDeviceAsync(deviceid);
            ConnectedService = await ConnectedDevice.GetServiceAsync(servid);
            ConnectedCharacteristic = await ConnectedService.GetCharacteristicAsync(charid);
            ConnectedCharacteristic.ValueUpdated += OnConnectedValueUpdate;
            IsConnected = true;
        }

        public Task DisconnectAsync()
        {
            return new Task(() =>
            {
                ConnectedCharacteristic.ValueUpdated -= OnConnectedValueUpdate;
                ConnectedService.Dispose();
                ConnectedDevice.Dispose();
                IsConnected = false;
            });
        }

        public async Task<Status> GetStatusAsync()
        {
            var protocol = await SendProtocol(new DoorProtocol(ProtocolType.State));
            Status status = new Status(DoorState.Unknown);
            if (protocol.ID == ProtocolType.Lock) status.State = DoorState.Locked;
            else if (protocol.ID == ProtocolType.Unlock) status.State = DoorState.Unlocked;
            return status;
        }

        public async Task<bool> SetStatusAsync(Status status)
        {

            var protocol = new DoorProtocol(ProtocolType.Unknown);
            if (status.State == DoorState.Locked) protocol.ID = ProtocolType.Lock;
            else if (status.State == DoorState.Unlocked) protocol.ID = ProtocolType.Unlock;

            var answer = await SendProtocol(protocol);

            return answer.ID == ProtocolType.Acknowledge;            
        }

    
        private async Task<IDoorProtocol<ProtocolType>> SendProtocol(IDoorProtocol<ProtocolType> protocol)
        {
            if (!IsConnected) return null;
            WaitingProtocol = null;
            await ConnectedCharacteristic.StartUpdatesAsync();
            await ConnectedCharacteristic.WriteAsync(protocol.BytesProtocol);
            
            while(WaitingProtocol == null)
                await Task.Delay(25);

            return WaitingProtocol;
        }

        private void OnConnectedValueUpdate(object sender, CharacteristicUpdatedEventArgs e)
        {
            Console.WriteLine($"BLE:{e.Characteristic.StringValue}");
            WaitingProtocol = new DoorProtocol().ParseProtocol(e.Characteristic.StringValue);
        }

        
    }
}

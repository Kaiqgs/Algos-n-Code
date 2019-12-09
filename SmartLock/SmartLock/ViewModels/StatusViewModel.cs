using SmartLock.Models;
using SmartLock.Services;
using System;
using Xamarin.Forms;

namespace SmartLock.ViewModels
{
    public class StatusViewModel : BaseViewModel
    {


        public string StateString { get => DoorLanguageResources.Instance.TranslateState(Status.State); }

        public string IconCode { get => Status.State == DoorState.Unlocked ? char.ConvertFromUtf32(0x1F513) : char.ConvertFromUtf32(0x1F510); }
        public Command ToggleDoorCommand { get; set; }

        private Status status;
        private Status Status
        {
            get { return status; }
            set
            {
                SetProperty(ref status, value);
                OnPropertyChanged(nameof(StateString));
                OnPropertyChanged(nameof(IconCode));
            }
        }

        public StatusViewModel()
        {
            ToggleDoorCommand = new Command(ToggleDoor, () => !IsBusy);
            Status = new Status(DoorState.Unknown);
            GetStatus();
            IsBusy = false;
        }


        private async void GetStatus()
        {

            Console.WriteLine("Getting door status");
            var doorconn = new DoorConnection();
            IsBusy = true;
            var res = await new DoorPermissions().RequestMissingPermissions();
            if (!res) await DoorLanguageResources.Instance.NeedLocationMessage();
            if (!doorconn.CanConnect) await DoorLanguageResources.Instance.NeedBluetoothMessage();
            if (!res || !doorconn.CanConnect) { IsBusy = false; return; }
            try { await doorconn.ConnectAsync(); }
            catch { IsBusy = false; return; }
            Status = await doorconn.GetStatusAsync();
            IsBusy = false;
        }

        public async void ToggleDoor()
        {
            Console.WriteLine("Toggling door");
            var doorconn = new DoorConnection();
            IsBusy = true;
            var res = await new DoorPermissions().RequestMissingPermissions();
            if (!res) await DoorLanguageResources.Instance.NeedLocationMessage();
            if (!doorconn.CanConnect) await DoorLanguageResources.Instance.NeedBluetoothMessage();
            if (!res || !doorconn.CanConnect) { IsBusy = false; return; }
            try { await doorconn.ConnectAsync(); }
            catch { IsBusy = false; return; }

            var result = await doorconn.SetStatusAsync(Status.Toggle());
            if (!result) Status = await doorconn.GetStatusAsync();
            else Status = Status.Toggle();
            IsBusy = false;
        }


    }
}

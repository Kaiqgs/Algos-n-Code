using Plugin.BLE;
using Plugin.BLE.Abstractions.Contracts;
using Plugin.BLE.Abstractions.Exceptions;
using Plugin.Permissions;
using Plugin.Permissions.Abstractions;
using SmartLock.Models;
using SmartLock.Services;
using SmartLock.Views;
using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;

namespace SmartLock.ViewModels
{
    public class LoginViewModel : BaseViewModel
    {
        public Command SignInCommand { get; set; }
        public Command SignUpCommand { get; set; }
        public string Email { get; set; }
        public string Password { get; set; }
        public LoginViewModel()
        {
            SignInCommand = new Command(SignIn, () => !IsBusy);
            SignUpCommand = new Command(SignUp, () => !IsBusy);
        }


        private void OpenMainPage()
        {
            Application.Current.MainPage = new MainPage();
        }


        private async Task<DoorConnection> ValidatePermissionsEntryAndConnect()
        {
            var dc = new DoorConnection();
            var emptyentry = string.IsNullOrEmpty(Email) || string.IsNullOrEmpty(Password);
            var res = await new DoorPermissions().RequestMissingPermissions();

            if (emptyentry)
            {
                await DoorLanguageResources.Instance.InvalidCredentialsMessage();
                return null;
            }
            if (!res)
            {
                await DoorLanguageResources.Instance.NeedLocationMessage();
                return null;
            }

            if (!dc.CanConnect)
            {
                await DoorLanguageResources.Instance.NeedBluetoothMessage();
                return null;
            }

            try
            {
                await dc.ConnectAsync();
            }
            catch (DeviceConnectionException dce)
            {
                Console.WriteLine(dce.ToString());
                await DoorLanguageResources.Instance.DoorNotFoundMessage();
                return null;
            }

            return dc;
        }


        private async void SignIn()
        {
            IsBusy = true;
            var dc = await ValidatePermissionsEntryAndConnect();
            if (dc == null) { IsBusy = false; return; }
            var res = await dc.AttemptSignInAsync(new SignIn(Email, Password));
            IsBusy = false;
            if (res) OpenMainPage();
            else await DoorLanguageResources.Instance.InvalidCredentialsMessage();
        }

        private async void SignUp()
        {
            IsBusy = true;
            var dc = await ValidatePermissionsEntryAndConnect();
            if (dc == null) { IsBusy = false; return; }
            var res = await dc.AttemptSignUpAsync(new SignUp(Email, Password));
            IsBusy = false;
            if (res) OpenMainPage();
            else await DoorLanguageResources.Instance.CredentialsAlreadyCreatedMessage();
        }


    }
}

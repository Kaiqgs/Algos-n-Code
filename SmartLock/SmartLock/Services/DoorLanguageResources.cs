using SmartLock.Models;
using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using Xamarin.Forms;

namespace SmartLock.Services
{
    public sealed class DoorLanguageResources
    {
        private static DoorLanguageResources instance = null;
        private static readonly object padlock = new object();


        public static DoorLanguageResources Instance
        {
            get
            {
                lock (padlock)
                {
                    if (instance == null)
                    {
                        instance = new DoorLanguageResources();
                    }
                    return instance;
                }
            }
        }

        public async Task NeedLocationMessage()
        {
            await Application.Current.MainPage.DisplayAlert("Localização", "Esse aplicativo precisa de acesso à localização", "Ok");
        }

        public async Task NeedBluetoothMessage()
        {
            await Application.Current.MainPage.DisplayAlert("Bluetooth", "Por favor ligue o Bluetooth para continuar", "Ok");
        }

        public async Task DoorNotFoundMessage()
        {
            await Application.Current.MainPage.DisplayAlert("Bluetooth", "O dispositivo da sua porta smart não foi encontrado!", "Ok");
        }

        public async Task InvalidCredentialsMessage()
        {
            await Application.Current.MainPage.DisplayAlert("Credenciais", "As credenciais providenciadas são invalidas.", "Ok");
        }

        public async Task CredentialsAlreadyCreatedMessage()
        {
            await Application.Current.MainPage.DisplayAlert("Credenciais", "As credenciais para essa porta já foram disponibilizadas.", "Ok");
        }


        public string TranslateState(DoorState doorState)
        {
            if (doorState == DoorState.Locked) return "Fechado";
            else if (doorState == DoorState.Unlocked) return "Aberto";
            return "Desconhecido";
        }


    }
}

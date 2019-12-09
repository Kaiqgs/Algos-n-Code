using System;
using System.Collections.Generic;
using System.Text;
using Xamarin.Essentials;
using Xamarin.Forms;

namespace SmartLock.ViewModels
{
    class AboutViewModel : BaseViewModel
    {
        public Command OpenWebCommand { get; set; }


        public AboutViewModel()
        {
            OpenWebCommand = new Command(async () => await Launcher.OpenAsync(new Uri("https://github.com/Kaiqgs")));
        }
    }
}

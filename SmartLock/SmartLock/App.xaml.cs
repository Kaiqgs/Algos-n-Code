using System;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;
using SmartLock.Services;
using SmartLock.Views;

namespace SmartLock
{
    public partial class App : Application
    {

        public App()
        {
            InitializeComponent();

            MainPage = new LoginPage();
            //MainPage = new StatusPage();
        }

        protected override void OnStart()
        {
        }

        protected override void OnSleep()
        {
        }

        protected override void OnResume()
        {
        }
    }
}

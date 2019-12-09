using SmartLock.Models;
using SmartLock.ViewModels;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace SmartLock.Views
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class StatusPage : ContentPage
    {
        StatusViewModel StatusViewModel;
        public StatusPage()
        {
            InitializeComponent();
            //Temporary
            StatusViewModel = new StatusViewModel();
            
            BindingContext = StatusViewModel;
        }
    }
}
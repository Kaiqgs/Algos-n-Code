
using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using SmartLock.Models;

namespace SmartLock.Services
{
    interface IDoorConnection
    {
        bool IsConnected { get; set; }
        bool CanConnect { get;}


        Task ConnectAsync();
        Task DisconnectAsync();
        Task<bool> AttemptSignInAsync(SignIn signin);
        Task<bool> AttemptSignUpAsync(SignUp signup);

        Task<Status> GetStatusAsync();
        Task<bool> SetStatusAsync(Status state);

    }
}

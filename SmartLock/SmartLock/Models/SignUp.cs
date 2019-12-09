using System;
using System.Collections.Generic;
using System.Text;

namespace SmartLock.Models
{
    public class SignUp
    {
        public string Email { get; set; }
        public string Password { get; set; }

        public SignUp(string email, string password)
        {
            Email = email;
            Password = password;
        }
    }
}

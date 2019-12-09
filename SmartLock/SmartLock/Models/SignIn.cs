﻿using System;
using System.Collections.Generic;
using System.Text;

namespace SmartLock.Models
{
    public class SignIn
    {
        public string Email { get; set; }
        public string Password { get; set; }

        public SignIn(string email, string password)
        {
            Email = email;
            Password = password;
        }
    }
}

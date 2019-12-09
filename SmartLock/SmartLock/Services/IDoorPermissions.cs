using Plugin.Permissions.Abstractions;
using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;

namespace SmartLock.Services
{
    public interface IDoorPermissions
    {
        Task<PermissionStatus> RequestAllPermissions();
        Task<bool> RequestMissingPermissions();
    }
}

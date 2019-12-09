using Plugin.Permissions;
using Plugin.Permissions.Abstractions;
using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;

namespace SmartLock.Services
{
    class DoorPermissions : IDoorPermissions
    {
        public async Task<PermissionStatus> RequestAllPermissions()
        {
            if (await CrossPermissions.Current.ShouldShowRequestPermissionRationaleAsync(Permission.Location))
            {
                await DoorLanguageResources.Instance.NeedLocationMessage();
            }
            var result = await CrossPermissions.Current.RequestPermissionsAsync(Permission.Location);
            if (result.ContainsKey(Permission.Location))
                return result[Permission.Location];
            return PermissionStatus.Denied;
        }

        public async Task<bool> RequestMissingPermissions()
        {
            var status = await CrossPermissions.Current.CheckPermissionStatusAsync(Permission.Location);
            if (status != PermissionStatus.Granted)
                status = await RequestAllPermissions();
            return status == PermissionStatus.Granted;
        }
    }
}

using System;
using System.Collections.Generic;
using System.Text;

namespace SmartLock.Models
{
    public class Status
    {

        public DoorState State { get; set; }

        public Status(DoorState state)
        {
            State = state;
        }

        public Status Toggle()
        {
            DoorState newstate;
            if (State == DoorState.Unlocked) newstate = DoorState.Locked;
            else newstate = DoorState.Unlocked;

            return new Status(newstate);
        }
    }
}

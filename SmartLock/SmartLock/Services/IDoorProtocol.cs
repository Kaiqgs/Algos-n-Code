using System;
using System.Collections.Generic;
using System.Text;

namespace SmartLock.Services
{
    interface IDoorProtocol<T>
    {
        T ID { get; set; }
        string Data { get; set; }
        string Protocol { get; }
        byte[] BytesProtocol { get; }

        bool QuerySuccess { get; }

        IDoorProtocol<T> ParseProtocol(string protocol);
        

    }
}

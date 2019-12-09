using System;
using System.Collections.Generic;
using System.Text;

namespace SmartLock.Services
{

    public enum ProtocolType
    {
        Acknowledge,
        Error,
        Lock,
        Unlock,
        Unknown,
        State,
        SignUpPassword,
        SignUpEmail,
        SignInPassword,
        SignInEmail
    }

    class DoorProtocol : IDoorProtocol<ProtocolType>
    {
        public ProtocolType ID { get; set; }
        public string Data { get; set; }
        public string Protocol { get => $"{Translate[(int)ID]}{Data}\r\n"; }
        public byte[] BytesProtocol { get => Encoding.UTF8.GetBytes(Protocol); }

        public bool QuerySuccess { get => ID == ProtocolType.Acknowledge; }

        private readonly string[] Translate = { "_ack_", "_err_", "_lck_", "_ulk_", "_unk_", "_sts_", "_sup_", "_sue_", "_sip_", "_sie_" };

        public DoorProtocol(ProtocolType protocolType, string data="")
        {
            ID = protocolType;
            Data = data;
        }
        public DoorProtocol()
        {
            ID = ProtocolType.Unknown;
            Data = "";
        }

        public IDoorProtocol<ProtocolType> ParseProtocol(string protocol)
        {
            for(int i = 0; i < Translate.Length; ++i)
            {
                int idx = protocol.IndexOf(Translate[i]);
                if (idx != 0) continue;
                string data = protocol.Substring(idx);
                return new DoorProtocol((ProtocolType)i, data);
            }
            return null;
        }
    }
}

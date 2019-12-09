using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Nucleo;

namespace Kernel
{
    /*
     * This is being rendered useless. 
     */
    public class ProcessEventArgs : EventArgs
    {
        public IEnumerable<Process> Processes { get; set; }
        public ProcessEventArgs(IEnumerable<Process> processes)
        {
            Processes = processes;
        }

        public ProcessEventArgs(Process process)
        {
            Processes = new List<Process>() { process };
        }
    }
}

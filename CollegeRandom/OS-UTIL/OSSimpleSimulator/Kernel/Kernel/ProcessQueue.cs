using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Nucleo;

namespace Kernel
{
    public class ProcessQueue // Fila de processo;
    {

        //GUI -> NUCLEO(BIBLIOTECA), KERNEL(BIBLIOTECA);
        //KERNEL -> NUCLEO(BIBLIOTECA);
        //NUCLEO -> eps;
        public Process.Priorities Priority { get; set; }// TBI;
        public List<Process> Processes { get; private set; }

        public ProcessQueue(Process.Priorities priority)
        {
            Priority = priority;
            Processes = new List<Process>();
        }

        public void AddProcess(Process process)
        {
            Processes.Add(process);
        }

        public bool RemoveProcess(string procname)
        {
            for (int i = 0; i < Processes.Count; i++)
            {
                if(Processes[i].Name == procname)
                {
                    Processes.RemoveAt(i);
                    return true;
                }
            }
            return false;
        }

        //ATUALIZA A CABECA
        public void Update(IEnumerable<Process> externprocs)
        {
            if (Processes.Count <= 0) return;

            Processes[0].CheckDependency(externprocs);
            if (Processes[0].Finished || Processes[0].Blocked)
            {
                QueueBack();
            }
            else
            {
                //Kernel;
                int quantumTime = (int)Processes[0].Priority;
                Processes[0].Update(new Quantum(quantumTime + 1));
            }
        }

        public void QueueBack()
        {
            if(Processes.Count > 0)
            {
                var out_ = Processes[0];
                Processes.RemoveAt(0);
                Processes.Add(out_);
            }
        }

        public bool Contains(string procname)
        {
            var found = Processes.Find(x => x.Name == procname);
            return found != null;
        }

        void ClearProcess()
        {
            Processes.Clear();
        }
    }
}

using System;
using System.Collections.Generic;
using System.Linq;
using Nucleo;

namespace Kernel
{
    public class OS
    {
        public Memory Memory { get; set; }
        public delegate void ProcessEventHandler(object sender, ProcessEventArgs p);
        public event ProcessEventHandler ProcessAdded;
        public event ProcessEventHandler ProcessRemoved;
        public event ProcessEventHandler ProcessesCleared;

        public Dictionary<Process.Priorities, ProcessQueue> MultipleQueue { get; set; }

        /*
         * CHAVES["tal"] = coisa;
         * 
         * CHAVES[ALTA] = MULTIPLEQUEUE;
         * CHAVES[LOW] = 
         * */

        public List<Process> Processes
        {
            get
            {
                var processes = new List<Process>();
                foreach(var kv in MultipleQueue)
                {
                    processes.AddRange(kv.Value.Processes);
                }
                return processes;
            }
        }

        public IEnumerable<string> ProcessesNames {get => Processes.Select(x => x.Name);}

        private int queueIndex;//TALVEZ TBI;
        private string[] priorityNames; // "Low", "Medium", "High" .count

        public OS()
        {
            Memory = new Memory(1024 * 2);
            SetupProcesses();
        }

        public void AddProcess(Process process)
        {
            if (ProcessesNames.Contains(process.Name))
                throw new ArgumentException("Process already exists");
            MultipleQueue[process.Priority].AddProcess(process);
            Memory.Alloc(process.Name, new byte[1048576]);
            ProcessAdded?.Invoke(this, new ProcessEventArgs(process));
        }

        public void RemoveProcess(string procName)
        {
            foreach (var pri in GetPriorities())
            {
                if (MultipleQueue[pri].RemoveProcess(procName))
                {
                    Memory.Free(procName);
                    ProcessRemoved?.Invoke(this, null);
                    return;
                }   
            }
            throw new KeyNotFoundException();
        }

        public void ClearProcesses()
        {
            Memory.Clear();
            SetupProcesses();
            ProcessesCleared?.Invoke(this, new ProcessEventArgs(Processes));
        }

        public void Update()
        {
            var priority = UpdateQueueIndex();
            MultipleQueue[priority].Update(Processes);
        }

        private void SetupProcesses()
        {
            queueIndex = 0;
            priorityNames = Enum.GetNames(typeof(Process.Priorities));
            MultipleQueue = new Dictionary<Process.Priorities, ProcessQueue>();
            foreach (var pri in GetPriorities())
                MultipleQueue.Add(pri, new ProcessQueue(pri));
        }

        private IEnumerable<Process.Priorities> GetPriorities()
        {
            for (int i = 0; i < priorityNames.Length; ++i)
                yield return (Process.Priorities)i;
        }

        private Process.Priorities UpdateQueueIndex()
        {
            queueIndex = (queueIndex + 1) % Enum.GetNames(typeof(Process.Priorities)).Count();
            return (Process.Priorities)queueIndex;
        }



    }
}

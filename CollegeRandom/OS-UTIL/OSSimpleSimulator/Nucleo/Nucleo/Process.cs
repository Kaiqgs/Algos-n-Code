using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Nucleo
{
    public class Process
    {

        public enum Priorities
        {
            Low,
            Medium,
            High
        }

        public enum States
        {
            Done,
            Running,
            Blocked,
            Finished
        }

        public string Name { get; set; }
        public Priorities Priority { get; set; }
        public States State { get; set; }
        public Dependency Dependency { get; set; }

        public float Progress { get; set; }
        public bool Finished { get => State == States.Finished; }
        public bool Blocked { get => State == States.Blocked; }
        public bool Done { get => State == States.Done; }
        public bool Running { get => State == States.Running; }

        public Quantum QuantumNeeded { get; set; }

        public Process(string name,
                       Priorities priority,
                       Dependency dependency)
        {
            //User defined;
            Name = name;
            Priority = priority;
            Dependency = dependency;

            //Default assignments;             
            State = States.Done;
            Progress = 0;
            QuantumNeeded = new Quantum(100);
        }

        public Process(string name, Priorities priority) : this(name, priority, null)
        {
        }

        //SE UPDATE;
        public void Update(Quantum givenQuantum)
        {
            if (!Finished && !Blocked)
            {
                Progress += (float)givenQuantum.Amount / QuantumNeeded.Amount;
                State = States.Running;
                if (Progress > 1)
                {
                    Progress = 1;
                    State = States.Finished;
                }
            }
        }

        public void CheckDependency(IEnumerable<Process> processes)
        {
            if (Dependency == null) return;
            foreach (var proc in processes)
            {
                if (proc.Name == Dependency.ExternProcessName)
                {
                    var isProcGood = (proc.Progress >= Dependency.ProcessDependencyPercentage);
                    if (!isProcGood)
                        State = States.Blocked;
                    else if (State == States.Blocked)
                        State = States.Done;
                    return;
                }
            }
            State = States.Blocked;
        }
    }
}

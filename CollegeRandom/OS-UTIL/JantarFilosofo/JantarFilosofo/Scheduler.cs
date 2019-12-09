using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Threading.Tasks;
using System.Windows.Forms;

namespace JantarFilosofo
{
    public class Scheduler
    {

        public const int NumberPhilosophers = 5;
        public const int UpdatePeriod = 1000;
        public const int MaxPeriod = 50;
        public const int MaxEat = 2;

        public Philosopher[] Philosophers;
        public Fork[] Forks;
        public bool IsActive { get; set; }

        private Timer LoopTimer;
        private int Counter;
        private readonly Label  StatusLabel;
        private readonly Label TimeLabel;
        private int? EatingStartedCount;
        private int StartPos;
        private int EndPos;
        
        public Scheduler(Philosopher[] philosephers, Fork[] forks, Label statuslbl, Label timeLabel)
        {
            Philosophers = philosephers;
            Forks = forks;
            LoopTimer = new Timer();
            IsActive = false;
            LoopTimer.Interval = UpdatePeriod;
            LoopTimer.Tick += Loop;
            StatusLabel = statuslbl;
            TimeLabel = timeLabel;
            StartPos = 0;
            EndPos = 2;
        }



        public void Start()
        {
            LoopTimer.Start();
            IsActive = true;
        }

        public void Stop()
        {
            LoopTimer.Stop();
            IsActive = false;
        }

        private void Loop(object sender, EventArgs e)
        {
                

            Counter++;
            string statusText = "Esperando...";
            TimeLabel.Text = $"{Counter} segundos...";


            if (EatingStartedCount.HasValue)
            {
                if (Counter - EatingStartedCount >= (int)Quantum.Eat)
                {
                    for (int i = 0; i < NumberPhilosophers; i++)
                        if (Philosophers[i].CanEat)
                            Philosophers[i].Eat(Forks[Philosophers[i].LeftFID],
                                            Forks[Philosophers[i].RightFID]);
                    EatingStartedCount = null;
                    StartPos = (StartPos + 1) % NumberPhilosophers;
                    EndPos = (EndPos + 1) % NumberPhilosophers;
                }
                else
                    statusText = "Filósofos comendo...";
            }
            else if ((Counter+1) % (int)Quantum.Select == 0)
            {
                statusText = "Procurando filósofo...";
                MakePickFork(StartPos);
                MakePickFork(EndPos);   
                if (BothCanEat()) EatingStartedCount = Counter;
            }



            if (Counter > MaxPeriod)
                Stop();
            else if (!ShouldContinue())
            {
                statusText = "Todos filósofos se alimentaram...";
                Stop();
            }
                

            StatusLabel.Text = statusText;
        }

        private void MakePickFork(int idx)
        {
            int rfid = Philosophers[idx].RightFID;
            int lfid = Philosophers[idx].LeftFID;
            Philosophers[idx].PickFork(Forks[lfid], Forks[rfid]);
        }

        private bool ShouldContinue()
        {
            foreach (var phi in Philosophers) if (!phi.DoneEating) return true;
            return false;
        }

        private bool BothCanEat()
        {
            return Philosophers[StartPos].CanEat && Philosophers[EndPos].CanEat;
        }


    }
}
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace JantarFilosofo
{
    public class Philosopher
    {
        public States CurrentState { get; set; }
        public int PID { get; set; }
        public int LeftFID { get; set; }
        public int RightFID { get; set; }

        public bool PickedRightFork { get; set; }
        public bool PickedLeftFork { get; set; }

        public bool CanEat { get => PickedRightFork && PickedLeftFork; }
        public bool HasAnyFork { get => PickedLeftFork || PickedRightFork; }
        public bool DoneEating { get => EatCounter >= Scheduler.MaxEat;  }
        public bool ShouldaEaten { get; set; }

        public int EatCounter { get; set; }
        private PictureBox Spaghetti { get; set; }
        private PictureBox Self { get; set; }
        private Label Status { get; set; }
        
        private Random ForkPicker;

        public enum States
        {
            Thinking,
            Eating
        }

        public Philosopher(PictureBox spaghetti,
                            PictureBox self,
                            Label status,
                            int pid)
        {
            EatCounter = 0;
            Spaghetti = spaghetti;
            Self = self;
            Status = status;
            ShouldaEaten = false;
            PID = pid;
            CurrentState = States.Eating;
            SetStatus(States.Thinking);
            Spaghetti.BackColor = Color.Transparent;
            LeftFID = PID;
            RightFID = (PID + 1) % Scheduler.NumberPhilosophers;
            ForkPicker = new Random();
            Spaghetti.SetAlpha(255 / 2);
            //Status.Text = LeftFork + " <> " + RightFork + " | " + Scheduler.NumberPhilosophers;
        }

        private void SetStatus(States state)
        {
            if (state == CurrentState) return;

            if(state == States.Eating)
            {
                Spaghetti.SetAlpha(255 * 4);
                Status.Text = $"... [{EatCounter}x]";
            }
            else if(state == States.Thinking)
            {
                Spaghetti.SetAlpha(255 / 2);
                Status.Text = $"Sentido da vida? [{EatCounter}x]";
            }

            CurrentState = state;
            Self.FlipHorizontal();
        }

        public void PickFork(Fork lfork, Fork rfork)
        {
            Point loc = Self.Location;
            bool pickRight = ForkPicker.Next(2) == 1;

            if (DoneEating || CanEat) return;
            if ((!lfork.Available && !MyFork(lfork)) || (!rfork.Available && !MyFork(rfork)))
            {
                ShouldaEaten = true;
                return;
            }

            if ((pickRight && !PickedRightFork) || PickedLeftFork || !lfork.Available )
            {
                Console.WriteLine("Picking right fork");
                loc.X += 30;
                loc.Y += 35;
                PickedRightFork = rfork.Pick(loc, PID);
            }
            else if((!pickRight && !PickedLeftFork) || PickedRightFork || !rfork.Available)
            {
                Console.WriteLine("Picking left fork");
                loc.X -= 70;
                loc.Y += 35;
                PickedLeftFork = lfork.Pick(loc, PID);
            }

            if (CanEat) SetStatus(States.Eating);
        }

        public void Eat(Fork lfork, Fork rfork)
        {
            lfork.UnPick();
            rfork.UnPick();
            PickedLeftFork = false;
            PickedRightFork = false;
            EatCounter++;
            ShouldaEaten = false;
            SetStatus(States.Thinking);
        }

        public bool MyFork(Fork fork)
        {
            return fork.PID == PID;
        }
    }
}

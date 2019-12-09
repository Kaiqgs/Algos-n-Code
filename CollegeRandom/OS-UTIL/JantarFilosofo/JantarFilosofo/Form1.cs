using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace JantarFilosofo
{
    public partial class Form1 : Form
    {

        
        PictureBox[] SpaghettiPics;
        PictureBox[] ForkPics;
        PictureBox[] PhiloPics;
        Label[] StatusLbls;

        Philosopher[] Philosophers;
        Fork[] ForksRegion;

        Scheduler Scheduler;
        
        public Form1()
        {
            InitializeComponent();
            Philosophers = new Philosopher[Scheduler.NumberPhilosophers];
            ForksRegion = new Fork[Scheduler.NumberPhilosophers];

            phi1.FlipHorizontal();
            phi2.FlipHorizontal();
            phi3.FlipHorizontal();


            SpaghettiPics = new PictureBox[Scheduler.NumberPhilosophers]
            {
                spag1,
                spag2,
                spag3,
                spag4,
                spag5
            };

            ForkPics = new PictureBox[Scheduler.NumberPhilosophers]
            {
                fork1,
                fork2,
                fork3,
                fork4,
                fork5
            };

            PhiloPics = new PictureBox[Scheduler.NumberPhilosophers]
            {
                phi1,
                phi2,
                phi3,
                phi4,
                phi5
            };

            StatusLbls = new Label[Scheduler.NumberPhilosophers]
            {
                label1,
                label2,
                label3,
                label4,
                label5
            };


            for (int i = 0; i < Scheduler.NumberPhilosophers; i++)
            {
                SpaghettiPics[i].BackColor = Color.Transparent;
                
                Philosophers[i] = new Philosopher(SpaghettiPics[i], PhiloPics[i], StatusLbls[i], i);
                ForksRegion[i] = new Fork(ForkPics[i], i);
            }
            
            Scheduler = new Scheduler(Philosophers, ForksRegion, schedulerLabel, timeLabel);
            Scheduler.Start();
        }

        private void ToggleScheduler(object sender, EventArgs e)
        {
            if (Scheduler.IsActive) Scheduler.Stop();
            else Scheduler.Start();
        }
    }
}

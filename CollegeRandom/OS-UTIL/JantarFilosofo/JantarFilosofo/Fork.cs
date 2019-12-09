using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace JantarFilosofo
{
    public class Fork
    {

        public int FID { get; set; }
        public bool Available { get => !PID.HasValue; }

        public int? PID { get; set; }
        private PictureBox Self;
        private Point OriginalLoc;
        public Fork(PictureBox self, int fid)
        {
            Self = self;
            FID = fid;
            PID = null;
            OriginalLoc = Self.Location;
            
            
        }

        public bool Pick(Point location, int PID)
        {

            if (Available)
            {
                Self.Location = location;
                
                this.PID = PID;
                return true;
            }

            return false;
        }

        public void UnPick()
        {
            if (!Available)
            {
                Self.Location = OriginalLoc;
                
                PID = null;
            }
            
        }
    }
}

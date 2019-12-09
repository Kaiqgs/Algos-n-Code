using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;



namespace Nucleo
{
    public class Memory
    {
        public static int mb2kb = 1048576 ;// TBI;
        public Dictionary<string, byte[]> Ram { get; set; }
        private int IndexCounter;// TBI;
        private int mb; // TBI;
        // 1048576 <- 1mb
        // 2147483648 <- 2gb
           
        public Memory(int mb)
        {
            this.mb = mb;
            IndexCounter = 0;
            Ram = new Dictionary<string, byte[]>(mb);
        }

        public int Alloc(string name, byte[] data)
        {          
            Ram.Add(name, data); 
            return IndexCounter;            
        }
        
        public void Free(string name)
        {
            Ram.Remove(name);
            GC.Collect();
        }

        public void Clear()
        {
            Ram.Clear();
            GC.Collect();
        }
    }
}

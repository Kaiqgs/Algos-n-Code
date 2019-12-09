using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Nucleo
{
    /// <summary>
    /// Defines each process dependency against another process;
    /// </summary>
    public class Dependency
    {
        public string ExternProcessName { get; set; }
        public float? ProcessDependencyPercentage { get; set; } = null;

        public Dependency(string externProcessName,
                          float processDependencyPercentage)
        {
            ExternProcessName = externProcessName;
            ProcessDependencyPercentage = processDependencyPercentage;
        }       
    }
}

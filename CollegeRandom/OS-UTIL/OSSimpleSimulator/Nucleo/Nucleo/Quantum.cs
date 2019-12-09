using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Nucleo
{
    public class Quantum
    {
        public enum Metrics
        {
            Millisecond = 1/1000,
            CentSecond = 1/100,
            DecSecond = 1/10,
            Second = 1
        }

        public static readonly Metrics DefaultMetric = Metrics.DecSecond;

        public int Amount { get; set; }
        public Metrics Metric { get; set; }

        public Quantum(int amount)
        {
            Amount = amount;
            Metric = DefaultMetric;
        }

        public Quantum(int amount, Metrics metric)
        {
            Amount = amount;
            Metric = metric;
        }
    }
}

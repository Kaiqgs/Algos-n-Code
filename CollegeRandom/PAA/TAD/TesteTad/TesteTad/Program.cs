using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using LinAlg;

namespace TesteTad
{
    class Program
    {
        static void Main(string[] args)
        {
            var a = new float[,]{
                                    {1,2,3,4},
                                    {5,6,7,8}
                                };

            var b = new float[,]{
                                    {8, 7, 6, 5},
                                    {4, 3, 2, 1}
                                };

            var c = 32;
            var d = 21;

            Console.WriteLine("\nA) Array --");
            a.Print(1);

            Console.WriteLine("\nB) Array --");
            b.Print(1);

            Console.WriteLine("\nC) Scalar --");
            Console.WriteLine("\t" + c);

            Console.WriteLine("\nD) Scalar --");
            Console.WriteLine("\t" + d);

            Console.WriteLine("\n(A . B) Array --");
            a.MatMul(b.T()).Print(1);

            Console.WriteLine("\n(A - C) Array --");
            a.Sub(c).Print(1);

            Console.WriteLine("\n(B + D) Array --");
            b.Add(d).Print(1);


            Console.ReadKey();
        }
    }
}

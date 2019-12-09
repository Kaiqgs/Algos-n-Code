using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LinAlg
{
    /// <summary>
    /// Classe para manipulações de Algebra Linear.
    /// Poderia ser usada em aplicações de redes neurais e A.I. no geral.
    /// Kaique Alan Gualter dos Santos RA: 120176;
    /// </summary>
    public static class LinAlg
    {
        /// <summary>
        /// Multiplica duas matrizes de tamanho (a,b) x (c,d).
        /// Retorna uma matriz de tamanho (a,d).
        /// </summary>
        /// <param name="self">Matriz extendida.</param>
        /// <param name="data">Matriz da direita na operação.</param>
        /// <returns>Uma multiplicação entre as matrizes.</returns>
        public static float[,] MatMul(this float[,] self, float[,] data)
        {

            float[,] out_obj = null;

            /*
             * Caso array seja de tamnhos interiores diferentes (sabemos que a multiplicação não pode ocorroer)
             */
            if (self.GetLength(1) != data.GetLength(0))
                throw new ArrayTypeMismatchException($@"Array provided is not of equal inner size,
                                                     [{self.GetLength(0)},{self.GetLength(1)}] x [{data.GetLength(0)},{data.GetLength(1)}]");

            out_obj = new float[self.GetLength(0), data.GetLength(1)];

            float temp = default(float);

            for (int i = 0; i < self.GetLength(0); i++)
                for (int j = 0; j < data.GetLength(1); j++)
                {
                    temp = 0;
                    for (int k = 0; k < self.GetLength(1); k++)
                        temp += self[i, k] * data[k, j];

                    out_obj[i, j] = temp;
                }

            return out_obj;
        }


        /// <summary>
        /// Adiciona a nível de objeto o valor do escalar 'b'.
        /// </summary>
        /// <param name="self">Matriz extendida</param>
        /// <param name="b">Valor escalar a ser somado por toda matriz.</param>
        /// <returns>A matriz com os valores somados.</returns>
        public static float[,] Add(this float[,] self, float b)
        {
            for (int i = 0; i < self.GetLength(0); i++)
                for (int j = 0; j < self.GetLength(1); j++)
                    self[i, j] += b;

            return self;
        }

        /// <summary>
        /// Subtrai a nível de objeto o valor do escalar 'b'.
        /// </summary>
        /// <param name="self">Matriz extendida</param>
        /// <param name="b">Valor escalar a ser subtraido por toda matriz.</param>
        /// <returns>A matriz com os valores subtraidos.</returns>
        public static float[,] Sub(this float[,] self, float b)
        {

            for (int i = 0; i < self.GetLength(0); i++)
                for (int j = 0; j < self.GetLength(1); j++)
                    self[i, j] -= b;

            return self;
        }

        /// <summary>
        /// Transpõe a matriz.
        /// </summary>
        /// <param name="self">A matriz extendida a ser transposta.</param>
        /// <returns>A matriz transposta.</returns>
        public static float[,] T(this float[,] self)
        {
            var out_self = new float[self.GetLength(1), self.GetLength(0)];

            for (int i = 0; i < self.GetLength(0); ++i)
                for (int j = 0; j < self.GetLength(1); j++)
                    out_self[j, i] = self[i, j];

            return out_self;
        }

        /// <summary>
        /// Formata e printa uma matriz.
        /// </summary>
        /// <param name="self">Matriz a ser printada.</param>
        /// <param name="nTab">Quantidade de tabs para formatação.</param>
        public static void Print(this float[,] self, int nTab=0)
        {
            PrintTab(nTab);
            Console.Write("[");
            for (int i = 0; i < self.GetLength(0); ++i)
            {

                if (i != 0)
                {
                    Console.Write(",\n");
                    PrintTab(nTab);
                    Console.Write(" ");
                }
                Console.Write("[");
                for (int j = 0; j < self.GetLength(1); j++)
                {
                    if (j != 0) Console.Write(", ");
                    Console.Write(self[i, j]);
                }
                Console.Write("]");
                
            }
            Console.WriteLine("]");
        }

        /// <summary>
        /// Printa \t (tab) 'n' vezes.
        /// </summary>
        /// <param name="n">Quantas vezes printar tab.</param>
        private static void PrintTab(int n)
        {
            for (int i = 0; i < n; i++)Console.Write("\t");
        }
    }
}

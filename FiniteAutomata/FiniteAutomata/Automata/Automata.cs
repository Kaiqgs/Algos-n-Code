using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FiniteAutomata.Automata
{
    using Sigma = List<char>;
    using Delta = List<Transicao>;
    using q = Int32;
    using Q = List<Int32>;

    class Automata
    {
        //Estado nulo;
        public static int Qnull { get; } = -1;
        
        //Conjunto de estados;
        private Q Q { get; set; }

        //Alfabeto (símbolos);
        public Sigma Sigma { get; private set; }

        //Conjunto de função de transições;
        public Delta Delta { get; private set; }

        //Estado inicial;
        public q Q0 { get; private set; }

        //Conjunto de estados finais;
        public Q QF { get; private set; }

        //Construtores;
        public Automata(Q Q, Sigma Sigma, Delta Delta, q Q0, Q QF)
        {
            this.Q = Q;
            this.Sigma = Sigma;
            this.Delta = Delta;
            this.Q0 = Q0;
            this.QF = QF;
        }

        public Automata()
        {
            Q = new Q();
            Sigma = new Sigma();
            Delta = new Delta();
            Q0 = Qnull;
            QF = new Q();
        }

        //Transição A -> B, dado símbolo;
        public q Transiciona(q Qn, char simbolo)
        {
            for (int i = 0; i < Delta.Count; i++)
            {
                if (Delta[i].Qa == Qn && Delta[i].Simbolo == simbolo)
                {
                    return Delta[i].Qb;
                }
            }
            return Qnull;
        }

        //Formata novo estado dado posicação e o adiciona a lista de estados;
        public q CriaQ(int idx)
        {
            q newQ = idx;
            if (!Q.Contains(newQ)) Q.Add(newQ);
            return newQ;
        }

        //Formata novo estado dado posicação, adiciona a lista de estados e o adiciona a lista de finais;
        public q CriaQf(int idx)
        {
            q newQ = CriaQ(idx);
            if (!QF.Contains(newQ)) QF.Add(newQ);
            return newQ;
        }

        //Formata novo estado dado posicação, adiciona a lista de estados o atribui a estado inicial;
        public q CriaQ0(int idx)
        {
            q newQ = CriaQ(idx);
            Q0 = newQ;
            return newQ;
        }

        //Retorna verdadeiro caso estado dado seja final;
        public bool EhQFinal(q Qn)
        {
            return QF.Contains(Qn);
        }

        //Caso seja inválido (-1);
        public static bool QInvalido(q Qn)
        {
            return Qn == Qnull;
        }
    }
}

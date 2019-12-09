using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FiniteAutomata.Automata
{
    using q = Int32;
    //Classe que define formato da transição;
    public class Transicao
    {
        //Estado 'A' inicial;
        public q Qa { get; private set; }
        //Símbolo intermédio;
        public char Simbolo { get; private set; }
        //Estado 'B' final;
        public q Qb { get; private set; }

        //Ctor;
        public Transicao(q Sa, char Simbolo, q Sb)
        {
            this.Qa = Sa;
            this.Simbolo = Simbolo;
            this.Qb = Sb;
        }

        //Representação em string;
        public override string ToString()
        {
            return string.Format("(Q{0}, {1}) -> Q{2}", Qa, Simbolo, Qb);
        }
    }
}

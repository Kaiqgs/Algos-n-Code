using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FiniteAutomata.Automata
{
        using q = Int32;
        //Definição da máquina que opera o automato;
        class MaquinaEstadosFinito
        {
            //O automato propriamente dito;
            public Automata Automata { get; set; }
            
            //Construtores;
            public MaquinaEstadosFinito()
            {
                Automata = new Automata();
            }

            public MaquinaEstadosFinito(Automata automata)
            {
                Automata = automata;
            }
            
            //Dado fita, itera por cada posição da fita reconhecendo ou não;
            public bool Reconhece(char[] fita)
            {
                q Qn = Automata.Q0;
                foreach (var simbolo in fita)
                {
                    Qn = Automata.Transiciona(Qn, simbolo);
                    if (Automata.QInvalido(Qn)) return false;
                }
                return Automata.EhQFinal(Qn);
            }
        
    }
}

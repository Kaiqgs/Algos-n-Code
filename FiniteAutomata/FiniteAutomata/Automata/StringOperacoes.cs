using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using FiniteAutomata.Automata;


namespace FiniteAutomata.Automata
{
    using Sigma = List<char>;
    using q = Int32;

    static class OperacoesAutomata
    {
        //Alfabeto padrão definido com caracteres básicos;
        public static Sigma StdSigma = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz _".ToList();
        
        //Definição de um gerador de automato reconhecedor de prefixo, dado prefixo e alfabeto;
        public static Automata ComecaCom(string prefixo, Sigma sigma)
        {
            if (!EhValido(prefixo, sigma)) return null;
            var auto = new Automata();
            q Q0 = auto.CriaQ0(0);

            int i;
            for (i = 0; i < prefixo.Length; ++i)
            {
                q Qa = auto.CriaQ(i);
                q Qb = auto.CriaQ(i + 1);

                auto.Delta.Add(new Transicao(Qa, prefixo[i], Qb));
            }
            q Qn = auto.CriaQf(i);
            sigma.ForEach(simb => auto.Delta.Add(new Transicao(Qn, simb, Qn)));
            return auto;
        }

        //Definição de um gerador de automato reconhecedor de suffixo, dado suffixo e alfabeto;
        public static Automata TerminaCom(string suffixo, Sigma sigma)
        {
            if (!EhValido(suffixo, sigma)) return null;

            var auto = new Automata();
            q Q0 = auto.CriaQ0(0);
            q Q1 = auto.CriaQ(1);
            int i = 0;
            var primeiraLetra = suffixo[0];

            auto.Delta.Add(new Transicao(Q1, suffixo[0], Q1));

            for (i = 0; i < suffixo.Length; ++i)
            {
                q Qa = auto.CriaQ(i);
                q Qb = auto.CriaQ(i + 1);
                auto.Delta.Add(new Transicao(Qa, suffixo[i], Qb));
                sigma.ForEach(sim =>
                {
                    if (sim != suffixo[i]) auto.Delta.Add(new Transicao(Qa, sim, Q0));
                    else if (sim == primeiraLetra) auto.Delta.Add(new Transicao(Qa, sim, Q1));
                });
            }

            q Qn = auto.CriaQf(i);
            foreach (var sim in sigma)
            {
                if (sim == primeiraLetra) auto.Delta.Add(new Transicao(Qn, sim, Q1));
                else auto.Delta.Add(new Transicao(Qn, sim, Q0));
            }
            return auto;
        }

        //Definição de um gerador de automato reconhecedor de sub-palavra, dado sub-palavra e alfabeto;
        public static Automata Contem(string subPalavra, Sigma sigma)
        {
            if (!EhValido(subPalavra, sigma)) return null;
            Automata auto = new Automata();
            int i;
            q Q0 = auto.CriaQ0(0);

            for (i = 0; i < subPalavra.Length; ++i)
            {
                q Qa = auto.CriaQ(i);
                q Qb = auto.CriaQ(i + 1);

                auto.Delta.Add(new Transicao(Qa, subPalavra[i], Qb));
                foreach (var simbolo in sigma)
                {
                    if (simbolo != subPalavra[i])
                    {
                        auto.Delta.Add(new Transicao(Qa, simbolo, Q0));
                    }
                }
            }
            q Qn = auto.CriaQf(i);
            sigma.ForEach(simb => auto.Delta.Add(new Transicao(Qn, simb, Qn)));
            return auto;
        }

        //Caso palavra w, não esteja contido em sigma, é inválido;
        private static bool EhValido(string w, Sigma sigma)
        {
            foreach (var letra in w) if (!sigma.Contains(letra)) return false;
            return true;
        }
    }
}

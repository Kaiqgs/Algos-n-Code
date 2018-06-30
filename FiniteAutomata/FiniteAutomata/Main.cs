using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using FiniteAutomata.Automata;

namespace FiniteAutomata
{
    public partial class Main : Form
    {
        //Três operações;
        MaquinaEstadosFinito TerminaCom;
        MaquinaEstadosFinito Contem;
        MaquinaEstadosFinito ComecaCom;

        public Main()
        {
            InitializeComponent();
        }

        //Atualiza interface com o novo reconhecedor dado três operações;
        void Atualiza(object sender, EventArgs e)
        {
            var input = InputTextBox.Text;
            if (!String.IsNullOrEmpty(input))
            {
                TerminaCom = new MaquinaEstadosFinito(OperacoesAutomata.TerminaCom(input, OperacoesAutomata.StdSigma));
                Contem = new MaquinaEstadosFinito(OperacoesAutomata.Contem(input, OperacoesAutomata.StdSigma));
                ComecaCom = new MaquinaEstadosFinito(OperacoesAutomata.ComecaCom(input, OperacoesAutomata.StdSigma));
                Reconhece(null, null);
            }
        }

        //Atualiza interface, reconhecendo novo caso input-teste;
        void Reconhece(object sender, EventArgs e)
        {
            if(TerminaCom!=null && Contem != null && ComecaCom != null)
            {
                var test = TesteTextBox.Text.ToArray();
                ComecaCheckBox.Checked = ComecaCom.Reconhece(test);
                ContemCheckBox.Checked = Contem.Reconhece(test);
                TerminaCheckBox.Checked = TerminaCom.Reconhece(test);
            }
        }

        //Imprime informações básicas sobre o programa ao usuário;
        private void InfoButton_Click(object sender, EventArgs e)
        {
            string msg = String.Format("Alfabeto:\n{{{0}}}\n\nKaique Alan Gualter dos Santos, RA:120176;", String.Join(",", OperacoesAutomata.StdSigma));
            MessageBox.Show(msg, "Informações", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }
    }
}

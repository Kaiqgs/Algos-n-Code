namespace FiniteAutomata
{
    partial class Main
    {
        /// <summary>
        /// Variável de designer necessária.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Limpar os recursos que estão sendo usados.
        /// </summary>
        /// <param name="disposing">true se for necessário descartar os recursos gerenciados; caso contrário, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Código gerado pelo Windows Form Designer

        /// <summary>
        /// Método necessário para suporte ao Designer - não modifique 
        /// o conteúdo deste método com o editor de código.
        /// </summary>
        private void InitializeComponent()
        {
            this.InputTextBox = new System.Windows.Forms.TextBox();
            this.TesteTextBox = new System.Windows.Forms.TextBox();
            this.ContemCheckBox = new System.Windows.Forms.CheckBox();
            this.ComecaCheckBox = new System.Windows.Forms.CheckBox();
            this.TerminaCheckBox = new System.Windows.Forms.CheckBox();
            this.InfoButton = new System.Windows.Forms.Button();
            this.InputLabel = new System.Windows.Forms.Label();
            this.TestLabel = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // InputTextBox
            // 
            this.InputTextBox.Location = new System.Drawing.Point(46, 89);
            this.InputTextBox.Name = "InputTextBox";
            this.InputTextBox.Size = new System.Drawing.Size(154, 20);
            this.InputTextBox.TabIndex = 0;
            this.InputTextBox.TextChanged += new System.EventHandler(this.Atualiza);
            // 
            // TesteTextBox
            // 
            this.TesteTextBox.Location = new System.Drawing.Point(46, 132);
            this.TesteTextBox.Name = "TesteTextBox";
            this.TesteTextBox.Size = new System.Drawing.Size(154, 20);
            this.TesteTextBox.TabIndex = 1;
            this.TesteTextBox.TextChanged += new System.EventHandler(this.Reconhece);
            // 
            // ContemCheckBox
            // 
            this.ContemCheckBox.AutoCheck = false;
            this.ContemCheckBox.AutoSize = true;
            this.ContemCheckBox.Location = new System.Drawing.Point(12, 35);
            this.ContemCheckBox.Name = "ContemCheckBox";
            this.ContemCheckBox.Size = new System.Drawing.Size(65, 17);
            this.ContemCheckBox.TabIndex = 1;
            this.ContemCheckBox.TabStop = false;
            this.ContemCheckBox.Text = "Contém;";
            this.ContemCheckBox.UseVisualStyleBackColor = true;
            // 
            // ComecaCheckBox
            // 
            this.ComecaCheckBox.AutoCheck = false;
            this.ComecaCheckBox.AutoSize = true;
            this.ComecaCheckBox.Location = new System.Drawing.Point(12, 12);
            this.ComecaCheckBox.Name = "ComecaCheckBox";
            this.ComecaCheckBox.Size = new System.Drawing.Size(92, 17);
            this.ComecaCheckBox.TabIndex = 1;
            this.ComecaCheckBox.TabStop = false;
            this.ComecaCheckBox.Text = "Começa Com;";
            this.ComecaCheckBox.UseVisualStyleBackColor = true;
            // 
            // TerminaCheckBox
            // 
            this.TerminaCheckBox.AutoCheck = false;
            this.TerminaCheckBox.AutoSize = true;
            this.TerminaCheckBox.Location = new System.Drawing.Point(12, 58);
            this.TerminaCheckBox.Name = "TerminaCheckBox";
            this.TerminaCheckBox.Size = new System.Drawing.Size(91, 17);
            this.TerminaCheckBox.TabIndex = 10;
            this.TerminaCheckBox.TabStop = false;
            this.TerminaCheckBox.Text = "Termina Com;";
            this.TerminaCheckBox.UseVisualStyleBackColor = true;
            // 
            // InfoButton
            // 
            this.InfoButton.Location = new System.Drawing.Point(160, 12);
            this.InfoButton.Name = "InfoButton";
            this.InfoButton.Size = new System.Drawing.Size(40, 23);
            this.InfoButton.TabIndex = 11;
            this.InfoButton.Text = "info";
            this.InfoButton.UseVisualStyleBackColor = true;
            this.InfoButton.Click += new System.EventHandler(this.InfoButton_Click);
            // 
            // InputLabel
            // 
            this.InputLabel.AutoSize = true;
            this.InputLabel.Location = new System.Drawing.Point(9, 92);
            this.InputLabel.Name = "InputLabel";
            this.InputLabel.Size = new System.Drawing.Size(31, 13);
            this.InputLabel.TabIndex = 12;
            this.InputLabel.Text = "Input";
            // 
            // TestLabel
            // 
            this.TestLabel.AutoSize = true;
            this.TestLabel.Location = new System.Drawing.Point(9, 132);
            this.TestLabel.Name = "TestLabel";
            this.TestLabel.Size = new System.Drawing.Size(34, 13);
            this.TestLabel.TabIndex = 12;
            this.TestLabel.Text = "Teste";
            // 
            // Main
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(212, 161);
            this.Controls.Add(this.TestLabel);
            this.Controls.Add(this.InputLabel);
            this.Controls.Add(this.InfoButton);
            this.Controls.Add(this.TerminaCheckBox);
            this.Controls.Add(this.ComecaCheckBox);
            this.Controls.Add(this.ContemCheckBox);
            this.Controls.Add(this.TesteTextBox);
            this.Controls.Add(this.InputTextBox);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow;
            this.Name = "Main";
            this.Text = "Automato Finito";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox InputTextBox;
        private System.Windows.Forms.TextBox TesteTextBox;
        private System.Windows.Forms.CheckBox ContemCheckBox;
        private System.Windows.Forms.CheckBox ComecaCheckBox;
        private System.Windows.Forms.CheckBox TerminaCheckBox;
        private System.Windows.Forms.Button InfoButton;
        private System.Windows.Forms.Label InputLabel;
        private System.Windows.Forms.Label TestLabel;
    }
}


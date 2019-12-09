namespace GUI
{
    partial class OsSimulator
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.label1 = new System.Windows.Forms.Label();
            this.procNameText = new System.Windows.Forms.TextBox();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.addProcButton = new System.Windows.Forms.Button();
            this.label4 = new System.Windows.Forms.Label();
            this.dependencyPct = new System.Windows.Forms.NumericUpDown();
            this.label3 = new System.Windows.Forms.Label();
            this.dependencyProcName = new System.Windows.Forms.TextBox();
            this.procDependentCheck = new System.Windows.Forms.CheckBox();
            this.label2 = new System.Windows.Forms.Label();
            this.procPriorityCombo = new System.Windows.Forms.ComboBox();
            this.processGridView = new System.Windows.Forms.DataGridView();
            this.label5 = new System.Windows.Forms.Label();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.checkBox1 = new System.Windows.Forms.CheckBox();
            this.button4 = new System.Windows.Forms.Button();
            this.groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.dependencyPct)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.processGridView)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(6, 28);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(35, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "Name";
            // 
            // procNameText
            // 
            this.procNameText.Location = new System.Drawing.Point(65, 25);
            this.procNameText.Name = "procNameText";
            this.procNameText.Size = new System.Drawing.Size(100, 20);
            this.procNameText.TabIndex = 1;
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.addProcButton);
            this.groupBox1.Controls.Add(this.label4);
            this.groupBox1.Controls.Add(this.dependencyPct);
            this.groupBox1.Controls.Add(this.label3);
            this.groupBox1.Controls.Add(this.dependencyProcName);
            this.groupBox1.Controls.Add(this.procDependentCheck);
            this.groupBox1.Controls.Add(this.label2);
            this.groupBox1.Controls.Add(this.procPriorityCombo);
            this.groupBox1.Controls.Add(this.procNameText);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Location = new System.Drawing.Point(12, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(289, 225);
            this.groupBox1.TabIndex = 2;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Create Process";
            // 
            // addProcButton
            // 
            this.addProcButton.Location = new System.Drawing.Point(208, 196);
            this.addProcButton.Name = "addProcButton";
            this.addProcButton.Size = new System.Drawing.Size(75, 23);
            this.addProcButton.TabIndex = 9;
            this.addProcButton.Text = "Create";
            this.addProcButton.UseVisualStyleBackColor = true;
            this.addProcButton.Click += new System.EventHandler(this.AddProcessClick);
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(6, 132);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(126, 13);
            this.label4.TabIndex = 8;
            this.label4.Text = "Dependency Percentage";
            // 
            // dependencyPct
            // 
            this.dependencyPct.DecimalPlaces = 1;
            this.dependencyPct.Enabled = false;
            this.dependencyPct.Location = new System.Drawing.Point(152, 130);
            this.dependencyPct.Name = "dependencyPct";
            this.dependencyPct.Size = new System.Drawing.Size(120, 20);
            this.dependencyPct.TabIndex = 7;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(6, 107);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(140, 13);
            this.label3.TabIndex = 6;
            this.label3.Text = "Dependency Process Name";
            // 
            // dependencyProcName
            // 
            this.dependencyProcName.AutoCompleteMode = System.Windows.Forms.AutoCompleteMode.Suggest;
            this.dependencyProcName.AutoCompleteSource = System.Windows.Forms.AutoCompleteSource.CustomSource;
            this.dependencyProcName.Enabled = false;
            this.dependencyProcName.Location = new System.Drawing.Point(152, 104);
            this.dependencyProcName.Name = "dependencyProcName";
            this.dependencyProcName.Size = new System.Drawing.Size(131, 20);
            this.dependencyProcName.TabIndex = 5;
            // 
            // procDependentCheck
            // 
            this.procDependentCheck.AutoSize = true;
            this.procDependentCheck.Location = new System.Drawing.Point(9, 78);
            this.procDependentCheck.Name = "procDependentCheck";
            this.procDependentCheck.Size = new System.Drawing.Size(90, 17);
            this.procDependentCheck.TabIndex = 4;
            this.procDependentCheck.Text = "Is Dependent";
            this.procDependentCheck.UseVisualStyleBackColor = true;
            this.procDependentCheck.Click += new System.EventHandler(this.DependencyCheckbox);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(6, 54);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(38, 13);
            this.label2.TabIndex = 3;
            this.label2.Text = "Priority";
            // 
            // procPriorityCombo
            // 
            this.procPriorityCombo.FormattingEnabled = true;
            this.procPriorityCombo.Items.AddRange(new object[] {
            "High",
            "Medium",
            "Low"});
            this.procPriorityCombo.Location = new System.Drawing.Point(57, 51);
            this.procPriorityCombo.Name = "procPriorityCombo";
            this.procPriorityCombo.Size = new System.Drawing.Size(121, 21);
            this.procPriorityCombo.TabIndex = 2;
            this.procPriorityCombo.Text = "Medium";
            // 
            // processGridView
            // 
            this.processGridView.AllowUserToAddRows = false;
            this.processGridView.AllowUserToDeleteRows = false;
            this.processGridView.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.processGridView.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.Fill;
            this.processGridView.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.processGridView.Location = new System.Drawing.Point(307, 37);
            this.processGridView.Name = "processGridView";
            this.processGridView.ReadOnly = true;
            this.processGridView.Size = new System.Drawing.Size(432, 362);
            this.processGridView.TabIndex = 3;
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(307, 21);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(64, 13);
            this.label5.TabIndex = 9;
            this.label5.Text = "Process List";
            // 
            // timer1
            // 
            this.timer1.Tick += new System.EventHandler(this.TimerTick);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(12, 317);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 23);
            this.button1.TabIndex = 10;
            this.button1.Text = "Example #1";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.FirstExampleClick);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(12, 346);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(75, 23);
            this.button2.TabIndex = 11;
            this.button2.Text = "Example #2";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.SecondExampleClick);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(12, 375);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(75, 23);
            this.button3.TabIndex = 12;
            this.button3.Text = "Example #3";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.ThirdExampleClick);
            // 
            // checkBox1
            // 
            this.checkBox1.AutoSize = true;
            this.checkBox1.Location = new System.Drawing.Point(144, 379);
            this.checkBox1.Name = "checkBox1";
            this.checkBox1.Size = new System.Drawing.Size(61, 17);
            this.checkBox1.TabIndex = 10;
            this.checkBox1.Text = "Update";
            this.checkBox1.UseVisualStyleBackColor = true;
            this.checkBox1.CheckedChanged += new System.EventHandler(this.UpdateCheckboxChanged);
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(12, 243);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(75, 23);
            this.button4.TabIndex = 13;
            this.button4.Text = "Clear";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.ClearClick);
            // 
            // OsSimulator
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(751, 411);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.checkBox1);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.processGridView);
            this.Controls.Add(this.groupBox1);
            this.Name = "OsSimulator";
            this.Text = "OS Simulator";
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.dependencyPct)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.processGridView)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox procNameText;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.ComboBox procPriorityCombo;
        private System.Windows.Forms.CheckBox procDependentCheck;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox dependencyProcName;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.NumericUpDown dependencyPct;
        private System.Windows.Forms.DataGridView processGridView;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.Button addProcButton;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.CheckBox checkBox1;
        private System.Windows.Forms.Button button4;
    }
}


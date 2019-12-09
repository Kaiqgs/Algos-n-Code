using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Kernel;
using Nucleo;

namespace GUI
{
    public partial class OsSimulator : Form
    {
        DataGridViewColumn[] Columns = new DataGridViewColumn[]
        {
            new DataGridViewTextBoxColumn
            {
                HeaderText = "Name",
                Name = "Name",
                AutoSizeMode = DataGridViewAutoSizeColumnMode.Fill,
                ReadOnly = true,
                SortMode = DataGridViewColumnSortMode.NotSortable
            },
            new DataGridViewTextBoxColumn
            {
                HeaderText = "Status",
                Name = "Status",
                AutoSizeMode = DataGridViewAutoSizeColumnMode.Fill,
                ReadOnly = true,
                SortMode = DataGridViewColumnSortMode.NotSortable
            },
            new DataGridViewTextBoxColumn
            {
                HeaderText = "Priority",
                AutoSizeMode = DataGridViewAutoSizeColumnMode.Fill,
                ReadOnly = true,
                SortMode = DataGridViewColumnSortMode.NotSortable
            },
            new DataGridViewProgressColumn
            {
                HeaderText = "Progress",
                Name = "Progress",
                AutoSizeMode = DataGridViewAutoSizeColumnMode.Fill,
                ReadOnly = true
            },
            new DataGridViewButtonColumn
            {
                HeaderText = "Delete",
                Name = "Delete",
                AutoSizeMode = DataGridViewAutoSizeColumnMode.Fill,
            }
        };

        OS os;
        private bool ShouldUpdate;
        Dictionary<string, int> VisualMap { get; set; }

        public OsSimulator()
        {
            InitializeComponent();

            os = new OS();
            os.ProcessAdded += SetupDataGrid;
            os.ProcessesCleared += SetupDataGrid;
            os.ProcessRemoved += SetupDataGrid;

            processGridView.CellClick += DeleteProcessHandler;

            //os.ProcessesCleared += 

            VisualMap = new Dictionary<string, int>();
            checkBox1.Checked = true;
            processGridView.AllowUserToAddRows = false;
            processGridView.Columns.AddRange(Columns);

            timer1.Start();
        }



        private void DependencyCheckbox(object sender, EventArgs e)
        {

            dependencyPct.Enabled = procDependentCheck.Checked;
            dependencyProcName.Enabled = procDependentCheck.Checked;
        }


        private void SetupDataGrid(object sender, ProcessEventArgs p)
        {
            var suggestions = new AutoCompleteStringCollection();
            suggestions.AddRange(os.ProcessesNames.ToArray());
            dependencyProcName.AutoCompleteCustomSource = suggestions;

            VisualMap.Clear();
            processGridView.Rows.Clear();
            
            int index = 0;
            foreach(var proc in os.Processes)
            {
                VisualMap[proc.Name] = index++;
                var stateName = Enum.GetName(typeof(Process.States), proc.State);
                var priorityName = Enum.GetName(typeof(Process.Priorities), proc.Priority);
                int progress = Convert.ToInt32(proc.Progress * 100);
                var delete = "Delete";
                if (proc.Done) delete = "----";
                processGridView.Rows.Add(new object[] { proc.Name, stateName, priorityName, progress, delete });
            }
        }

        private void TimerTick(object sender, EventArgs e)
        {
            if (!ShouldUpdate) return;
            os.Update();

            foreach (var proc in os.Processes)
            {
                int row = VisualMap[proc.Name];
                //Values to update;
                int progress = Convert.ToInt32(proc.Progress * 100);
                var delete = proc.State == Process.States.Finished ? "----" : "Delete";
                var stateName = Enum.GetName(typeof(Process.States), proc.State);

                //Assigning updated values;
                processGridView.Rows[row].Cells["Progress"].Value = progress;
                processGridView.Rows[row].Cells["Delete"].Value = delete;
                processGridView.Rows[row].Cells["Status"].Value = stateName;
            }
        }

        private void AddProcessClick(object sender, EventArgs e)
        {
            Dependency dependency = null;
            Process.Priorities priority = Process.Priorities.Low;

            if (os.ProcessesNames.Contains(procNameText.Text))
            {
                MessageBox.Show("You must inform a unique process name");
                return;
            }

            if (procDependentCheck.Checked)
            {
                if (!os.ProcessesNames.Contains(dependencyProcName.Text))
                {
                    MessageBox.Show("You must inform a valid Process Dependency Value");
                    return;
                }
                dependency = new Dependency(dependencyProcName.Text, (float)dependencyPct.Value / 100F);
            }

            if (procPriorityCombo.Text.ToUpper() == "HIGH")
                priority = Process.Priorities.High;
            else if (procPriorityCombo.Text.ToUpper() == "MEDIUM")
                priority = Process.Priorities.Medium;

            var proc = new Process(procNameText.Text, priority, dependency);

            os.AddProcess(proc);
        }

        private void DeleteProcessHandler(object sender, DataGridViewCellEventArgs e)
        {
            var senderGrid = (DataGridView)sender;
            if (e.RowIndex < 0) return;
            if (senderGrid.Columns[e.ColumnIndex].Name == "Delete")
            {
                var procName = (string)senderGrid.Rows[e.RowIndex].Cells["Name"].Value;
                os.RemoveProcess(procName);
            }
        }

        private void FirstExampleClick(object sender, EventArgs e)
        {
            os.ClearProcesses();
            checkBox1.Checked = false;
            os.AddProcess(new Process("LOLzinho", Process.Priorities.High, null));
            os.AddProcess(new Process("Youtube", Process.Priorities.Low, new Dependency("LOLzinho", .8F)));
            os.AddProcess(new Process("Dota2", Process.Priorities.High, new Dependency("LOLzinho", 1F)));
            os.AddProcess(new Process("VideosMotivacionais", Process.Priorities.Medium, new Dependency("Youtube", 1F)));
            os.AddProcess(new Process("VingadoresUltimato", Process.Priorities.Low, new Dependency("Dota2", 1F)));
            os.AddProcess(new Process("Programar", Process.Priorities.High, new Dependency("VingadoresUltimato", .5F)));
        }

        private void UpdateCheckboxChanged(object sender, EventArgs e)
        {
            ShouldUpdate = checkBox1.Checked;
        }

        private void SecondExampleClick(object sender, EventArgs e)
        {
            os.ClearProcesses();
            checkBox1.Checked = false;
            os.AddProcess(new Process("Spotify", Process.Priorities.High, new Dependency("DriverAudio",.5F)));
            os.AddProcess(new Process("Chrome[Youtube]", Process.Priorities.High, new Dependency("Chrome[Facebook]", .3F)));
            os.AddProcess(new Process("Chrome[Facebook]", Process.Priorities.High, new Dependency("DriverVideo", .6F)));
            os.AddProcess(new Process("Chrome[Slither]", Process.Priorities.High, new Dependency("Chrome[twitter]", .1F)));
            os.AddProcess(new Process("Chrome[twitter]", Process.Priorities.High, new Dependency("Chrome[Youtube]", 1F)));
            os.AddProcess(new Process("NetBeans", Process.Priorities.Medium));
            os.AddProcess(new Process("Steam", Process.Priorities.Medium));
            os.AddProcess(new Process("CS:GO", Process.Priorities.Medium, new Dependency("Steam", .7F)));
            os.AddProcess(new Process("LOL", Process.Priorities.Low));
            os.AddProcess(new Process("Origin", Process.Priorities.Low));
            os.AddProcess(new Process("Bf5", Process.Priorities.Low, new Dependency("Origin", 1F)));
            os.AddProcess(new Process("CodeBlocks", Process.Priorities.Low));
            os.AddProcess(new Process("MediaPlayer", Process.Priorities.Low, new Dependency("DriverAudio", 1F)));
            os.AddProcess(new Process("DriverVideo", Process.Priorities.High));
            os.AddProcess(new Process("DriverAudio", Process.Priorities.High));
            os.AddProcess(new Process("TaskManager", Process.Priorities.Low, new Dependency("VStudio", .75F)));
            os.AddProcess(new Process("C#Prog", Process.Priorities.Medium));
            os.AddProcess(new Process("VStudio", Process.Priorities.Medium));
            os.AddProcess(new Process("JavaProg", Process.Priorities.Medium, new Dependency("NetBeans", .75F)));
            os.AddProcess(new Process("CProg", Process.Priorities.Medium, new Dependency("CodeBlocks", .8F)));
        }

        private void ThirdExampleClick(object sender, EventArgs e)
        {
            os.ClearProcesses();
            checkBox1.Checked = false;
            os.AddProcess(new Process("NetBeans", Process.Priorities.High, new Dependency("MongoDB", 1F)));
            os.AddProcess(new Process("MongoDB", Process.Priorities.Medium));
            os.AddProcess(new Process("AttWindows", Process.Priorities.High));
            os.AddProcess(new Process("Chrome", Process.Priorities.Low));
            os.AddProcess(new Process("ChromeApp", Process.Priorities.High, new Dependency("NetBeans", .8F)));
            os.AddProcess(new Process("AttMongoDB", Process.Priorities.Medium));
        }

        private void ClearClick(object sender, EventArgs e)
        {
            os.ClearProcesses();
        }
    }
}

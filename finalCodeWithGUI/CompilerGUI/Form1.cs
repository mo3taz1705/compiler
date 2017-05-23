using System;
using System.IO;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using FastColoredTextBoxNS;
using System.Text.RegularExpressions;
using System.Diagnostics;

namespace WindowsFormsApplication2
{
    public partial class Compiler : Form
    {
        string currentPath = "";
        string[] keywords = { "int", "boolean", "constant", "if", "else", "while", "do", "switch", "case", "break", "default", "for", "true", "false", "and", "or", "not" };
        string[] snippets = { "if (^){\n\t\n}", "if (^){\n\t\n}\nelse {\n\t\n}", "for (^;;){\n\t\n}", "while (^){\n\t\n}", "do {\n\t^\n} while();", "switch (^){\n\tdefault : break;\n}", "if (^){\n\t\n }\nelse if (){\n\t\n }\nelse {\n\t\n}", "int main (){\n\t^\n}" };
        public Compiler()
        {
            InitializeComponent();
            //create autocomplete popup menu
            AutocompleteMenu popupMenu = new AutocompleteMenu(this.codeTextBox);
            BuildAutocompleteMenu(popupMenu);
            openFile.Filter = "C files (*.c)|*.c";
            saveFile.Filter = "C files (*.c)|*.c";
        }


        private void hideShowErrorToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (errorTextBox.Visible == true)
            {
                errorTextBox.Visible = false;
                errorWarnLabel.Visible = false;
            }
            else
            {
                errorWarnLabel.Visible = true;
                errorTextBox.Visible = true;
            }
        }

        private void hideShowSymTableToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (symTableGridView.Visible == true)
            {
                symTableGridView.Visible = false;
                symTableLabel.Visible = false;
            }
            else
            {
                symTableGridView.Visible = true;
                symTableLabel.Visible = true;
            }
        }

        private void openFileToolStripMenuItem_Click(object sender, EventArgs e)
        {
            codeTextBox.Text = "";
            if (openFile.ShowDialog() == DialogResult.OK)
            {
                currentPath = openFile.FileName.ToString();
                inputFileName.Text = "Input: " + openFile.SafeFileName.ToString();
                StreamReader file = new StreamReader(currentPath);
                String line;
                while ((line = file.ReadLine()) != null)
                {
                    codeTextBox.Text = codeTextBox.Text + line + '\n';
                }
                file.Close();
            }
        }

        private void newFileToolStripMenuItem_Click(object sender, EventArgs e)
        {
            createFile();
            codeTextBox.Text = "";
        }

        private void saveFileToolStripMenuItem_Click(object sender, EventArgs e)
        {
            save();
        }
        private bool createFile()
        {
            if (saveFile.ShowDialog() == DialogResult.OK)
            {
                currentPath = saveFile.FileName.ToString();
                string filename = Path.GetFileName(currentPath);
                inputFileName.Text = "Input: " + filename;
                return true;
            }
            return false;
        }
        private bool save()
        {
            bool created = true;
            if (currentPath == "")
            {
                created = createFile();
            }
            if (created)
            {
                File.WriteAllText(currentPath, codeTextBox.Text.ToString());
                return created;
            }
            else return created;
        }

        private void runToolStripMenuItem_Click(object sender, EventArgs e)
        {
            bool flag = save();
            if (flag)
            {
                codeCompile();
                errorWarnings();
                outputFile();
                symbolTable();
            }
            
        }
        private void codeCompile()
        {
            Process process = new System.Diagnostics.Process();
            process.StartInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden;
            process.StartInfo.CreateNoWindow = true;
            process.StartInfo.FileName = "python";
            process.StartInfo.Arguments = "compiler.py ";
            process.StartInfo.Arguments += '"' + currentPath + '"' + " ";
            process.StartInfo.UseShellExecute = false;
            process.Start();
            process.WaitForExit();
        }
        private void errorWarnings()
        {
            errorTextBox.Clear();
            String[] Lines = File.ReadAllLines(@"warns.txt");
            String str = "WARNING: ";
            int number_warning = Lines.Length;
            for (int i = 0; i < Lines.Length; i++)
            {
                errorTextBox.Text = this.errorTextBox.Text + str + Lines[i] + '\n';
            }
            Lines = File.ReadAllLines(@"errors.txt");
            str = "ERROR: ";
            int number_errors = Lines.Length;
            for (int i = 0; i < Lines.Length; i++)
            {
                errorTextBox.Text = errorTextBox.Text + str + Lines[i] + '\n';
            }
            errorWarnLabel.Text = "Error : " + number_errors.ToString() + " Warnings :" + number_warning.ToString();
        }
        private void outputFile()
        {
            outputTextBox.OpenFile(@"out.txt");
        }
        private void symbolTable()
        {
            //TODO
            try
            {
                String[] Lines = File.ReadAllLines(@"symtable.txt");
                File.Delete(@"symtable.txt");
                this.symTableGridView.Rows.Clear();
                for (int i = 0; i < Lines.Length; i++)
                    this.symTableGridView.Rows.Add();

                for (int i = 0; i < Lines.Length; i++)
                {
                    string[] cells = Lines[i].Split('\t');
                    symTableGridView.Rows[i].Cells[0].Value = cells[0];
                    symTableGridView.Rows[i].Cells[1].Value = cells[1];
                    symTableGridView.Rows[i].Cells[2].Value = cells[2];
                    symTableGridView.Rows[i].Cells[3].Value = cells[3];
                }
            }
            catch
            {
                //Do nothing
            }
            
        }

        private void BuildAutocompleteMenu(AutocompleteMenu popupMenu)
        {
            List<AutocompleteItem> items = new List<AutocompleteItem>();

            foreach (var item in snippets)
                items.Add(new SnippetAutocompleteItem(item));
            foreach (var item in keywords)
                items.Add(new AutocompleteItem(item));

            items.Add(new InsertSpaceSnippet());
            items.Add(new InsertSpaceSnippet(@"^(\w+)([=<>!:]+)(\w+)$"));
            items.Add(new InsertEnterSnippet());

            //set as autocomplete source
            popupMenu.Items.SetAutocompleteItems(items);
            popupMenu.SearchPattern = @"[\w\.:=!<>]";
        }
        class InsertSpaceSnippet : AutocompleteItem
        {
            string pattern;

            public InsertSpaceSnippet(string pattern)
                : base("")
            {
                this.pattern = pattern;
            }

            public InsertSpaceSnippet()
                : this(@"^(\d+)([a-zA-Z_]+)(\d*)$")
            {
            }

            public override CompareResult Compare(string fragmentText)
            {
                if (Regex.IsMatch(fragmentText, pattern))
                {
                    Text = InsertSpaces(fragmentText);
                    if (Text != fragmentText)
                        return CompareResult.Visible;
                }
                return CompareResult.Hidden;
            }

            public string InsertSpaces(string fragment)
            {
                var m = Regex.Match(fragment, pattern);
                if (m == null)
                    return fragment;
                if (m.Groups[1].Value == "" && m.Groups[3].Value == "")
                    return fragment;
                return (m.Groups[1].Value + " " + m.Groups[2].Value + " " + m.Groups[3].Value).Trim();
            }

            public override string ToolTipTitle
            {
                get
                {
                    return Text;
                }
            }
        }

        /// <summary>
        /// Inerts line break after '}'
        /// </summary>
        class InsertEnterSnippet : AutocompleteItem
        {
            Place enterPlace = Place.Empty;

            public InsertEnterSnippet()
                : base("[Line break]")
            {
            }

            public override CompareResult Compare(string fragmentText)
            {
                var r = Parent.Fragment.Clone();
                while (r.Start.iChar > 0)
                {
                    if (r.CharBeforeStart == '}')
                    {
                        enterPlace = r.Start;
                        return CompareResult.Visible;
                    }

                    r.GoLeftThroughFolded();
                }

                return CompareResult.Hidden;
            }

            public override string GetTextForReplace()
            {
                //extend range
                Range r = Parent.Fragment;
                Place end = r.End;
                r.Start = enterPlace;
                r.End = r.End;
                //insert line break
                return Environment.NewLine + r.Text;
            }

            public override void OnSelected(AutocompleteMenu popupMenu, SelectedEventArgs e)
            {
                base.OnSelected(popupMenu, e);
                if (Parent.Fragment.tb.AutoIndent)
                    Parent.Fragment.tb.DoAutoIndent();
            }

            public override string ToolTipTitle
            {
                get
                {
                    return "Insert line break after '}'";
                }
            }
        }

        
    }
}

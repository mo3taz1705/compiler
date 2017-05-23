namespace WindowsFormsApplication2
{
    partial class Compiler
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Compiler));
            this.menu = new System.Windows.Forms.MenuStrip();
            this.fileToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.openFileToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.newFileToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.saveFileToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.optionToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.hideShowErrorToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.hideShowSymTableToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.codeToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.runToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.inputFileName = new System.Windows.Forms.Label();
            this.outputFileName = new System.Windows.Forms.Label();
            this.errorWarnLabel = new System.Windows.Forms.Label();
            this.symTableGridView = new System.Windows.Forms.DataGridView();
            this.ColName = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Scope = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Type = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Constant = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.symTableLabel = new System.Windows.Forms.Label();
            this.openFile = new System.Windows.Forms.OpenFileDialog();
            this.saveFile = new System.Windows.Forms.SaveFileDialog();
            this.codeTextBox = new FastColoredTextBoxNS.FastColoredTextBox();
            this.outputTextBox = new FastColoredTextBoxNS.FastColoredTextBox();
            this.errorTextBox = new FastColoredTextBoxNS.FastColoredTextBox();
            this.menu.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.symTableGridView)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.codeTextBox)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.outputTextBox)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.errorTextBox)).BeginInit();
            this.SuspendLayout();
            // 
            // menu
            // 
            this.menu.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.fileToolStripMenuItem,
            this.optionToolStripMenuItem,
            this.codeToolStripMenuItem});
            this.menu.Location = new System.Drawing.Point(0, 0);
            this.menu.Name = "menu";
            this.menu.Size = new System.Drawing.Size(957, 24);
            this.menu.TabIndex = 0;
            this.menu.Text = "menu";
            // 
            // fileToolStripMenuItem
            // 
            this.fileToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.openFileToolStripMenuItem,
            this.newFileToolStripMenuItem,
            this.saveFileToolStripMenuItem});
            this.fileToolStripMenuItem.Name = "fileToolStripMenuItem";
            this.fileToolStripMenuItem.Size = new System.Drawing.Size(37, 20);
            this.fileToolStripMenuItem.Text = "File";
            // 
            // openFileToolStripMenuItem
            // 
            this.openFileToolStripMenuItem.Name = "openFileToolStripMenuItem";
            this.openFileToolStripMenuItem.Size = new System.Drawing.Size(124, 22);
            this.openFileToolStripMenuItem.Text = "Open File";
            this.openFileToolStripMenuItem.Click += new System.EventHandler(this.openFileToolStripMenuItem_Click);
            // 
            // newFileToolStripMenuItem
            // 
            this.newFileToolStripMenuItem.Name = "newFileToolStripMenuItem";
            this.newFileToolStripMenuItem.Size = new System.Drawing.Size(124, 22);
            this.newFileToolStripMenuItem.Text = "New File";
            this.newFileToolStripMenuItem.Click += new System.EventHandler(this.newFileToolStripMenuItem_Click);
            // 
            // saveFileToolStripMenuItem
            // 
            this.saveFileToolStripMenuItem.Name = "saveFileToolStripMenuItem";
            this.saveFileToolStripMenuItem.Size = new System.Drawing.Size(124, 22);
            this.saveFileToolStripMenuItem.Text = "Save File";
            this.saveFileToolStripMenuItem.Click += new System.EventHandler(this.saveFileToolStripMenuItem_Click);
            // 
            // optionToolStripMenuItem
            // 
            this.optionToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.hideShowErrorToolStripMenuItem,
            this.hideShowSymTableToolStripMenuItem});
            this.optionToolStripMenuItem.Name = "optionToolStripMenuItem";
            this.optionToolStripMenuItem.Size = new System.Drawing.Size(56, 20);
            this.optionToolStripMenuItem.Text = "Option";
            // 
            // hideShowErrorToolStripMenuItem
            // 
            this.hideShowErrorToolStripMenuItem.Name = "hideShowErrorToolStripMenuItem";
            this.hideShowErrorToolStripMenuItem.Size = new System.Drawing.Size(187, 22);
            this.hideShowErrorToolStripMenuItem.Text = "Hide/Show Error";
            this.hideShowErrorToolStripMenuItem.Click += new System.EventHandler(this.hideShowErrorToolStripMenuItem_Click);
            // 
            // hideShowSymTableToolStripMenuItem
            // 
            this.hideShowSymTableToolStripMenuItem.Name = "hideShowSymTableToolStripMenuItem";
            this.hideShowSymTableToolStripMenuItem.Size = new System.Drawing.Size(187, 22);
            this.hideShowSymTableToolStripMenuItem.Text = "Hide/Show SymTable";
            this.hideShowSymTableToolStripMenuItem.Click += new System.EventHandler(this.hideShowSymTableToolStripMenuItem_Click);
            // 
            // codeToolStripMenuItem
            // 
            this.codeToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.runToolStripMenuItem});
            this.codeToolStripMenuItem.Name = "codeToolStripMenuItem";
            this.codeToolStripMenuItem.Size = new System.Drawing.Size(47, 20);
            this.codeToolStripMenuItem.Text = "Code";
            // 
            // runToolStripMenuItem
            // 
            this.runToolStripMenuItem.Name = "runToolStripMenuItem";
            this.runToolStripMenuItem.Size = new System.Drawing.Size(95, 22);
            this.runToolStripMenuItem.Text = "Run";
            this.runToolStripMenuItem.Click += new System.EventHandler(this.runToolStripMenuItem_Click);
            // 
            // inputFileName
            // 
            this.inputFileName.AutoSize = true;
            this.inputFileName.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.inputFileName.Location = new System.Drawing.Point(13, 28);
            this.inputFileName.Name = "inputFileName";
            this.inputFileName.Size = new System.Drawing.Size(56, 24);
            this.inputFileName.TabIndex = 3;
            this.inputFileName.Text = "Input:";
            // 
            // outputFileName
            // 
            this.outputFileName.AutoSize = true;
            this.outputFileName.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.outputFileName.Location = new System.Drawing.Point(495, 34);
            this.outputFileName.Name = "outputFileName";
            this.outputFileName.Size = new System.Drawing.Size(71, 24);
            this.outputFileName.TabIndex = 4;
            this.outputFileName.Text = "Output:";
            // 
            // errorWarnLabel
            // 
            this.errorWarnLabel.AutoSize = true;
            this.errorWarnLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.errorWarnLabel.Location = new System.Drawing.Point(12, 371);
            this.errorWarnLabel.Name = "errorWarnLabel";
            this.errorWarnLabel.Size = new System.Drawing.Size(165, 24);
            this.errorWarnLabel.TabIndex = 7;
            this.errorWarnLabel.Text = "Error and Warning";
            // 
            // symTableGridView
            // 
            this.symTableGridView.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.symTableGridView.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.ColName,
            this.Scope,
            this.Type,
            this.Constant});
            this.symTableGridView.Location = new System.Drawing.Point(498, 404);
            this.symTableGridView.Name = "symTableGridView";
            this.symTableGridView.ReadOnly = true;
            this.symTableGridView.Size = new System.Drawing.Size(441, 177);
            this.symTableGridView.TabIndex = 8;
            // 
            // ColName
            // 
            this.ColName.HeaderText = "Name";
            this.ColName.Name = "ColName";
            this.ColName.ReadOnly = true;
            // 
            // Scope
            // 
            this.Scope.HeaderText = "scope";
            this.Scope.Name = "Scope";
            this.Scope.ReadOnly = true;
            // 
            // Type
            // 
            this.Type.HeaderText = "Level";
            this.Type.Name = "Level";
            this.Type.ReadOnly = true;
            // 
            // Constant
            // 
            this.Constant.HeaderText = "Enclosing scope";
            this.Constant.Name = "Enclosing scope";
            this.Constant.ReadOnly = true;
            // 
            // symTableLabel
            // 
            this.symTableLabel.AutoSize = true;
            this.symTableLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.symTableLabel.Location = new System.Drawing.Point(494, 371);
            this.symTableLabel.Name = "symTableLabel";
            this.symTableLabel.Size = new System.Drawing.Size(126, 24);
            this.symTableLabel.TabIndex = 9;
            this.symTableLabel.Text = "Symbol Table";
            // 
            // openFile
            // 
            this.openFile.FileName = "open File";
            // 
            // codeTextBox
            // 
            this.codeTextBox.AutoCompleteBrackets = true;
            this.codeTextBox.AutoCompleteBracketsList = new char[] {
        '(',
        ')',
        '{',
        '}',
        '[',
        ']',
        '\"',
        '\"',
        '\'',
        '\''};
            this.codeTextBox.AutoIndentCharsPatterns = "\r\n^\\s*[\\w\\.]+(\\s\\w+)?\\s*(?<range>=)\\s*(?<range>[^;]+);\r\n^\\s*(case|default)\\s*[^:]" +
    "*(?<range>:)\\s*(?<range>[^;]+);\r\n";
            this.codeTextBox.AutoScrollMinSize = new System.Drawing.Size(29, 18);
            this.codeTextBox.BackBrush = null;
            this.codeTextBox.BracketsHighlightStrategy = FastColoredTextBoxNS.BracketsHighlightStrategy.Strategy2;
            this.codeTextBox.CharHeight = 18;
            this.codeTextBox.CharWidth = 9;
            this.codeTextBox.Cursor = System.Windows.Forms.Cursors.IBeam;
            this.codeTextBox.DisabledColor = System.Drawing.Color.FromArgb(((int)(((byte)(100)))), ((int)(((byte)(180)))), ((int)(((byte)(180)))), ((int)(((byte)(180)))));
            this.codeTextBox.Font = new System.Drawing.Font("Consolas", 12F);
            this.codeTextBox.IsReplaceMode = false;
            this.codeTextBox.Language = FastColoredTextBoxNS.Language.CSharp;
            this.codeTextBox.LeftBracket = '(';
            this.codeTextBox.LeftBracket2 = '{';
            this.codeTextBox.Location = new System.Drawing.Point(12, 61);
            this.codeTextBox.Name = "codeTextBox";
            this.codeTextBox.Paddings = new System.Windows.Forms.Padding(0);
            this.codeTextBox.RightBracket = ')';
            this.codeTextBox.RightBracket2 = '}';
            this.codeTextBox.SelectionColor = System.Drawing.Color.FromArgb(((int)(((byte)(60)))), ((int)(((byte)(0)))), ((int)(((byte)(0)))), ((int)(((byte)(255)))));
            this.codeTextBox.ServiceColors = ((FastColoredTextBoxNS.ServiceColors)(resources.GetObject("codeTextBox.ServiceColors")));
            this.codeTextBox.Size = new System.Drawing.Size(429, 288);
            this.codeTextBox.TabIndex = 13;
            this.codeTextBox.Zoom = 100;
            // 
            // outputTextBox
            // 
            this.outputTextBox.AutoCompleteBrackets = true;
            this.outputTextBox.AutoCompleteBracketsList = new char[] {
        '(',
        ')',
        '{',
        '}',
        '[',
        ']',
        '\"',
        '\"',
        '\'',
        '\''};
            this.outputTextBox.AutoIndentCharsPatterns = "\r\n^\\s*[\\w\\.]+(\\s\\w+)?\\s*(?<range>=)\\s*(?<range>[^;]+);\r\n^\\s*(case|default)\\s*[^:]" +
    "*(?<range>:)\\s*(?<range>[^;]+);\r\n";
            this.outputTextBox.AutoScrollMinSize = new System.Drawing.Size(29, 18);
            this.outputTextBox.BackBrush = null;
            this.outputTextBox.BracketsHighlightStrategy = FastColoredTextBoxNS.BracketsHighlightStrategy.Strategy2;
            this.outputTextBox.CharHeight = 18;
            this.outputTextBox.CharWidth = 9;
            this.outputTextBox.Cursor = System.Windows.Forms.Cursors.IBeam;
            this.outputTextBox.DisabledColor = System.Drawing.Color.FromArgb(((int)(((byte)(100)))), ((int)(((byte)(180)))), ((int)(((byte)(180)))), ((int)(((byte)(180)))));
            this.outputTextBox.Font = new System.Drawing.Font("Consolas", 12F);
            this.outputTextBox.IsReplaceMode = false;
            this.outputTextBox.Language = FastColoredTextBoxNS.Language.CSharp;
            this.outputTextBox.LeftBracket = '(';
            this.outputTextBox.LeftBracket2 = '{';
            this.outputTextBox.Location = new System.Drawing.Point(499, 61);
            this.outputTextBox.Name = "outputTextBox";
            this.outputTextBox.Paddings = new System.Windows.Forms.Padding(0);
            this.outputTextBox.ReadOnly = true;
            this.outputTextBox.RightBracket = ')';
            this.outputTextBox.RightBracket2 = '}';
            this.outputTextBox.SelectionColor = System.Drawing.Color.FromArgb(((int)(((byte)(60)))), ((int)(((byte)(0)))), ((int)(((byte)(0)))), ((int)(((byte)(255)))));
            this.outputTextBox.ServiceColors = ((FastColoredTextBoxNS.ServiceColors)(resources.GetObject("outputTextBox.ServiceColors")));
            this.outputTextBox.Size = new System.Drawing.Size(429, 288);
            this.outputTextBox.TabIndex = 14;
            this.outputTextBox.Zoom = 100;
            // 
            // errorTextBox
            // 
            this.errorTextBox.AutoCompleteBrackets = true;
            this.errorTextBox.AutoCompleteBracketsList = new char[] {
        '(',
        ')',
        '{',
        '}',
        '[',
        ']',
        '\"',
        '\"',
        '\'',
        '\''};
            this.errorTextBox.AutoIndentCharsPatterns = "\r\n^\\s*[\\w\\.]+(\\s\\w+)?\\s*(?<range>=)\\s*(?<range>[^;]+);\r\n^\\s*(case|default)\\s*[^:]" +
    "*(?<range>:)\\s*(?<range>[^;]+);\r\n";
            this.errorTextBox.AutoScrollMinSize = new System.Drawing.Size(29, 18);
            this.errorTextBox.BackBrush = null;
            this.errorTextBox.BracketsHighlightStrategy = FastColoredTextBoxNS.BracketsHighlightStrategy.Strategy2;
            this.errorTextBox.CharHeight = 18;
            this.errorTextBox.CharWidth = 9;
            this.errorTextBox.Cursor = System.Windows.Forms.Cursors.IBeam;
            this.errorTextBox.DisabledColor = System.Drawing.Color.FromArgb(((int)(((byte)(100)))), ((int)(((byte)(180)))), ((int)(((byte)(180)))), ((int)(((byte)(180)))));
            this.errorTextBox.Font = new System.Drawing.Font("Consolas", 12F);
            this.errorTextBox.IsReplaceMode = false;
            this.errorTextBox.Language = FastColoredTextBoxNS.Language.CSharp;
            this.errorTextBox.LeftBracket = '(';
            this.errorTextBox.LeftBracket2 = '{';
            this.errorTextBox.LineNumberColor = System.Drawing.Color.Transparent;
            this.errorTextBox.Location = new System.Drawing.Point(17, 404);
            this.errorTextBox.Name = "errorTextBox";
            this.errorTextBox.Paddings = new System.Windows.Forms.Padding(0);
            this.errorTextBox.ReadOnly = true;
            this.errorTextBox.RightBracket = ')';
            this.errorTextBox.RightBracket2 = '}';
            this.errorTextBox.SelectionColor = System.Drawing.Color.FromArgb(((int)(((byte)(60)))), ((int)(((byte)(0)))), ((int)(((byte)(0)))), ((int)(((byte)(255)))));
            this.errorTextBox.ServiceColors = ((FastColoredTextBoxNS.ServiceColors)(resources.GetObject("errorTextBox.ServiceColors")));
            this.errorTextBox.Size = new System.Drawing.Size(424, 177);
            this.errorTextBox.TabIndex = 15;
            this.errorTextBox.Zoom = 100;
            // 
            // Compiler
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(957, 621);
            this.Controls.Add(this.errorTextBox);
            this.Controls.Add(this.outputTextBox);
            this.Controls.Add(this.codeTextBox);
            this.Controls.Add(this.symTableLabel);
            this.Controls.Add(this.symTableGridView);
            this.Controls.Add(this.errorWarnLabel);
            this.Controls.Add(this.outputFileName);
            this.Controls.Add(this.inputFileName);
            this.Controls.Add(this.menu);
            this.MainMenuStrip = this.menu;
            this.Name = "Compiler";
            this.Text = "Compiler Gui";
            this.menu.ResumeLayout(false);
            this.menu.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.symTableGridView)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.codeTextBox)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.outputTextBox)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.errorTextBox)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menu;
        private System.Windows.Forms.ToolStripMenuItem optionToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem hideShowErrorToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem hideShowSymTableToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem codeToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem runToolStripMenuItem;
        private System.Windows.Forms.Label inputFileName;
        private System.Windows.Forms.Label outputFileName;
        private System.Windows.Forms.Label errorWarnLabel;
        private System.Windows.Forms.DataGridView symTableGridView;
        private System.Windows.Forms.Label symTableLabel;
        private System.Windows.Forms.DataGridViewTextBoxColumn ColName;
        private System.Windows.Forms.DataGridViewTextBoxColumn Scope;
        private System.Windows.Forms.DataGridViewTextBoxColumn Type;
        private System.Windows.Forms.DataGridViewTextBoxColumn Constant;
        private System.Windows.Forms.OpenFileDialog openFile;
        private System.Windows.Forms.SaveFileDialog saveFile;
        private System.Windows.Forms.ToolStripMenuItem fileToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem openFileToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem newFileToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem saveFileToolStripMenuItem;
        private FastColoredTextBoxNS.FastColoredTextBox codeTextBox;
        private FastColoredTextBoxNS.FastColoredTextBox outputTextBox;
        private FastColoredTextBoxNS.FastColoredTextBox errorTextBox;
    }
}


namespace WindowsFormsApp1
{
  partial class Form1
  {
    /// <summary>
    /// 필수 디자이너 변수입니다.
    /// </summary>
    private System.ComponentModel.IContainer components = null;

    /// <summary>
    /// 사용 중인 모든 리소스를 정리합니다.
    /// </summary>
    /// <param name="disposing">관리되는 리소스를 삭제해야 하면 true이고, 그렇지 않으면 false입니다.</param>
    protected override void Dispose(bool disposing)
    {
      if (disposing && (components != null))
      {
        components.Dispose();
      }
      base.Dispose(disposing);
    }

    #region Windows Form 디자이너에서 생성한 코드

    /// <summary>
    /// 디자이너 지원에 필요한 메서드입니다. 
    /// 이 메서드의 내용을 코드 편집기로 수정하지 마세요.
    /// </summary>
    private void InitializeComponent()
    {
      this.Search_btn = new System.Windows.Forms.Button();
      this.listBox1 = new System.Windows.Forms.ListBox();
      this.textBox1 = new System.Windows.Forms.TextBox();
      this.SearchResult_btn = new System.Windows.Forms.Button();
      this.BlackGroundSearch_btn = new System.Windows.Forms.Button();
      this.label1 = new System.Windows.Forms.Label();
      this.label2 = new System.Windows.Forms.Label();
      this.label3 = new System.Windows.Forms.Label();
      this.label4 = new System.Windows.Forms.Label();
      this.listBox2 = new System.Windows.Forms.ListBox();
      this.ListBoxReset_btn = new System.Windows.Forms.Button();
      this.WindowClose_btn = new System.Windows.Forms.Button();
      this.label7 = new System.Windows.Forms.Label();
      this.SuspendLayout();
      // 
      // Search_btn
      // 
      this.Search_btn.BackColor = System.Drawing.Color.Khaki;
      this.Search_btn.Location = new System.Drawing.Point(64, 165);
      this.Search_btn.Name = "Search_btn";
      this.Search_btn.Size = new System.Drawing.Size(258, 61);
      this.Search_btn.TabIndex = 0;
      this.Search_btn.Text = "네이버 창 모드 검색";
      this.Search_btn.UseVisualStyleBackColor = false;
      this.Search_btn.Click += new System.EventHandler(this.Search_btn_Click);
      // 
      // listBox1
      // 
      this.listBox1.FormattingEnabled = true;
      this.listBox1.ItemHeight = 12;
      this.listBox1.Location = new System.Drawing.Point(365, 165);
      this.listBox1.Name = "listBox1";
      this.listBox1.Size = new System.Drawing.Size(663, 136);
      this.listBox1.TabIndex = 1;
      // 
      // textBox1
      // 
      this.textBox1.Font = new System.Drawing.Font("Calibri", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
      this.textBox1.Location = new System.Drawing.Point(64, 108);
      this.textBox1.Multiline = true;
      this.textBox1.Name = "textBox1";
      this.textBox1.Size = new System.Drawing.Size(258, 38);
      this.textBox1.TabIndex = 3;
      // 
      // SearchResult_btn
      // 
      this.SearchResult_btn.BackColor = System.Drawing.Color.OliveDrab;
      this.SearchResult_btn.Location = new System.Drawing.Point(64, 327);
      this.SearchResult_btn.Name = "SearchResult_btn";
      this.SearchResult_btn.Size = new System.Drawing.Size(258, 54);
      this.SearchResult_btn.TabIndex = 4;
      this.SearchResult_btn.Text = "검색 결과 보기";
      this.SearchResult_btn.UseVisualStyleBackColor = false;
      this.SearchResult_btn.Click += new System.EventHandler(this.SearchResult_btn_Click);
      // 
      // BlackGroundSearch_btn
      // 
      this.BlackGroundSearch_btn.BackColor = System.Drawing.Color.Gold;
      this.BlackGroundSearch_btn.Location = new System.Drawing.Point(64, 247);
      this.BlackGroundSearch_btn.Name = "BlackGroundSearch_btn";
      this.BlackGroundSearch_btn.Size = new System.Drawing.Size(258, 54);
      this.BlackGroundSearch_btn.TabIndex = 5;
      this.BlackGroundSearch_btn.Text = "네이버 백그라운드 검색";
      this.BlackGroundSearch_btn.UseVisualStyleBackColor = false;
      this.BlackGroundSearch_btn.Click += new System.EventHandler(this.BlackGroundSearch_btn_Click);
      // 
      // label1
      // 
      this.label1.BackColor = System.Drawing.SystemColors.InactiveCaption;
      this.label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
      this.label1.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
      this.label1.Font = new System.Drawing.Font("Calibri", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
      this.label1.Location = new System.Drawing.Point(365, 9);
      this.label1.Name = "label1";
      this.label1.Size = new System.Drawing.Size(663, 67);
      this.label1.TabIndex = 6;
      this.label1.Text = "Search Result Print";
      this.label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
      // 
      // label2
      // 
      this.label2.BackColor = System.Drawing.SystemColors.InactiveCaption;
      this.label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
      this.label2.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
      this.label2.Font = new System.Drawing.Font("Calibri", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
      this.label2.Location = new System.Drawing.Point(64, 9);
      this.label2.Name = "label2";
      this.label2.Size = new System.Drawing.Size(258, 67);
      this.label2.TabIndex = 7;
      this.label2.Text = "Search Text Insert";
      this.label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
      // 
      // label3
      // 
      this.label3.BackColor = System.Drawing.SystemColors.GradientActiveCaption;
      this.label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
      this.label3.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
      this.label3.Font = new System.Drawing.Font("Calibri", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
      this.label3.Location = new System.Drawing.Point(365, 108);
      this.label3.Name = "label3";
      this.label3.Size = new System.Drawing.Size(663, 38);
      this.label3.TabIndex = 8;
      this.label3.Text = "Blog";
      this.label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
      // 
      // label4
      // 
      this.label4.BackColor = System.Drawing.SystemColors.GradientActiveCaption;
      this.label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
      this.label4.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
      this.label4.Font = new System.Drawing.Font("Calibri", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
      this.label4.Location = new System.Drawing.Point(365, 330);
      this.label4.Name = "label4";
      this.label4.Size = new System.Drawing.Size(663, 43);
      this.label4.TabIndex = 9;
      this.label4.Text = "Video";
      this.label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
      // 
      // listBox2
      // 
      this.listBox2.FormattingEnabled = true;
      this.listBox2.ItemHeight = 12;
      this.listBox2.Location = new System.Drawing.Point(365, 395);
      this.listBox2.Name = "listBox2";
      this.listBox2.Size = new System.Drawing.Size(663, 184);
      this.listBox2.TabIndex = 10;
      // 
      // ListBoxReset_btn
      // 
      this.ListBoxReset_btn.BackColor = System.Drawing.Color.YellowGreen;
      this.ListBoxReset_btn.Location = new System.Drawing.Point(64, 395);
      this.ListBoxReset_btn.Name = "ListBoxReset_btn";
      this.ListBoxReset_btn.Size = new System.Drawing.Size(258, 62);
      this.ListBoxReset_btn.TabIndex = 13;
      this.ListBoxReset_btn.Text = "리스트박스 선택 초기화";
      this.ListBoxReset_btn.UseVisualStyleBackColor = false;
      this.ListBoxReset_btn.Click += new System.EventHandler(this.ListBoxReset_btn_Click);
      // 
      // WindowClose_btn
      // 
      this.WindowClose_btn.BackColor = System.Drawing.Color.Azure;
      this.WindowClose_btn.Location = new System.Drawing.Point(64, 525);
      this.WindowClose_btn.Name = "WindowClose_btn";
      this.WindowClose_btn.Size = new System.Drawing.Size(258, 54);
      this.WindowClose_btn.TabIndex = 16;
      this.WindowClose_btn.Text = "열린 창 닫기";
      this.WindowClose_btn.UseVisualStyleBackColor = false;
      this.WindowClose_btn.Click += new System.EventHandler(this.WindowClose_btn_Click);
      // 
      // label7
      // 
      this.label7.BackColor = System.Drawing.SystemColors.Info;
      this.label7.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
      this.label7.Font = new System.Drawing.Font("Calibri", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
      this.label7.ForeColor = System.Drawing.Color.Red;
      this.label7.Location = new System.Drawing.Point(64, 492);
      this.label7.Name = "label7";
      this.label7.Size = new System.Drawing.Size(258, 23);
      this.label7.TabIndex = 17;
      this.label7.Text = "* 주의 : 모든 크롬 창을 닫습니다.";
      this.label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
      // 
      // Form1
      // 
      this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.None;
      this.ClientSize = new System.Drawing.Size(1050, 607);
      this.Controls.Add(this.label7);
      this.Controls.Add(this.WindowClose_btn);
      this.Controls.Add(this.ListBoxReset_btn);
      this.Controls.Add(this.listBox2);
      this.Controls.Add(this.label4);
      this.Controls.Add(this.label3);
      this.Controls.Add(this.label2);
      this.Controls.Add(this.label1);
      this.Controls.Add(this.BlackGroundSearch_btn);
      this.Controls.Add(this.SearchResult_btn);
      this.Controls.Add(this.textBox1);
      this.Controls.Add(this.listBox1);
      this.Controls.Add(this.Search_btn);
      this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
      this.Name = "Form1";
      this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
      this.Text = "네이버 검색 동영상 / 블로그 크롤러 (ver 0.1 Created by 트레커)";
      this.ResumeLayout(false);
      this.PerformLayout();

    }

        #endregion

        private System.Windows.Forms.Button Search_btn;
        private System.Windows.Forms.ListBox listBox1;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.Button SearchResult_btn;
        private System.Windows.Forms.Button BlackGroundSearch_btn;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.ListBox listBox2;
        private System.Windows.Forms.Button ListBoxReset_btn;
        private System.Windows.Forms.Button WindowClose_btn;
        private System.Windows.Forms.Label label7;
    }
}


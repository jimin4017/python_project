using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using System;
using System.Diagnostics;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
  public partial class Form1 : Form
  {
    string result1,result2,result3,result4,result5,result6,result7,result8;

    public Form1()
    {
      InitializeComponent();
    }
    private void Search_btn_Click(object sender, EventArgs e)
    {
      ChromeDriverService service = ChromeDriverService.CreateDefaultService();
      service.HideCommandPromptWindow = true;

      IWebDriver driver = new ChromeDriver(service);
      driver.Url = "https://www.naver.com";
      driver.FindElement(By.Name("query")).SendKeys(textBox1.Text);
      driver.FindElement(By.Id("search_btn")).Click();
      listBox1.Items.Clear();
      listBox2.Items.Clear();

      try
      {
        listBox1.Items.Add(driver.FindElement(By.XPath("//*[@id=\"sp_blog_1\"]/dl/dt/a")).Text);
        result1 = driver.FindElement(By.XPath("//*[@id=\"sp_blog_1\"]/dl/dd[3]/span/a[2]")).Text;
        listBox1.Items.Add(driver.FindElement(By.XPath("//*[@id=\"sp_blog_2\"]/dl/dt/a")).Text);
        result2 = driver.FindElement(By.XPath("//*[@id=\"sp_blog_2\"]/dl/dd[3]/span/a[2]")).Text;
        listBox1.Items.Add(driver.FindElement(By.XPath("//*[@id=\"sp_blog_3\"]/dl/dt/a")).Text);
        result3 = driver.FindElement(By.XPath("//*[@id=\"sp_blog_3\"]/dl/dd[3]/span/a[2]")).Text;
        listBox1.Items.Add(driver.FindElement(By.XPath("//*[@id=\"sp_blog_4\"]/dl/dt/a")).Text);
        result4 = driver.FindElement(By.XPath("//*[@id=\"sp_blog_4\"]/dl/dd[3]/span/a[2]")).Text;
      }

      catch { listBox1.Items.Add("블로그가 없습니다."); }

      try
      {
        listBox2.Items.Add(driver.FindElement(By.XPath("//*[@id=\"videoItem0\"]/dl/dt/a")).Text);
        result5 = driver.FindElement(By.XPath("//*[@id=\"videoItem0\"]/dl/dt/a")).GetAttribute("href");
        listBox2.Items.Add(driver.FindElement(By.XPath("//*[@id=\"videoItem1\"]/dl/dt/a")).Text);
        result6 = driver.FindElement(By.XPath("//*[@id=\"videoItem1\"]/dl/dt/a")).GetAttribute("href");
        listBox2.Items.Add(driver.FindElement(By.XPath("//*[@id=\"videoItem2\"]/dl/dt/a")).Text);
        result7 = driver.FindElement(By.XPath("//*[@id=\"videoItem2\"]/dl/dt/a")).GetAttribute("href");
        listBox2.Items.Add(driver.FindElement(By.XPath("//*[@id=\"videoItem3\"]/dl/dt/a")).Text);
        result8 = driver.FindElement(By.XPath("//*[@id=\"videoItem3\"]/dl/dt/a")).GetAttribute("href");
      }
      catch { listBox2.Items.Add("동영상이 없습니다."); }
      if (driver.Manage().Window == null) driver.Close();        // 이렇게 하면 창은 남기고 드라이버만 닫을 수 있다.
    }
    private void SearchResult_btn_Click(object sender, EventArgs e)
    {
      ChromeDriverService service = ChromeDriverService.CreateDefaultService();
      service.HideCommandPromptWindow = true;
      IWebDriver driver = new ChromeDriver(service);
      //driver.Manage().Window.Maximize();
      if (listBox1.SelectedItem != null && listBox2.SelectedItem == null)
      {
        if (listBox1.SelectedIndex.Equals(0)) driver.Url = "http://" + result1;
        else if (listBox1.SelectedIndex.Equals(1)) driver.Url = "http://" + result2;
        else if (listBox1.SelectedIndex.Equals(2)) driver.Url = "http://" + result3;
        else if (listBox1.SelectedIndex.Equals(3)) driver.Url = "http://" + result4;
      }

      else if (listBox2.SelectedItem != null && listBox1.SelectedItem == null)
      {
        if (listBox2.SelectedIndex.Equals(0)) driver.Url = result5;
        else if (listBox2.SelectedIndex.Equals(1)) driver.Url = result6;
        else if (listBox2.SelectedIndex.Equals(2)) driver.Url = result7;
        else if (listBox2.SelectedIndex.Equals(3)) driver.Url = result8;
      }

      if(driver.Manage().Window == null) driver.Close();        // 이렇게 하면 창은 남기고 드라이버만 닫을 수 있다.
    }

    private void BlackGroundSearch_btn_Click(object sender, EventArgs e)
    {
      ChromeDriverService service = ChromeDriverService.CreateDefaultService();
      service.HideCommandPromptWindow = true;
      ChromeOptions options = new ChromeOptions();
      options.AddArguments("headless");
      IWebDriver driver = new ChromeDriver(service,options);
      driver.Url = "https://www.naver.com";
      driver.FindElement(By.Name("query")).SendKeys(textBox1.Text);
      driver.FindElement(By.Id("search_btn")).Click();
      listBox1.Items.Clear();
      listBox2.Items.Clear();

      try
      {
        listBox1.Items.Add(driver.FindElement(By.XPath("//*[@id=\"sp_blog_1\"]/dl/dt/a")).Text);
        result1 = driver.FindElement(By.XPath("//*[@id=\"sp_blog_1\"]/dl/dd[3]/span/a[2]")).Text;
        listBox1.Items.Add(driver.FindElement(By.XPath("//*[@id=\"sp_blog_2\"]/dl/dt/a")).Text);
        result2 = driver.FindElement(By.XPath("//*[@id=\"sp_blog_2\"]/dl/dd[3]/span/a[2]")).Text;
        listBox1.Items.Add(driver.FindElement(By.XPath("//*[@id=\"sp_blog_3\"]/dl/dt/a")).Text);
        result3 = driver.FindElement(By.XPath("//*[@id=\"sp_blog_3\"]/dl/dd[3]/span/a[2]")).Text;
        listBox1.Items.Add(driver.FindElement(By.XPath("//*[@id=\"sp_blog_4\"]/dl/dt/a")).Text);
        result4 = driver.FindElement(By.XPath("//*[@id=\"sp_blog_4\"]/dl/dd[3]/span/a[2]")).Text;
      }
      catch { listBox1.Items.Add("블로그가 없습니다."); }
      try
      {
        listBox2.Items.Add(driver.FindElement(By.XPath("//*[@id=\"videoItem0\"]/dl/dt/a")).Text);
        result5 = driver.FindElement(By.XPath("//*[@id=\"videoItem0\"]/dl/dt/a")).GetAttribute("href");
        listBox2.Items.Add(driver.FindElement(By.XPath("//*[@id=\"videoItem1\"]/dl/dt/a")).Text);
        result6 = driver.FindElement(By.XPath("//*[@id=\"videoItem1\"]/dl/dt/a")).GetAttribute("href");
        listBox2.Items.Add(driver.FindElement(By.XPath("//*[@id=\"videoItem2\"]/dl/dt/a")).Text);
        result7 = driver.FindElement(By.XPath("//*[@id=\"videoItem2\"]/dl/dt/a")).GetAttribute("href");
        listBox2.Items.Add(driver.FindElement(By.XPath("//*[@id=\"videoItem3\"]/dl/dt/a")).Text);
        result8 = driver.FindElement(By.XPath("//*[@id=\"videoItem3\"]/dl/dt/a")).GetAttribute("href");
      }
      catch { listBox2.Items.Add("동영상이 없습니다."); }
      driver.Close();
    }
    private void WindowClose_btn_Click(object sender, EventArgs e)
    {
      try
      {
        Process[] process = new Process[100];
        process = Process.GetProcessesByName("chrome");
        foreach (Process x in process) x.Kill();
        process = Process.GetProcessesByName("chromedriver");
        foreach (Process x in process) x.Kill();
        process = Process.GetProcessesByName("conhost");
        foreach (Process x in process) x.Kill();
      }
      catch { }
    }
    private void ListBoxReset_btn_Click(object sender, EventArgs e)
    {
      listBox1.SelectedItem = null;
      listBox2.SelectedItem = null;
    }
  }
}

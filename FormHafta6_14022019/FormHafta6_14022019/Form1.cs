using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace FormHafta6_14022019
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnTikla_Click(object sender, EventArgs e)
        {
            
             MessageBox.Show("Merhaba", "Hoşgeldin", MessageBoxButtons.OK, MessageBoxIcon.Information);
            
        }

        private void btnGiris_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Merhaba " + txtAdi.Text);
        }

        private void btnKontrol_Click(object sender, EventArgs e)
        {
            try
            {
                int parola = Int16.Parse(txtParola.Text);
                //parola = Convert.ToInt16(txtParola.Text);
                //İki tanımlama da int türüne dönüştürür
                string ad = txtKullanici.Text;


                if (ad == "admin" && parola == 123)
                {
                    MessageBox.Show("Giriş Başarılı");
                }
                else
                    MessageBox.Show("Giriş Başarısız");
            }
            catch (Exception)
            {

                MessageBox.Show("Lütfen geçerli bir değer giriniz");
            }
            
        }

        private void btnHesapla_Click(object sender, EventArgs e)
        {
            int sayi1 = Convert.ToInt16(txtSayi1.Text);
            int sayi2 = Convert.ToInt16(txtSayi2.Text);
            
            txtToplam.Text = (sayi1+sayi2).ToString();
        }

        private void btnHesapla2_Click(object sender, EventArgs e)
        {
            try
            {
                bool kontrol = true;
                int sayi1 = Convert.ToInt16(txtS1.Text);
                int sayi2 = Convert.ToInt16(txtS2.Text);
                int sonuc = 0;
                if (rbTopla.Checked)
                    sonuc = sayi1 + sayi2;
                else if (rbCarp.Checked)
                    sonuc = sayi1 * sayi2;
                else if (rbCikar.Checked)
                    sonuc = sayi1 - sayi2;
                else if (rbBol.Checked)
                    sonuc = sayi1 / sayi2;
                else
                    kontrol = false;

                if (!kontrol) //kontrol==false
                    MessageBox.Show("seçim yapınız");
                else
                    txtT.Text = sonuc.ToString();
            }
            catch(DivideByZeroException)
            {
                MessageBox.Show("Sayı sıfıra bölünemez.","Hata",MessageBoxButtons.OK,MessageBoxIcon.Error);
            }
            catch(FormatException)
            {
                MessageBox.Show("Sayı girişi yapınız.", "Hata", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            catch (Exception)
            {
                MessageBox.Show("Yönetici ile iletişime geçiniz.", "Hata", MessageBoxButtons.OK, MessageBoxIcon.Error);

            }
            
        }
    }
}

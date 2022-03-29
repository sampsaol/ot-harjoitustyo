import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luodut_kassapaate_ja_maksukortti_ovat_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)
        self.assertNotEqual(self.maksukortti, None)
    def test_pohja_kassa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_myydyt_lounaat_oikein(self):
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)

    def test_edullinen_toimii_kateisella(self):
        help = self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+(500-help))
        self.assertEqual(help, 260)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullinen_kateinen_ei_riita(self):
        help = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset,0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(help, 200)
    
    def test_maukas_toimii_kateisella(self):
        help = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+(500-help))
        self.assertEqual(help, 100)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukas_kateinen_ei_riita(self):
        help = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat,0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(help, 200)

    def test_edullinen_korttimaksu_toimii(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        help1 = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        help2 = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 0.4")
        self.assertEqual(help1, True)
        self.assertEqual(help2, False)
        self.assertEqual(self.kassapaate.edulliset, 4)

    def test_maukas_korttimaksu_toimii(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        help1 = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        help2 = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 2.0")
        self.assertEqual(help1, True)
        self.assertEqual(help2, False)
        self.assertEqual(self.kassapaate.maukkaat, 2)

    def test_kortille_lataus_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+500)
        self.assertEqual(str(self.maksukortti), "saldo: 15.0")
        help = self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(str(self.maksukortti), "saldo: 15.0")
        self.assertEqual(help, None)
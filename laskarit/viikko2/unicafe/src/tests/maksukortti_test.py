import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_saldo_kasvaa_oikein(self):
        self.maksukortti.lataa_rahaa(300)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 13.00 euroa")

    def test_saldo_vahenee(self):
        self.maksukortti.ota_rahaa(300)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.00 euroa")

    def test_saldo_ei_mene_alle_nollan(self):
        self.maksukortti.ota_rahaa(2000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahat_riittavat_palauttaa_true(self):
        arvo = self.maksukortti.ota_rahaa(300)
        self.assertEqual(arvo, True)

    def test_rahat_ei_riita_palauttaa_false(self):
        arvo = self.maksukortti.ota_rahaa(2000)
        self.assertEqual(arvo, False)

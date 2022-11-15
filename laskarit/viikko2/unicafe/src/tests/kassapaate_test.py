import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_alkuraha_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_myydyt_edulliset_alkuun_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_myydyt_maukkaat_alkuun_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_edulliset_kateinen_nousee(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    def test_kateisosto_edulliset_lounaat_nousee(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset, 1)
    def test_kateisosto_edulliset_palautus_toimii(self):
        palautus = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(palautus, 60)

    def test_kateisosto_edulliset_kateinen_ei_nouse(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    def test_kateisosto_edulliset_lounaat_ei_nouse(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)
    def test_kateisosto_edulliset_palautus_toimii_kun_ei_riittavasti_rahaa(self):
        palautus = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(palautus, 200)

    def test_kateisosto_maukkaat_kateinen_nousee(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    def test_kateisosto_maukkaat_lounaat_nousee(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    def test_kateisosto_maukkaat_palautus_toimii(self):
        palautus = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(palautus, 100)

    def test_kateisosto_maukkaat_kateinen_ei_nouse(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    def test_kateisosto_maukkaat_lounaat_ei_nouse(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    def test_kateisosto_maukkaat_palautus_toimii_kun_ei_riittavasti_rahaa(self):
        palautus = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(palautus, 200)               

    def test_edullinen_korttiosto_veloittaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.60 euroa")
    def test_edullinen_korttiosto_nostaa_lounaiden_maaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
    def test_edullinen_korttiosto_hyvaksytty_palauttaa_true(self):
        arvo = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(arvo, True)
    def test_edullinen_korttiosto_ei_veloita_jos_saldo_riittamaton(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")
    def test_edullinen_korttiosto_ei_nosta_lounaiden_maaraa_jos_saldo_riittamaton(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
    def test_edullinen_korttiosto_hylatty_palauttaa_false(self):
        kortti = Maksukortti(200)
        arvo = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(arvo, False)

    def test_maukas_korttiosto_veloittaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 6.00 euroa")
    def test_maukas_korttiosto_nostaa_lounaiden_maaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    def test_maukas_korttiosto_hyvaksytty_palauttaa_true(self):
        arvo = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(arvo, True)
    def test_maukas_korttiosto_ei_veloita_jos_saldo_riittamaton(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")
    def test_maukas_korttiosto_ei_nosta_lounaiden_maaraa_jos_saldo_riittamaton(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    def test_maukas_korttiosto_hylatty_palauttaa_false(self):
        kortti = Maksukortti(200)
        arvo = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(arvo, False)

    def test_edullinen_kassan_rahamaara_ei_muutu_korttiostolla(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    def test_maukas_kassan_rahamaara_ei_muutu_korttiostolla(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lataa_rahaa_kasvattaa_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 11.00 euroa")
    def test_lataa_rahaa_kasvattaa_kassan_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
    def test_lataa_rahaa_negatiivinen_ei_muuta_korttia(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    def test_lataa_rahaa_negatiivinen_ei_muuta_kassan_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        self.viitegeneraattori_mock.uusi.return_value = 42


        self.varasto_mock.saldo.side_effect = self.varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = self.varasto_hae_tuote
    
    def varasto_saldo(self,tuote_id):
            if tuote_id == 1:
                return 10
            elif tuote_id == 2:
                return 5
            elif tuote_id == 3:
                return 0
    
    def varasto_hae_tuote(self,tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            elif tuote_id == 2:
                return Tuote(1, 'Juusto', 3)
            elif tuote_id == 3:
                return Tuote(3, 'Makkara', 4)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called()

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_arvoilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("Pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with('Pekka',42,'12345',"33333-44455",5)

    def test_liataan_kaksi_tuotetta_jota_varastossa_on_ja_kusutaan_tilinsiirtoa_oikeilla_arvoilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("Matti","12345")

        self.pankki_mock.tilisiirto.assert_called_with("Matti",42,'12345','33333-44455',8)

    def test_liataan_kaksi_samaa_tuotetta_jota_varastossa_on_ja_kusutaan_tilinsiirtoa_oikeilla_arvoilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu('Matti','12345')

        self.pankki_mock.tilisiirto.assert_called_with('Matti',42,'12345','33333-44455',6)

    def test_kortiin_lisataan_tuote_on_varastossa_ja_jota_ei_ole_varastossa(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu('Pekka','12345')

        self.pankki_mock.tilisiirto.assert_called_with('Pekka',42,'12345','33333-44455',5)
    
    def test_aloita_asiointi_nollaa_ostoskorin(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu('Matti','12345')

        self.pankki_mock.tilisiirto.assert_called_with('Matti',42,'12345','33333-44455',3)

    def test_kauppa_pyytaa_uuden_viitenumeron_jokaiselle_maksutapahtumalle(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu('Matti','12345')


        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu('Matti','12345')

        self.assertEqual(self.pankki_mock.tilisiirto.call_count,2)

    def test_poista_tuote_korista(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(2)
        self.kauppa.tilimaksu('Matti','12345')

        self.pankki_mock.tilisiirto.assert_called_with('Matti',42,'12345','33333-44455',0)
    

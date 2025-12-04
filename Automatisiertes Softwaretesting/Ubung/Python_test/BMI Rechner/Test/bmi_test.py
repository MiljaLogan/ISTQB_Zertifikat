import pytest
from bmi_rechner import berechne_bmi,kategorisiere_bmi

"""
TC    Name                  Gewicht     Größe   BMI   ÄK
TC01  Utergewicht              45,00    1.75    14,7  gÄk1
TC02  Normalgewicht(Mitte)     70,00    1.75    22,9  gÄk2
TC03  Übergewicht              85,00    1.75    27,8   gÄk3
TC04  Adipositas              100,00    1.75    32,7  gÄk4
"""
class TestÄKBMI:
    """Test für fir ÄK der BMI Kategorieren (TC01 -TC04)"""
    def test_tc01_untergewicht(self):
        """TC01 : Untergewicht - repräsentant für gÄK1"""
        kategorie = kategorisiere_bmi(14.7)
        assert kategorie == "Untergewicht"
    def test_tc02_Normalgewicht(self):
        """TC02 : Untergewicht - repräsentant für gÄ21"""
        kategorie = kategorisiere_bmi(22.9)
        assert kategorie == "Normalgewicht"
    def test_tc03_Übergewicht(self):
        """TC03 : Untergewicht - repräsentant für gÄK3"""
        kategorie = kategorisiere_bmi(27.8 )
        assert kategorie == "Übergewicht"
    def test_tc04_Adipositas(self):
        """TC04 : Untergewicht - repräsentant für gÄK4"""
        kategorie = kategorisiere_bmi(32.7)
        assert kategorie == "Adipositas"




        """bmi= berechne_bmi(45,00,1.75)
        assert bmi== 14.7
        kategorie = kategorisiere_bmi(bmi)
        assert kategorie == "Untergewicht"""


class TestGrenzwertBMI:
    """Tests für Grenzwerte zwischen Kategorien (TC05 - TC08)"""

    def test_tc05_grenzwert_ug_normal(self):
        """TC05: GW ug/normal - Grenze bei 18.5"""
        kategorie = kategorisiere_bmi(18.5)

    def test_tc06_grenzwert_normal_üg(self):
        """TC06: GW normal/üg - Grenze bei 24.9"""
        kategorie = kategorisiere_bmi(24.8)

    def test_tc07_grenzwert_üg_adipositas(self):
        """TC07: GW üg/adipositas - Grenze bei 29.9"""
        kategorie = kategorisiere_bmi(29.9)

    def test_tc08_grenzwert_adipositas(self):
        """TC08: GW adipositas - Grenze bei 30"""
        kategorie = kategorisiere_bmi(30)

class TestBerechnungBMI:
    """Tests for die BMI-Berechnung aus TC01 - TC04"""

    def test_tc01_berechnung_untergewicht(self):
        """TC01 : Berechnung - 45kg / 1.75m = 14.7"""
        bmi = berechne_bmi(45.00,1.75)
        assert bmi == 14.7

    def test_tc01_berechnung_normalgewicht(self):
        """TC02 : Berechnung - 70kg / 1.75m = 22.9"""
        bmi = berechne_bmi(70.00,1.75)
        assert bmi == 22.9

    def test_tc01_berechnung_ubergewicht(self):
        """TC03 : Berechnung - 85kg / 1.75m = 27.8"""
        bmi = berechne_bmi(85.00,1.75)
        assert bmi == 27.8

    def test_tc01_berechnung_adipositas(self):
        """TC04 : Berechnung - 100kg / 1.75m = 32.7"""
        bmi = berechne_bmi(100.00,1.75)
        assert bmi == 32.7


class TestEingabevalidierung:
    """Tests für ungültige Eingabewerte (TC09 - TC13)"""
    
    def test_tc09_gewicht_null(self):
        """TC09: Gewicht = 0 (ungültig) - Grenze bei 0"""
        with pytest.raises(ValueError, match="Gewicht muss größer als 0 sein"):
            berechne_bmi(0.00,1.75)

    def test_tc10_gewicht_negativ(self):
        """TC10: Gewicht negativ (ungültig) - Grenze < 0"""
        with pytest.raises(ValueError, match="Gewicht muss größer als 0 sein"):
            berechne_bmi(-70.00,1.75)

    def test_tc11_groesse_null(self):
        """TC11: Große = 0 (ungültig) - Grenze bei 0"""
        with pytest.raises(ValueError, match="Größe muss größer als 0 sein"):
            berechne_bmi(70.00,0.00)

    def test_tc12_groesse_negativ(self):
        """TC12: Große negativ (ungültig) - Grenze < 0"""
        with pytest.raises(ValueError, match="Größe muss größer als 0 sein"):
            berechne_bmi(70.00,-1.75)

    def test_tc13_gewicht_nan(self):
        """TC13: Gewicht NaN(ungültig) - Nicht-numerischer Wert"""
        with pytest.raises(TypeError):
            berechne_bmi("abc",1.75)

class TestIntergrationBerechneundKategorisiereBMI:
    """Tests für Integration der MI-Kategorien (TC01-TC04) """
    def test_tc01_untergewicht(self):
        bmi = berechne_bmi(45.00,1.75)
        assert bmi == 14.7
        kategorie = kategorisiere_bmi(bmi)
        assert kategorie == "Untergewicht"

    def test_tc02_normalgewicht(self):
        bmi = berechne_bmi(70.00,1.75)
        assert bmi == 22.9
        kategorie = kategorisiere_bmi(bmi)
        assert kategorie == "Normalgewicht"

    def test_tc03_ubergewicht(self):
        bmi = berechne_bmi(85.00,1.75)
        assert bmi == 27.8
        kategorie = kategorisiere_bmi(bmi)
        assert kategorie == "Übergewicht"

    def test_tc04_adipositas(self):
        bmi = berechne_bmi(100.00,1.75)
        assert bmi == 32.7
        kategorie = kategorisiere_bmi(bmi)
        assert kategorie == "Adipositas"

        
    

    





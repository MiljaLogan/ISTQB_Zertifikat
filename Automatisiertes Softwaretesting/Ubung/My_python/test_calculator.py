
from calculator import Calculator
import pytest

def test_addiere_zwei_zahlen():
    # Arrange
    calc = Calculator()
    
    # Act
    ergebnis = calc.addiere(2, 3)
    
    # Assert
    assert ergebnis == 5


def test_subtrahiere_zwei_zahlen():
    # Arrange
    calc = Calculator()
    
    # Act
    ergebnis = calc.subtrahiere(10, 4)
    
    # Assert
    assert ergebnis == 6


def test_dividiere_zwei_zahlen():
    # Arrange
    calc = Calculator()
    
    # Act
    ergebnis = calc.dividiere(10, 2)
    
    # Assert
    assert ergebnis == 5


def test_dividiere_durch_null_wirft_fehler():
    # Arrange
    calc = Calculator()
    
    # Assert & Act kombiniert
    with pytest.raises(ValueError):
        calc.dividiere(10, 0)

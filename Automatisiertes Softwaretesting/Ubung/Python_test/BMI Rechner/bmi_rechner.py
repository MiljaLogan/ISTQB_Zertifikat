

def berechne_bmi(gewicht, groesse):
    
    if gewicht <= 0:
        raise ValueError("Gewicht muss größer als 0 sein")
    if groesse <= 0:
        raise ValueError("Größe muss größer als 0 sein")
    return round(gewicht / (groesse**2),1)

def kategorisiere_bmi(bmi):

    if bmi < 18.5:
        return "Untergewicht"
    elif bmi <= 24.9:
        return "Normalgewicht"
    elif bmi <= 29.9:
        return "Übergewicht"
    else:
        return "Adipositas"
    


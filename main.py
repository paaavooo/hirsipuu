import random

sanathelppo = ["kissa", "koira", "talo", "auto", "juna", "kukka", "puisto", "saari", "lumi", "kala"]
sanatkeski = ["kirjasto", "elefantti", "viikset", "pannukakku", "mainoskyltti", "kultaraha", "televisio", "vesiputous", "maailmankaikkeus", "tietokone"]
sanatvaikea = ["ammattikorkeakoulu", "joululahjapaperi", "ruohosipulituorejuusto", "lentokonemekaanikko", "laboratorioanalyysi", "jauhelihaperunasoselaatikko", "lastensuojeluviranomainen", "matkapuhelinoperaattori", "mustaviinimarjamehu", "tuplajuustohampurilainen"]

HANGMANKUVA = ['''
   ___
  |   |
  |   
  |   
  |   
  |   
=========''','''
   ___
  |   |
  |   O
  |   
  |   
  |   
=========''','''
   ___
  |   |
  |   O
  |   |
  |   
  |   
=========''','''
   ___
  |   |
  |   O
  |  /|
  |   
  |   
=========''','''
   ___
  |   |
  |   O
  |  /|\\
  |   
  |   
=========''','''
   ___
  |   |
  |   O
  |  /|\\
  |  /
  |   
=========''','''
   ___
  |   |
  |   O
  |  /|\\
  |  / \\
  |   
=========''']

def arvosana(vaikeustaso):
    #Valitsee satunnaisen sanan valitun vaikeustason mukaan.
    if vaikeustaso == "helppo":
        sanalista = sanathelppo
    elif vaikeustaso == "keski":
        sanalista = sanatkeski
    elif vaikeustaso == "vaikea":
        sanalista = sanatvaikea
    else:
        print("Virheellinen vaikeustaso")
        return None

    return random.choice(sanalista)

def nayta_vihje(sana, arvatut_kirjaimet):
    """Muodostaa sanasta vihjeen arvattavaksi kirjaimet alaviivoiksi."""
    vihje = ""
    for kirjain in sana:
        if kirjain in arvatut_kirjaimet:
            vihje += kirjain + " "
        else:
            vihje += "_ "
    return vihje

def pelaajaarvaakirjainta():
    #Pyytää pelaajaa arvaamaan kirjainta ja tarkistaa syötteen.
    while True:
        arvaus = input("Arvaa kirjain (tai kirjoita 'end' lopettaaksesi): ").lower()
        if arvaus == "end":
            return arvaus
        if len(arvaus) == 1 and arvaus.isalpha():
            return arvaus
        else:
            print("Syötteen tulee olla yksi kirjain.")

def pelaahirsipuuta():
    #Pääfunktio, jossa peliä pelataan.
    print("Tervetuloa pelaamaan hirsipuuta! Arvaa kirjain tai kirjoita 'end' lopettaaksesi pelin.")

    while True:
        vaikeustaso = input("Valitse vaikeustaso (helppo / keski / vaikea tai kirjoita 'end' lopettaaksesi): ").lower()
        if vaikeustaso == "end":
            print("Peli lopetettu.")
            return
        sana = arvosana(vaikeustaso)  # Arvotaan sana
        if sana is not None:
            break

    arvatut_kirjaimet = set()  # Alustetaan arvatut kirjaimet tyhjäksi joukoksi
    yritykset = 0  # Alustetaan yritykset laskuri
    maksimiyritykset = 6

    while True:
        vihje = nayta_vihje(sana, arvatut_kirjaimet)  # Näytetään vihje
        print("\nSana:", vihje)

        arvaus = pelaajaarvaakirjainta()  # Pelaajan arvaus
        if arvaus == "end":
            print("Peli lopetettu.")
            break

        arvatut_kirjaimet.add(arvaus)  # Lisätään arvaus arvattujen joukkoon

        

        if arvaus not in sana:  # Tarkistetaan, oliko arvaus väärin
            yritykset += 1  # Päivitetään yritysten määrää
            jaljella = maksimiyritykset - yritykset
            print(f"Väärin! Yritä uudelleen. Elämiä jäljellä {jaljella}.")

        print(HANGMANKUVA[yritykset])
        
        if set(sana) <= arvatut_kirjaimet:  # Tarkistetaan, onko kaikki kirjaimet arvattu
            print(f"\nOnneksi olkoon, voitit pelin! Oikea sana oli \"{sana}\".")
            break

        if yritykset == maksimiyritykset:  # Tarkistetaan, onko yrityksiä käytetty liikaa
            print("\nHävisit pelin! Oikea sana oli:", sana)
            break

def pelaahirsipuuta_uudelleen():
    while True:
        pelaahirsipuuta()
        uudelleen = input("Haluatko pelata uudelleen? (kyllä/ei): ").lower()
        if uudelleen != "kyllä":
            print("Kiitos pelaamisesta!")
            break

# Käynnistetään peli
if __name__ == "__main__":
    pelaahirsipuuta_uudelleen()

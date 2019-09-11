
        ## Dit bestand bevat de meesterproeven voor week 2
        ## Matthijs Verwoerd, 500731032



def leeftijdberekening():
    # Meesterproef 1
        # leeftijdberekening

        # Input van naam en geboortejaar
    inputNaam = input("Hoe heet je?")
    inputGeboorteJaar = int(input("In welk jaar ben je geboren?"))
    #debug  print("Naam:", inputNaam)
    #debug  print("Geboortejaar:", inputGeboorteJaar)

        # Vaststellen van benodigde variabelen
    aardeJaarTal = 2019
    venusJaarTal = aardeJaarTal / 0.62

        # Jaartal op Venus
    #debug  print("Jaartal op Venus:", round(venusJaarTal))

        # Leeftijd op Aarde
    aardeLeeftijd = aardeJaarTal - inputGeboorteJaar
    #debug  print("Leeftijd op Aarde:", aardeLeeftijd)

        # Leeftijd op Venus
    venusGeboorteJaar = inputGeboorteJaar / 0.62
    venusLeeftijd = venusJaarTal - venusGeboorteJaar
    #debug  print("Leeftijd op Venus:", round(venusLeeftijd, 2))

        # Print van de eindgegevens
    print(inputNaam, ", je bent op Aarde ", aardeLeeftijd, " en dat zou op Venus ", round(venusLeeftijd, 2), " jaar zijn.", sep="")

leeftijdberekening()

def bmiberekening():

    # Meesterproef 2
        # BMI berekenen

    # Berekening van BMI
        # MBI = kG/(L^2)

        # Input van naam, gewicht en lengte
    inputNaam = str(input("Vertel je naam:"))
    inputGewicht = float(input("Gewicht in kilogram:"))
    inputLengte = int(input("Lengte in centimeter:"))
    #debug  print(inputNaam)
    #debug  print(inputGewicht)
    #debug  print(inputLengte)

        # Lengte van cm naar m
            # van integer naar float
    inputLengte = float(inputLengte/100)
    #debug  print(inputLengte)

        # Berekening van de BMI
    uitkomstBmi = inputGewicht/(inputLengte * inputLengte)
    #debug  print(round(uitkomstBmi, 2))

        # Print van het eindresultaat
    print("Beste ", inputNaam, ", jouw BMI is: ", round(uitkomstBmi, 2), ".", sep= "")

bmiberekening()
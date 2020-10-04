print("     /////WELCOME TO THE BENDING MACHINE PROGRAM/////     ")
print("                     BY: TEAM PURPLE\n   ")
#DEFINICION DE TODOS LOS PRODUCTOS DE LA MAQUINA EXPENDEDORA CON SU PRECIO
SabritasOriginales = 11
SabritasLimon = 12
SabritasFlaminHot = 12
SabritasAdobadas = 12
SabritasCrema = 12
ChipsOriginales = 12
ChipsJalapeño = 12
ChipsAdobadas = 12
ChipsFlaminHot = 12
TakisFuego = 10
TakisOriginales = 10
Pinguinos = 14
DonaBlanca = 14
DonaNegra = 14
Palomitas = 13
Principe = 10
Oreo = 12
OreoBlanca = 14
Bubuluboo = 8
Mantecadas = 14
Snickers = 10
KitKat = 12
HotNuts = 13
Nitos = 18
Halls = 10
A = True
while A != False:
    # DECISION PARA VER EL CATALOGO
    Catalogo = str(input("WOULD YOU LIKE TO SEE THE PRODUCTS AVIABLE? (Y/N) "))
    if Catalogo == 'Y' or Catalogo == 'y':
        Catalogo = True
        while Catalogo != False:
            print("\n/////PRODUCT/////          /////PRICE/////")
            print("1A  Chips Originales                 $" + str(ChipsOriginales))
            print("2A  Chips Flamin´hot                 $" + str(ChipsFlaminHot))
            print("3A  Chips Adobadas                   $" + str(ChipsAdobadas))
            print("4A  Chips Jalapeño                   $" + str(ChipsJalapeño))
            print("1B  Sabritas Originales              $" + str(SabritasOriginales))
            print("2B  Sabritas Limon                   $" + str(SabritasLimon))
            print("3B  Sabritas Fuego                   $" + str(SabritasFlaminHot))
            print("4B  Sabritas Adobadas                $" + str(SabritasAdobadas))
            print("5B  Sabritas Crema                   $" + str(SabritasCrema))
            print("1C  Takis Fuego                      $" + str(TakisFuego))
            print("2C  Takis Originales                 $" + str(TakisOriginales))
            print("1D  Pinguinos                        $" + str(Pinguinos))
            print("2D  Dona Blanca                      $" + str(DonaBlanca))
            print("3D  Dona Negra                       $" + str(DonaNegra))
            print("4D  Palomitas                        $" + str(Palomitas))
            print("1E  Principe                         $" + str(Principe))
            print("2E  Oreo                             $" + str(Oreo))
            print("3E  Oreo Blanca                      $" + str(OreoBlanca))
            print("4E  Bubuluboo                        $" + str(Bubuluboo))
            print("5E  Mantecadas                       $" + str(Mantecadas))
            print("1F  Snickers                         $" + str(Snickers))
            print("2F  KitKat                           $" + str(KitKat))
            print("3F  Hot Nuts                         $" + str(HotNuts))
            print("4F  Nitos                            $" + str(Nitos))
            print("5F  Halls                            $" + str(Halls))
            End = str(input("PRESS Y TO CONTINUE: "))
            if End == "Y" or End == 'y':
                # INICIAMOS CON EL WHILE
                Decision = True
                Total = 0
                while Decision != False:
                    Product = str(input("ENTER THE CODE OF THE PRODUCT "))
                    if Product == '1A' or Product == '1a':
                        Product = ChipsOriginales
                        Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
                    elif Product == '2A' or Product == '2a':
                        Product = ChipsFlaminHot
                        Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
                    elif Product == '3A' or Product == '3a':
                        Product = ChipsAdobadas
                        Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
                    elif Product == '4A' or Product == '4a':
                        Product = ChipsJalapeño
                        Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
                    elif Product == '1B' or Product == '1b':
                        Product = SabritasOriginales
                        Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
                    elif Product == '2B' or Product == '2b':
                        Product = SabritasLimon
                        Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
                    elif Product == '3B' or Product == '3b':
                        Product = SabritasFlaminHot
                        Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
                    elif Product == '4B' or Product == '4b':
                        Product = SabritasAdobadas
                        Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
                    elif Product == '5B' or Product == '5b':
                        Product = SabritasCrema
                        Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
                    elif Product == '1C' or Product == '1c':
                        Product = TakisFuego
                        Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
                    elif Product == '2C' or Product == '2c':
                        Product = TakisOriginales
                        Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
                    elif Product == '1D' or Product == '1d':
                        Product = Pinguinos
                        Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
                    elif Product == '2D' or Product == '2d':
                        Product = DonaBlanca
                        Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
                    elif Product == '3D' or Product == '3d':
                        Product = DonaNegra
                        Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
                    elif Product == '4D' or Product == '4d':
                        Product = Palomitas
                        Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
                    elif Product == '1E' or Product == '1e':
                        Product = Principe
                        Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
                    elif Product == '2E' or Product == '2e':
                        Product = Oreo
                        Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
                    elif Product == '3E' or Product == '3e':
                        Product = OreoBlanca
                        Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
                    elif Product == '4E' or Product == '4e':
                        Product = Bubuluboo
                        Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
                    elif Product == '5E' or Product == '5e':
                        Product = Mantecadas
                        Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
                    elif Product == '1F' or Product == '1f':
                        Product = Snickers
                        Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
                    elif Product == '2F' or Product == '2f':
                        Product = KitKat
                        Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
                    elif Product == '3F' or Product == '3f':
                        Product = HotNuts
                        Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
                    elif Product == '4F' or Product == '4f':
                        Product = Nitos
                        Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
                    elif Product == '5F' or Product == '5f':
                        Product = Halls
                        Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
                    else:
                        print("ERROR 404: COMMAND NOT FOUND")
                    Total = Total + (Product * Quantitie)
                    C = True
                    while C != False:
                        Final = str(input("DO YOU WANT ANOTHER PRODUCT: (Y/N)"))
                        if Final == 'N' or Final == 'n':
                            Decision = False
                            C = False
                        elif Final == 'Y' or Final == 'y':
                            Decision = True
                            C = False
                        else:
                            print("ERROR 404: COMMAND NOT FOUND")
                            Decision = True
                            C = True
                print("YOUR TOTAL IS: $" + str(Total))
                Pago = int(input("ENTER THE PAYMENT: "))
                Pago1 = True
                while Pago1 != False:
                    if Pago < Total:
                        print("ERROR: MISSING MONEY")
                        Pago1 = True
                    elif Pago >= Total:
                        Pago1 = False
                    else:
                        print("ERROR 404: COMMAND NOT FOUND")
                        Pago1 = True
                Change = Pago - Total
                print("YOUR CHANGE IS: $" + str(Change))
                print("THANKS FOR USING THE PROGRAM HAVE A GOOD DAY!!!")
                Catalogo = False
                A = False
    elif Catalogo == 'N' or Catalogo == 'n':
        # INICIAMOS CON EL WHILE
        Decision = True
        Total = 0
        while Decision != False:
            Product = str(input("ENTER THE CODE OF THE PRODUCT "))
            if Product == '1A' or Product == '1a':
                Product = ChipsOriginales
                Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
            elif Product == '2A' or Product == '2a':
                Product = ChipsFlaminHot
                Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
            elif Product == '3A' or Product == '3a':
                Product = ChipsAdobadas
                Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
            elif Product == '4A' or Product == '4a':
                Product = ChipsJalapeño
                Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
            elif Product == '1B' or Product == '1b':
                Product = SabritasOriginales
                Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
            elif Product == '2B' or Product == '2b':
                Product = SabritasLimon
                Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
            elif Product == '3B' or Product == '3b':
                Product = SabritasFlaminHot
                Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
            elif Product == '4B' or Product == '4b':
                Product = SabritasAdobadas
                Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
            elif Product == '5B' or Product == '5b':
                Product = SabritasCrema
                Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
            elif Product == '1C' or Product == '1c':
                Product = TakisFuego
                Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
            elif Product == '2C' or Product == '2c':
                Product = TakisOriginales
                Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
            elif Product == '1D' or Product == '1d':
                Product = Pinguinos
                Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
            elif Product == '2D' or Product == '2d':
                Product = DonaBlanca
                Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
            elif Product == '3D' or Product == '3d':
                Product = DonaNegra
                Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
            elif Product == '4D' or Product == '4d':
                Product = Palomitas
                Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
            elif Product == '1E' or Product == '1e':
                Product = Principe
                Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
            elif Product == '2E' or Product == '2e':
                Product = Oreo
                Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
            elif Product == '3E' or Product == '3e':
                Product = OreoBlanca
                Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
            elif Product == '4E' or Product == '4e':
                Product = Bubuluboo
                Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
            elif Product == '5E' or Product == '5e':
                Product = Mantecadas
                Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
            elif Product == '1F' or Product == '1f':
                Product = Snickers
                Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
            elif Product == '2F' or Product == '2f':
                Product = KitKat
                Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
            elif Product == '3F' or Product == '3f':
                Product = HotNuts
                Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
            elif Product == '4F' or Product == '4f':
                Product = Nitos
                Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
            elif Product == '5F' or Product == '5f':
                Product = Halls
                Quantitie = int(input("ENTER HOW MUCH YOU WANT: "))
            else:
                print("ERROR 404: COMMAND NOT FOUND")
            Total = Total + (Product * Quantitie)
            C = True
            while C != False:
                Final = str(input("DO YOU WANT ANOTHER PRODUCT: (Y/N)"))
                if Final == 'N' or Final == 'n':
                    Decision = False
                    C = False
                elif Final == 'Y' or Final == 'y':
                    Decision = True
                    C = False
                else:
                    print("ERROR 404: COMMAND NOT FOUND")
                    Decision = True
                    C = True
        print("YOUR TOTAL IS: $" + str(Total))
        Pago = int(input("ENTER THE PAYMENT: "))
        Pago1 = True
        while Pago1 != False:
            if Pago < Total:
                print("ERROR: MISSING MONEY")
                Pago1 = True
            elif Pago >= Total:
                Pago1 = False
            else:
                print("ERROR 404: COMMAND NOT FOUND")
                Pago1 = True
        Change = Pago - Total
        print("YOUR CHANGE IS: $" + str(Change))
        print("THANKS FOR USING THE PROGRAM HAVE A GOOD DAY!!!")
        Catalogo = False
        A = False
    else:
        print("ERROR 404: COMMAND NOT FOUND")
        Catalogo = False
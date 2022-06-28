import random
import time
import os

class bcolors:
    VERDE = '\033[92m' #GREEN
    AMARELO = '\033[93m' #YELLOW
    VERMELHO = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

class Aviao:
    def __init__(self, modelo, combustivel):
        self.modelo = modelo
        self.combustivel = combustivel
    def __str__(self):
        return str(self.item) + ' ' + str(self.combustivel)
    pass

def rodar():
    
    pista1 = []
    pista2 = []
    pista3 = []
    aviao1 = Aviao("RS 532 BRA", random.randint(15, 85))
    aviao2 = Aviao("TL 924 COL", random.randint(15, 85))
    aviao3 = Aviao("HF 667 ARG", random.randint(15, 85))
    for i in range(15):
        aviao1.combustivel = aviao1.combustivel - 1
        aviao2.combustivel = aviao2.combustivel - 1
        aviao3.combustivel = aviao3.combustivel - 1

        if aviao1.modelo not in pista1 and aviao2.modelo not in pista1 and aviao3.modelo not in pista1:

            print(bcolors.VERMELHO + "Aviões comunicando o desejo de pouso:")
            time.sleep(1)
            print(bcolors.AMARELO + "Avião:", aviao1.modelo, "|", "Combustível:", aviao1.combustivel, "%", "tempo restante de combustível:", aviao1.combustivel, "segundos")
            time.sleep(1)
            print("Avião:", aviao2.modelo, "|", "Combustível:", aviao2.combustivel, "%", "tempo restante de combustível:", aviao2.combustivel, "segundos")
            time.sleep(1)
            print("Avião:", aviao3.modelo, "|", "Combustível:", aviao3.combustivel, "%", "tempo restante de combustível:", aviao3.combustivel, "segundos")
            time.sleep(1)
            print(bcolors.RESET +  "Pistas disponíveis para pouso:")
            print("Pista 1:", pista1)
            print("Pista 2:", pista2)
            time.sleep(2)

        elif aviao1.modelo in pista1 and pista2 == []:
            print(bcolors.VERMELHO + "Aviões comunicando o desejo de pouso:")
            print(bcolors.AMARELO + "Avião:", aviao2.modelo, "|", "Combustível:", aviao2.combustivel, "%", "tempo restante de combustível:", aviao2.combustivel, "segundos")
            print(bcolors.AMARELO + "Avião:", aviao3.modelo, "|", "Combustível:", aviao3.combustivel, "%", "tempo restante de combustível:", aviao3.combustivel, "segundos")
            print(bcolors.RESET + "Pistas disponíveis para pouso:")
            print("Pista 2:", pista2)

        elif aviao2.modelo in pista1 and pista2 == []:
            print(bcolors.VERMELHO + "Aviões comunicando o desejo de pouso:")
            print(bcolors.AMARELO + "Avião:", aviao1.modelo, "|", "Combustível:", aviao1.combustivel, "%", "tempo restante de combustível:", aviao1.combustivel, "segundos")
            print(bcolors.AMARELO + "Avião:", aviao3.modelo, "|", "Combustível:", aviao3.combustivel, "%", "tempo restante de combustível:", aviao3.combustivel, "segundos")
            print(bcolors.RESET + "Pistas disponíveis para pouso:")
            print("Pista 2:", pista2)

        elif aviao3.modelo in pista1 and pista2 == []:
            print(bcolors.VERMELHO + "Aviões comunicando o desejo de pouso:")
            print(bcolors.AMARELO + "Avião:", aviao1.modelo, "|", "Combustível:", aviao1.combustivel, "%", "tempo restante de combustível:", aviao1.combustivel, "segundos")
            print("Avião:", aviao2.modelo, "|", "Combustível:", aviao2.combustivel, "%", "tempo restante de combustível:", aviao2.combustivel, "segundos")
            print(bcolors.RESET + "Pistas disponíveis para pouso:")
            print("Pista 2:", pista2)

        if pista1 == []:
            if aviao1.combustivel < aviao2.combustivel and aviao1.combustivel < aviao3.combustivel:
                pista1.append(aviao1.modelo)
                print(bcolors.VERDE + "Avião:", aviao1.modelo, "pousou na pista 1")
                print("Pista 1:", pista1)

            elif aviao2.combustivel < aviao3.combustivel and aviao2.combustivel < aviao1.combustivel:
                pista1.append(aviao2.modelo)
                print(bcolors.VERDE + "Avião:", aviao2.modelo, "pousou na pista 1")
                print("Pista 1:", pista1)

            elif aviao3.combustivel < aviao2.combustivel and aviao3.combustivel < aviao1.combustivel:
                pista1.append(aviao3.modelo)
                print(bcolors.VERDE + "Avião:", aviao3.modelo, "pousou na pista 1")
                print("Pista 1:", pista1)

        elif pista2 == []:
            
            if aviao1.modelo not in pista1 and (aviao1.combustivel < aviao2.combustivel or aviao1.combustivel < aviao3.combustivel):
            
                pista2.append(aviao1.modelo)
                print(bcolors.VERDE + "Avião:", aviao1.modelo, "pousou na pista 2")
                print("Pista 2:", pista2)

            elif aviao2.modelo not in pista1 and (aviao2.combustivel < aviao3.combustivel or aviao2.combustivel < aviao1.combustivel):
                pista2.append(aviao2.modelo)
                print(bcolors.VERDE + "Avião:", aviao2.modelo, "pousou na pista 2")
                print("Pista 2:", pista1)

            elif aviao3.modelo not in pista1 and (aviao3.combustivel < aviao2.combustivel or aviao3.combustivel < aviao1.combustivel):
                pista2.append(aviao3.modelo)
                print(bcolors.VERDE + "Avião:", aviao3.modelo, "pousou na pista 2")
                print("Pista 2:", pista2)


        elif pista1 != [] and pista2 != []:
            if aviao1.modelo not in pista1 and aviao1.modelo not in pista2:
                print(bcolors.VERMELHO + "Aviões comunicando o desejo de pouso:")
                print(bcolors.AMARELO + "Avião:", aviao1.modelo, "|", "Combustível:", aviao1.combustivel, "%", "tempo restante de combustível:", aviao1.combustivel, "segundos")
                time.sleep(2)
                print(bcolors.VERMELHO + "TODAS AS PISTAS ESTÃO LOTADAS!")
                time.sleep(2)
                print(bcolors.AMARELO + "Avião:", pista1, "sendo enviado para decolagem na pista 3!")
                time.sleep(2)
                print(bcolors.VERDE + "Pista 1 liberada!" + bcolors.RESET)
                pista3.append(pista1)
                pista1.clear()
                pista1.append(aviao1.modelo)
                time.sleep(2)
                print("Pousando o avião:", aviao1.modelo, "na pista 1")
                break

            elif aviao2.modelo not in pista1 and aviao2.modelo not in pista2:
                print(bcolors.VERMELHO + "Aviões comunicando o desejo de pouso:")
                print(bcolors.AMARELO + "Avião:", aviao2.modelo, "|", "Combustível:", aviao2.combustivel, "%", "tempo restante de combustível:", aviao2.combustivel, "segundos")
                time.sleep(2)
                print(bcolors.VERMELHO + "TODAS AS PISTAS ESTÃO LOTADAS!")
                time.sleep(2)
                print(bcolors.AMARELO + "Avião:", pista1, "sendo enviado para decolagem na pista 3!")
                time.sleep(2)
                print(bcolors.VERDE + "Pista 1 liberada!" + bcolors.RESET)
                pista3.append(pista1)
                pista1.clear()
                pista1.append(aviao2.modelo)
                time.sleep(2)
                print("Pousando o avião:", aviao2.modelo, "na pista 1")
                break

            if aviao3.modelo not in pista1 and aviao3.modelo not in pista2:
                print(bcolors.VERMELHO + "Aviões comunicando o desejo de pouso:")
                print(bcolors.AMARELO + "Avião:", aviao3.modelo, "|", "Combustível:", aviao3.combustivel, "%", "tempo restante de combustível:", aviao3.combustivel, "segundos")
                time.sleep(2)
                print(bcolors.VERMELHO + "TODAS AS PISTAS ESTÃO LOTADAS!")
                time.sleep(2)
                print(bcolors.AMARELO + "Avião:", pista1, "sendo enviado para decolagem na pista 3!")
                time.sleep(2)
                print(bcolors.VERDE + "Pista 1 liberada!" + bcolors.RESET)
                pista3.append(pista1)
                pista1.clear()
                pista1.append(aviao3.modelo)
                time.sleep(2)
                print("Pousando o avião:", aviao3.modelo, "na pista 1")
                break
        
        time.sleep(4)

rodar()


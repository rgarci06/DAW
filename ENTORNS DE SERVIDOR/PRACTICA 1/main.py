from cc_GarciaRaúl import CompteCorrent

def main():
    print("=== CREACIÓ DE COMPTE CORRENT ===")
    dni = input("Introdueix el DNI: ")
    nom = input("Introdueix el nom: ").capitalize()
    cognoms = input("Introdueix els cognoms: ").capitalize()
    saldo_inicial = float(input("Introdueix el saldo inicial (€): "))

    compte = CompteCorrent(dni, nom, cognoms, saldo_inicial)

    while True:
        print("\n--- MENÚ ---")
        print("1. Ingressar diners")
        print("2. Retirar diners")
        print("3. Veure saldo")
        print("4. Veure dades del compte")
        print("5. Sortir")

        opcio = input("Escull una opció: ")

        if opcio == "1":
            quantitat = float(input("Quant vols ingressar (€): "))
            compte.ingressar(quantitat)
        elif opcio == "2":
            quantitat = float(input("Quant vols retirar (€): "))
            compte.retirar(quantitat)
        elif opcio == "3":
            compte.veure_saldo()
        elif opcio == "4":
            compte.veure_dades()
        elif opcio == "5":
            print("Sortint de la compta")
            break
        else:
            print("Opció no vàlida. Torna-ho a provar.")

if __name__ == "__main__":
    main()

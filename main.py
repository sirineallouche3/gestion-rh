
from employes import menu_employes
print("Bienvenue dans notre application Gestion RH !")


def afficher_menu():
    print("\n" + "=" * 45)
    print("       APPLICATION DE GESTION RH")
    print("=" * 45)
    print("1. Gestion des employés")
    print("2. Gestion des congés")
    print("3. Gestion des évaluations")
    print("4. Gestion des formations")
    print("5. Messagerie interne")
    print("6. Alertes")
    print("7. Rapports et statistiques")
    print("0. Quitter")

    print("=" * 45)


def main():
    while True:
        afficher_menu()

        choix = input("Votre choix : ")

        if choix == "1":
            menu_employes()

        elif choix == "2":
            print("Module des congés à venir.")

        elif choix == "3":
            print("Module des évaluations à venir.")

        elif choix == "4":
            print("Module des formations à venir.")

        elif choix == "5":
            print("Module de messagerie à venir.")

        elif choix == "6":
            print("Module des alertes à venir.")

        elif choix == "7":
            print("Module des rapports à venir.")

        elif choix == "0":
            print("Merci d'avoir utilisé notre application !")
            break

        else:
            print("Choix invalide. Réessayez.")


if __name__ == "__main__":
    main()

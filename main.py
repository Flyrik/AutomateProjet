import A5_functions as f

#Menu
print("\n*********************************************************************************************************************************************************\n")
#Menu d’accueil qui s’affiche à l’écran lors du lancement
print("Bienvenue dans le logiciel de traitement d'automates finis de l'équipe 5\n")
print("Que souhaitez-vous faire ?\n")

print("1 - Lire et afficher un automate.")
print("2 - Savoir si un automate est déterministe ou non.")
print("3 - Savoir si un automate est standard ou non.")
print("4 - Savoir si un automate est complet ou non.")
print("5 - Lire et afficher un automate reconnaissant un langage complémentaire.\n")

choix =int(input("Entrez votre choix : \n")) 
while choix not in [1,2,3,4,5]:
    choix =int(input("Entrez votre choix : \n"))

#Permet en fonction de la réponse choisi à la question « Que souhaitez-vous faire ? » d’etre redirigé. Si 1 est choisi, l’utilisateur va être redirigé sur la case 1 et va donc avoir la lecture et affichage de l’automate.
       
match choix :    
        case 1:
            print("\nChoix 1 sélectionné : Lecture et affichage d'un automate \n")
            num_automate = f.Choix_automate() #permet de choisir l’automate sur laquelle on va faire l’opération
            automate = f.tranformer_txt_en_dico(num_automate) 
            f.afficher_automate(automate)
            f.Continuer() #Permet de continuer ou d’arreter le programme

        case 2:
            print("\nChoix 2 sélectionné : L'automate est-il déterministe ?\n")
            num_automate = f.Choix_automate()
            automate = f.tranformer_txt_en_dico(num_automate)
            if (f.est_deterministe(automate) == True): #permet de savoir si c'est deterministe 
                print("\nL'automate N°" + num_automate + " est déterministe",end="")
                if(f.est_complet(automate)): #permet de savoir si l’automate est complet 
                    print("-complet")
                else:
                    print(" mais pas complet.\n\nVoici l'automate déterministe et complet : ")
                    f.complétion_deterministe(automate) #permet de completer l'automate
            else:
                print("\nL'automate N°" + num_automate + " n'est pas déterministe.\n\nVoici l'automate déterministe-complet : ")
                f.determinisation_complete(automate)#permet de determiniser et completer l'automate
            f.Continuer()

        case 3:
            print("\nChoix 3 sélectionné : L'automate est-il standard ? \n")
            num_automate = f.Choix_automate()
            automate = f.tranformer_txt_en_dico(num_automate)
            
            if(f.est_standard(automate) == False): #permet de savoir si l'automate est standard 
                print("\nL'automate N°" + num_automate + " n'est pas standard.\n\nVoulez-vous le standardiser ?\n\n")
                
                rep=int(input("Entrez votre choix (1 pour Oui ou 0 pour Non): ")) #on demande à l'utilisateur si il souhaite ou non avoir l'automate standardiser
                while rep not in [1,0]:
                    rep=int(input("Entrez votre choix (1 pour Oui ou 0 pour Non): "))
                
                if rep == 1:
                    f.standardisation(automate) #permet de standardiser l'automate

            else:
                print("\n\nL'automate N°" + num_automate + " est standard")
            f.Continuer()

        case 4:
            print("\nChoix 4 sélectionné : L'automate est-il complet ? \n")
            num_automate = f.Choix_automate()
            automate = f.tranformer_txt_en_dico(num_automate)
            if (f.est_complet(automate)): #verification si l'automate est complet
                print("\nL'automate N°" + num_automate + " est complet")
            else:
                print("\nL'automate N°" + num_automate + " n'est pas complet")
            f.Continuer()

        case 5:
            print("\nChoix 5 sélectionné : Lecture et affichage d'un automate reconnaissant un langage complémentaire\n")  
            num_automate = f.Choix_automate()
            automate = f.tranformer_txt_en_dico(num_automate)
            if (f.est_deterministe(automate) == True): #verifie si l'automate est deterministe
                if(f.est_complet(automate)): #verifie si l'automate est complet
                    f.afficher_complementaire_automate_si_deterministe_complet(automate) #affiche l'automate reconnaissant le langage complementaire
                 
                else:
                    f.afficher_complementaire_automate_si_deterministe_non_complet(automate) #complete et affiche l'automate reconnaissant le langage complémentaire
                  
            else:
                f.complementaire(automate)#permet de determiniser compléter et afficher l'automate reconnaissant le langage complementaire
            
            f.Continuer()

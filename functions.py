PATH = "automates_de_tests/"

def tranformer_txt_en_dico(nom_automate):
    
    automate={}

    f = open(PATH + nom_automate + ".txt", "r")
    lignes = f.readlines()

    #On récupère les lignes du fichier txt
    temp_mot=""
    for i in range(len(lignes)):
        for j in range(len(lignes[i])):
            if lignes[i][j] != (" " and "\n"):
                temp_mot += lignes[i][j]
        automate[i] = temp_mot
        temp_mot = ""

    return automate

def afficher_automate(automate):
    
    alphabet = ['a','b','c','d']
    #On affiche la table de transition
    print("\n\tEtats\t\t", end="")
    for i in range(int(automate[0])):
        print("| ",end="")
        print(alphabet[i], end=" |\t\t")
    print("\n")

    for i in range(int(automate[1])):
        
        if str(i) in automate[2]:
            print("E", end=" ")
        
        if str(i) in automate[3]:
            print("S", end=" ")
        print("\t| ",end="")
        print(i, end=" |")

        if (int(automate[0]) >= 1):
            print("\t\t| ",end="")

        for k in range(5, len(automate)):
            if ((str(i) + " a"))  in automate[k]:
                print(automate[k].split(" ")[-1],end=" ")
        
        if (int(automate[0]) >= 2):
            print("|\t\t| ",end="")

        for l in range(5, len(automate)):
            if ((str(i) + " b")) in automate[l]:
                print(automate[l].split(" ")[-1],end=" ")
        
        if (int(automate[0]) >= 3):
            print("|\t\t| ",end="")

        for m in range(5, len(automate)):
            if ((str(i) + " c"))  in automate[m]:
                print(automate[m].split(" ")[-1],end=" ")
        if (int(automate[0]) >= 4):
            print("|\t\t| ",end="")

        for n in range(5, len(automate)):
            if ((str(i) + " d")) in automate[n]:
                print(automate[n].split(" ")[-1],end=" ")
        if(int(automate[0]) >= 1):
            print("|\n")
        else:
            print("\n")
   
    return 

def est_complet(automate):
    alphabet = ['a','b','c','d']
    cpt = 0 #Compteur de cases
    cpt_doublon=0 #Permet de savoir si on a déja compté la case
    for i in range(int(automate[1])): #nb_etats
        for j in range(int(automate[0])): #nb_symboles
            for k in range(5,len(automate)): #nb_transitions
                ch = str(i) + " " + alphabet[j]
                if ch in automate[k] and cpt_doublon==0:
                    print(ch, "===", automate[k])
                    cpt+=1
                    cpt_doublon=1
            cpt_doublon=0

    if cpt == int(int(automate[0])*int(automate[1])) :
        print("L'automate est complet\n")
    else:
        print("L'automate n'est pas complet\n")

    return 

def est_deterministe(automate):
    cpt=0
    if len(automate[2].split(" ")) >= 2:
        print("L'automate n'est pas deterministe\n")
    
    else:
        cpt_a = 0
        cpt_b = 0
        cpt_c = 0
        cpt_d = 0
        while (cpt <= int(automate[1])) and ((cpt_a <= 1 and cpt_b <= 1 and cpt_c <= 1 and cpt_d <= 1)):
            for k in range(5, len(automate)):
                if ((str(cpt) + " a")) in automate[k]:
                    cpt_a+=1
  
            for l in range(5, len(automate)):
                if ((str(cpt) + " b")) in automate[l]:
                    cpt_b+=1
            
            for m in range(5, len(automate)):
                if ((str(cpt) + " c")) in automate[m]:
                    cpt_c+=1
  
            for n in range(5, len(automate)):
                if ((str(cpt) + " d")) in automate[n]:
                    cpt_d+=1
            
            if (cpt_a > 1 or cpt_b > 1 or cpt_c > 1 or cpt_d > 1):
                print("L'automate n'est pas deterministe\n")

            else:
                cpt+=1
                cpt_a = 0
                cpt_b = 0
                cpt_c = 0
                cpt_d = 0
        
            if cpt == int(automate[1]):
                print("L'automate est deterministe\n")
            
    return

def est_standard(automate):
    cpt=0
    standard=True
    if len(automate[2].split(" ")) >= 2:
        print("L'automate n'est pas standard\n")
    
    else:
        etat_inital = int(automate[2])

        while (cpt <= int(automate[1])) and (standard==True):

            for k in range(5, len(automate)):
                if (((str(cpt) + " a")) in automate[k]) and (int(automate[k].split(" ")[-1]) == etat_inital):
                    standard=False
  
            for l in range(5, len(automate)):
                if (((str(cpt) + " b")) in automate[l]) and (int(automate[l].split(" ")[-1]) == etat_inital):
                    standard=False
            
            for m in range(5, len(automate)):
                if (((str(cpt) + " c")) in automate[m]) and (int(automate[m].split(" ")[-1]) == etat_inital):
                    standard=False
  
            for n in range(5, len(automate)):
                if (((str(cpt) + " d")) in automate[n]) and (int(automate[n].split(" ")[-1]) == etat_inital):
                    standard=False
            cpt+=1

        if standard == False:
            print("L'automate n'est pas standard\n")
        else:
            print("L'automate est standard\n")
    
    return

def standardisation(automate):    
    etats_initiaux = automate[2].split(" ")
    etats_terminaux = automate[3].split(" ")
    print(etats_initiaux, etats_terminaux)

    afficher_automate(automate)

    print("E",end=" ")
    for element in etats_initiaux:
        if element in etats_terminaux:
            print("S",end="")

    print("\t| i |",end="")

    if (int(automate[0]) >= 1):
        print("\t\t| ",end="")

    for k in range(5, len(automate)):
        for i in range(len(etats_initiaux)):
            if ((etats_initiaux[i] + " a"))  in automate[k]:
                print(automate[k].split(" ")[-1],end=" ")
        
    if (int(automate[0]) >= 2):
        print("|\t\t| ",end="")

    for l in range(5, len(automate)):
        for i in range(len(etats_initiaux)):
            if (etats_initiaux[i] + " b") in automate[l]:
                print(automate[l].split(" ")[-1],end=" ")
        
    if (int(automate[0]) >= 3):
        print("|\t\t| ",end="")

    for m in range(5, len(automate)):
        for i in range(len(etats_initiaux)):
            if (etats_initiaux[i] + " c") in automate[m]:
                print(automate[m].split(" ")[-1],end=" ")
    if (int(automate[0]) >= 4):
        print("|\t\t| ",end="")

    for n in range(5, len(automate)):
        for i in range(len(etats_initiaux)):
            if (etats_initiaux[i] + " d") in automate[n]:
                print(automate[n].split(" ")[-1],end=" ")

    if(int(automate[0]) >= 1):
        print("|\n")

def determinisation_complete(automate): 
    sortie=False
    etats_initiaux = automate[2].split(" ")
    etats_terminaux = automate[3].split(" ")
    alphabet = ['a','b','c','d']
    
    etats_suivants=[]
    temp_a=[]
    temp_b=[]
    temp_c=[]
    temp_d=[]
    
    print("\n\tEtats\t\t", end="")
    for i in range(int(automate[0])):
        print("| ",end="")
        print(alphabet[i], end=" |\t\t")
    print("\n")

    if len(etats_suivants) == 0:
        print("E",end=" ")
    for element in etats_initiaux:
        if element in etats_terminaux:
            print("S",end="")

    print("\t| ",end="")
    for i in range(len(etats_initiaux)):
        print(etats_initiaux[i],end="")
    print(" |",end="")

    for k in range(5, len(automate)):
        for i in range(len(etats_initiaux)):
            if ((etats_initiaux[i] + " a"))  in automate[k]:
                temp_a.append(automate[k].split(" ")[-1])
            if (etats_initiaux[i] + " b") in automate[k]:
                temp_b.append(automate[k].split(" ")[-1])
            if (etats_initiaux[i] + " c") in automate[k]:
                temp_c.append(automate[k].split(" ")[-1])
            if (etats_initiaux[i] + " d") in automate[k]:
                temp_d.append(automate[k].split(" ")[-1])
    
    if(int(automate[0]) >= 1):
        temp_a = sorted(temp_a)
        etats_suivants.append(temp_a)

    if(int(automate[0]) >= 2):
        temp_b = sorted(temp_b)
        etats_suivants.append(temp_b)

    if(int(automate[0]) >= 3):
        temp_c = sorted(temp_c)
        etats_suivants.append(temp_c)

    if(int(automate[0]) >= 4):
        temp_d = sorted(temp_d)
        etats_suivants.append(temp_d)


    for i in range(len(etats_suivants)):
        print("\t\t| ",end="")
        for j in range(len(etats_suivants[i])):
            print(etats_suivants[i][j],end="")
        print(" |",end="")
    print("\n")
    
    temp_a=[]
    temp_b=[]
    temp_c=[]
    temp_d=[]
    
    for i in range(len(etats_suivants)):
        for m in range(len(etats_suivants[i])):
            if etats_suivants[i][m] in etats_terminaux:
                print("S",end="")           
        print("\t|",''.join(etats_suivants[i]),end=" |")
        for j in range(5, len(automate)):
            for k in range(len(etats_suivants[i])):
                if ((etats_suivants[i][k] + " a"))  in automate[j]:
                    temp_a.append(automate[j].split(" ")[-1])

                if (etats_suivants[i][k] + " b") in automate[j]:
                    temp_b.append(automate[j].split(" ")[-1])

                if (etats_suivants[i][k] + " c") in automate[j]:
                    temp_c.append(automate[j].split(" ")[-1])

                if (etats_suivants[i][k] + " d") in automate[j]:
                    temp_d.append(automate[j].split(" ")[-1])
        
        if len(temp_a) == 0:
            temp_a.append('P')
        
        if len(temp_b) == 0:
            temp_b.append('P')
        
        if len(temp_c) == 0:
            temp_c.append('P')
        
        if len(temp_d) == 0:
            temp_a.append('P')
        
        temp_a=list(set(temp_a))
        temp_b=list(set(temp_b))
        temp_c=list(set(temp_c))
        temp_d=list(set(temp_d))

        if(int(automate[0]) >= 1):
            print("\t\t|",''.join(temp_a),end="")
            print(" |",end="")

        if(int(automate[0]) >= 2):
            print("\t\t|",''.join(temp_b),end="")
            print(" |",end="")

        if(int(automate[0]) >= 3):
            print("\t\t|",''.join(temp_c),end="")
            print(" |",end="")

        if(int(automate[0]) >= 4):
            print("\t\t|",''.join(temp_d),end="")
            print(" |",end="")

        print("\n")

    if 'P' in (temp_a or temp_b or temp_c or temp_d): 
        print("\t| P |",end=" ")
        for i in range(int(automate[0])):
            print("\t\t| P |",end="")
        

        
   
    return

      
  
    

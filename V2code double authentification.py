import random

mot_de_passe = input("Choisissez un mot de passe : ")

max_essais = 1
essais_restants = max_essais

while essais_restants > 0:
    saisie = input("Tapez votre mot de passe : ")
    
    if saisie == mot_de_passe:
        print("Mot de passe correct !")
        break  
    else:
        essais_restants -= 1
        print(f"Mot de passe incorrect. Il vous reste {essais_restants} essai(s).")

if essais_restants == 0:
    print("Vous avez épuisé tous vos essais. Trois chiffres vont être générés.")
    
    chiffres = [random.randint(0, 9) for _ in range(3)]
    code_secret = ''.join(map(str, chiffres))

    with open('/Users/REAGAN/Desktop/code_verif/code_secret.txt', 'w') as fichier:
        fichier.write(code_secret)

    print(f"Les trois chiffres aléatoires ont été enregistrés dans 'code_secret.txt'") 
    
    code_verification = input("Entrez le code de vérification envoyé : ") 

    if code_verification == code_secret:
        print("Code de vérification correct. Connexion réussie.")
    else:
        print("Code de vérification incorrect. Connexion échouée.")




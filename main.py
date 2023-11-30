historique_total = [] 

def calculatrice():
    while True:
        num1 = float(input("Entrez le premier nombre : "))
        operator = input("Entrez l'opérateur (+, -, *, /, %) : ")
        num2 = float(input("Entrez le deuxième nombre : "))

        resultat = None

        if operator == "+":
            resultat = num1 + num2
        elif operator == "-":
            resultat = num1 - num2
        elif operator == "*":
            resultat = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Division impossible par 0")
            else:
                resultat = num1 / num2
        elif operator == "%":
            resultat = num1 % num2
        else:
            print("Le signe n'est pas correct")

        if resultat is not None:
            operation = f"{num1} {operator} {num2} = {resultat}"
            historique_total.append(operation)

        continuer = input("Voulez-vous continuer à faire des calculs ? (y/n)")
        if continuer != "y":
            break

def historique():
    for operation in historique_total:
        print(operation)

    supp=input("Voulez vous supprimer l'historique ? (y/n)")
    if supp == "y" :
        del historique_total[:]

        
while True:
    calculatrice()
    historique()

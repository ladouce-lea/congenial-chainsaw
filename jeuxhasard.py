from random import*

print("jeux de hasard")
print("retrouve le chiffre entre 1 et 1000")

def jeux():
    
    valeur=randrange(1001)
    
    rep = int(input("enter une réponse :"))
    k=0

    while rep<valeur or rep>valeur:
        
        if rep<valeur:
            print("trop petit, recommence ")
            k=k+1
            rep = int(input("enter une réponse :"))
        elif rep>valeur:
            print("trop grand, recommence")
            k=k+1
            rep = int(input("enter une réponse :"))

    if rep==valeur:
        print("bravo, tu a trouver en ",k,"essais")
        a=int(input("tu veux rcommencer? tape 1 sinon 2 :"))
        if a==1:
            jeux()
        else:
            exit
        

jeux()


print("Entrez deux nombres a et b: ")
a = int(input("Entrez un nombre a :"))
b = int(input("Entrez un nombre b :"))

print("""
      # pour faire la somme entrer 1.
      # pour faire le produit entrer 2.
      # pour faire la soustraction entrer 3.
      # pour faire la division entrez 4.
      # pour Quiter enrez 0.
      """)

 
choix = input()
if choix == '1':
    print(f"la somme et de a et b est = {a+b}")

elif choix == '2':
    print(f"le produit de a et b est = {a*b}")
elif choix == '3':
    print(f"la soustraction de a et b est = {a-b}")
else:
    print(f"la division de a sur b est = {a/b}")
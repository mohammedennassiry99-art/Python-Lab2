entier = 42              # int
flottant = 3.14          # float
texte = "Python"         # str
vrai_ou_faux = True      # bool

print(entier, "→", type(entier))
print(flottant, "→", type(flottant))
print(texte, "→", type(texte))
print(vrai_ou_faux, "→", type(vrai_ou_faux))

age_str = input("Quel âge as-tu ? ")
print("Tu as saisi :", age_str, "→", type(age_str))

age = int(age_str)
print("Après conversion :", age, "→", type(age))
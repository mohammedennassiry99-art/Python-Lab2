mot = input("Enrez un mot: ")
print(f"la longuer de ce mot est:{len(mot)}")
print(f"en majuscule: {str.upper(mot)}")
print(f"en minuscules : {str.lower(mot)}")
print(f"inverse : {mot[::-1]}")
inverse = mot[::-1]
n = len(mot)
palindrome  = True

for i in range(n):
    if mot[i] != inverse[i]:
        palindrome  = False

 

if palindrome  == True:
    print("le mot est palindrome ")
else:
    print("le n'est pas palindrome ")

c = int(input("Entrez une valeur en °C:"))
f = c + 9/5 + 32
k = c + 273.15

print(f"{c}°C = {f}°F = {k}K")

f1 = float(input("Entrez une valeur en °F:"))
c1 = f - 9/5 - 32

k1 = f1 + 273.15 - 9/5 - 32

print(f"{f1}°F = {c1}°C = {k1}°K ")

k2 = float(input("Entrez une valeur en °K:"))

f2 = k2 - 273.15 + 9/5 + 32
c2 = k2 - 273.15

print(f"{k2}°K = {c2}°C = {f2}°F ")


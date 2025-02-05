"""
tupla = (15,"Mesa",(59,14,"hola", False),3.1416,True,["Mazda","Renault","Fiat"],15)

print(tupla[2][2])
"""
frutas = ("fresa","papaya","manzana","papaya")
print(frutas.count("papaya"))
print(frutas.index("papaya"))

copia = list(frutas)
print(frutas)
print(copia)

copia.append("mango")
print(copia)

frutas = tuple(copia)
print(frutas)
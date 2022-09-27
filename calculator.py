from re import A


print("Simple Calculator")
a = 100
b = 50
 
# Operators
Add = a + b
Sub = a - b
Mul = a * b
Div = a / b
Mod = a % b
Sq = a * a
Sq2 = b * b
Sq3 = Sq + Sq2 + 2 * a * b
Cube = a * a * a
Cube2 = b * b * b

print("The sum of",a,"and",b,"is:",Add)
print("The diff of",a,"and",b,"is:",Sub)
print("The product of",a,"and",b,"is:",Mul)
print("The div of",a,"and",b,"is:",Div)
print("The Mod of",a,"and",b,"is:",Mod)
print("The Sq of",a,"is:",Sq)
print("The Sq2 of",b,"is:",Sq2)
print("The Sq3 of",a,"and",b,"is:",Sq3)
print("The cube of",a,"is:",Cube)
print("The cube of",b,"is:",Cube2)
#rectangule_area
#10.	Crie um algoritmo que calcule a área de um retângulo, sendo que os comprimentos da altura e da base são informados pelo usuário. A área do retângulo é calculada multiplicando-se a altura pela base.

base = float(input("Insira a base de seu retângulo em centimetros: "))
height = float(input("Insira a altura de seu retângulo em centimetros: "))

rectangule_area = base * height

print(f"A área de um retângulo com base {base:.2f}cm e altura {height:.2f}cm é: {rectangule_area:.2f}cm")
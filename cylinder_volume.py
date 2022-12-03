#cylinder_volume
#13.	Crie um algoritmo que calcule o volume de uma caixa d’água cilíndrica, sendo que os comprimentos do raio e a altura são informados pelo usuário. O volume é calculado multiplicando-se pi, o raio ao quadrado e a altura.

radius = float(input("Insira o raio do cilindro em centimetros: "))
pi = 3.14
height = float(input("Insira a altura da cilindro em centimetros: "))

cylinder_volume = (pi*((radius**2)*height))

print(f"O volume de um cilindro de raio {radius:.0f}cm e altura {height:.0f}cm é: {cylinder_volume}cm³")
#circle_area
#11.	Crie um algoritmo que calcule a área de um círculo, sendo que o comprimento do raio é informado pelo usuário. A área do círculo é calculada multiplicando-se pi e o raio ao quadrado.

radius = float(input("Insira o raio da circunferência em centimetros: "))
pi = 3.14

circle_area = (radius**2)*pi

print(f"O a área de uma circunferência de raio {radius:.2f}cm é: {circle_area:.2f}cm")
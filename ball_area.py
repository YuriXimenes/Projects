#ball_area
#12.	Crie um algoritmo que calcule a área de uma esfera, sendo que o comprimento do raio é informado pelo usuário. A área da esfera é calculada multiplicando-se 4 vezes pi e o raio ao quadrado.

radius = float(input("Insira o raio da circunferência em centimetros: "))
pi = 3.14

ball_area = (4*(pi*(radius**2)))

print(f"A área de uma esfera de raio {radius:.0f}cm é: {ball_area:,.0f}cm")
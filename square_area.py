#square_area
#9.	Crie um algoritmo que calcule a área de um quadrado, sendo que o comprimento do lado é informado pelo usuário. A área do quadrado é calculada elevando-se o lado ao quadrado.

side = float(input("Insira o lado do quadrado em centimetros: "))
area_square = side **2

print(f"A área do quadrado de lado {side} é: {area_square:.2f} cm.")
#gasoline_calculator
#5.	Um motorista deseja abastecer um valor X em reais, de combustível. Escreva um algoritmo para ler o preço do litro do combustível e o valor que o motorista deseja abastecer. Em seguida, informe quantos litros foram abastecidos.

liter_value = input("Coloque o valor da cotação atual do litro de gasolina em reais: ")
liter_gasoline = input("Qual valor o motorista deseja abastecer? ")

liter_value_float = float(liter_value)
liter_gasoline_float = float(liter_gasoline)

print(f"A cotação atual do litro da gasolina é de R${liter_value_float:.2f} e o motorista deseja abastecer R${liter_gasoline_float:.2f}.")

liter = liter_gasoline_float/liter_value_float

liter_value_float = float(liter)

print(f"A quantidade de litros que o motorista terá abastecido com R${liter_gasoline_float:.2f} é de {liter:.2f} litros")
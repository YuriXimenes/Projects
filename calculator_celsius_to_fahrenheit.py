# calculator_celsius_to_fahrenheit
#4.	Crie um algoritmo que recebe um valor de temperatura em Celsius e o converte para Fahrenheit. 
#F = (C * 9/5)+32

celsius = input("Entre com o valor de Celsius ")
celsius_float = float(celsius)
result = ((celsius_float*9)/5)+32
print(f"O resultado da conversão de {celsius_float:.2f}ºC para Fahrenheit é: {result:.2f}ºF")
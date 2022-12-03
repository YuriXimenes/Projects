#tips_calculator
#7.	Crie um algoritmo que calcule a gorjeta a ser paga de uma conta de restaurante. A gorjeta é calculada como sendo 10% do valor da conta, que deve ser informado pelo usuário.

value = input("Qual foi o valor final da mesa que está atendendo? ")

value_float = float(value)

tip = value_float * 0.1

tip_float = float(tip)

value_final = value_float + tip_float

print(f"O valor de consumação da mesa que estava atendendo é de R${value_float:.2f} e sua gorjeta é de R${tip:.2f}.")

while tip:
    tip_choice = input("O cliente aceitou pagar a gorjeta? [1] Sim [2] Não. ")
    if(tip_choice == "1"):
        print(f"Obrigado por contribuir com a gorgeta, logo seu pagamento é de R${value_final:.2f}")
        break
    elif(tip_choice == "2"):
        print(f"Entendemos que não deseje pagar a gorgeta, logo, seu pagamento é de R${value_float:.2f}")
        break
    else:
        print("O valor inserido não corresponde a nenhuma das opções.")
        
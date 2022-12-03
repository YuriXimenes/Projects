#salary_adjustment
#8.	Crie um algoritmo que calcule o novo valor de um salário a partir de um valor percentual de reajuste. O valor atual do salário e o valor percentual do reajuste devem ser informados pelo usuário como, por exemplo, 7,3%.

name = input("Qual é o seu nome? ")
salary = input(f"{name}, informe seu salário atual: ")
adjustment = input(f"{name}, informe, em porcentagem, o reajuste que receberá: ")

salary_float = float(salary)
adjustment_float = float(adjustment)

change_to_percent = adjustment_float / 100

percent_float = float(change_to_percent)

increase_salary = salary_float * percent_float

increase_salary_float = float(increase_salary)

new_salary = float(increase_salary_float + salary_float)

print(f"{name}, atualmente você recebe R${salary_float:,.2f} e receberá um reajuste de {adjustment_float:.2f}%.")
print(f"Isso significa que terá um aumento de R${increase_salary:,.2f} e seu novo salário será: R${new_salary:,.2f}.")
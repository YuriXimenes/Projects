#Personal_Finance

name = str(input("Qual seu nome? "))
monthly_income = float(input("Informe sua renda mensal: "))
housing_expenses = float(input("Informe sua despesa mensal com moradia: "))
education_expenses = float(input("Informe sua despesa mensal com educação: "))
transportation_expenses = float(input("Informe sua despesa mensal com transporte: "))

housing = 0.3
education = 0.2
transportation = 0.1

max_housing = monthly_income*housing
max_education = monthly_income*education
max_transportation = monthly_income*transportation

print(f"Sua receita mensal é de: R${monthly_income:,.2f}")
if(housing_expenses > max_housing):
    print(f"{name}, você está com uma despesa com moradia maior do que o ideal. Ela deve representar, no máximo, 30% de sua receita mensal, sua atual despesa é de: R${housing_expenses:,.2f} e o ideal seria, no máximo, R${max_housing:,.2f}. Você está acima do limite em R${housing_expenses-max_housing:,.2f}")
else:
    print(f"Parabéns {name}, você está abaixo do que o máximo ideal para despesa com moradia. Sua atual despesa é de: R${housing_expenses:,.2f} e o máximo ideal é de R${max_housing:,.2f}. Você está abaixo do limite máximo em R${max_housing-housing_expenses:,.2f}")

if(education_expenses > max_education):
    print(f"{name}, você está com uma despesa com educação maior do que o ideal. Ela deve representar, no máximo, 20% de sua receita mensal, sua atual despesa é de: R${education_expenses:,.2f} e o ideal seria, no máximo, R${max_education:,.2f}. Você está acima do limite em R${education_expenses-max_education:,.2f}")
else:
    print(f"Parabéns {name}, você está abaixo do que o máximo ideal para despesa com educação. Sua atual despesa é de: R${education_expenses:,.2f} e o máximo ideal é de R${max_education:,.2f}. Você está abaixo do limite máximo em R${max_education-education_expenses:,.2f}")

if(transportation_expenses > max_transportation):
    print(f"{name}, você está com uma despesa com transporte maior do que o ideal. Ela deve representar, no máximo, 10% de sua receita mensal, sua atual despesa é de: R${transportation_expenses:,.2f} e o ideal seria, no máximo, R${max_transportation:,.2f}. Você está acima do limite em R${transportation_expenses-max_transportation:,.2f}")
else:
    print(f"Parabéns {name}, você está abaixo do que o máximo ideal para despesa com transporte. Sua atual despesa é de: R${transportation_expenses:,.2f} e o máximo ideal é de R${max_transportation:,.2f}. Você está abaixo do limite máximo em R${max_transportation-transportation_expenses:,.2f}")
#1.	Crie um algoritmo que receba, como entrada, o valor de três notas de um aluno - com valor entre 0 e 10, e, em seguida, informe a média entre elas. 
# a.	Neste momento, não é necessário validar se a nota está dentro do intervalo válido!

name = input("What's the student's name? ")

note_av1 = input(f"What's {name}'s first note? ")
note_av2 = input(f"What's {name}'s second note? ")
note_av3 = input(f"What's {name}'s third note? ")

note_av1_float = float(note_av1)
note_av2_float = float(note_av2)
note_av3_float = float(note_av3)

average = (note_av1_float + note_av2_float + note_av3_float) / 3

print(f"{name} had the average {average:.2f}")

if(average >= 6):
    print(f"{name} passed his subject")
else:
    print(f"{name} didn't passed his subject")
# two_notes_average
#6.	Crie um algoritmo para calcular a média de duas notas digitadas pelo usuário, sendo que a segunda nota tem peso dois.

name = input("Insira o nome do aluno avaliado: ")
note_1_info = input("Insira a 1º nota: ")
note_2_info = input("Insira a 2º nota: ")

note_1_float = float(note_1_info)
note_2_float = float(note_2_info)

name_str = str(name)
note_1 = note_1_float
note_2 = note_2_float * 2

media = (note_1 + note_2) / (1 + 2)

if(media >= 7):
    print(f"O aluno {name} passou de ano! Sua média foi {media:.2f}")
else:
    print(f"O aluno {name} reprovou de ano! Sua média foi {media:.2f}")
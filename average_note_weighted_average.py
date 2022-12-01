name = input("What's the student's name? ")

note_av1 = input(f"What's {name}'s first note? ")
note_av2 = input(f"What's {name}'s second note? ")
note_av3 = input(f"What's {name}'s third note? ")

note_av1_float = float(note_av1)
note_av2_float = float(note_av2)
note_av3_float = float(note_av3)



average = ((note_av1_float*1) + (note_av2_float*2) + (note_av3_float*3))/(1 + 2 + 3)

print(f"{name} had the average {average:.2f}")

if(average >= 6):
    print(f"{name} passed his subject")
else:
    print(f"{name} didn't passed his subject")

    5
    10
    14
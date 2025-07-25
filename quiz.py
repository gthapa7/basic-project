print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What is the height of Mount Everest, the highest mountain in the world?")
if answer.lower() == "8,848.86 meters":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Which mountain is known as the 'Fishtail Mountain' in Nepal?")
if answer.lower() == "Machapuchare":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Which mountain in Nepal is the third highest in the world?")
if answer.lower() == "Kangchenjunga":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Which region in Nepal is famous for trekking routes?")
if answer.lower() == "The Annapurna Region":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
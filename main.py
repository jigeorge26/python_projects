print("Welcome to my computer quiz project")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Okay! Let's begin the quiz. :)")
score = 0

answer = input("What animal is Alabama's football team mascot? ").lower()
if answer == "elephant":
    print("correct")
    score += 1
else:
    print("incorrect!")

answer = input("What animal is Georgia's football team mascot? ").lower()
if answer == "bulldog":
    print("correct")
    score += 1
else:
    print("incorrect!")

answer = input("What animal is Florida's football team mascot? ").lower()
if answer == "alligator":
    print("correct")
    score += 1
else:
    print("incorrect!")

answer = input("What animal is Michigan's football team mascot? ").lower()
if answer == "wolverine":
    print("correct")
    score += 1
else:
    print("incorrect!")

answer = input("What animal is Oregon's football team mascot? ").lower()
if answer == "duck":
    print("correct")
    score =+ 1
else:
    print("incorrect!")

print("You got " + str(score) + " questions correct")
print("You got " + str((score / 5) * 100) + "%." )

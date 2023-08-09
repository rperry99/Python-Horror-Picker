import random

horrorList = ["Friday the 13th", "Halloween", "Nightmare on Elm Street", "Hellraiser"]

userEntry = input("Are you ready to be scared?\n")
randomMovie = random.choice(horrorList)

print("Looks like", randomMovie, "is going to give you nightmares tonight.")
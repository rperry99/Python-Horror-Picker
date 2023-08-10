import random
import numpy as np

# Create the random list of horror movies along with their sub-genre
horrorList = np.array([
        ["Friday the 13th", "Slasher"],
        ["Halloween", "Slasher"],
        ["Nightmare on Elm Street", "Slasher"],
        ["Hellraiser", "Slasher"],
        ["Paranormal Activity", "Supernatural" ],
        ["The Blair Witch Project", "Supernatural"],
        ["Saw", "Torture"],
        ["Killer Klowns from Outer Space", "Comedy"],
        ["[REC]", "Found Footage"]])

# Ask for user input
userEntry = input("Are you ready to be scared?\n")

# Choose a random row in the numpy array
randomRow = np.random.randint(len(horrorList), size = 1)

# Select the movie from this row.
randomMovie = random.choice(horrorList[randomRow[0]])

print("Looks like", randomMovie, "is going to give you nightmares tonight.")
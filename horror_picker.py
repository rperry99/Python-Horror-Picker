import random
import numpy as np

def giveOutput(entry, movie):
    print(entry.title(), "is what you are looking for? Cool, give", movie, "a try.")

# Function to pick a random row, and then a random movie.
def pickMovie(movies, entry):
    np.random.shuffle(movies)

    for movie in movies:
        movieStr = movie[1]
        if movieStr.lower() == entry.lower():
            giveOutput(entry, movie[0])
            return
        
    print("Looks like we don't have a movie in the", entry, "subgenre. Sorry!")
    return

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
userEntry = input("What subgenre of horror movie do you want to watch?\n")

# Run the program
pickMovie(horrorList, userEntry)
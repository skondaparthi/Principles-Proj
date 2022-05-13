import random

print(
    "Try cracking the code by guessing the secret word! You have 4 chances, so choose wisely. Enter the singluar form of animal you guess and the plural form of the NFL team you guess."
)
print("")

chosen_list = input(
    "Would you like to play the NFL version or the animal version?\n(A = animal, N = NFL): "
)
if chosen_list.lower() != "a" and chosen_list.lower() != "n":
    while True:
        print("")
        chosen_list = input(
            "Invalid input! Please try again!\n(A = animal, N = NFL): ")
        if chosen_list.lower() == "a" or chosen_list.lower() == "n":
            break

animal_list = {
    "giraffe": ('"I am a herbivore"', '"I eat off of trees"'),
    "mouse": ('"I am small and have a short brown tail"','"I am only attracted to cheeeese!"'),
    "skunk": ('"I am mostly black"', '"If you scare me, your nose will regret it"'),
    "tiger": ('"You can sometimes see me in trees"', '"I do have black stripes, but am mostly another color"'),
    "chicken": ('"I have wings"', '"People love eating me"'),
    "whale": ('"I live in the ocean"', '"I am the biggest animal alive"'),
    "elephant": ('"I am big"', '"I am big and have really good memory"'),
    "bear": ('"I like honey."', '"I can be black, brown, or white."'),
    "deer": ('"I am famous for being prey."', '"I am frozen in headlights"'),
    "camel": ('"I eat a lot of leaves and grass but not a lot of water"', '"I have a hump or two"'),
    "penguin": ('"I have webbed feet and wings"', '"I love it when it is cold"'),
    "monkey": ('"I love playing in trees"', '"I make funny faces when kids look at me"'),
    "kangaroo": ('"I jump so much and its hard to stop"', '"I carry my baby in my pouch"'),
    "turtle": ('"I hide my head if I am shy"', '"My home is always with me"'),
    "buffalo": ('"I am heavy and hairy"', '"I was an animal whose parts were not wasted when eaten"'),
    "caterpillar": ('"I have many legs"', '"Once I turn older, I will be able to fly"'),
    "cat": ('"I am furry and very gentle"', '"I am a common pet for people"'),
    "cow": ('"You sometimes see me when traveling"', '"Without me, your bones will be brittle"'),
    "jellyfish": ('"I do sting sometimes"', '"I live in the water"'),
    "butterfly": ('"I fly around unpredictably"', '"I live landing on flowers"'),
    "octopus": ('"I have a big head"', '"I have 8 \'legs\'"'),
    "squid": ('"My eye can sometimes be the size of a dinner plate"', '"I shoot out ink when I get startled"'),
    "snake": ('"I can sometimes be very deadly"', '"I have fangs"'),
}

sports_list = {
    "chiefs": ('"I won super bowl IV"', '"I am associated with a tiktoker"'),
    "packers": ('"Georgia copied us"', '"Cheese is tradition"'),
    "seahawks": ('"I am a bird"', '"I am afraid of the 1 yard line"'),
    "vikings": ('"I am known for horns"', '"I sail on ships"'),
    "bears": ('"I cannot find a QB to save my life"', '"Double-doink"'),
    "lions": ('"I am supposed to be ferocious, but I am not in the NFL"', '"I am the king of the jungle"'),
    "broncos": ('"I am only relevant because of my QB"', '"There is a car named after me"'),
    "chargers": ('"I have no fans"', '"I am part of a city that hosts 2 teams"'),
    "raiders": ('"Our team is full of controversies"', '"We have a very fast player"'),
    "cowboys": ('"We are over valued"', '"I am the team of America"'),
    "cardinals": ('"I fly"', '"Calamari"'),
    "patriots": ('"Everyone hates us cuz of our success"', '"I <3 deflated balls"'),
    "ravens": ('"I run so much and its hard to stop"', '"I am a regular season god"'),
    "rams": ('"I moved to a different city"', '"I got a new stadium"'),
    "bills": ('"You see me at Yellowstone"', '"My city is an animal"'),
    "jets": ('"I fly"', '"I always have multiple first rounders"'),
    "jaguars": ('"My uniforms are ugly"', '"I was only relevant because of my defense a couple years ago"'),
    "titans": ('"People attack me."', '"We get carried by our runningback"'),
    "dolphins": ('"I make weird noises"', '"I always beat the patriots"'),
    "bengals": ('"I mainly live in India"', '"I burrow"'),
    "browns": ('"I have more ads than wins"', '"My QB beats more women than NFL teams"'),
    "texans": ('"I blew a 24 point lead in the playoffs recently"', '"My former coach traded our franchise for a bag of chips"'),
    "panthers": ('"The Falcons ruined our clean slate"', '"My QB did not dive for a fumble"'),
}


def category(selection):
    if chosen_list.lower() == "a":
        secret_word = random.choice(tuple(animal_list.keys()))
        selection = animal_list.get(secret_word)
    elif chosen_list.lower() == "n":
        secret_word = random.choice(tuple(sports_list.keys()))
        selection = sports_list.get(secret_word)

    guess = ""
    guess1 = ""
    guess5 = ""
    guess_count = 0
    guess_limit = 1
    out_of_guesses = False

    while guess.lower() != secret_word and not (out_of_guesses):
        if guess_count == 0:
            guess1 = input("Here's a hint: " + str(selection[0]) +
                           " Enter your first guess: ")
            if guess1.lower() == secret_word:
                print("")
                print("First Try!?")
                break
        elif guess_count == 2:
            guess5 = input("Incorrect! Your final hint is: " + str(selection[1]) +
                           " Enter your final guess: ")
            if guess5.lower() == secret_word:
                print("")
                print("Last Try?! You probably got lucky.")
                break
        if guess_count < 1 + guess_limit:
            guess_count += 1
            guess = input("Incorrect! Enter another guess: ")

        else:
            out_of_guesses = True

    if out_of_guesses:
        print("")
        print("Out of guesses, YOU LOSE! The correct answer was, " +
              secret_word + "! Press F5 to play again.")
    else:
        if guess == secret_word:
            print("")
            print(
                "Correct, You Win!! Press Ctrl + Enter if you want to play again!"
            )
        else:
            print("Correct, You Win!!")


category(chosen_list)

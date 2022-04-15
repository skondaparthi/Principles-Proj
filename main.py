import random
print("Try cracking the code by guessing a zoo animal! You have 5 chances, so choose wisely. Enter the singluar form of animal you guess.")
print("")


animal_list = {"giraffe": ('"I am a herbivore"', '"I eat off of trees"'),
               "mouse": ('"I am small and have a short brown tail"', '"I am only attracted to cheeeese!"'),
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
               "donkey": ('""', '"I have fangs"'),
               }
    
secret_word = random.choice(tuple(animal_list.keys()))

hints = animal_list.get(secret_word)

guess = ""
guess1 = ""
guess5 = ""
guess_count = 0
guess_limit = 2
out_of_guesses = False

while guess.lower() != secret_word and not (out_of_guesses):
        #for index in range(1):
    if guess_count == 0:
        guess1 = input("Here's a hint: " + str(hints[0]) +  " Enter your first guess: ")
        if guess1.lower() == secret_word:
            print("")
            print("First Try!?")
            break
    elif guess_count == 3:
        guess5 = input("Incorrect! Your final hint is: " + str(hints[1]) + " Enter your final guess: ")
        if guess5.lower() == secret_word:
            print("")
            print("Last Try?! You probably got lucky.")
            break
    if guess_count < 1 + guess_limit:
        guess_count += 1
        if guess_count == 1:
            guess = input("Incorrect! Enter another guess: ")
        else:
            guess = input("Incorrect! Enter another guess: ")
            
    else: out_of_guesses = True

if out_of_guesses:
    print("")
    print("Out of guesses, YOU LOSE! The correct answer was, " + secret_word + "! Press F5 to play again.")
else:
    if guess == secret_word:
        print("")
        print("Correct, You Win!! Press F5 if you want to play again!")
    else:
        print("Correct, You Win!!")
    


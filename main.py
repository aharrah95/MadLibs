# string concatenation (a.k.a. How to put strings together)
# example: let's say we want to create a string that says "My favorite game is ____"
import verb as verb

game_title = "Kingdom Hearts III"  # a string variable, like "Batman: Arkham Knight"
youtuber = "Markiplier"
favorite_food = "breakfast burger, with fried egg and bacon!"

# a few different ways to do this
print("My favorite game is " + game_title + ".")
print("I just subscribed to {}!".format(youtuber))
print(f"My favorite game is a {favorite_food}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
thing = input("Thing: ")
celebrity = input("Celebrity: ")


madlib = f"Computer programming is such a(n) {adj}. But I still love it, it's always so thrilling when I {verb1}! In " \
         f"my spare time I like to {verb2} in my {thing}. My favorite singer is {celebrity}. "

print(madlib)

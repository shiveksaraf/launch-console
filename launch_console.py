# launch_console.py
# Elite 101 prework - my Launch Console
# Shivek Saraf
#
# Menu-loop shape (greet -> name -> while loop over a menu) is adapted from the
# Elite 101 prework example in the Guided Practice zone.
# Drafted with help from Claude (AI assistant); I read every line, changed the
# menu options and the text, and tested it in my Codespace.

print("Welcome to the Launch Console!")
print()

name = input("What's your name? ")
print("Welcome to " + name + "'s Launch Console!")

running = True
while running:
    print()
    print("1) About me")
    print("2) My goals")
    print("3) Fun fact")            # my own menu option
    print("4) The product I'm eyeing")  # my own menu option
    print("5) Exit")
    choice = input("Pick 1-5: ")

    if choice == "1":
        print("I'm a high school student and a builder-in-training in Elite 101.")
        print("I like problems that look impossible right up until they don't.")
    elif choice == "2":
        print("My goal this term: ship a real project I'd be proud to show someone,")
        print("and get comfortable reading code I didn't write.")
    elif choice == "3":
        print("Fun fact: this is the first program I ever pushed to GitHub.")
    elif choice == "4":
        print("I'm eyeing StudySprint - I'd actually use a flashcard app that")
        print("made the review stick instead of just feeling productive.")
    elif choice == "5":
        print("Goodbye, " + name + "! Console shutting down.")
        running = False
    else:
        print("Please pick a number from 1 to 5.")

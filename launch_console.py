# launch_console.py
# Elite 101 prework - my Launch Console
# Shivek Saraf
#
# Menu-loop shape (greet -> name -> while loop over a menu) is adapted from the
# Elite 101 prework example in the Guided Practice zone.
# Drafted with help from Claude (AI assistant); I read every line, wrote my own
# menu options and text, and tested it in my Codespace.

print("Welcome to the Launch Console!")
print()

name = input("What's your name? ")
print("Welcome to " + name + "'s Launch Console!")

running = True
while running:
    print()
    print("1) About me")
    print("2) My goals")
    print("3) Fun fact")                # my own menu option
    print("4) The product I'm eyeing")  # my own menu option
    print("5) Exit")
    choice = input("Pick 1-5: ")

    if choice == "1":
        print("I'm a high school student in Elite 101, and I've been putting")
        print("projects on GitHub since middle school - mostly Python, plus")
        print("whatever the project needs. I like problems that look impossible")
        print("right up until they don't.")
    elif choice == "2":
        print("My goal this term: build something with an actual team instead")
        print("of solo. Tickets, code review, the whole loop. And get faster at")
        print("reading code I didn't write, because that's most of the job.")
    elif choice == "3":
        print("Fun fact: I rigged up my Dyson fan so I could control it from my")
        print("laptop over MQTT. More satisfying than the remote it shipped with.")
    elif choice == "4":
        print("I'm eyeing StudySprint. I've crammed the night before enough")
        print("times to know the review never actually sticks - I'd use")
        print("something that fixed that.")
    elif choice == "5":
        print("Thanks for stopping by, " + name + ". Console shutting down.")
        running = False
    else:
        print("Please pick a number from 1 to 5.")

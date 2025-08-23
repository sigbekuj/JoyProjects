#choose your own adventure game

name = input("Hi, type your name: ")
print("Hello " + name + " welcome to my game!")

should_we_play = input("Do you want to play? ").lower()
if should_we_play == "yes" or "y":
    print("Let's play!")
    direction = input("Do you want to go left or right? (left/right)").lower()
    if direction == "left":
        print("Ohno you went left and fell off a cliff, game over, try again ")
    else: 
        choice = input("Ohk you see a bridge, do you want to swim under it or cross it? swim/cross ")
        if choice == "swim":
            print("Ohno, you got eaten by a shark, game over, the end!")

else:
    print("Ohk,bye...")
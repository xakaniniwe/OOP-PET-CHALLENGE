from pet import Pet
import time 

if __name__ == "__main__":
    nini = Pet("Nini.Explorer")
    nini.get_status()

    print("Let's start our adventure with Nini.Explorer!\n")
    time.sleep(1)

    print("Nini.Explorer is feeling a bit peckish...")
    nini.eat()
    nini.get_status()
    time.sleep(1.5)

    print("Time for some exploration!")
    nini.play()
    nini.get_status()
    time.sleep(1.5)

    print("Nini.Explorer needs some rest after all that excitement...")
    nini.sleep()
    nini.get_status()
    time.sleep(2)

    print("\n--- Training Session ---")

    print("\nLet's try teaching Nini.Explorer a new skill...")
    trick1 = "spot hidden trails"
    print(f"Teaching '{trick1}'...")
    nini.train(trick1)
    nini.get_status()
    time.sleep(2)

    print("\nAnother useful explorer skill to learn...")
    trick2 = "identify rare plants"
    print(f"Teaching '{trick2}'...")
    nini.train(trick2)
    nini.get_status()
    time.sleep(2)

    print("\nOne more for today's lesson...")
    trick3 = "signal for help"
    print(f"Teaching '{trick3}'...")
    nini.train(trick3)
    nini.get_status()
    time.sleep(2)

    print("\nNini.Explorer remembers all the new tricks!")
    nini.show_tricks()
    time.sleep(1)

    print("\nAfter a long day of learning, Nini.Explorer plays some more...")
    nini.play()
    nini.get_status()
    time.sleep(1.5)

    print("Time for a good meal to replenish energy!")
    nini.eat()
    nini.eat()
    nini.get_status()

    print("\nNini.Explorer is ready for more adventures tomorrow!")
import random
from time import sleep
#Deez nuts
cowDrops = ["Bones ", "Cowhide", "Beef"]
greenDragonDrops = ["Dragon bones", "Green dragonhide", "Steel platelegs"]
bloodveldDrops = ["Bones", "Blood runes", "Mithril full-helm"]
spiderDrops = "Absolutely fucking nothing."

slayerTasks = ["cow", "green dragon", "bloodveld", "spider"]


def task():
    getTask = input("Hello, adventurer. Would you like a slayer task?\n")
    if getTask.lower() != "yes":
        print("Well fuck off back to lumby then!")
        return False

    else:
        newTask = random.choice(slayerTasks)
        print("Your slayer task is to kill one, singular " + newTask + ".")
        print("Okay!")
        sleep(1)
        if newTask == "cow":
            print("You kill the " + newTask + ", and it drops:")
            sleep(1)
            print(*cowDrops, sep="\n")
        elif newTask == "green dragon":
            print("You kill the " + newTask + ", and it drops:")
            sleep(1)
            print(*greenDragonDrops, sep="\n")
        elif newTask == "bloodveld":
            print("You kill the " + newTask + ", and it drops:")
            sleep(1)
            print(*bloodveldDrops, sep="\n")
        elif newTask == "spider":
            print("You kill the " + newTask + ", and it drops: ")
            sleep(1)
            print(spiderDrops)


task()

goAgain = input("Would you like another task?")
if goAgain.lower() == "yes":
    task()
else:
    print("Alright cya lol")
# Mad Lib Game

print("MAD LIB GAME")
print("Enter answers to the following prompts\n")

guy = input("Name of a man: ")
girl = input("Name of a woman: ")
food = input("Your favorite food (plural): ")
ship = input("Name of a space ship: ")
drive = input("Name of the ships fastest drive: ")
job = input("Name of a profession (plural): ")
planet = input("Name of a planet: ")
drink = input("Your favorite drink: ")
number = input("A number from 1 to 10: ")
enemy = input("Name of your enemy: ")
weapon = input("Name of your favorite weapon: ")
material = input("A random material: ")




story = "\nA famous married couple, GUY and GIRL, went on\n" +\
        "vacation to the planet PLANET. It took NUMBER\n" +\
        "weeks to get there travelling by SHIP. They\n" +\
        "enjoyed a luxurious candlelight dinner over-\n" +\
        "looking a DRINK ocean while eating FOOD. But,\n" +\
        "since they were both JOB, they had to cut their\n" +\
        "vacation short.\n" +\
        "\nWhen they returned they were greeted by ENEMY.\n" +\
        "They both grabed their WEAPON and the battle started.\n" +\
        "While retreating to their SHIP GUY was hit.\n" +\
        "GIRL quickly activated the DRIVE to escape,\n" +\
        "and suddenly they were all made of MATERIAL.\n"


story = story.replace("GUY", guy)
story = story.replace("GIRL", girl)
story = story.replace("FOOD", food)
story = story.replace("SHIP", ship)
story = story.replace("JOB", job)
story = story.replace("PLANET", planet)
story = story.replace("DRINK", drink)
story = story.replace("NUMBER", number)

story = story.replace("ENEMY", enemy)
story = story.replace("WEAPON", weapon)
story = story.replace("DRIVE", drive)
story = story.replace("MATERIAL", material)

print(story)



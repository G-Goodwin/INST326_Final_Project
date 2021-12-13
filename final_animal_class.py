import random
class Animal:
    """This class reads the file of animals in the zoo and organizes them into a zoo dictionary.
    Attributes:
        filepath(str): a path to a file.
    """
    def __init__(self, filepath):
        """Opens a file, unpacks it by line and appends it to a list as a dictionary.
        Args:
            filepath(str): a path to a file.
        Side Effects:
            opens and modifies a file.
        """
        self.zoo = []
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line.rstrip("\n")
                name, type1, eat, sleep, talk, play, fact = line.split(",")
                x = {"name": name.strip(" "), "type": type1.strip(" "), "eat": eat.strip(" "), \
                    "sleep":sleep.strip(" "), "talk": talk.strip(" "), "play": play.strip(" "), \
                        "fact": fact.rstrip("\n")}
                self.zoo.append(x)
            self.zoo = self.zoo[1:]
        print(self.zoo)
        # self.action(self.zoo)
    def action(self, fle):
        copy_zoo = self.zoo
        selection_list = []
        selection_list2 = []
        f = open(fle, "w", encoding="utf-8")
        for x in copy_zoo:
            for x in copy_zoo:
                name = x["name"]
                type1 = x["type"]
                eat = x["eat"]
                sleep = x["sleep"]
                talk = x["talk"]
                play = x["play"]
                selection_list.append(name +", The " + name + " says " + talk + " to ")
                selection_list.append(name +", The " + name + " is able to " + play + " with ")
                selection_list.append(name +", The "  + name + " sleeps " + sleep + " and ")
                selection_list.append(name +", The " + name + " eats " + eat + " and ")
                selection_list.append(name +", The " + name + " is a " + type1+ " and ")
            for x in copy_zoo:
                name = x["name"]
                type1 = x["type"]
                eat = x["eat"]
                sleep = x["sleep"]
                talk = x["talk"]
                play = x["play"]
                selection_list2.append("the " + name + " says " + talk)
                selection_list2.append("the " + name + " that plays " + play)
                selection_list2.append("the " + name + " that sleeps " + sleep)
                selection_list2.append("the " + name + " eats " + eat)
                selection_list2.append("the " + name + " that is a " + type1)
            
            f.writelines(random.choice(selection_list)+random.choice(selection_list2)+"."+"\n")
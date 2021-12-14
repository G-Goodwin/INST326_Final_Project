import random 
import sys
import pandas as pd
import re
import matplotlib.pyplot as plt

class Human: # Written by: Leilani and Mandy
    """
    Basic Human class, framework for Zookeeper and Human class
    
    Attributes:
        name (str): Human's name
        age (int): Human's age
        isadult (boolean): whether the Human is an "adult" or not
        prounouns (str): Human's pronouns
    """
    def __init__(self):
        """
        Raises: 
            TypeError if age is an invalid input.
        """
        self.name = input("What is your name? ")
        self.age = int(input("How old are you? "))
        
        if not isinstance(self.age, int) or self.age <= 0:
            raise TypeError("Please enter a valid age.")
        
        if self.age >= 18:
            self.isadult = True
        else:
            self.isadult = False
        
        self.pronouns = input("What are your pronouns? ")

class User(Human): # Written by: Leilani and Mandy
    """
    Defines a User for the virtual Zoo.
    
    Attributes:
        prev_user (boolean): whether the User is new to the Zoo or not.
        username (str): the User's unique username.
    """
    def account(self, filepath): # Written by: Leilani 
        """
        Allows User to create an account if they are a first-time visiter.
        
        Args:
            filepath (str): contains a path to a file with usernames in it.
        Raises:
            TypeError if the User's status is not inputted as 'y'/'n' 
            
        Side Effects:
            if User is new, write their username into the file of other 
                usernames.
            self.prev_user: set to either True or False depending on User's 
                answer.
            self.username: set to a String representing the User's username. 
            printing: prompts the User, via the console to input their user 
                status and their username. Also, welcomes the user back if they
                are a returning user. 
        """
        user_status = input("Are you a new user? (y/n) ")
        if user_status == "y":
            self.prev_user = False
            self.username = input("Enter a unique username: ")
        elif user_status == "n":
            self.prev_user = True
            print(f"Welcome back! ")
            self.username = input("Please enter your username: ")
        else:
            raise TypeError("Enter 'y' for yes and 'n' for no.")
        
        with open(filepath, 'w', encoding = 'utf-8') as f:
            f.write(self.username)

    def best_time_display(self, filepath): # Written by: Leilani 
        """
        Display a bar plot of what amounts of times animal sleep, allowing 
            User to choose the best animals to see, at what times.
        
        Args:
            filepath (str): a path to a file with animals, their sleep times, 
                noises they make, and fun facts
            
        returns:
            data visualization (bar plot) displaying animal's sleeping times
        """
        
        expr = r"""(?xm)
                    ^
                    (?P<animal_name>\w+((\s\w+)?))
                    ,
                    (?P<animal_type>\s\w+)
                    ,
                    \s\w+(\s\w+)?,\s
                    (?P<hours_sleep>\d+(-?)(\d+)?)
                """

        df = pd.DataFrame()
        
        hours_sleep = []
        animal_name = []
        
        with open(filepath, 'r', encoding = 'utf-8') as f:
            for line in f:
                line = line.strip()
                match = re.search(expr, line)
                if match:
                    hours_sleep.append(match.group("hours_sleep"))
                    animal_name.append(match.group("animal_name"))
        
        for index, i in enumerate(hours_sleep): 
            if len(i) > 2:
                if len(i) == 4 and i[2] == "1":
                    hours_sleep[index] = i[2:]
                elif len(i) == 5 and i[3] == "1":
                    hours_sleep[index] = i[3:]
                else:
                    hours_sleep[index] = i[-1]
        
        for index, i in enumerate(hours_sleep):
            hours_sleep[index] = int(i)
        
        df["Animal Name"] = animal_name
        df["Animal Type"] = match.group("animal_type")
        df["Hours of Sleep"] = hours_sleep
        
        return df.plot.bar(x = "Animal Name", y = "Hours of Sleep")        
                    
    def summary(self, filepath): # Written by: Mandy
        """ Provides the user with a summary of their visit
        
        Args:
            filepath (str): contains a path to a file with the summary of the
            user's experiences at the zoo
            
        Side effects:
            Prints the user's experiences at the zoo onto the console
        """
        print("During your visit, you... ")
        with open(filepath, 'r', encoding = 'utf-8') as f:
            for line in f:
                line = line.strip()
                expr = """(?xm)
                (?P<category_or_activity>^\w+)
                \:\s
                \n?
                (?P<animals>[^\:].+)"""
                match = re.search(expr, line)
                if match:
                    activity = match.group("category_or_activity")
                    animal = match.group("animals")
                    print(f"{activity} these animals: {animal}")
        print("We hope you enjoyed your visit and we hope to see you soon!")


    def navigate_zoo(self, filepath, actions, summary): # Written by: Mandy
        """Asks the user questions and prompts them to visit animals at the zoo
        
        Args:
            filepath (str): The path to a file that contains all the animals 
                in the zoo
            actions (str): The path to the summary file that the method will 
                read from
            summary (str): The path to the summary file that the method will 
                write onto

        Raises:
            ValueError if the animal the user selected is not an option in the 
                zoo
            
        Side effects:
            Prints the animal's actions and takes the user's input on the 
                console
        """
        reptiles = []
        birds = []
        fish = []
        mammals = []
        animals_seen = []
        with open(filepath, 'r', encoding = 'utf-8') as f:
            for line in f:
                line = line.strip().split(', ')
                animal = line[0].title()
                type = line[1]
                if type == 'Reptile':
                    reptiles.append(animal)
                if type == 'Birds':
                    birds.append(animal)
                if type == 'Mammals':
                    mammals.append(animal)
                if type == 'Fish':
                    fish.append(animal)
            
        ans = "y"
        action_dict = {}
        while ans == "y":            
            with open(actions, 'r', encoding = 'utf-8') as f2:
                for line in f2:
                    line2 = line.strip().split(', ')
                    action_dict[line2[0].title()] = line2[1]
            print("R = reptile, B = bird, F = fish, M = mammal")
            interest = input("What type of animal are you most interested in" \
                                " seeing? (R/B/F/M): ").upper()
            if interest == 'R':
                print("Reptile display: ")
                print(', '.join(reptiles))
                choice = input("Select an animal to visit: ").title()
                if choice in action_dict:
                    print(action_dict[f"{choice}"])
                
                else:
                    print(f"The {choice} is sleeping right now!")
                if choice in reptiles:
                    animals_seen.append(choice)
                else:
                    raise ValueError("Please select an animal in our display!")
                ans = input("Would you like to visit another animal (y/n)? ")
            if interest == 'B':
                print("Bird display: ")
                print(', '.join(birds))
                choice = input("Select an animal to visit: ").title()
                if choice in action_dict:
                    print(action_dict[f"{choice}"])
                else:
                    print(f"The {choice} is sleeping right now!")
                if choice in birds:
                    animals_seen.append(choice)
                else:
                    raise ValueError("Please select an animal in our display!")
                ans = input("Would you like to visit another animal (y/n)? ")
            if interest == 'F':
                print("Fish display: ")
                print(', '.join(fish))
                choice = input("Select an animal to visit: ").title()
                if choice in action_dict:
                    print(action_dict[f"{choice}"])
                else:
                    print(f"The {choice} is sleeping right now!")
                if choice in fish:
                    animals_seen.append(choice)
                else:
                    raise ValueError("Please select an animal in our display!")
                ans = input("Would you like to visit another animal (y/n)? ")
            if interest == 'M':
                print("Mammal display: ")
                print(', '.join(mammals))
                choice = input("Select an animal to visit: ").title()
                if choice in action_dict:
                    print(action_dict[f"{choice}"])
                else:
                    print(f"The {choice} is sleeping right now!")
                if choice in mammals:
                    animals_seen.append(choice)
                else:
                    raise ValueError("Please select an animal in our display!")
                ans = input("Would you like to visit another animal (y/n)? ")
                
        
        with open(summary, 'w', encoding = 'utf-8') as f3:
            f3.write(f"saw: {', '.join(animals_seen)}")
        return animals_seen   

            
class Animal: # Written by: Hanna
    """This class reads the file of animals in the zoo and organizes them into 
        a zoo dictionary.
    Attributes:
        filepath(str): a path to a file.
    """
    def __init__(self, filepath):
        """Opens a file, unpacks it by line and appends it to a list as a 
            dictionary.
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
                x = {"name": name.strip(" "), "type": type1.strip(" "), "eat": \
                    eat.strip(" "), "sleep":sleep.strip(" "), "talk": \
                    talk.strip(" "), "play": play.strip(" "),"fact": \
                    fact.rstrip("\n")}
                self.zoo.append(x)
            self.zoo = self.zoo[1:]

    def action(self, fle):
        """Creates a copy of the dictionary and writes random interaction 
                statements to a list, then writes statements to a file.
        Args:
            fle(str): a path to a file
        Side Effects:
            Opens and writes to a file.
        """
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
                selection_list.append(name +", The " + name + " says " + talk 
                    + " to ")
                selection_list.append(name +", The " + name + " is able to " 
                    + play + " with ")
                selection_list.append(name +", The "  + name + " sleeps " 
                    + sleep + " and ")
                selection_list.append(name +", The " + name + " eats " + eat 
                    + " and ")
                selection_list.append(name +", The " + name + " is a " 
                    + type1+ " and ")
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
            
            f.writelines(random.choice(selection_list)+
                random.choice(selection_list2)+"."+"\n")


class Zookeeper(Animal,Human): # Written by: G Goodwin
    """
    The Zookeeper class is a subclass of the Human class and Animal Class. 
        It inherits attributes of the Human class (name, age) and the Animal 
        Class (zoo). The quiz method allows users to type answers to quesetions 
        asked by the Zookeeper. The feed method simulates the Zookeeper feeding
        the animal of the user's choice.
    Attributes:
        (see Human Class and Animal Class)

        questions (dictionary): A dictionary of questions from a file and the
            correct answer.
        asked_questions (list): A list of the questions the user answers.
        answer_dict (dictionary): A dictionary with the question asked as the
            key and a tuple of values. The first is the correct answer 
            and the second is the user's answer.
        score (int): The number of questions the user answered correctly.
        unasked_questions (set): A set of questions that have not been asked.
        quest (str): A question printed to the console for the user to answer. 
        answer (str): The user's answer to the question.  

        animal_options (list): A list of all of the animals in the Zoo. 
        animals_visited (list): A list of all of the animals fed by the 
            Zookeeper. The user has "visited" any animal the Zookeeper 
            interacts with. 
        animal_list (list of dictionaries): A list of dictionaries containing 
            information about animals in the Zoo. 
        options (list): A list of the capitalized names of all of the animals 
            in the Zoo.
        desired_animal (str): The animal the user wants to see.
        animal (str): Capitalized name of the animal the user wants to see. 
        food (str): The food the animal eats from the file of animal 
            information.
        talk (str): The sound the animal makes from the file of animal 
            information. 
    """
    def quiz(self, user, file): 
        """
        Reads a file of quiz questions and answers. Prints a number (determined 
            by wheter or not the user is an adult) of questions about animals 
            in the Zoo for the user to type answers to. Creates a dictionary of 
            questions asked, correct answers, and the user's answers. 
        Args: 
            user (User class object): the user. 
            file (str): path to a file with quiz questions and answers. 
        Returns: 
            score (int): The number of questions the user answered correctly. 
        Side effects: 
            Prints the questions for the user to answer, question and answer 
                dictionary, and user's final quiz score to the console. 
        """
        self.questions = {}
        self.asked_questions = []
        self.answer_dict = {}
        self.score = 0

        with open(file, "r", encoding = "UTF-8") as f:   
            for line in f:  
                line.strip()
                line = line.split(":") 
                q,a = line[1].strip(), line[2].strip().upper()
                self.questions[q] = a
        self.unasked_questions = (set(self.questions.keys()) - 
            set(self.asked_questions))
        print(f"{user.name}, you will now take a true/false quiz!")
        if user.isadult == True: 
            for i in range(5): 
                self.quest = random.choice(list(self.unasked_questions))
                self.asked_questions.append(self.quest)
                self.unasked_questions = (set(self.questions.keys()) - 
                    set(self.asked_questions))
                self.answer = input(f"{self.quest}: ")
                self.answer_dict[self.quest] = (self.questions.get(self.quest), 
                    self.answer.upper())
        else: 
            for i in range(3): 
                self.quest = random.choice(list(self.unasked_questions))
                self.asked_questions.append(self.quest)
                self.unasked_questions = (set(self.questions.keys()) - 
                    set(self.asked_questions))
                self.answer = input(f"{self.quest}: ")
                self.answer_dict[self.quest] = (self.questions.get(self.quest), 
                    self.answer.upper())
        for cor_ans, user_ans in self.answer_dict.values(): 
            if cor_ans == user_ans: 
                self.score += 1
        print(f"{user.name} answered", self.score, "quiz questions correctly.")
        print(f"The quiz questions and answers are displayed" \
            " 'Question : (Correct Answer, User Answer)'. Your results are:"\
                ,self.answer_dict)
        return self.score

    def feed(self, lst):
        """
        Creates a list of animals the user has the option to feed. Simulates a 
            Zookeeper feeding an animal of the user's choice. 
        Returns:
            animals_visited (list): A list of all of the animals the user 
                visited. Equivalent to the animals the Zookeeper fed. 
        Raises: 
            ValueError: The animal the user wants to visit is not in the Zoo.
        """
        print(f"You will now feed the animals!")
        self.animal_options = []
        self.all_visited = []
        self.animal_list = self.zoo.copy()
        for a in self.animal_list: 
            self.animal_options.append(a["name"])
        self.options = [a.upper() for a in self.animal_options]
        for a in lst: 
            self.animal = a.upper()
            self.all_visited.append(self.animal)
            if self.animal in self.options: 
                s = random.randint(0,9)
                for n in self.animal_list: 
                    if self.animal == n["name"].upper(): 
                        self.food = n["eat"]
                        self.talk = n["talk"]
                if s == 9:
                    print(f"Sorry, the {a} is sleeping" \
                    " right now.")
                else: 
                    print(f"{a}'s eat {self.food}. I will feed" \
                        " it now.")
                    print(f"Listen to that, {a}'s make" \
                        f" {self.talk} sound.")
            else: 
                raise ValueError(f"Sorry, we don't have {a}'s" \
                    " at this zoo!")
        return self.all_visited


if __name__ == "__main__": # Written by: G
    a = Animal("zoo.txt")
    z = Zookeeper("zoo.txt")
    u = User()
    u.account("usernames.txt")
    u.best_time_display("zoo.txt")
    a.action("sample.txt") 
    z.feed(u.navigate_zoo("zoo.txt", "sample.txt", "summary.txt"))
    z.quiz(u, "quiz_questions.txt")
    u.summary("summary.txt")
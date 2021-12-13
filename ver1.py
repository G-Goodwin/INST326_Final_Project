import random 
import sys
from argparse import ArgumentParser

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
        
        # if self.age is not type(int) or self.age <= 0:
        #     raise TypeError("Please enter a valid age.")
        if self.age <= 0:
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
    def account(self, filepath):
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
        
        with open(filepath, 'a+', encoding = 'utf-8') as f:
            for line in f:
                line = line.strip()
                if line == self.username:
                    self.username = input("That username already exists, "\
                        "please nter a different one: ")
                else:
                    f.write(self.username)
                    
    def summary(self, filepath):
        """ Provides the user with a summary of their previous visit if they
        are an existing user
        
        Args:
            filepath (str): contains a path to a file with the summary of the
            user's previous experiences at the zoo
            
        Side effects:
            Prints the user's previous experiences at the zoo onto the console
        """
        if self.prev_user == True:
            print("During your previous visit, you... ")
            with open(filepath, 'r', encoding = 'utf-8') as f:
                for line in f:
                    line = line.strip()
                    print(line)
                    if 'complete' in line:
                        print("You have completed your goal from your last " \
                        "visit! Make sure to set a new goal for this visit.")
            
            expr = """(?xm)
            (?P<category_or_activity>^\w+[^\:]+)
            \:\s
            (?P<animals>[^\:].+)"""
    
    def navigate_zoo(self):
        print("r = reptile, b = bird, f = fish, m = mammal")
        interest = input("What type of animal are you most interested in " \
        "seeing? (r/b/f/m) ")
        if interest == 'r':
             print("Amphibian display: ")
        if interest == 'b':
            print("Bird display: ")
        if interest == 'f':
            print("Fish display: ")
        if interest == 'm':
            print("Mammal display: ")
            
class Animal: # Written by: Hanna
    """This class reads the file of animals in the zoo and organizes them 
        into a zoo dictionary.
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
                #line.rstrip("\n")
                line.strip()
                name, type1, eat, sleep, talk, play, fact = line.split(",")
                x = {"name": name, "type": type1.strip(), "eat": eat, \
                    "sleep":sleep, "talk": talk, "play": play, \
                        "fact": fact.strip()}
                # x = {"name": name, "type": type1.lstrip(), "eat": eat, \
                #     "sleep":sleep, "talk": talk, "play": play, \
                #         "fact": fact.rstrip("\n")}
                self.zoo.append(x)
        #self.action(self.zoo)
# made new animal file - took out the commas in one of the fun facts because it was messing up the method

    def action(self, animal):
        copy_zoo = self.zoo
        for x in copy_zoo:
            name = x["name"]
            type1 = x["type"]
            eat = x["eat"]
            sleep = x["sleep"]
            talk = x["talk"]
            play = x["play"]
            print("The name of the animal is " + name)
            print("This animal is a " + type1)
            print("This animal eats " + eat)
            print("This animal sleeps " + sleep + " a day")
            print("This animal says " + talk)
            print("This animal plays by " + play)

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

    def feed(self):
        """
        Creates a list of animals the user has the option to feed. Simulates a 
            Zookeeper feeding an animal of the user's choice. 
        Returns:
            animals_visited (list): A list of all of the animals the user 
                visited. Equivalent to the animals the Zookeeper fed. 
        Raises: 
            ValueError: The animal the user wants to visit is not in the Zoo.
        """
        self.animal_options = []
        self.animals_visited = []
        self.animal_list = self.zoo.copy()
        for a in self.animal_list: 
            self.animal_options.append(a["name"])
        self.animal_options.remove("NAME")
        self.options = [a.upper() for a in self.animal_options]
        print(f"Animals in the Zoo:{self.animal_options}")
        self.desired_animal = input(f"What animal would you like to see? ")
        self.animal = self.desired_animal.upper()
        self.animals_visited.append(self.animal)
        if self.animal in self.options: 
            s = random.randint(0,9)
            for n in self.animal_list: 
                if self.animal == n["name"].upper(): 
                    self.food = n["eat"]
                    self.talk = n["talk"]
            if s > 8:
                print(f"Sorry, the {self.desired_animal} is sleeping" \
                " right now.")
            else: 
                print(f"{self.desired_animal}'s eat {self.food}. I will feed" \
                    " it now.")
                print(f"Listen to that, {self.desired_animal}'s make" \
                    f" {self.talk} sound.")
        else: 
            raise ValueError(f"Sorry, we don't have {self.desired_animal}'s" \
                " at this zoo!")
        return self.animals_visited

# def parse_args(arglist): 
#     """ 
#     Parse command-line arguments.
    
#     Expects # mandatory arguments:
#         filepath: a path to a tab-delimited file containing book data 
#             (title, author, and call number). 
    
#     Args:
#         arglist (list of str): arguments from the command line.
    
#     Returns:
#         namespace: the parsed arguments, as a namespace.
#     """
#     parser = ArgumentParser()
#     parser.add_argument("filepath", help="path to tab-delimited text file with"
#                         " book data (title, author, and call number)") 
#     return parser.parse_args(arglist)

if __name__ == "__main__": # Written by: G
    a = Animal("animals.txt")
    z = Zookeeper("animals.txt")
    u = User()
    u.account("userName.txt")
    #data viz stuff here
    # need an animal for next method
    #a.action() 
    u.navigate_zoo()
    # duplicate kind of animal display printed text between these two methods 
    z.feed()
    z.quiz(u, "quiz_questions.txt")
    u.summary("sum.txt")
#     args = parse_args(sys.argv[1:])
#     main(args.filepath)
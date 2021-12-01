import random 

class Human:
    """
    Basic Human class, framework for Zookeeper and Human class
    
    Attributes:
        name (str): Human's name
        age (int): Human's age
        isadult (boolean): whether the Human is an "adult" or not
        pronouns (str): Human's pronouns
    """
    def __init__(self):
        """
        Raises: 
            TypeError if age is an invalid input.
        """
        self.name = input("What is your name? ")
        self.age = int(input("How old are you? "))
        
        if self.age is not type(int) or self.age <= 0:
            raise TypeError("Please enter a valid age.")
        
        if self.age >= 18:
            self.isadult = True
        else:
            self.isadult = False
        
        self.pronouns = input("What are your pronouns? ")

class User(Human):
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
        
        with open(filepath, 'r', encoding = 'utf-8') as f:
            for line in f:
                line = line.strip()
                if line == self.username:
                    self.username = input("That username already exists, please\
                                         enter a different one: ")
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
                        print("You have completed your goal from your last \
                            visit! Make sure to set a new goal for this visit.")
                    
    def pre_visit(self, filepath):
        """ Allows the user to set a goal before their actual visit
        
        Args:
            filepath (str): contains a path to a file that will document their
            goals for this visit
        
        Side effects: 
            Prompts the user to enter their goals for this visit and sets it to
            goals, as well as writing the new goals into the text file
        """
        goals = input("Is there anything specific you would like to do during \
            this visit? ")
        with open(filepath, 'w', encoding = 'utf-8') as f:
            f.write(goals)

class Zookeeper(Human): 
    """
    The Zookeeper class is a subclass of the Human class and inherits 
        the __init__() method attributes of the Human class. It interacts  
        with the User class and Animal class. 
        The Zookeeper class includes a quiz method where the user can type
        answers to quesetions asked by the Zookeeper. 
        A seperate method will be made to calculate the user's quiz score. 
    """
    def quiz(self, user, file): 
        """
        Reads a file of quiz questions and answers. Prints a number 
            (determined by the age of the user) of questions about animals in 
            the Zoo for the user to type answers to. Records the questions  
            asked and the user's answers to for later use. 
        Args: 
            user (User class object): the user. 
            file (str): path to a file with quiz questions and answers. 
        Returns: 
            answer_list (list): a list of the user's responses the the questions
        """
        questions = {}
        cor_answers = {}
        asked_questions = []
        answer_list = []

        with open(file, "r", encoding = "UTF-8") as f:   
            for line in f:  
                line.strip()
                line = line.split(":") 
                n,q,a = line[0], line[1].strip(), line[2].strip()
                questions[n] = q
                cor_answers[n] = a
        unasked_questions = set(questions.values()) - set(asked_questions)
        if user.age > 18: 
            for i in range(5): 
                quest = random.choice(list(unasked_questions))
                asked_questions.append(quest)
                unasked_questions = set(questions.values()) - set(asked_questions)
                answer = input(f"{quest}: ")
                answer_list.append(answer)
        else: 
            for i in range(3): 
                quest = random.choice(list(unasked_questions))
                asked_questions.append(quest)
                unasked_questions = set(questions.values()) - set(asked_questions)
                answer = input(f"{quest}: ")
                answer_list.append(answer)
        return answer_list

class Animal:
    """This class reads the file of animals in the zoo and organizes
        them into a zoo dictionary.
    Attributes:
        filepath(str): a path to a file.
    """
    def __init__(self, filepath):
        """Opens a file, unpacks it by line and appends it to a list as 
            a dictionary.
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
                x = {name: [type1.lstrip(), eat, sleep, talk, play, 
                            fact.rstrip("\n")]}
                self.zoo.append(x)
        print(self.zoo)
    def action(self, animal):
        for line in self.zoo:
            
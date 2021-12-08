import random 
class Human:
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
            
            expr = """(?xm)
            (?P<category_or_activity>^\w+[^\:]+)
            \:\s
            (?P<animals>[^\:].+)"""
    
    
    def navigate_zoo(self):
        print("r = reptile, b = bird, f = fish, m = mammal")
        interest = input("What type of animal are you most interested in \
             seeing? (r/b/f/m) ")
        if interest == 'r':
             print("Amphibian display: ")
        if interest == 'b':
            print("Bird display: ")
        if interest == 'f':
            print("Fish display: ")
        if interest == 'm':
            print("Mammal display: ")
            

class Zookeeper(Human): 
    """
    The Zookeeper class is a subclass of the Human class and inherits 
        attributes of the Human class. It interacts with the User class 
        and Animal class. The Zookeeper class includes a quiz method where 
        the user can type answers to quesetions asked by the Zookeeper. 

    """
    def quiz(self, user, file): 
        """
        Reads a file of quiz questions and answers. Prints a number 
            (determined by the age of the user) of questions about animals in 
            the Zoo for the user to type answers to. Records the questions  
            asked, correct answers, and the user's answers. 
        Args: 
            user (User class object): the user. 
            file (str): path to a file with quiz questions and answers. 
        Returns: 
            answer_dict (dict): a dictionary with keys corresponding to the 
                quiz questions asked, and a tuple of the correct answer and 
                the user's answer as the values. 
        Side effects: 
            Prints the number of questions the user correctly answered to the 
                console.
        """
        questions = {}
        asked_questions = []
        answer_dict = {}
        score = 0

        with open(file, "r", encoding = "UTF-8") as f:   
            for line in f:  
                line.strip()
                line = line.split(":") 
                q,a = line[1].strip(), line[2].strip().upper()
                questions[q] = a
        unasked_questions = set(questions.keys()) - set(asked_questions)
        if user.age > 18: 
            for i in range(5): 
                quest = random.choice(list(unasked_questions))
                asked_questions.append(quest)
                unasked_questions = set(questions.keys()) - set(asked_questions)
                answer = input(f"{quest}: ")
                answer_dict[quest] = questions.get(quest), answer.upper()
        else: 
            for i in range(3): 
                quest = random.choice(list(unasked_questions))
                asked_questions.append(quest)
                unasked_questions = set(questions.keys()) - set(asked_questions)
                answer = input(f"{quest}: ")
                answer_dict[quest] = questions.get(quest), answer.upper()
        for cor_ans, user_ans in answer_dict.values(): 
            if cor_ans == user_ans: 
                score += 1
        print(f"{user.name} answered", score, "questions correctly.")
        print(answer_dict)
        return score
    
    def feed(self, animal_list):
        animal_info = []
        animal_options = []
        animals_visited = []
        with open(animal_list, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip().split(",")
                n,e,ta = line[0].strip(), line[2].strip(), line[4].strip()
                animal_options.append(n)
                a = {n.upper():(e,ta)}
                animal_info.append(a)
        animal_options.remove("NAME")
        options = [a.upper() for a in animal_options]
        print(f"Animals in the Zoo:{animal_options}")
        desired_animal = input(f"What animal would you like to see? ")
        animal = desired_animal.upper()
        animals_visited.append(animal)
        #for x in Animal(self.zoo)
            #if animal == self.zoo["name"]:
        if animal in options: 
            s = random.randint(0,9)
            for a in animal_info:
                for n in a.keys():
                    if n == animal: 
                        for v in a.values(): 
                            food = v[0]
                            talk = v[1]
            if s > 7:
                print(f"Sorry, the {desired_animal} is sleeping right now.")
            else: 
                print(f"{desired_animal}'s eat {food}. I will feed it now.")
            d = random.randint(0,9)     
            if d < 8 and s < 7: 
                print(f"Listen to that, {desired_animal} makes {talk} sound.")
        else: 
            raise ValueError(f"Sorry, we don't have {desired_animal}'s' at this zoo!")
        return animals_visited

class Animal:
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
                line.rstrip("\n")
                name, type1, eat, sleep, talk, play, fact = line.split(",")
                x = {"name": name, "type": type1.lstrip(), "eat": eat, \
                    "sleep":sleep, "talk": talk, "play": play, \
                        "fact": fact.rstrip("\n")}
                self.zoo.append(x)
        #print(self.zoo)
        self.action(self.zoo)
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
            #Turn print statements into return statements (try to mak more 
            # complicated if possible), maybe read into a new file to create a
            #fact sheet
def main():  
    pass

def parse_args(arglist): 
    """ 
    Parse command-line arguments.
    
    Expects # mandatory arguments:
        filepath: a path to a tab-delimited file containing book data 
            (title, author, and call number). 
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("filepath", help="path to tab-delimited text file with"
                        " book data (title, author, and call number)") 
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filepath)
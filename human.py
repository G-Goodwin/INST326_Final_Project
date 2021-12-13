import re

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
        
class ZooKeeper(Human):
    pass

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

    
   def navigate_zoo(self, filepath, summary):
        reptiles = []
        birds = []
        fish = []
        mammals = []
        animals_seen = []
        
        with open(filepath, 'r', encoding = 'utf-8') as f:
            for line in f:
                line = line.strip().split(', ')
                animal = line[0]
                type = line[1]
                if type == 'Reptile':
                    reptiles.append(animal)
                if type == 'Birds':
                    birds.append(animal)
                if type == 'Mammals':
                    mammals.append(animal)
                if type == 'Fish':
                    fish.append(animal)
                    
#         with open(filepath2, 'r', encoding = 'utf-8') as f2:
#             for line in f2:
#                 line = line.strip.split(', ')
#                 animal2 = line[0]
#                 interaction = line[1]

        ans = "y"
        while ans == "y":            
            print("r = reptile, b = bird, f = fish, m = mammal")
            interest = input("What type of animal are you most interested in seeing? (r/b/f/m): ")
            if interest == 'r':
                print("Reptile display: ")
                print(', '.join(reptiles))
                choice = input("Select an animal to visit: ")
                if choice in reptiles:
                    animals_seen.append(choice)
                else:
                    raise ValueError("Please select an animal in our display!")
                ans = input("Would you like to visit another animal (y/n)? ")
            if interest == 'b':
                print("Bird display: ")
                print(', '.join(birds))
                choice = input("Select an animal to visit: ")
                if choice in birds:
                    animals_seen.append(choice)
                else:
                    raise ValueError("Please select an animal in our display!")
                ans = input("Would you like to visit another animal (y/n)? ")
            if interest == 'f':
                print("Fish display: ")
                print(', '.join(fish))
                choice = input("Select an animal to visit: ")
                if choice in fish:
                    animals_seen.append(choice)
                else:
                    raise ValueError("Please select an animal in our display!")
                ans = input("Would you like to visit another animal (y/n)? ")
            if interest == 'm':
                print("Mammal display: ")
                print(', '.join(mammals))
                choice = input("Select an animal to visit: ")
                if choice in mammals:
                    animals_seen.append(choice)
                else:
                    raise ValueError("Please select an animal in our display!")
                ans = input("Would you like to visit another animal (y/n)? ")
        print("Thank you for visiting our zoo! Have a nice day!")
        with open(summary, 'w', encoding = 'utf-8') as f3:
            f3.write(f"saw: {', '.join(animals_seen)}")
           
        
    def summary(self, filepath):
        """ Provides the user with a summary of their previous visit if they
        are an existing user
        
        Args:
            filepath (str): contains a path to a file with the summary of the
            user's previous experiences at the zoo
            
        Side effects:
            Prints the user's previous experiences at the zoo onto the console
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
            
    
            

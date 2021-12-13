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
    
    # def pre_visit(self, filepath):
    #     """ Allows the user to set a goal before their actual visit
        
    #     Args:
    #         filepath (str): contains a path to a file that will document their
    #         goals for this visit
        
    #     Side effects: 
    #         Prompts the user to enter their goals for this visit and sets it to
    #         goals, as well as writing the new goals into the text file
    #     """
    #     goals = input("Is there anything specific you would like to do during \
    #         this visit? ")
    #     with open(filepath, 'w', encoding = 'utf-8') as f:
    #         f.write(goals)
    # #   goals for this current visit, ie. pet a giraffe or see a shark
    
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
            

            
    
        
    
                    
        
    
 
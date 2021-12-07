import random 

class Human: 
    def __init__(self, age, name):
        self.age = age
        self.name = name
class User(Human): 
    pass

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
        #print(answer_dict)
        return answer_dict
    
    def feed(self, animal_list):
        animal_options = ["Burmese Python", "Diamondback Terrapin", "Gecko", /
        "Alligator", "Lizard", "Owl", "Penguin", "Eagle", "Hummingbird", /
        "Peacock", "Aardvark", "Tiger", "Giraffe", "Panda", "Zebra", "Shark",/
         "Dolphin", "Swordfish", "Pufferfish", "Seahorse"]
        print(f"Animals in the Zoo:{animal_options}"")
        desired_animal = input(f"What animal would you like to see?")
        desired_animal.upper()
        # need to fix the animal list pulling info, make names captial
        if desired_animal in animal_list: 
            s = randint(0,1)
            if s == 1: 
                print(f"Sorry, {desired_animal} is sleeping right now.")
            else: 
                if desired_animal in animal_list: 
                    food = animal_list[desired_animal]
                    print(f"{desired_animal}, eats {food}. I will feed it now.")    
            d = randint(0,1)
            if d == 1: 
                talk = animal[desired_animal]
                print(f"Listen to that, {desired_animal} makes {talk} sound.")
        else: 
            raise ValueError(f"Sorry, we don't have {desired_animal} at this zoo!")

h = User(9, "E")
z = Zookeeper.quiz(9, h,"quiz_questions.txt")
#z = Zookeeper.feed(19,)



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


#h = User(19, "33")
#h2 = User(19, "B")
#z = Zookeeper.quiz(9, h,"quiz_questions.txt")
#z2 = Zookeeper.quiz(9, h2,"quiz_questions.txt")
h = User(17, "F")
z = Zookeeper.feed("D", "zoo.txt")


import random 

class Human: 
    def __init__(self, age):
        self.age = age
        
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

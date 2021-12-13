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
        print(f"{user.name} answered", score, "quiz questions correctly.")
        print(f"The quiz questions and answers are displayed 'Question : (Correct Answer, User Answer)'.",answer_dict)
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


h = User(19, "33")

z = Zookeeper.quiz(9, h,"quiz_questions.txt")
#h2 = User(19, "B")
#z2 = Zookeeper.quiz(9, h2,"quiz_questions.txt")
# h = User(17, "F")
# z = Zookeeper.feed("D", "zoo.txt")

# class Zookeeper(Animal,Human): 
#     """
#     The Zookeeper class is a subclass of the Human class and inherits 
#         attributes of the Human class. It interacts with the User class 
#         and Animal class. The Zookeeper class includes a quiz method where 
#         the user can type answers to quesetions asked by the Zookeeper. 

#     """
#     def quiz(self, user, file): 
#         """
#         Reads a file of quiz questions and answers. Prints a number 
#             (determined by the age of the user) of questions about animals in 
#             the Zoo for the user to type answers to. Records the questions  
#             asked, correct answers, and the user's answers. 
#         Args: 
#             user (User class object): the user. 
#             file (str): path to a file with quiz questions and answers. 
#         Returns: 
#             answer_dict (dict): a dictionary with keys corresponding to the 
#                 quiz questions asked, and a tuple of the correct answer and 
#                 the user's answer as the values. 
#         Side effects: 
#             Prints the number of questions the user correctly answered to the 
#                 console.
#         """
#         self.questions = {}
#         self.asked_questions = []
#         self.answer_dict = {}
#         self.score = 0

#         with open(file, "r", encoding = "UTF-8") as f:   
#             for line in f:  
#                 line.strip()
#                 line = line.split(":") 
#                 q,a = line[1].strip(), line[2].strip().upper()
#                 self.questions[q] = a
#         self.unasked_questions = set(self.questions.keys()) - set(self.asked_questions)
#         if user.isadult == True: 
#             for i in range(5): 
#                 self.quest = random.choice(list(self.unasked_questions))
#                 self.asked_questions.append(self.quest)
#                 self.unasked_questions = set(self.questions.keys()) - set(self.asked_questions)
#                 self.answer = input(f"{self.quest}: ")
#                 self.answer_dict[quest] = self.questions.get(self.quest), self.answer.upper()
#         else: 
#             for i in range(3): 
#                 self.quest = random.choice(list(self.unasked_questions))
#                 self.asked_questions.append(self.quest)
#                 self.unasked_questions = set(self.questions.keys()) - set(self.asked_questions)
#                 self.answer = input(f"{self.quest}: ")
#                 self.answer_dict[self.quest] = self.questions.get(self.quest), self.answer.upper()
#         for cor_ans, user_ans in self.answer_dict.values(): 
#             if cor_ans == user_ans: 
#                 self.score += 1
#         print(f"{user.name} answered", self.score, "quiz questions correctly.")
#         print(f"The quiz questions and answers are displayed 'Question : (Correct Answer, User Answer)'.",self.answer_dict)
#         return self.score

#     def feed(self):
#         self.animal_options = []
#         self.animals_visited = []
#         self.animal_list = self.zoo.copy()
#         for a in self.animal_list: 
#             self.animal_options.append(a["name"])
#         self.animal_options.remove("NAME")
#         self.options = [a.upper() for a in self.animal_options]
#         print(f"Animals in the Zoo:{self.animal_options}")
#         self.desired_animal = input(f"What animal would you like to see? ")
#         self.animal = self.desired_animal.upper()
#         self.animals_visited.append(self.animal)
#         if self.animal in self.options: 
#             s = random.randint(0,9)
#             for n in self.animal_list: 
#                 if self.animal == n["name"].upper(): 
#                     self.food = n["eat"]
#                     self.talk = n["talk"]
#             if s > 8:
#                 print(f"Sorry, the {self.desired_animal} is sleeping right now.")
#             else: 
#                 print(f"{self.desired_animal}'s eat {self.food}. I will feed it now.")
#                 print(f"Listen to that, {self.desired_animal}'s' make {self.talk} sound.")
#         else: 
#             raise ValueError(f"Sorry, we don't have {self.desired_animal}'s' at this zoo!")
#         return self.animals_visited
#             #     print(n)
#             # print(a)
#             # print(a.items())
#             # if animal == a.values()[0]: 
#             #     self.food = a.values()[]

#             #self.animal_options.append(self.animal_list["name"])
#             # if animal == self.animal_list["name"]: 
#             #     self.food = self.animal_list["food"]
#             #     self.sleep = self.animal_list["talk"]
#         # self.options = [a.upper() for a in self.animal_options]
#         # print(f"Animals in the Zoo:{self.animal_options}")
#         # self.desired_animal = input(f"What animal would you like to see? ")
#         # self.animal = self.desired_animal.upper()
#         # self.animals_visited.append(self.animal)
#         # if self.animal in self.options: 
#         #     s = random.randint(0,9)
#         #     if s > 7:
#         #         print(f"Sorry, the {self.desired_animal} is sleeping right now.")
#         #     else: 
#         #         print(f"{self.desired_animal}'s eat {self.food}. I will feed it now.")
#         #     d = random.randint(0,9)     
#         #     if d < 8 and s < 7: 
#         #         print(f"Listen to that, {self.desired_animal} makes {self.talk} sound.")
#         # else: 
#         #     raise ValueError(f"Sorry, we don't have {self.desired_animal}'s' at this zoo!")
#         # return self.animals_visited
# # made new animal file - took out the commas in one of the fun facts because it was messing up the method
# # a = Animal("animals.txt")
# # s = Zookeeper("animals.txt")
# # h = User()
# # z2 = Zookeeper.feed(s)
# # z = Zookeeper.quiz(s,h, "quiz_questions.txt")


#             # for a in self.animal_info:
#             #     for n in a.keys():
#             #         if n == animal: 
#             #             for v in a.values(): 
#             #                 food = v[0]
#             #                 talk = v[1]

#     # Original idea: 
#     # def feed(self, animal_list):
#     #     animal_info = []
#     #     animal_options = []
#     #     animals_visited = []
#     #     with open(animal_list, "r", encoding="utf-8") as f:
#     #         for line in f:
#     #             line = line.strip().split(",")
#     #             n,e,ta = line[0].strip(), line[2].strip(), line[4].strip()
#     #             animal_options.append(n)
#     #             a = {n.upper():(e,ta)}
#     #             animal_info.append(a)
#     #     animal_options.remove("NAME")
#     #     options = [a.upper() for a in animal_options]
#     #     print(f"Animals in the Zoo:{animal_options}")
#     #     desired_animal = input(f"What animal would you like to see? ")
#     #     animal = desired_animal.upper()
#     #     animals_visited.append(animal)
#     #     #for x in Animal(self.zoo)
#     #         #if animal == self.zoo["name"]:
#     #     if animal in options: 
#     #         s = random.randint(0,9)
#     #         for a in animal_info:
#     #             for n in a.keys():
#     #                 if n == animal: 
#     #                     for v in a.values(): 
#     #                         food = v[0]
#     #                         talk = v[1]
#     #         if s > 7:
#     #             print(f"Sorry, the {desired_animal} is sleeping right now.")
#     #         else: 
#     #             print(f"{desired_animal}'s eat {food}. I will feed it now.")
#     #         d = random.randint(0,9)     
#     #         if d < 8 and s < 7: 
#     #             print(f"Listen to that, {desired_animal} makes {talk} sound.")
#     #     else: 
#     #         raise ValueError(f"Sorry, we don't have {desired_animal}'s' at this zoo!")
#     #     return animals_visited

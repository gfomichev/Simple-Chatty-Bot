class Bot:
    interlocutor_name = ""
    interlocutor_age = 0

    def __init__(self, bot_name, birth_year):
        self.bot_name = bot_name
        self.birth_year = birth_year

    def greet(self):
        print(f'Hello! My name is {self.bot_name}.')
        print(f'I was created in {self.birth_year}.')
        self.set_interlocutor()

    def set_interlocutor(self):
        self.interlocutor_name = input("Please, remind me your name.\n")
        print(f'What a great name you have, {self.interlocutor_name}!')

    def guess_age(self):
        print('Let me guess your age.')
        print('Enter remainders of dividing your age by 3, 5 and 7.')
        remainder3 = int(input())
        remainder5 = int(input())
        remainder7 = int(input())
        self.interlocutor_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
        print(f"Your age is {self.interlocutor_age}; that's a good time to start programming!")

    @staticmethod
    def count():
        count = int(input("Now I will prove to you that I can count to any number you want.\n"))
        for i in range(0, count + 1):
            print(f'{i} !')

    @staticmethod
    def test():
        print("Let's test your programming knowledge.")
        print("""Why do we use methods?
1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.""")
        while int(input()) != 2:
            print("Please, try again.")
        print("Completed, have a nice day!")

    @staticmethod
    def end():
        print('Congratulations, have a nice day!')


alice = Bot("Alice", 2020)
alice.greet()
alice.guess_age()
alice.count()
alice.test()
alice.end()

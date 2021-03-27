from abc import ABC


class Singleton(type):  # Singleton, so no new instance if the variable is called for the operations
    _instances = {}     # maybe other, simpler Singleton version can be used, I only managed with this

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls) \
                .__call__(*args, **kwargs)
        return cls._instances[cls]


class Calculator(metaclass=Singleton):      # main class, this has to be initialized to run the calculations

    def __init__(self):
        self.current_first_number = None
        self.current_second_number = None
        self.current_result = None
        self.current_operand = None
        self.escape = False                 # For user to terminate the program
        self.allowed_operands_list = []
        self.fact = OperationFactory()      # initializes Factory so that the operations get initialized

    def calculate(self):
        for key in OperationFactory.dict_operations.keys():     # compile a list of allowed operands to print at
            self.allowed_operands_list.extend(list(key))        # start and also for error message

        if not self.current_result:         # at start to print the instructions and allowed operands
            self.initialize()

        self.get_number()                   # read in first number
        if self.escape:                     # for user to terminate program
            print(f'bye!')
            return

        while True:                         # loop until terminated by user
            self.get_operand()              # read in operand
            if self.escape:
                print(f'bye!')
                return

            elif self.current_operand == '=':
                self.fact.call_operation()

            else:                           # read in second number for operation and execute operation
                self.get_number()
                if self.escape:
                    print(f'bye!')
                    return

                self.fact.call_operation()

                self.current_second_number = self.current_result

    def initialize(self):                   # at start to print the instructions and allowed operands
        print(f'Wilkommen im Kalkulator!\nZahlen und Operanden können nacheinander eingegeben werden'
              f'\nErlaubte Operanden (ohne Klammern):\n')
        for key in OperationFactory.dict_operations.keys():
            print(key)
        print(f'\nFür Abbruch jederzeit E eingeben\n')

    def get_number(self):                   # method to read in number, check correct number format
        self.current_first_number = self.current_second_number
        while True:                         # loop until correct number format or terminated by user
            current_input = input('Zahl eingeben:\n')
            if current_input == 'E':
                self.escape = True
                return
            else:
                try:
                    self.current_second_number = float(current_input)       # checking if number is float
                    return
                except ValueError:
                    try:
                        self.current_second_number = int(current_input)     # checking if number is int
                        return
                    except ValueError:
                        print('Zahl darf int oder float sein')              # incorrect format, ask for new input

    def get_operand(self):                  # method to read in operand, check if allowed operand
        while True:                         # loop until allowed operand input or terminated by user
            self.current_operand = input('Operand eingeben:\n')
            if self.current_operand == 'E':
                self.escape = True
                return
            elif self.current_operand not in self.allowed_operands_list:    # check operand if allowed
                print(f'Erlaubte Operanden:\n')
                for key in OperationFactory.dict_operations.keys():         # print out allowed operands
                    print(key)
            else:
                return


class Operation(ABC):                   # abstract class to make sure operation is implemented
    def do_operation(self):             # eventual new operation must be added here as subclass
        pass


class Addition(Operation):
    def do_operation(self):
        Calculator().current_result = Calculator().current_first_number + Calculator().current_second_number


class Subtraktion(Operation):
    def do_operation(self):
        Calculator().current_result = Calculator().current_first_number - Calculator().current_second_number


class Multiplikation(Operation):
    def do_operation(self):
        Calculator().current_result = Calculator().current_first_number * Calculator().current_second_number


class Dividieren(Operation):
    def do_operation(self):
        Calculator().current_result = Calculator().current_first_number / Calculator().current_second_number


class Ergebnis(Operation):
    def do_operation(self):
        print(f'Ergebnis:\n{Calculator().current_result}')


class OperationFactory:     # called as Calculator is initialized, this class will initialize and execute the ops

    dict_operations = {('+', 'add', 'plus'): Addition(),            # allowed operands and the respective operations
                       ('-', 'sub', 'minus'): Subtraktion(),        # eventual new operations and operands have to be
                       ('*', 'mal'): Multiplikation(),              # added here
                       ('/', 'div'): Dividieren(),
                       ('=', 'ergebnis'): Ergebnis()}

    def __init__(self):
        for i in self.dict_operations.values():
            i

    def call_operation(self):                                   # execute op based on the last input operand
        for k, v in self.dict_operations.items():
            if Calculator().current_operand in k:
                return v.do_operation()

if __name__ == '__main__':
    a = Calculator()
    a.calculate()

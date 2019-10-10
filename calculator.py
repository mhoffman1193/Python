import os, pickle


UI = '''
Which application would you like to do?:
'''


UI2 = '''
1. Add
2. Subtract
3. Divide
4. Multiply
5. Exit
'''



class Person(object):


    def __init__(self, number1, number2, total):

        self.number1 = number1
        self.number2 = number2
        self.total = total

    def __str__(self):
        return '{}'



class Calculator(object):


    def __init__(self, database):
            
            self.database = database
            self.persons = {}


            if os.path.getsize(database) > 0:   
               
                with open(database, "rb") as f:
                    unpickler = pickle.Unpickler(f)
             # if file is not empty scores will be equal
             # to the value unpickled
                    database = unpickler.load()
            else:
                with open(self.database, 'rb') as person_list:
                    self.database = pickle.load(person_list)

    def getNums(self):
        
        number1 = input('1st Number: ')
        number2 = input('2nd Number: ')
        return number1, number2


    def Add(self):
        number1, number2 = self.getNums()
        total = int(number1) + int(number2)
        print(str(number1) + ' + ' + str(number2) + ' = ' + str(total))


    def Subtract(self):
        number1, number2 = self.getNums()
        total = int(number1) - int(number2)
        print(str(number1) + ' - ' + str(number2) + ' = ' + str(total))


    def Divide(self):
        number1, number2 = self.getNums()
        total = int(number1)/int(number2)
        print(str(number1) + ' / ' + str(number2) + ' = ' + str(total))

    def Multiply(self): 
        number1, number2 = self.getNums()
        total = int(number1)*int(number2)
        print(str(number1) + ' X ' + str(number2) + ' = ' + str(total))

    def __str__(self):
        ''' return calculator interface '''

        return UI2




def main():
    app = Calculator('contacts.data')
    choice = ''
    while choice != '5':
        print(app)
        choice = input('Choose: ')
        if choice == '1':
            app.Add()
        elif choice == '2':
            app.Subtract()
        elif choice == '3':
            app.Divide()
        elif choice == '4':
            app.Multiply()
        elif choice == '5':
            print('Exiting')
        else:
            print('Invalid choice.')



if __name__ == '__main__':
    main()























# Polymorphism
'''
>> Polymorphism means one thing existing in several different forms.

'''

class vscode:
    def execute(self):
        print('Compiling')
        print('Running')
        print('Interpreter')
        
class userER:
    def execute(self):
        print('Compiling')
        print('Running')
        print('Interpreter')
        print('Healing')
        print('Mode')
        
class laptop:
    def code(self,env):
        env.execute()

ev = vscode()  # here just by changing the class name we can get to the different class.
lap1 = laptop()
lap1.code(ev)


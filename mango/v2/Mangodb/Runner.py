"""
Class for running mango database.
Create Runner class object and use mangoDB as usual
"""
from mango.v2.Mangodb.Interpreter import Interpreter


class Runner:
    interpreter: Interpreter

    def __init__(self):
        self.interpreter = Interpreter()

    def exec(self):
        while True:
            print('execute mangodb command')
            print()
            print()
            print('Settings')
            print('exit from mangodb shell')

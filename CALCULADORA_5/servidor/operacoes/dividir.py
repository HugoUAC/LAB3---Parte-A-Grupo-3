from typing import Union

class Dividir:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.res = 0


    def execute(self)->Union[float,str]:
        try:
            self.res = self.x / self.y
        except ZeroDivisionError:
            return "error:dividing by zero"
        return self.res

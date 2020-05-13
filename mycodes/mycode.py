class WantTest:
    def hello_world(self):
        return "hello,world"

    def integer_division(self,a,b):
        try:
            return int(a/b)         
        except ZeroDivisionError:
            raise
        except TypeError:
            raise

class AdditionalClass:
    def __init__(self, mylist):
        self.mylist = mylist

    def counter(self):
        count = 0
        for _ in self.mylist:
            count += 1 

        return count
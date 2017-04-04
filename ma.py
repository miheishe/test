class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value

class Parent(object):
    pass

class First(Parent):
    pass

class Second(Parent):
    pass

class A(First):
    def __init__(self):
        self.i = 3
        self.isSecond = 0

    def fnc(self,a1):
        if a1 == 7:
            raise MyError("Error text")
        return 6 * a1

    def isFirst(self):
        return 1

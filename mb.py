class B(object):
    def __init__(self, b1):
        self.tempfive = b1
        self.isSecond = 1

    def fnc(self,b1,b2):
        return b1 * b2 * self.tempfive

    def isFirst(self):
        return 0
__author__ = 'wangui'

var = 4

def myPrint(str):
    global var
    var = var + 1
    print var, str

class HELLO:
    def __init__(self):
        pass
    def hPrint(self, String):
        print String
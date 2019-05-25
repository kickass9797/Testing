class Stack(object):

    def __init__(self):
        self.__stacklist = []

    def push(self, element):
        self.__stacklist.append(element)

    def pop(self)
        self.__stacklist.pop()

    def count(self)
        return len(self.__stacklist)



class Teams:
    
    def __init__(self, members):
        self.__myTeam = members

    def __len__(self):
        return len(self.__myTeam)
    # Add the __contains__ protocol
    def __contains__(self,members):
        '''__contains__ : Defines behavior for membership tests using in and not in. 
            Python just iterates over the sequence and returns True if it comes across the item it is looking for
        '''
        return members in self.__myTeam
    # Add the __iter__ protocol
    def __iter__(self):
        '''__iter__(self): Should return an iterator for the container'''
        return iter(self.__myTeam)
    # Add __len__ method
    def __len__(self):
        '''__len__(self): Returns the length of the container'''
        return len(self.__myTeam)

def main():
    classmates = Teams(["John", "Steve", "Tim"])

    print("John" in classmates)
    print("Mike" in classmates)

    iterator = iter(classmates)
    for members in iterator:
        print(members, end = ", ")
    print()
    print (len(classmates))

main()
class Singleton:
    ans = None

    # used to access one instance therefore static method
    @staticmethod
    def instance():
        # checks the instance in the class dictionary if its not in there it adds it to the dictionary instance
        if '_instance' not in Singleton.__dict__:
            Singleton._instance = Singleton()
        return Singleton._instance
    
# we check the method and if they are the same
s1 = Singleton.instance()
s2 = Singleton.instance()

assert s1 is s2
s1.ans = 42

assert s2.ans == s2.ans
print('Assertion passed.')
#Hierarichal and multiple
class Human:
    def hprintt(self):
        print("you are a human")
class Mother(Human):
    def mprintt(self):
        print("I am mother")
class Father(Human):
    def fprintt(self):
        print("I am father")
class Child(Mother,Father):
    def cprintt(self):
        print("I am the child")
obj=Child()
obj.cprintt()
obj.fprintt()
obj.mprintt()

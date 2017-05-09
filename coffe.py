class coffe(object):
    def __init__(self,names, Type, number):
        self.number = number
        self.names = names
        self.Type = Type
    def make_coffe(self):
        for i in range(self.number):
            print("take a cup")
            print("pour coffe in the cup")
            if(self.Type == "milk"):
                print("pour milk")
                print("stir")
                self.order = "Coffe with milk ready"
            elif(self.Type == "water"):
                print("pour water")
                print("stir")
                self.order = "Coffe with water ready"

    def serve_coffe(self):
        for i in range(len(self.names)):
            print self.names[i]
            print self.order
            print ("serve coffe")

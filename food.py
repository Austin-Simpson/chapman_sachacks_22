class food:
    genre = "default"
    votes = 0
    def __init__(self, g):
        self.genre = g

    def display(self):
        print("genre -" + self.genre)
        print("votes -" + str(self.votes))

tArr = []    

obj = food("mexican")
obj.vote
obj.vote()
obj.display()
    
    


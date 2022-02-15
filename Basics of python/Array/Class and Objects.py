class cricketplayer:
    name="cricketplayer"

    def __init__(self,coach,captain):
        self.coach=coach
        self.captain=captain

Dhoni = cricketplayer("He is a legend", "He is a Cool captain")

print("Dhoni information:")
print("Dhoni is a",Dhoni.name)
print("coach:",Dhoni.coach)
print("captain:",Dhoni.captain)


class actor:
    def __init__(self,name,movie):
        self.name=name
        self.movie=movie

    def new(self):
        print(" Actor name is ",self.name)
        print(" Movie name is ",self.movie)

a = actor("Sharukh","Baazigar")
a.new()
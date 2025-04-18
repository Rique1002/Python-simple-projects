class user:
    def __init__(self,firstName,lastName,likesCount, *friendsName):
        self.firstName = firstName
        self.lastName = lastName
        self.likesCount = likesCount
        self.friendsName = friendsName

    def introduce(self):
        print("Hi I am " + self.firstName + " "+ self.lastName)

    def fullProfile(self):
        print("Full Name: " + self.firstName + " " + self.lastName)
        print("Likes: " + str(self.likesCount))
        print("Friends")
        for friend in self.friendsName:
            print(" -" + friend )
            



userA = user("David", "SDPT", 10, "Alenere Sdpt", "Jaymar Catapang", "Joshua Emmanuel Seria", "Patrick Macaraig")  
userA.introduce()
userA.fullProfile()

     

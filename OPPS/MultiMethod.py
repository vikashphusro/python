class MultiMethod : 
    def __init__(self, name):
        self.name = name
        self.namelist = []

    def add_name(self, friend) :
        self.namelist.append(friend)
        print(f"Friend added in list {friend}")

    def del_name(self, friend): 
        if friend in self.namelist :
            self.namelist.remove(friend)
            print(f"Friend removed from list {friend}")
        else : 
            print(f"Friend not exist in this list {friend}")

    def display_friend_list(self) :
        for frn in self.namelist :
            print(f"Friend : {frn}")

multi = MultiMethod("Multi")
multi.add_name("rajesh")
multi.add_name("karan")
multi.add_name("varun")
multi.display_friend_list() 
multi.del_name("rajesh") 
multi.display_friend_list() 
multi.del_name("Pratibha")

    
        
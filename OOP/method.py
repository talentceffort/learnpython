class User:
    def say_my_name(self):
        print("My name is " + self.name)


user = User()
user.name = "Young"
user.email = "young@gmail.com"
user.id = "zozod"

User.say_my_name(user)
user.say_my_name()
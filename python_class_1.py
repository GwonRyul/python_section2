import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class UserInfo :
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def print_info(self) :
        print("-----------")
        print("Name: " + self.name)
        print("Phone: " + self.phone)
        print("-----------")

    def __del__(self) :
        print("Delete!")

user1 = UserInfo("Tony Stark", "010-1234-1111")
user2 = UserInfo("Stive Rovert", "010-3456-2222")

print(id(user1))
print(id(user2))

#user1.set_info("Tony Stark", "010-1234-1111")
#user2.set_info("Stive Rovert", "010-3456-2222")

user1.print_info()
user2.print_info()

print(user1.__dict__)
print(user2.__dict__)

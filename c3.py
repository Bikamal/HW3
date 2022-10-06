# . Write a class called Password_manager. 
# The class should have a list called old_passwords that holds all of the user’s past passwords. 
# The last item of the list is the user’s current password. 
# There should be a method called get_password that returns the current password and a method 
# called set_password that sets the user’s password. 
# The set_password method should only change the password if the attempted password is different from all the user’s past passwords. 
# Finally, create a method called is_correct that receives a string and returns a boolean True or False 
# depending on whether the string is equal to the current password or not

class Password_manager():
    def __init__(self,old_passwords,current):
        self.old_passwords=old_passwords
        self.current=current
    def get_password(self):
        return self.old_passwords[-1]
    def set_password(self):
        if self.current in self.old_passwords:
            return "match"
        else:
            new_password=input("enter your new password")
            return new_password

    def is_correct(self):
        if self.current in self.old_passwords:
            return True
        else:
            return False
    

old_pds=["abcge", "abcgg", "bggt", "btss"]
current=input("enter your current password")
    
    
a = Password_manager(old_pds,current)
print(a.is_correct())
print(a.set_password())
print(a.get_password())

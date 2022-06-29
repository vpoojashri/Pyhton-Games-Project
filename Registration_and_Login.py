import re
from colorama import Fore, Back, Style
heading=(Fore.CYAN+"REGISTRATION FORM")
print(heading.center(160))
#getting valid userid
def name():
    user = input("Enter Your Email ID: ")
    pattern=("\w+@gmail.com\Z")
    r=re.match(pattern,user)
    pattern1 = ("\w+@yahoo.com\Z")
    r1 = re.match(pattern1, user)
    if (r1 is None) and (r is None):
        print("Invalid Username")
        name()
    else:
       return pass_word(user)
#getting valid user password
def pass_word(user):

    password = input("Enter Your Password: ")
    num = 0
    upper = 0
    lower = 0
    spl = 0
    for i in password:
        if i.isdigit():
            num = num + 1
        elif i.isupper():
            upper = upper + 1
        elif i.islower():
            lower = lower + 1
        elif i in ".,@,$,#,*,%,^,&,~,_,!,?,*":
            spl = spl + 1
    if num > 0 and spl > 0 and lower > 0 and upper > 0 and len(password) > 6 and len(password) < 17:
        file = open("C:\\Users\\ADMIN\\Documents\\loginreg.txt", "a")
        gender = input("Gender : ")
        age = input("Age :")
        file.write(user + "," + password +","+ gender +","+ age + "\n")
        print("Your Are Sucessfully Registered")

        return
    else:
        if num == 0:
            print("Please add NUMERIC Character",end=" ,")
        if spl == 0:
            print("Please add SPECIAL Character",end=" ,")
        if upper == 0:
            print("Please add UPPERCASE",end=" ,")
        if len(password) < 6 or len(password) > 17:
            print("Minimun lenght is 6 ,Maximum lenght is 17")

        print("Enter a Valid Password")
        pass_word(user)

def main_fun():
    reg = int(input("Select 1 to Register\nSelect 2 to Login : "))
    if reg==1:

        name()
    if reg==2:
            values = []
            file = open("C:\\Users\\ADMIN\\Documents\\loginreg.txt", "r")
            for datas in file:
                j = (datas.split(","))
                for g in j:
                    values.append(g.strip("\n"))

            user = input("USERNAME(Email-id): ")
            password = input("PASSWORD: ")

            if (user in values) and (password in values):
                print("You Have Sucessfully Login")
                return
            if (user in values) and (password not in values):
                print(Fore.RED+"Your Password is Incorrect")
                print("Try Again")
                pw = input("PASSWORD: ")
                if (user in values) and (pw in values):
                    print("You Have Sucessfully Login")
                    return
                forget_pass=int(input("Press 1 to retrive Your Password: "))
                if forget_pass==1:
                        if user in values:
                            ind = (values.index(user))
                            print("This is your password "+ values[ind + 1])
                            return
            if (user not in values) and (password not in values):
                print("You Are Not Registered")
                name()
    if reg > 2 or reg < 0:
        print("Invalid Number")
        main_fun()
        return
main_fun()
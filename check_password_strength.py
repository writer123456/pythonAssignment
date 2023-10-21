import re
def check_password_strength(password):
    if ' ' in password:
        return (0,"Password should not contain spaces")
    if(len(password)<8):
        return (0,"The password should be atleast 8 characters long")
    # if(password.isalpha()||password.islower()||password.isupper()||password.isnumeric()):
    #     print("The password should  contain atleast one digit(0-9),both upper and lowercase letters")
    #     return 0
    if(not re.search('[!@#$%^&*.]',password)):
        return (0,"Invalid password-Password must include one or more special characters")
    if(not re.search('[A-Z]',password)):
        return (0,"Invalid password-Password must contain both upper and lower case letters")
    if(not re.search('[a-z]',password)):
        return (0,"Invalid password-Password must contain both upper and lower case letters")
    if(not re.search('[0-9]',password)):
        return (0,"Invalid password-Password must contain atleast one digit")
    else:
        return (1,"Valid password-")

pwd=input("Please enter a password\n")
result=check_password_strength(pwd)
print(result)


    



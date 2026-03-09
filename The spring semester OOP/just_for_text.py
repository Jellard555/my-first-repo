#
#the first try
enter_pw = input("let me try whether your pw is good")
has_digit = False
def check_password_security(char):
     a = len(enter_pw)
     if a >= 8:
          for char in enter_pw:
               if char.isdigit():
                    has_digit = True
                    return True
     else:
          return False
print(check_password_security(enter_pw))


# after learning from AI
# written by myself
enter_password = input("enter a password")
def check_security(password):
     if len(password) >= 8:
          return False
     def check_digit(char):
          if len(char) != 1:
               return False
          ascii_code = ord(char)
          return 48 <= ascii_code <= 57
result = check_security(enter_password)
print(result)


# the last one try:finish all the demand
enter_password = input("enter a password")
def check_security(password):
     if len(password) < 8:
          return False
     def check_digit(char):
          if len(char) != 1:
               return False
          ascii_code = ord(char)
          return 48 <= ascii_code <= 57
     def check_upper(char):
          if len(char) != 1:
               return False
          ascii_code = ord(char)
          return 65 <= ascii_code <= 90
     def check_lower(char):
          if len(char) != 1:
               return False
          ascii_code = ord(char)
          return 97 <= ascii_code <= 122
     has_digit = False
     has_lower = False
     has_upper = False
     for char in password:
          if check_digit(char):
               has_digit = True
          if check_upper(char):
               has_upper = True
          if check_lower(char):
               has_lower = True
          if has_digit and has_lower and has_upper:
               break
     return has_digit and has_lower and has_upper

result = check_security(enter_password)
if result == True:
     print(f"{enter_password} is a good password")
else:
     print(f"I think the password {enter_password} is risky")
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
import re
def email_valid(email):
             regex= r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
             if(re.fullmatch(regex, email)):
                    print(email)
             else:
                    print("Invalid email")
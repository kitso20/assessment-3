import re

def email_validator(email_list):
    dic = {"valid": [],
           "invalid":[]}
    
    for email in email_list:
        print(email)
        sc = re.match(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',email)
        print(sc)
        if sc:
            dic["valid"].append(email)
        else:
            dic["invalid"].append(email)
    return dic

print(email_validator([
        "test@example.com",
        "invalid-email",
        "user@domain.co",
        "user@domain"
    ]))
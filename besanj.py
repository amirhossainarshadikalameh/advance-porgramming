import re


def validate_email(email: str) -> bool:
    if re.match(r'^[a-zA-Z1-9\.]+@[a-zA-Z1-9]+\.[a-zA-Z]{3}$',email):
        return True
    else:
        return False
    pass


def validate_phone(number: str) -> bool:
    length=len(number)
    if length==11:
        if re.match(r'^09+[0-9]{9}',number):
            return 'true'
        else:
            return 'false'
    elif length==13:
        if re.match(r'^\+989+[0-9]{9}',number):
            return 'true'
        else:
            return 'false'

    elif length==14:
        if re.match(r'00989+[0-9]{9}',number):
            return 'true'
        else:
            return 'false'

    pass
print(validate_phone(input()))
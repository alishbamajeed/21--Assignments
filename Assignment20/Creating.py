class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18")
    return "Access granted"

# Usage
try:
    print(check_age(17))
except InvalidAgeError as e:
    print("Exception:", e)


def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
def main():
    s = input("Enter a string")
    if is_palindrome(s):
        print(f"{s} is a palindrome")
    else:
        print(f"{s} is not a palindrome")
        
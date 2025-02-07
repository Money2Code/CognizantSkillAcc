

def palindrome(String1):
    if String1 == String1[::-1]:
        value="palindrome"
        return value
    

value=input("Enter the word"+"\n")
call=palindrome(value)

print(call)
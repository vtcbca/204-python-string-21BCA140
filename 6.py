#Write a script to enter any string and check it is palidrome or not.
a=input("Enter any string")
if(a==a[::-1]):
   print("The string is palindrome")
else:
    print("The string is not palindrome")

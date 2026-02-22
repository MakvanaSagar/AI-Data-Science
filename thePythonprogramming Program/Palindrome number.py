#Palindrome number or not


num = int(input("Enter number : "))  

to_str = str(num)
    
i = to_str == to_str[::-1]
    
print("\n It's Palindrome number is",i)
#gets input from user
text = list(input("Enter text to be encrypted: "))
shiftBy = int(input("Shift by: "))

#reference for shifted message
ref = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#hold for output
result = ""

#iterates for every char in list
for x in text:
    if x == " ":
        result += " "

#Checks if message contains capital letters and adds a shifted capital       
    elif x != x.lower():
        result += ref[(ref.index(x.lower()) + shiftBy) % 26].upper()

#Adds lowercase char        
    else:
        result += ref[(ref.index(x.lower()) + shiftBy) % 26]

print(result)

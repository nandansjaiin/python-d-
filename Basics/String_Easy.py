#1. Print a string
s = "Hello World"
print(s)

#2. Length of string
s = "python"
print(len(s))

#3. First character
s = "python"
print(s[0])

#4. Last character
s = "python"
print(s[-1])

#5. Uppercase string
s = "hello"
print(s.upper())

#6. Lowercase string
s = "HELLO"
print(s.lower())

#7. Capitalize first letter
s = "python"
print(s.capitalize())

#8. Capitalize each word
s = "hello world"
print(s.title())

#9. Swap case
s = "PyTHOn"
print(s.swapcase())

#10. Check if string is uppercase
s = "HELLO"
print(s.isupper())

#11. First three characters
s = "Python"
print(s[:3])

#12. Last three characters
s = "Python"
print(s[-3:])

#13. Reverse string
s = "hello"
print(s[::-1])

#14. String without first character
s = "Python"
print(s[1:])

#15. String without last character
s = "Python"
print(s[:-1])

#16. Check substring presence
s = "Python is fun"
print("fun" in s)

#17. Find index of substring
s = "programming"
print(s.find("gram"))

#18. Check startswith
s = "Python"
print(s.startswith("Py"))

#19. Check endswith
s = "Python"
print(s.endswith("on"))

#20 Replace substring
s = "I love Java"
print(s.replace("Java", "Python"))

#21. Remove space (strip)
s = "  hello  "
print(s.strip())

#22. Remove left spaces
s = "   hello"
print(s.lstrip())

#23. Remove right spaces
s = "hello   "
print(s.rstrip())

#24. Join characters with hyphen
s = "hello"
print("-".join(s))

#25. Split string into words
s = "Python is fun"
print(s.split())

#26. Check if string is digits
s = "12345"
print(s.isdigit())

#27. Check if string is alphabets
s = "abc123"
print(s.isalpha())

#28. Check if string is alphanumeric
s = "abc123"
print(s.isalnum())

#29. Concatenate two strings
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)

#30. Repeat string multiple times
s = "Hi "
print(s*3)
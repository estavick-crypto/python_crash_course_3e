# A Python program that removes whitespace, formats accordingly and prints

name = " \tCallen Stavick "
print("Unformatted:")
print(name)

print("\nRemoving left whitespace:") 
print(name.lstrip())

print("\nRemoving all whitespace:") 
print(name.strip())

print("\nRemoving right whitespace:")
print(name.rstrip())

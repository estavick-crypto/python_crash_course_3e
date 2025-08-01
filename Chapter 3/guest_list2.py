# A list of guests that updates and sends out invitation

# Variable for list of names
guest_names = ['renzo', 'emy', 'roland']

name = guest_names[0].title()
message = "Would you like to come this weekend for dinner?"
print(f"{name}, would you like to come for dinner this weekend?")

name = guest_names[1].title()
message = "Would you like to come this weekend for dinner?"
print(f"\n{name}, would you like to come for dinner this weekend?")

name = guest_names[2].title()
message = "Would you like to come this weekend for dinner?"
print(f"\n{name}, would you like to come for dinner this weekend?")

# Variable for the person who can't make it
absent_name = 'renzo'

guest_names.remove(absent_name)

# Remove person who can't attend and replace with another person
guest_names.insert(0, 'shalene')

print(f"\n{absent_name.title()} can't make it")
print(f"Here are the people going:\n{guest_names}")
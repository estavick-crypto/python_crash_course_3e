# A list of guests that updates and sends out invitation
guest_names = ['renzo', 'emy', 'roland']
absent_name = 'renzo'
guest_names.remove(absent_name)

print(guest_names)
guest_names.insert(0, 'shalene')
print(guest_names)  


name = guest_names[0].title()
message = "Would you like to come this weekend for dinner?"
print(f"\n{name}, would you like to come for dinner this weekend?")

name = guest_names[1].title()
message = "Would you like to come this weekend for dinner?"
print(f"\n{name}, would you like to come for dinner this weekend?")

name = guest_names[2].title()
message = "Would you like to come this weekend for dinner?"
print(f"\n{name}, would you like to come for dinner this weekend?")

print(f"{absent_name.title()} can't make it")
print(f"Here are the people going:\n{guest_names}")

# A list of guests that updates and sends out invitation 
# and invites more guest if there is more room
guest_names = ['renzo', 'emy', 'roland']
absent_name = 'renzo'
guest_names.remove(absent_name)

print(guest_names)

# Remove invitee who can't attend and update the guest list
guest_names.insert(0, 'shalene')

print(guest_names)  

# Send messages to invite guests
guest_name = guest_names[0].title()
message = "Would you like to come this weekend for dinner?"
print(f"\n{guest_name}, would you like to come for dinner this weekend?")

name = guest_names[1].title()
message = "Would you like to come this weekend for dinner?"
print(f"\n{guest_name}, would you like to come for dinner this weekend?")

name = guest_names[2].title()
message = "Would you like to come this weekend for dinner?"
print(f"\n{guest_name}, would you like to come for dinner this weekend?")


## Invite more guests since a bigger a table was found
another_guest = "wali"
message = "Would you like to come this weekend for dinner?"
print(f"\n{another_guest}, would you like to come for dinner this weekend?")
guest_names.insert(0, another_guest)
print(f"Added {another_guest.title()} to the beginning of the list:")
print(guest_names)

another_guest = "roland"
message = "Would you like to come this weekend for dinner?"
print(f"\n{another_guest}, would you like to come for dinner this weekend?")
guest_names.insert(2, another_guest)
print(f"Added {another_guest.title()} to the middle of the list:")
print(guest_names)

another_guest = "emy"
message = "Would you like to come this weekend for dinner?"
print(f"\n{another_guest}, would you like to come for dinner this weekend?")
guest_names.append(another_guest)
print(f"Added {another_guest} to the end of the list:")
print(guest_names)

print(f"\n{absent_name.title()} can't make it")
print(f"Here are the people going:\n{guest_names}")

print("\nI found a bigger table")
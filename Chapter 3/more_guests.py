# A list of guests that updates and sends out invitation 
# and invites more guest if there is more room

# List of first set invitees
guest_names = ['renzo', 'charles', 'ej']
print(f"Here are the people I am inviting for dinner: \n{guest_names}")

# Remove guest who can't attend and update the list
absent_name = 'renzo'
print(f"\n{absent_name.title()} can't make it")
guest_names.remove(absent_name)

# Print updated list of guests
print(f"\nSince {absent_name.title()} can't go, here are the only people going:")
print(f"{guest_names}")

print("\nI found a bigger table. I should invite three more guests.")

# Invite more guests since a bigger a table was found
another_guest = "wali"
message = "Would you like to come this weekend for dinner?"
print(f"\n{another_guest.title()}, would you like to come for dinner this weekend?")
guest_names.insert(0, another_guest)
print(f"Added {another_guest.title()} to the beginning of the list:")
print(guest_names)

another_guest = "roland"
message = "Would you like to come this weekend for dinner?"
print(f"\n{another_guest.title()}, would you like to come for dinner this weekend?")
guest_names.insert(1, another_guest)
print(f"Added {another_guest.title()} to the middle of the list:")
print(guest_names)

another_guest = "emy"
message = "Would you like to come this weekend for dinner?"
print(f"\n{another_guest.title()}, would you like to come for dinner this weekend?")
guest_names.append(another_guest)
print(f"Added {another_guest.title()} to the end of the list:")
print(guest_names)

print(f"\nHere are the people going:\n{guest_names}")

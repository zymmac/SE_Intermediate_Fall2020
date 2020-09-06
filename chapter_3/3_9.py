# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (page 42), use len() to print a message indicating the number of people you are inviting to dinner.

invitees = ['Obama','Senna','Einstein']
print(f'You\'re invited to my dinner, {invitees[0].title()}!')
print(f'You\'re invited to my dinner, {invitees[1].title()}!')
print(f'You\'re invited to my dinner, {invitees[-1].title()}!')

print(f'I\'m inviting {len(invitees)} guests!')

print(f'Unfortunately, {invitees[2].title()} couldn\'t make it!')

invitees[2] = "Merkel"

print(f'You\'re invited to my dinner, {invitees[0].title()}!')
print(f'You\'re invited to my dinner, {invitees[1].title()}!')
print(f'You\'re invited to my dinner, {invitees[-1].title()}!')

print(f'I\'m inviting {len(invitees)} guests!')

print("We found a bigger table! Let's get more people invited!")

invitees.insert(0, 'Jordan')
invitees.insert(2, 'Brady')
invitees.append('Madonna')

print(f'You\'re invited to my dinner, {invitees[0].title()}!')
print(f'You\'re invited to my dinner, {invitees[1].title()}!')
print(f'You\'re invited to my dinner, {invitees[2].title()}!')
print(f'You\'re invited to my dinner, {invitees[3].title()}!')
print(f'You\'re invited to my dinner, {invitees[4].title()}!')
print(f'You\'re invited to my dinner, {invitees[5].title()}!')

print(f'I\'m inviting {len(invitees)} guests!')

uninvite = invitees.pop()
print(f'I\'m sorry but you\'re not invited anymore, {uninvite.title()}!')

uninvite = invitees.pop()
print(f'I\'m sorry but you\'re not invited anymore, {uninvite.title()}!')

uninvite = invitees.pop()
print(f'I\'m sorry but you\'re not invited anymore, {uninvite.title()}!')

uninvite = invitees.pop()
print(f'I\'m sorry but you\'re not invited anymore, {uninvite.title()}!')

print(f'You\'re still invited to my dinner, {invitees[0].title()}!')
print(f'You\'re still invited to my dinner, {invitees[1].title()}!')

print(f'I\'m inviting {len(invitees)} guests!')

del invitees[-1]
del invitees[-1]

print(invitees)
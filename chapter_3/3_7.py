# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

# • Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# • Print a message to each of the two people still on your list, letting them know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

invitees = ['Obama','Senna','Einstein']
print(f'You\'re invited to my dinner, {invitees[0].title()}!')
print(f'You\'re invited to my dinner, {invitees[1].title()}!')
print(f'You\'re invited to my dinner, {invitees[-1].title()}!')

print(f'Unfortunately, {invitees[2].title()} couldn\'t make it!')

invitees[2] = "Merkel"

print(f'You\'re invited to my dinner, {invitees[0].title()}!')
print(f'You\'re invited to my dinner, {invitees[1].title()}!')
print(f'You\'re invited to my dinner, {invitees[-1].title()}!')

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

del invitees[-1]
del invitees[-1]

print(invitees)
# 3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() call to the end of your program informing people that you found a bigger dinner table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

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




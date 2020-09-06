## 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
# • Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still in your list.

invitees = ['Obama','Senna','Einstein']
print(f'You\'re invited to my dinner, {invitees[0].title()}!')
print(f'You\'re invited to my dinner, {invitees[1].title()}!')
print(f'You\'re invited to my dinner, {invitees[-1].title()}!')

print(f'Unfortunately, {invitees[2].title()} couldn\'t make it!')

invitees[2] = "Merkel"

print(f'You\'re invited to my dinner, {invitees[0].title()}!')
print(f'You\'re invited to my dinner, {invitees[1].title()}!')
print(f'You\'re invited to my dinner, {invitees[-1].title()}!')
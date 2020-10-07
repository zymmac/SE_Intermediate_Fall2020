import random

lottery_choices = (1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e')

def pick_ticket():
    new_ticket = set()
    while len(new_ticket) < 4:
        pick_result = str(random.choice(lottery_choices))
        if pick_result not in new_ticket:
            new_ticket.add(pick_result)
    return new_ticket

winning_ticket = pick_ticket()
print("The winning ticket must be equal", winning_ticket)

ticket_attempt = 0
ticket_bought = set()
while ticket_bought != winning_ticket:
    ticket_bought = pick_ticket()
    ticket_attempt += 1
    print(f'{ticket_attempt} ticket(s) bought: {ticket_bought}')

print("You have won after", ticket_attempt, "tries. Ticket bought is", ticket_bought)
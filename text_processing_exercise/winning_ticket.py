def is_winning(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    winning_symbols = ['@', '#', '$', '^']
    left_part = ticket[:10]
    right_part = ticket[10:]
    for match_symbol in winning_symbols:
        for uninterrupted_match_length in range(10, 5, -1):
            winning_repetitions = match_symbol * uninterrupted_match_length
            if winning_repetitions in left_part and winning_repetitions in right_part:
                if uninterrupted_match_length == 10: # we have jackpot here
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!'
                else: # we have winning ticket
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}'
    return f'ticket "{ticket}" - no match'

tickets = [ticket.strip() for ticket in input().split(',')]
for ticket in tickets:
    print(is_winning(ticket))
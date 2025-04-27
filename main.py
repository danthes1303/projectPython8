import art
print(art.logo)
print("Welcome to the secret auction program.")
bid_list = []
game = True
while game:
    name = input("What is your name?:\n")
    bid = int(input("What's your bid?:\n"))
    bid_list.append({name: bid})
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if other_bidders == 'no':
        max_bid = 0
        did_max_bid = ''
        for dic in bid_list:
            for k in dic:
                v = dic[k]
                if v > max_bid:
                    max_bid = v
                    did_max_bid = k
        print(f"The winner is {did_max_bid} with a bid of ${max_bid}")
        game = False
if not game:
    exit()
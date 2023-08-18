from art import logo

def print_empty_lines(num_lines=100):
    for _ in range(num_lines):
        print()

print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_records):
    highest_bid = 0
    winner = ""
    # example {"Angela": 123, "James": 321}
    for bidder in bidding_records:
        bid_amount = bidding_records[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

while not bidding_finished:
    name = input("What is your name? \n")
    price = int(input("Whatis your bid? \n$"))
    bids[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print_empty_lines()
    else:
        bidding_finished = True
        find_highest_bidder(bids)






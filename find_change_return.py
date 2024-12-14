'''
The user enters a cost and then the amount of money given.  The program will figure out the change and the number of quarters, dimes, nickles, pennies needed for the change
'''

cost = float(input('Enter the price: $'))
given = float(input('Enter the amount you paid: $'))

diff_cents = int(round(given*100 - cost*100))


def calc_changes(cents):
    quarters = 25
    dimes = 10
    nickels = 5
    pennies = 1

    num_quarters, cents = divmod(cents, quarters)
    num_dimes, cents = divmod(cents, dimes)
    num_nickles, cents = divmod(cents, nickels)
    num_pennies = cents

    return num_quarters, num_dimes, num_nickles, num_pennies


quarters, dimes, nickels, pennies = calc_changes(diff_cents)
print(f"quarters={quarters}, dimes={
      dimes}, nickels={nickels}, pennies={pennies}")

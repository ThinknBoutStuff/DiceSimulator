import random
import time

def flavor_text(dice,sides,reroll):
    '''Checks whether roll or reroll, delivers appropriate text accordingly'''
    if len(reroll) < 1:
        print("\nRolling (%d) d%d:\n" %(dice,sides))

    else:
        print("\nRerolling d%d: #%s \n" %(sides,", #".join([str(i) for i in reroll])))

def roll(dice, sides, reroll=[], totals=0):
    '''Takes number of dice, sides per dice. Optionally, an iterable of dies to reroll
    and list of roll results "totals" can be provided'''

    flavor_text(dice,sides,reroll)
    time.sleep(0.5)

    # Create die per dice to store results
    if totals == 0:
        totals = [0]*dice

    # Roll Dice
    for d in range(dice):
        # Convert Dice # for user readability
        die = d+1
        # "Roll Dice Check"
        if die not in reroll and totals[-1] != 0:
            print("Roll %d: %d (unrolled)" % (die, totals[d]))
            continue
        result = random.randrange(1,sides+1)
        print("Roll %d: %d" % (die, result))
        totals[d] = result

    time.sleep(0.5)
    print("\n    Total: %d \n" % (sum(totals)))

    # Post Roll User Options
    while True:
        user_in = input("Reroll? List dice (separate with commas) or 0 for new dice: ")
        try:
            reroll = list(int(i) for i in user_in.split(','))
        except:
            print("\nOops! Remember, enter numbers separated by commas (nothing else).\n")
            time.sleep(0.5)
            continue
        # No rerolls, start new dice
        if reroll[0] == 0:
            first = False
            return main(first)

        # Reroll dice (recursive)
        elif reroll[0] != -1:
            # Reroll must be an iterable
            return roll(dice, sides, reroll, totals)

        # Quit
        else:
            break

# Error Handling
def check_input(user_in):
    '''Checks input for positive int or -1 (quits application)'''
    try:
        user_in = int(user_in)
        if user_in == -1:
            quit()
        if user_in < 0 or type(user_in) != int:
            time.sleep(0.5)
            print("\nInputs must be positive integers...")
            time.sleep(1)
            user_in = input("\nTry again? ")
            check_input(user_in)

        return user_in

    except:
        time.sleep(0.5)
        print("\nInputs must be positive integers...")
        time.sleep(1)
        user_in = input("\nTry again? ")
        check_input(user_in)

def main(first=True):
    '''Get user input and run roll function, enter -1 to quit'''

    # Instructions
    if first == True:
        print("\n        Welcome to Dice Simulator!")
        print("    Follow inputs or enter -1 to quit. ")
        time.sleep(1)

    # Collect dice parameters
    sides = input("\nHow many sides per dice? ")
    sides = check_input(sides)
    dice = input("\nHow many dice? ")
    dice = check_input(dice)

    return roll(dice, sides)

main()

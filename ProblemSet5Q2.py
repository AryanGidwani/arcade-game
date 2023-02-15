# Aryan Gidwani
# November 26, 2021
# ICS3UO - A
# This is an arcade, dice roll game! You, the user, will begin with exactly
# 1000 coins. You will guess whether the sum of the roll of two dice is
# either high or low. Getting a 8 to 12 is high, while getting a 2 to 6;
# however, getting a 7 is neutral. If you predict innacurately, you will lose
# the amount of coins that you bet at the start.
import random
# imports a module that helps with calculations
import sys
# imports a module that helps with the overall system

def stopProgram(userInput):
    if userInput == "quit":
        print("Thank you for using this program!")
        # concluding message
        sys.exit()
        # terminates the program if the user types in quit
    else:
        pass
        # passes, or effectively does nothing

def lowGuesser(bet):
    global totalCoins
    # makes the variable global
    diceOne = random.randint(1, 6)
    # rolls a dice
    print("For the first dice, you rolled a " + str(diceOne) + "!")
    # tells the user what number they got
    diceTwo = random.randint(1, 6)
    # rolls the second dice
    total = diceOne + diceTwo
    # calculates the sum of the two rolls
    print("For the second dice, you rolled a " + str(diceTwo) + "!" + "\n" + "Thus, the sum of the dice is " + str(total) + "!")
    # tells the user the sum of the two rolls

    if (total >= 2) and (total <= 6):
        totalCoins = totalCoins + (2 * bet)
        # updates the amount of coins when the user wins
        print("You guessed correctly, because the sum of the two rolls is " + str(total) + "!" + "\n" + "Original Bet: " + str(bet) + " coins " + "\n" + "Total coins after bet: " + str(totalCoins))
        # tells the user that they guessed correctly
        bettingCoins()
        # calls the function

    elif (total == 7):
        print("You rolled  a 7! If you roll a 7, what we do is that if you re-roll the dice and get an odd number, half of the money that you bet will be added to your total money! Good luck!!")
        # tells the user that they rolled a 7
        rollOne = random.randint(1, 6)
        # rolls the first dice again
        print("You have rolled a " + str(rollOne) + "!")
        # informs the user on the first roll
        rollTwo = random.randint(1, 6)
        # rolls the second dice again
        print("You have rolled a " + str(rollTwo) + "!")
        # informs the user on the second roll
        rollTotal = rollOne + rollTwo
        # finds the sum of the two rolls

        if rollTotal % 2 != 0:
            totalCoins = totalCoins + (bet / 2)
            # adds the bet to the total money
            totalCoins = round(totalCoins)
            # rounds it to the nearest integer in case of decimals
            print("The sum is " + str(rollTotal) + " which means you won your money! You now have " + str(totalCoins) + " total coins.")
            # tells the user if they won

        else :
            totalCoins = totalCoins - bet
            # player loses out on the bet money
            print("The sum is " + str(rollTotal) + ", which means, unfortunately, you lost out on the money. You now have " + str(totalCoins) + " total coins.")
            # tells the user if they won
    else:
        totalCoins = totalCoins - bet
        # updates the amount of coins when the user loses
        print("Unfortunately, you guessed incorrectly, because the sum of the two rolls is " + str(total) + ", which is not in the lower range of numbers. " + "\n" + "Original Bet: " + str(bet) + "\n" + "Total coins after bet: " + str(totalCoins))
        # tells the user the result of their bet
        bettingCoins()
        # calls the function
        
def highGuesser(bet):
    global totalCoins
    # makes the variable global
    diceOne = random.randint(1, 6)
    # rolls a dice
    print("For the first dice, you rolled a " + str(diceOne) + "!")
    # tells the user what number they got
    diceTwo = random.randint(1, 6)
    # rolls the second dice
    total = diceOne + diceTwo
    # calculates the sum of the two rolls
    print("For the second dice, you rolled a " + str(diceTwo) + "!" + "\n" + "Thus, the sum of the dice is " + str(total) + "!")
    # tells the user the sum of the two rolls

    if (total >= 2) and (total <= 6):
        totalCoins = totalCoins - bet
        # updates the amount of coins when the user wins
        print("Unfortunately, you guessed incorrectly, because the sum of the two rolls is " + str(total) + ", which is not in the higher range of numbers." + "\n" + "Original Bet: " + str(bet) + " coins " + "\n" + "Total coins after bet: " + str(totalCoins))
        # tells the user that they guessed correctly
        bettingCoins()
        # calls the function

    elif (total == 7):
        print("You rolled  a 7! If you roll a 7, what we do is that if you re-roll the dice and get an odd number, half of the money that you bet will be added to your total money! Good luck!!")
        # tells the user that they rolled a 7
        rollOne = random.randint(1, 6)
        # rolls the first dice again
        print("You have rolled a " + str(rollOne) + "!")
        # informs the user on the first roll
        rollTwo = random.randint(1, 6)
        # rolls the second dice again
        print("You have rolled a " + str(rollTwo) + "!")
        # informs the user on the second roll

        rollTotal = rollOne + rollTwo
        # finds the sum of the two rolls

        if rollTotal % 2 != 0:
            totalCoins = totalCoins + (bet / 2)
            # adds the bet to the total money
            totalCoins = round(totalCoins)
            # rounds it to the nearest integer in case of decimals
            print("The sum is " + str(rollTotal) + " which means you won your money! You now have " + str(totalCoins) + " total coins.")
            # tells the user if they won

        else :
            totalCoins = totalCoins - bet
            # player loses out on the bet money
            print("Unfortunately, you lost out on the money. You now have " + str(totalCoins) + " total coins.")
            # tells the user if they won

    else:
        totalCoins = totalCoins + ( 2 * bet)
        # updates the amount of coins when the user loses
        print("Fortunately, you guessed correctly, because the sum of the two rolls is " + str(total) + ", which falls into the higher range! " + "\n" + "Original Bet: " + str(bet) + " coins " + "\n" + "Total coins after bet: " + str(totalCoins))
        # message
        bettingCoins()
        # calls the function
        
def bettingCoins():
    flag = True
    # flag holds a boolean value
    while flag:
        bet = input("How many coins are you willing to bet? ")
        # asks the user how much they are willing to bet
        stopProgram(bet)
        # checks to see if the user typed "quit"
        try:
            bet = int(bet)
            # casts it to an integer
            if (bet >= 0) and (bet <= totalCoins):
                print("a. Low" + "\n" + "b. High")
                # tells the user the different options
                chosenBet = input("Enter in the letter that corresponds to the bet you want to make!")
                # asks the user on if they want to bet high or low
                if chosenBet == "a":
                    lowGuesser(bet)
                    # calls the lowGuesser function if the user guessed low

                elif chosenBet == "b":
                    highGuesser(bet)
                    # calls the highGuesser function if the user guesesd high

                else:
                    print("Please input a valid value!")
                    # invalid input message

            else :
                print("Please input a valid number. You cannot bet more than what you have!")
                # invalid input message

        except:
            print("Please input something valid!")
            # invalid input message

name = input("Hello! What is your name? ")
# asks the user for their name
print("Hello " + name + "! You have 1000 coins! Firstly, enter in a number to show how many coins you are willing to bet! You will then have to choose between two options: high or low. The program will automatically roll two dice, and then calculate the sum of the rolls. Below is a list of the information on the sum of the rolls." + "\n" + "Rolling a 2 to 6 is low." + "\n" + "Rolling a 7 is neutral." + "\n" + "Rolling an 8 to 12 is high." + "\n" + "If you guess the opposite of what is rolled(like high instead of low), you will lose the money you bet! However, if you guess correctly, the amount you bet will be doubled, and added it to your total money! Have fun!")
# introductory message
totalCoins = 1000
# initializes the total number of coins to 1000

bettingCoins()
# calls the function




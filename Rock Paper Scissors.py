userName=str(input("What's your name???"))
userName1=str(input("And your name???"))
userChoice=str(input(f"{userName}, do you want to choose rock, paper or scissors?"))
userChoice1=str(input(f"{userName1}, do you want to choose rock, paper or scissors?"))

if userChoice == userChoice1:
    print("It's a tie!")
elif (userChoice == 'rock' and userChoice1 == 'scissors') or (userChoice == 'paper' and userChoice1 == 'rock') or (userChoice == 'scissors' and userChoice1 == 'paper')  :
    print(f"{userName} wins!!")
elif (userChoice == 'scissors' and userChoice1 == 'rock') or (userChoice == 'rock' and userChoice1 == 'paper') or (userChoice == 'paper' and userChoice1 == 'scissors')  :
    print(f"{userName1} wins!!")

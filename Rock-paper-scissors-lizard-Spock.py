 Rock-paper-scissors-lizard-Spock 


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    if name=='rock':
        name=0
    elif name=='Spock':
        name=1
    elif name=='paper':
        name=2
    elif name=='lizard':
        name=3
    elif name=='scissors':
        name=4
    else:
        print("Error")
    return name

    


def number_to_name(number):
    if number==0:
        number='rock'
    elif number==1:
        number='Spock'
    elif number==2:
        number='paper'
    elif number==3:
        number='lizard'
    elif number==4:
        number='scissors'
    else:
        print("Error")
    return number
    
   
    
import random
def rpsls(player_choice): 
    print "\n"
    
    print("Player chooses "+player_choice)
   
    player_number=name_to_number(player_choice)
    
    comp_number=random.randrange(0,5)
    
    comp_choice=number_to_name(comp_number)
   
    print("Computer chooses "+comp_choice)
   
    diff=(comp_number-player_number)%5
   
    if diff==0:
        print("Player and computer tie!")
    elif diff<3:
        print("Computer wins!")
    elif diff>=3:
        print("Player wins!")
   

    

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


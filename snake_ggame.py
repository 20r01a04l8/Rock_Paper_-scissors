import random
def rps(comp, mine):
    if (comp==mine):
        return None
    
   
    if(comp=='r' and mine=='p'):
        return True
    elif(comp=='p' and mine == 's'):
        return True
    elif(comp=='s'and mine == 'r'):
        return True
    else:
        return False



choice = ('r','p','s')
comp = random.randint(0, 2)
comp = choice[comp]
mine = input("Choose rock (r)\npaper(p)\nscissor(s)\n: ")


win = rps(comp, mine)
print(f"You choice {mine} and computer choose {comp}")
if win is None:
    print("Match Drawn")
   
elif win:
    print("You win")
else:
    print("You Lose")








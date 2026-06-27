while True:
    x=input("what do you choose")
    if x not in['r','p','s',"quit"]:
          print("invalid input")
    elif(x=="quit"):
          print("thanks for playing")
          break
    else:
        import random
        comp=random.choice(['r','p','s'])
        print(f"computer chose {comp}")
        if(x==comp):
          print("tie")
        elif(x=='r' and comp=='s'):
          print("you won")
        elif(x=='s' and comp=='p'):
          print("you won")
        elif(x=='p' and comp=='r'):
          print("you won")
        else:
            print("you lost")
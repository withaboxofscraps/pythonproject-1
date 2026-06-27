
while(0==0):
    condition=input("do you want to roll your dice? (yes/no): ")
    if(condition=="y" or condition=="Y"):
      tup=[]
      import random
      for i in range(2):
        thing=random.randint(1,6)
        tup.append(thing)
      result=tuple(tup)
      print(result)
    elif(condition=="n" or condition=="N"):
       print("thanks")
       break
    else:
      print("invalid input")
# excuse my messy code, I'll clean it..

import random

randlist = [0,1,2,3,4,5,6,7,8,9] 
c= 9
randomnum = 0
for i in range(4):
  randtemp = random.randrange(0,c) 
  temp = randlist[randtemp] 
  randomnum += temp*(10**i) 
  del randlist[randtemp] used again
  c-=1 

print("                game rules")
print("cow mean it's right and in the right place")
print('')
print("key mean it's right but not in the right piace")
print('')
print("bull mean it's a wrong number")
print('')
print("write 4 numbers to guess the right number")
print('')
n=input()
t=True
while t:
  if(n==randomnum):
    print("We got a winner here!!")
    t=False
  else:
    c=0
    b=0
    k=0
    for i in range(randomnum):
      if(n[i]==randomnum[i]):
        c+=1 
      elif(n[0]==randomnum[i] or n[1]==randomnum[i] or n[2]==randomnum[i] or n[3]==randomnum[i]):
        k+=1
      else: 
        b+=1 
    print("cows:",c)
    print('')
    print("keys:",k)
    print('')
    print("bulls:",b)
    print('')
    print("try again")
    n=input() 

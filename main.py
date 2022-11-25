#Import the libraries that we need
import data as mydata
import random
import os
from time import sleep
#random word
myord=random.choice(mydata.wordlist)
the_word=myord

#print hangman logo
print(mydata.hangart)
#veriabals
myword=[]
check=[]
lives=6
mych=len(myord)
#makisg list of _
for a in myord:
  myword.extend(a)
  check.append('_')
#printing hangman and dashes
def spcaes(myspace,stage=6):
    
  print(mydata.hangman[stage])
  if stage==0:
    print(mydata.gameover)
    print('The word was: '+the_word)
    fl=input('Enter any key to exit:')
    exit()
      
  for a in myspace:
    print(a,end='')
#all the logics
while(lives>=0):
  spcaes(check,lives)
  #user fill all the dashes
  if mych<=0:
    print(mydata.winner)
    fl=input('Enter any key to exit:')
    exit()
 #user inpurt
  letter=input("\nEnter a single letter:")
 #modify the list of dashes
  if letter in myord:
    for a in myword:
      if a==letter:
        check[myword.index(a)]=a
        myword[myword.index(a)]=str('$')
        mych=mych-1
   #taking life    
  else:
    lives=lives-1


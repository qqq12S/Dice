import random
seq=['rock','paper','clip']
i=4
while i>0:
    player1=random.choice(seq)
    player2=random.choice(seq)
    print (player1+' = '+ player2)
    if player1 == 'rock' and player2 == 'clip':
        print ('win player1!')
    elif player2 == 'rock' and player1 == 'clip':
        print ('win player2!')
    elif player2 == 'paper' and player1 == 'clip':
        print ('win player1!')
    elif player1 == 'paper' and player2 == 'clip':
        print ('win player2!')
    elif player1 == 'paper' and player2 == 'rock':
        print ('win player1!')
    elif player2 == 'paper' and player1 == 'rock':
        print ('win player2!')
    i=i-1


        
    
        
    

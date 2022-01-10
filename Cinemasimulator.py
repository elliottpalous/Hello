# Dictionary of films showing
films = {
     'Finding Dory':{'age':3, 'tickets':5},
     'Bourne':{'age':18, 'tickets':5},
     'Tarzan': {'age':15, 'tickets':5},
     'Ghost Busters':{'age':12, 'tickets':5}
     }
# what film they want to watch and store choice
while True:
     
    choice = input('What film would you like to watch?: ').strip().title()
    
    if choice in films:
         age = int(input('How old are you?: ').strip())
# Check user age
         if age >= films[choice]['age']:
              #Check enough seats
              if films[choice]['tickets'] >0:
                   print('Enjoy the film!')
              
              #if tickets sold out
              else:
                 print("Sorry we are sold out! another film perhaps?")
              films [choice]['tickets'] = films[choice]['tickets']-1
     #if too young
         else:
             print('You are too young to see that film!')
     #not in dictionary      
    else:
          print("We don't have that film...")
          


     
               

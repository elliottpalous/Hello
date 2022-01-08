known_users = ['Alice', 'Bob', 'Clair', 'Dan', 'Emma', 'Fred', 'Georgie', 'Harry']
print(len(known_users))

while True:
     print('Hi! My name is Travis')
     name = input ('What is your name?: ').strip().capitalize()

     if name in known_users:
          print('Hello {}! Nice to see you again'.format(name))
          remove = input('Would you like to be removed from the system (y/n)?: ').lower()
          
          if remove == 'y':
               known_users.remove(name)
               print('Travis is sad to see you leave :(')
          elif remove == 'n':
               print("No problem, I didn't want to see you leave anyway")
                    
               
     else:
          print("Hmmmm I don't think I have met you yet {}".format(name))
          add_me = input('Would you like to add me to the system (y/n)?: ').strip().lower()
          if add_me == 'y':
                known_users.append(name)
                print("Welcome abord {}, I'm so pleased you've joined us".format(name))
          elif add_me == 'n':
               print("No worries, see you around")
          
     

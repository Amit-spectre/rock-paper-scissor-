import random
print ("'r' for rock, 'p' for paper, 's' for scissor")

options = ['r', 'p', 's']
hw_many = int(input("How many times you want to play: "))

for i in range(1, hw_many+1):
    
    u = str(input("Enter choice: "))
    rand_choice = random.choice(options)

    if u == 'r' and rand_choice == 's':
        print ("Oh I lost! Mine was sciccor")
    if u == 'r' and rand_choice == 'p':
        print ("yayy! I won mine was paper")
    if u == 'r' and rand_choice == 'r':
        print ("Its a tie!")
        
    if u == 'p' and rand_choice == 'r':
        print ("Oh! I lost! Mine was rock")
    if u == 'p' and rand_choice == 's':
        print ("Yayy! I won. Mine was scissor")
    if u == 'p' and rand_choice == 'p':
        print ("Its a tie")
        
    if u == 's' and rand_choice == 'p':
        print ("Oh! I lost. Mine was paper")
    if u == 's' and rand_choice == 'r':
        print ("Yayy! I won. Mine was rock")
    if u == 's' and rand_choice == 's':
        print ("Its a tie")
         
   









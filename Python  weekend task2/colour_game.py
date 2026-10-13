print("this is a color guess game")

for number in range(3):
        guess = str(input("Enter any color:   "))

        favorite_color = "blue"
        second_favorite = "green"
        
        if guess == favorite_color:
          print ("correct!")
          break
    
        if guess == second_favorite:
                print ("close!")
        else:
            print ("Wrong")

  

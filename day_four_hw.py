# Problem One - Task One

import random
moods = ["Happy", "Sad", "Energetic", "Calm", "Excited", "Grateful", "Relaxed"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for i in range(len(days)):
    mood = random.choice(moods)
    print(f"On {days[i]}, you were feeling {mood}.") 




# Problem Two - Task One
import random # ask ryan if u have to import random per code sect or just once
moods = ["Happy", "Sad", "Energetic", "Calm", "Excited", "Tired", "Grateful"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
times_of_day = ["morning", "afternoon", "evening"]

for day in days:
    for time in times_of_day:
        mood = random.choice(moods)
        print(f"On {day} {time} you were {mood}.")



# Problem Three - Task One - ask to go over one more time
counter = 0
while True: # - condition won't be true
    print("Inside the infinite loop")
    counter += 1
    if counter >= 5:
        break  

# Problem Three - Task Two    
counter = 0
while counter < 10: 
    print("Inside the conditional exit loop")
    counter += 1




# Problem Four - Task One  #go over
import random
def random_choice_game(items):  
    selected_item = random.choice(items)
    guess = input("Guess which item was selected: ")
    if guess == selected_item:
        print("Congratulations! You guessed correctly.")
    else:
        print(f"Sorry, the selected item was {selected_item}. Better luck next time!")

items = ["Apple", "Banana", "Orange", "Grapes", "Watermelon"]

random_choice_game(items)    
    



# Problem Five - Task One
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

for i, genre in enumerate(genres, start=1):
    print(f"Track {i}: Now playing {genre}")

# Problem Five - Task Two
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
i = 1

while i <= len(genres):
    genre = genres[i - 1]
    print(f"Track {i}: Now playing {genre}")
    if genre == 'Hip-hop':
        break  
    i += 1 

# Problem Five - Task Three
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

for i in range(len(genres)):
    genre = genres[i]
    if genre == 'Classical':
        continue  
    print(f"Track {i + 1}: Light show ready for {genre}")




# Problem 6 - Task One - **** finsh in the morning *****
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

selected_genres = genres[1:4]
for genre in selected_genres:
    print(genre)
    
# Problem Six - Task Two
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
new_genres = [genre + " Music" for genre in genres]
print(new_genres)    

# Problem Six - Task Three
for i in range(10, 0, -1):
    print(i)
print("The beat drops now!")
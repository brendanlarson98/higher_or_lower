from random import choice
import higher_lower_help as help
import higher_lower_data as data

data = data.data # Nested dictionary 
score = 0
playing = True
options = set()                                             # Here we get make a set which has all available options for users.
                                                            #As we present a user for the game, we remove that user from the set
for i in data:
    options.add(i)

options, user_a = help.get_user(options, data)              # We get our first users for the game.
options, user_b = help.get_user(options, data)

print(help.logo)

while playing:
    help.display_selection(data, user_a, user_b)            # Display the users and their information

    selection = help.get_selection(user_a, user_b)          # player makes a selection of higher or lower

    help.print_followers(data, user_a)                      # print users followers
    help.print_followers(data, user_b)
    if help.compare_values(data, user_a, user_b, selection):  # Here we compare the users' follower counts and if we were correct or not
        score += 1
        print("Correct!")
    else:
        print("Incorrect")
        playing = False
        break
      
    user_a = user_b                                         # If we were correct, we shift user_b to be user_a so we can reset user_b to get a new user
    options, user_b = help.get_user(options, data)          # to compare with
    

print("You ended with a score of", score)

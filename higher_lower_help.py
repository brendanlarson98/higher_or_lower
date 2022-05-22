from random import choice


vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
def get_user(options_set, items_dict):
    user = choice(list(options_set))                  # get a random user from our data
    options_set.remove(user)                          # Remove that as an option from our set
    return options_set, user


def display_selection(items_dict, selection_a, selection_b):                # In display_selection, we obtain our important attributes to show.
    att_a, att_2a, att_3a = items_dict[selection_a]["name"], items_dict[selection_a]['description'], items_dict[selection_a]['country']
    att_b, att_2b, att_3b = items_dict[selection_b]['name'], items_dict[selection_b]['description'], items_dict[selection_b]['country']
    print(f"User A: {att_a} is a {att_2a} from {att_3a}",vs,f"\nUser B: {att_b} is a {att_2b} from {att_3b}")
    
    
def get_selection(user_a, user_b):                    
    valid = False
    while not valid:
        selection = input(f"Does {user_b} have a lower or higher follower count than {user_a}? ").lower()
        if selection != 'higher' and selection != 'lower':
            print("Please enter lower or higher")
            continue
        valid = True
    print()
    return selection


def compare_values(items_dict, choice_a, choice_b, selection):
    value_a = items_dict[choice_a]["follower_count"]
    value_b = items_dict[choice_b]["follower_count"]
    if selection == "lower":
        if value_b < value_a:
            return True
    elif selection == "higher":
        if value_b > value_a:
            return True
    return False

def print_followers(data, user):
    print(user, "has a follower count (in millions) of", data[user]['follower_count'])

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

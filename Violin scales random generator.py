#scale sets:
chroma_tones = ["A","B","C","D","E","F","G","Ab/G#","Bb/A#","Db/C#","Eb/D#","F#/Gb"]
beginner = ["G", "D", "A"]

#mode sets:
major_only = ["major", "major arpeggio", "chromatic scale"]
bi_mode = ["major", "minor", "major arpeggio", "minor arpeggio"]
more_minors = ["major", "major arpeggio", "minor arpeggio", "melodic minor", "harmonic minor", "natural minor"]

#bowing patterns:
main_bowing = ["separate bows", "slurred, two notes to a bow"]
more_bowing = ["separate bows", "slurred, two to a bow", "slurred, four to a bow", "slurred, three to a bow"]

#user dictionaries:
lilit = {
    "my_scale_set": chroma_tones,
    "my_mode": more_minors,
    "my_bow_pattern": main_bowing
    }
beginners = {
    "my_scale_set": beginner,
    "my_mode": major_only,
    "my_bow_pattern": main_bowing
    }
test = {
    "my_scale_set": [1,2,3],
    "my_mode": [4,5],
    "my_bow_pattern": [6]
    }

#list of all users
user_list = {
    "lilit":lilit,
    "nelson": beginners,
    "test": test
    }

#generate random scale
from random import randint
def random_scale(scale_set, mode, bow_pattern):
    s = len(scale_set)
    m = len(mode)
    b = len(bow_pattern)
    s_i = randint(1,s) -1
    m_i = randint(1,m) -1
    b_i = randint(1,b) -1
    practice = '{} {}, {}'.format(scale_set[s_i],mode[m_i],bow_pattern[b_i])
    return practice

"""this was my first attempt. below I make user selection easier when the number of users increases.
#select the dictionary of sets via username input
def user_selection1():
    choose_user = input("Enter your name: ")
    choose_user = choose_user.lower()
    if choose_user == "nelson":
        user = nelson
    elif choose_user == "lilit":
        user = lilit
    else:
        print ("This name is not recognised.")
        user_selection1()
    return user #this is a local variable, so be sure to create a variable to store the output of
                    this function before doing the next function."""

#select the dictionary of sets via username input:
"""an alternative way to select the user - by using a dictionary of dictionaries:
NB must be a dictionary not list, so that you can look up your desired set with the user input,
which is a sring.
This is the simple/first version, used while creating the random scale generator and go_again functions below,
and while debugging:"""
"""def user_selection(database):
    choose_user = input("Enter your name: ")
    choose_user = choose_user.lower()
    user = database[choose_user]
    return user """

#select the dictionary of sets via username input:
def user_selection(database):
    choose_user = input("Enter your name: ")
    choose_user = choose_user.lower()
    name_checklist = []
    for key in database:
        name_checklist.append(key)
    if choose_user in name_checklist:
        user = database[choose_user]
        return user
    else:
        print ("Oops, I think you have a typo.")
        user_selection(database)

#******************************************************
#i need to review how to filter out spaces in a string.
#******************************************************


#generate random scale tailored to the user's scale sets
#This is the first draft. I have modified this function far down below to avoid duplication
        #(though sometimes duplicating is good, you practice again and again)
        #(maybe i will set up the new version to allor duplication once you've made it all the way through).
"""def users_random_scale(username):
    user_will_practice = random_scale(username["my_scale_set"], username["my_mode"],username["my_bow_pattern"])
    print ()
    print (user_will_practice)
    print ()"""


"""this way of running the program below was before I created the double iterating functions
#run program:
#user = user_selection()
#output = random_scale(user["my_scale_set"], user["my_mode"],user["my_bow_pattern"])
#print (output)"""

#trying to set up iteration
"""def users_random_scale(username):
    user_will_practice = random_scale(username["my_scale_set"], username["my_mode"],username["my_bow_pattern"])
    print (user_will_practice)
    again = 1
    while again >0:
        go_again(username)

def go_again(username):
    redo = input("Try another scale? Y/N: ")
    redo = redo.lower()
    if redo =="y" or redo =="yes" or redo =="yep" or redo =="aye":
        users_random_scale(username)
        #again = True
        #return again
    elif redo =="n" or redo =="no" or redo =="nope" or redo =="no way":
        print ("Happy practising! See you next time")
        again -= 1
        return again
    else:
        print ("Sorry, I didn't catch that...")
        #again = True
        #return again
    #return again
    #while again == True:
     #   go_again(username)
        #if again == False:
         #   break"""
    

"""here are my notes while I was repeatedly trying to get the loop to work and for some reason I was thinking
in the wrong way or something because the fnal solutino i sweaer was something I had already tried?
like maybe i just didn't execute properly when i was tsting this version one time and so thought it was wrong?
I dunno. final version is below this green"""
"""def go_again(username):
    #again = 1
    #users_random_scale(username)
    
    redo = input("Try another scale? Y/N: ")
    redo = redo.lower()
    
    if redo =="y" or redo =="yes" or redo =="yep" or redo =="aye":
        #again = 1
        users_random_scale(username)
        go_again(username)
        #again = True
        #return again
    elif redo =="n" or redo =="no" or redo =="nope" or redo =="no way":
        print ("Happy practising! See you next time")
        #again -= 1
    else:
        print ("Sorry, I didn't catch that...")
        go_again(username)
        #again = True
        #return again
    #return again
    #while again == True:
     #   go_again(username)
        #if again == False:
         #   break
    #while again >0:
     #   users_random_scale(username)"""
"""need to put while statement here and not before the redo input prompt
or before the if statement because otherwise the function cuts straight to
users_random_scale and skips the redo input!"""

#to generate repeated scales for the same user without restarting:
def go_again(username, scale_checklist):    
    redo = input("Try another scale? Y/N: ")
    redo = redo.lower()
    
    if redo =="y" or redo =="yes" or redo =="yep" or redo =="aye":
        generate_scale(username, scale_checklist)
        go_again(username, scale_checklist)
    elif redo =="n" or redo =="no" or redo =="nope" or redo =="no way":
        print ("Happy practising! See you next time")
        
    else:
        print ("Sorry, I didn't catch that...")
        go_again(username, scale_checklist)


#customise the welcome text
welcome_text = """
Welcome to the RANDOM SCALE GENERATOR for violin.

This program will generate a scale in a random key and bowing pattern for you to practice.
Enter your name below to generate a scale out of the ones you are familiar with.

"""

#what if i want the random scales generated to avoid any duplication?
#i would have to add every generated scale to a list, and then check against that.

#generate random scale tailored to the user's scale sets
#first define a checklist, then define the function separately.

#duplicate_list = []
#need to know how many combinations are possible for your user's scale set in order to set limit on avoiding duplication.
#max_list_length = number of items in each list in user's dictionary multiplied together
def no_of_combos(username):
    max_combos = 1
    for key in username:
       max_combos *= len(username[key])
    return max_combos

"""#testing
list_1 = [12,5,2,3,4]
list_2 = [2,3]
diction = {"first": list_1, "second": list_2}

#number of combos is 3*2 = 6
print (no_of_combos(diction))"""

#check no of combos
#limit = no_of_combos(name)

def users_random_scale(username):
    a_scale = random_scale(username["my_scale_set"], username["my_mode"],username["my_bow_pattern"])
    return a_scale

def generate_scale(username,scale_checklist):
    limit = no_of_combos(username)
    if len(scale_checklist) == limit:
        print ("""
You have now tried every scale variation that you know so far.
You can now learn a new scale, practice a piece of music, or...
perhaps you'd like to try these scales again, in a different random order?
""")
        scale_checklist = [] #need to empty out the checklist in order to start again
        go_again(username, scale_checklist)
    else:
        scale = users_random_scale(username) #generate a scale
        if scale in scale_checklist:
            generate_scale(username, scale_checklist) #if the scale has already been generated before, repeat this function
        else:
            print ()
            print (scale)
            print ()
            scale_checklist.append(scale)
            go_again(username, scale_checklist)


#errors to check - why LILIT doesn't work. sometimes this hapens to test and nelson... (None type object not iterable)
# and why sometimes the exit doesn't exit first time, but second time. 
#*******************************
#run program
#print (welcome_text)
name = user_selection(user_list)
"""print (no_of_combos(name))"""
scale_list = []
generate_scale(name, scale_list)
#go_again(name, scale_list)
#*******************************


"""this was one attempt, but it is too long and unwieldy: 
#assign the sets from the selected dictionary via key access
def scale_parameters(username):
    my_scale_set = username["my_scale_set"]
    my_mode = username["my_mode"]
    my_bow_pattern = username["my_bow_pattern"]
##create a new list with the sets inside it?
    return my_scale_set, my_mode, my_bow_pattern


#run program:
user = user_selection()
i = scale_parameters(user)
#output_random_scale = random_scale(i[0], i[1], i[2])
#output_random_scale = (random_scale(my_scale_set, my_mode, my_bow_pattern))
print (output_random_scale)"""

#**********************************************************************************************************
#to modify sets (lists) or create new user dictionaries...:
"""skeleton of program:
1. choose whether to edit set (list) or go to scale generator.
1a. teacher access: modify other's and self's scale list.
2. generate repeated random scales from within your list. """

"""list amending methods:
list_name[1] = "new item" >> overwrite
list_name.remove(item) >> removes the item (not by index value)
list_name.append(item) >>add the item"""

#choose the list to amend, then choose the item to amend. 

#lilit["my_bow_pattern"] = more_bowing
#userdict[access key] = newlist

#add new set.
#add new user.
#modify user: inputs - dictionary, key, and new list.
#modify sets: inputs - list type (dictionary), and remove or add items.

"""def create_new_user():
    new_user = input("Enter new student's name: ")    
    new_user = {"my_scale_set": pass, "my_mode": pass, "my_bow_patterns": pass}
    print (user_list)
It has become apparent I don't know how to get a user to add a new dictionary."""
    #print ("Choose which set of scales to assign. See current sets below or create a new sets.")
"""I can't assign a string to be the name of the new dict,
so instead I will add the inputted string directly into the main list of dictionaries
and check if that means it has created a dictionary..."""
#create_new_user()



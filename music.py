from csv import DictReader
import random

# open file in read mode
with open("top50music.csv", 'r') as f:  
    dict_reader = DictReader(f)   
    list_of_dict = list(dict_reader)

#empty dictionary of users to be filled below
users = {
    
}

new_user = {

}

song = random.choice(list_of_dict)
song0 = song

song = random.choice(list_of_dict)
song1 = song

new_user[0] = {0:song0, 1:song1}

#this loop is saving 500 users top 3 songs (randomly)
for i in range(500):
    song = random.choice(list_of_dict)
    song0 = song
    
    song = random.choice(list_of_dict)
    song1 = song
    
    song = random.choice(list_of_dict)
    song2 = song
    
    users[i] = {0:song0,1:song1,2:song2}



#code below will print out all of the users and their 3 top songs

for item in new_users:
    print(item)
    print(users[item][0])
    print(users[item][1])
    #print(users[item][2])
    #to print out or access a specific data point (such as artist) use user[item][0]["artist"]

    
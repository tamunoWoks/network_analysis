# A list of users represented as a dictionary with an "id" and a "name".
users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"},
]

# A list of tuples representing friendship pairs.
friendship_pairs = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (5, 7),
    (6, 8),
    (7, 8),
    (8, 9),
]




# ADD A LIST OF FRIENDS TO EACH USER

## First create an empty list of friends for each user
#for user in users:
#   user["friends"] = []

## Then Populate the friends list with frienship_pairs data
#for i, j in friendship_pairs:
#    users[i]["friends"].append(users[j])
#    users[j]["friends"].append(users[i])

## Create method to count number of friends for each user
#def number_of_friends(user):
#    return len(user["friends"])
#We can also do this another way

# Alternate solution
# Initialize the dict with an empty list for each user id:
friendships = {user["id"]: [] for user in users}

# Loop over the friendship pairs to populate it:
for i, j in friendship_pairs:
    friendships[i].append(j)  # Add j as a friend of user i
    friendships[j].append(i)  # Add i as a friend of user j





# LET'S FIND THE AVERAGE NUMBER OF CONNECTIONS
# First create a method to count number of friends for each user
def number_of_friends(user):
    return len(friendships[user["id"]])  # Length of the friends list for the user's ID

# Calculate total connections 
total_connections = sum(number_of_friends(user) for user in users)

# Now Calculate the average number of connections
num_users = len(users)
avg_connections = total_connections / num_users





# LET'S FIND THE MOST CONNECTED PEOPLE
# First create a tuple(user_id, number of friends)
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

# Now sort it by second element (number of friends) from largest to smallest
num_friends_by_id.sort(
    key=lambda id_and_friends: id_and_friends[1], reverse=True
)

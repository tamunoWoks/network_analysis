# A list of users, where each user is represented as a dictionary with an "id" and a "name".
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

# A list of tuples representing friendship pairs. Each tuple contains two user IDs.
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

#--------------------------------------------
# Create empty list of friends for each user
for user in users:
    user["friends"] = []

# Populate the friends list with frienship_pairs data
for i, j in friendship_pairs:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

# Create method to count number of friends for each user
def number_of_friends(user):
    return len(user["friends"])

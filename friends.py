users =[
    { "id":0, "name": "Hero" },
    { "id":1, "name": "Dunn" },
    { "id":2, "name": "Sue" },
    { "id":3, "name": "Chi" },
    { "id":4, "name": "Thor" },
    { "id":5, "name": "Clive" },
    { "id":6, "name": "Hicks" },
    { "id":7, "name": "Devin" },
    { "id":8, "name": "Kate" },
    { "id":9, "name": "Klein" }    
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]

def num_friends(user):
    '''
    Find number of friends for a given user
    '''
    i_d = -1
    for u in users:
        if u['name'] == user:
            i_d = u['id']
            break

    count = 0
    for tup in friendship:
        if tup[0] == i_d or tup[1] == i_d:
            count += 1

    return count

def sort_by_num_friends():
    '''README.md
    Sort from "most friends" to "least friends"
    '''
    f = []
    for u in users:
        friend_counts = {}
        friend_counts['name'] = u['name']
        friend_counts['count']= num_friends(u['name'])
        f.append(friend_counts)
    
    f = sorted(f, key=lambda u: u['count'],reverse=True) 

    return f

final_ans = sort_by_num_friends()
for user in final_ans:
    print("{} has {} friends".format(user['name'],user['count']))
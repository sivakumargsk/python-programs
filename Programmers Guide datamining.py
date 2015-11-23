import math

users = {"Angelica": { "Blues Traveler" : 3.5, "Broken Bells" : 2.0,
		      "Norah Jones" : 4.5 , "Phoenix" : 5.0,
		      "Slightly Stoopid" : 1.5, "The Strokes" : 2.5, 
		      "Vampire Weekend" : 2.0},

	"Bill"    : {"Blues Traveler" : 2.0, "Broken Bells" : 3.5,
		     "Deadmau5" : 4.0, "Phoenix" : 2.0, "Slightly Stoopid" :3.5,
		     "Vampire Weekend" : 3.0},

	"Chan" 	  : {"Blues Traveler" : 5.0, "Broken Bells" : 1.0,
		     "Deadmau5" : 1.0,  "Norah Jones" : 3.0,
		     "Phoenix" : 5.0, "Slightly Stoopid" :1.0},

	"Dan"     : {"Blues Traveler" : 3.0, "Broken Bells" : 4.0,
		     "Deadmau5" : 4.5, "Phoenix" : 3.0,
		     "Slightly Stoopid" : 4.5, "The Strokes" : 4.0,
		     "Vampire while ": 2.0},

        "Hailey"  : {"Broken Bells" : 4.0, "Deadmau5" : 1.0, "Norah Jones" : 4.0,
		     "The Strokes" : 4.0, "Vampire Weekend" : 1.0 },

	"Jordyn"  : {"Broken Bells" : 4.5, "Deadmau5" : 4.0, "Norah Jones" : 5.0,
		     "Phoenix" : 5.0, "Slightly Stoopid" : 4.5,
		     "The Strokes" : 4.0, "Vampire Weekend" : 4.0},

	"Sam"	  : {"Blues Traveler" : 5.0, "Broken Bells" : 2.0,
		     "Norah Jones" : 3.0, "Phoenix" : 3.0, 
		     "Slightly Stoopid" : 4.0, "The Strokes" : 5.0},

	 "Veronica": {"Blues Traveler" : 3.0, "Norah Jones" : 5.0,
		     "Phoenix" : 4.0, "Slightly Stoopid" : 2.5,
		     "The Strokes" : 3.0}}


def manhattan (u_name1 , u_name2):
    dist_sum = 0
    for key in u_name1:
        if key in u_name2:
            dist_sum += abs(u_name1[key] - u_name2[key])
    return dist_sum

'''
>>> manhattan(users['Hailey'], users['Veronica'])
2.0
>>> manhattan(users['Hailey'], users['Jordyn'])
7.5
>>>
'''

#Now a function to find the closest person (actually this returns a sorted list with the closest person first):

def closest_person (u_name , users):
    closest_list = []
    for user in users:
        if user != u_name:
            distance = manhattan(users[user],users[u_name])
            closest_list.append((distance, user))
    return sorted (closest_list)
'''
>>> closest_person("Hailey",users)
[(2.0, 'Veronica'), (3.5, 'Dan'), (4.0, 'Chan'), (4.0, 'Sam'), (5.0, 'Angelica'), (5.5, 'Bill'), (7.5, 'Jordyn')]
>>> closest_person("Sam",users)
[(4.0, 'Hailey'), (5.5, 'Dan'), (6.0, 'Bill'), (6.0, 'Chan'), (8.0, 'Jordyn'), (8.5, 'Veronica'), (10.0, 'Angelica')]
'''

def recommend (u_name , users):
    #first find the nearest person
    nearest_person = closest_person (u_name , users)[0][1]
    recommendations = []
    # now find bands neighbor rated that user didn't
    neighborRatings = users[nearest_person]
    userRatings = users[u_name]
    for artist in neighborRatings:
        if not artist in userRatings:
            recommendations.append((artist, neighborRatings[artist]))
    return sorted(recommendations,
                  key = lambda x: x[1],
                  reverse = True)
'''
>>> recommend("Hailey", users)
[('Phoenix', 4.0), ('Blues Traveler', 3.0), ('Slightly Stoopid', 2.5)]
>>> recommend("Sam", users)
[('Deadmau5', 1.0), ('Vampire Weekend', 1.0)]
'''

#1) Implement the Minkowski Distance function.

def minkowski (u_name1 , u_name2 , r):
    dist_sum = 0
    for key in u_name1:
        if key in u_name2:
            dist_sum += pow(abs(u_name1[key] - u_name2[key]),r)
    return pow(dist_sum,1/r)

'''
>>> minkowski(users['Hailey'], users['Veronica'],1)#r=1 Manhattan-distance
2.0
>>> minkowski(users['Hailey'], users['Veronica'],2)#r=2 Ecludian-Distance
1.0
'''

#2) Alter the closest_person function to use Minkowski Distance.
    
def minkowski_closest_person (u_name , users , r):
    closest_list = []
    for user in users:
        if user != u_name:
            distance = manhattan(users[user],users[u_name],r)
            closest_list.append((distance, user))
    return sorted (closest_list)



# karl-pearsons correlation coefficient.

def xbar (dic1, dic2):
    size = 0
    sum1 = 0
    for key in dic1:
        if key in dic2:
            sum1 += dic1[key]
            size += 1
    return sum1/size
def ybar (dic1, dic2):
    size = 0
    sum1 = 0
    for key in dic1:
        if key in dic2:
            sum1 += dic2[key]
            size += 1
    return sum1/size

def pearson_corr(data1 , data2):
    cov_xy  = 0
    sigma_x = 0
    sigma_y = 0
    for key in data1:
        if key in data2:
            cov_xy += ((data1[key] - xbar(data1,data2)) * (data2[key] - ybar(data1, data2)))
            sigma_x   += pow((data1[key] - xbar(data1, data2)), 2)
            sigma_y   += pow((data2[key] - ybar(data1, data2)), 2)
    return cov_xy/(sqrt(sigma_x) * sqrt(sigma_y))
'''
Output

>>> pearson_corr(users['Angelica'], users['Bill'])
-0.9040534990682688

>>> pearson_corr(users['Angelica'], users['Hailey'])
0.42008402520840293

>>> pearson_corr(users['Angelica'], users['Jordyn'])
0.7639748605475432

'''

def pearson (ratings1, ratings2):
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    sum_x2 = 0
    sum_y2 = 0
    n = 0
    for key in ratings1:
        if key in ratings2:
            n += 1
            x = ratings1[key]
            y = ratings2[key]
            sum_x += x
            sum_y += y
            sum_xy += x*y
            sum_x2 += x**2
            sum_y2 += y**2
    denominator = sqrt (sum_x2 - (sum_x ** 2)/n) * sqrt (sum_y2 - (sum_y ** 2)/n)
    if n == 0:
        return 0
    if denominator == 0:
        return 0
    else:
        return (sum_xy-(sum_x * sum_y) / n)/ denominator

'''

>>> pearson(users['Angelica'], users['Bill'])
-0.9040534990682699

>>> pearson(users['Angelica'], users['Hailey'])
0.42008402520840293

>>> pearson(users['Angelica'], users['Jordyn'])
0.7639748605475432

'''


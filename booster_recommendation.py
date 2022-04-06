# Boost indexes and their associated descriptions
boost_descriptions = {
    0: "10% Off McDonald's",
    1: "$1 Off Any Pizza Shop",
    2: "$1 Off Any Coffee Shop",
    3: "10% Off Chipotle",
    4: "10% Off Whole Foods",
    5: "$2 Off Twitch",
}

# Customer Boost matrix where every row represents a customer,
# every column represents a Boost, and every cell represents
# if the customer has used that Boost before.
customer_boost_matrix = [
    [1, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [0, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 0],
]

#  Example output using a k-similar-customers = 3
# Boost recommendations for customer 0
# > ['$1 Off Any Coffee Shop', '10% Off Whole Foods', '10% Off Chipotle']*/


import scipy.spatial.distance


def cosine_similarity(vector1, vector2):
    return 1 - scipy.spatial.distance.cosine(vector1, vector2)


class Boost_users:
    def __init__(self):
        self.users = {}


    def find_user_similarity(self,matrix):

        user_sim = {}

        for i in range(len(matrix)):
            #current_sim = []
            for j in range(len(matrix)):
                if i != j:
                    sim = cosine_similarity(matrix[i],matrix[j])

                    if (i,j) not in user_sim:
                        user_sim[(i,j)] = sim

                    if (j,i) not in user_sim:
                        user_sim[(j,i)] = sim

        return user_sim

    def find_similar_users(self,matrix):

        user_sim = self.find_user_similarity(matrix)

        most_similar = []

        for i in range(len(matrix)):
            cur_sim = []
            for j in range(len(matrix)):
                if i!=j :
                    cur_sim.append((j,user_sim[(i,j)]))

            cur_sim.sort(key = lambda i: i[1],reverse=True)

            #print('sim', cur_sim)

            most_similar.append(cur_sim)


        return most_similar

    def recommend_boosters (self,matrix, cust_id, n=2):

        similar_users = self.find_similar_users(matrix)

        recommended_boosters = set()

        cur_similar = similar_users[cust_id][:n]

        cur_boosters = matrix[cust_id]

        used_boosters = set([n for n, x in enumerate(cur_boosters) if x == 1])




        for j in range(n):
            #recommended_boosters.append(cur_similar[j][0])
            their_boosters = set([n for n, x in enumerate(matrix[cur_similar[j][0]]) if x == 1])

            recommended = their_boosters - used_boosters

            for booster in recommended:
                recommended_boosters.add(boost_descriptions[booster])


        return recommended_boosters



recommend = Boost_users()

recom_boosters = recommend.recommend_boosters(customer_boost_matrix,0)

print('Recom boosters to user 0 are', recom_boosters)

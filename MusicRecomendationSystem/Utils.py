def load_users(file_name):
    """ This function loads users from users file and returns list of users to the caller"""
    with open(file_name, "r") as f:
        u = map(lambda line: line.strip(), f.readlines())
    return u


def get_songs_by_popularity(trainingFile):
    """ This function counts the number of users that listens to each song """
    s = dict()
    with open(file, "r") as f:
        for line in f:
            _, song, _ = line.strip().split('\t')
            try:
                s[song] += 1
            except:
                s[song] = 1
    return sort_dictionary(s)

def sort_dictionary(d):
    """ This function returns the given dictionary d sorted by its keys"""
    return sorted(d.keys(),key=lambda s:d[s],reverse=True)

def load_unique_users(trainingFile):
    """Load the users into the set"""
    u = set()
    with open(trainingFile,"r") as f:
        for line in f:
            user, _, _ = line.strip().split('\t')
            if user not in u:
                u.add(user)
    return u


def get_unique_users_list_with_indecies(unique_users_list):
    """ THis method is used to load indecies for user names"""
    indexDictionary = dict()
    for i,user_name in enumerate(unique_users_list):
        indexDictionary[user_name] = i
    return indexDictionary


def get_song_to_user_index_map(trainingFile, unique_users_list_with_indecies):
    """ This function loads user,song,play_count triplets to form the map of song with set of users who listens to that song """
    song_users_map = dict()
    with open(trainingFile,"r") as f:
        for line in f:
            user_id,song_id,_ = line.strip().split('\t')
            user_index = unique_users_list_with_indecies[user_id]
            try:
                song_users_map[song_id].add(user_index)
            except:
                song_users_map[song_id]=set([user_index])
    return  song_users_map
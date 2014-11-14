__author__ = 'pejakalabhargava'
import Utils

if __name__ == '__main__':
trainingFile = "train_triplets.txt"
testingFile = "kaggle_visible_evaluation_triplets.txt"

# Load users to a list
print("loading users to a list")
users_list = list(Utils.load_users("kaggle_users.txt"))

#Order songs by popularity
print("Fetching songs by popularity")
popular_songs = Utils.get_songs_by_popularity(trainingFile)

#load users Index
print("Load unique Users idecies")
unique_users_list = Utils.load_unique_users(trainingFile)

#Annotate userNames with index
print("Enumerate User with indexes")
unique_users_list_with_indecies = Utils.get_unique_users_list_with_indecies(unique_users_list)

#Get the mapping of song to userId set
print("Get the training data as song to user indecies")
song_to_user_index_map = Utils.get_song_to_user_index_map(trainingFile, unique_users_list_with_indecies)

#delete the user_id_to_index_mapping
del unique_users_list_with_indecies






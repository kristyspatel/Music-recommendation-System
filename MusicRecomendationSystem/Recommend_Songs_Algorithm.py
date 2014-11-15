__author__ = 'pejakalabhargava'
import Music_Recommender_Utils, Song_Based_Predictor, Music_Recommender,sys

if __name__ == '__main__':
# Get the userId on whom we need to recommend songs
	user_id = sys.argv[1]
	user_id = int(user_id)
	trainingFile = "Data\msd_train.txt"
	testingFile = "Data\kaggle_visible_evaluation_triplets.txt"
	out_put_filename = "Data\output.txt"


# Load users to a list
print("loading users to a list")
users_list = list(Music_Recommender_Utils.load_users("Data\kaggle_users.txt"))

#Order songs by popularity
print("Fetching songs by popularity")
popular_songs_by_id = Music_Recommender_Utils.get_songs_by_popularity("Data\msd_train.txt")

#load users Index
print("Load unique Users idecies")
unique_users_list = Music_Recommender_Utils.load_unique_users(trainingFile)

#Annotate userNames with index
print("Enumerate User with indexes")
unique_users_list_with_indecies = Music_Recommender_Utils.get_unique_users_list_with_indecies(unique_users_list)

#Get the mapping of song to userId set
print("Get the training data as song to user indecies")
song_to_user_index_map = Music_Recommender_Utils.get_song_to_user_index_map(trainingFile,
                                                                            unique_users_list_with_indecies)
#delete the user_id_to_index_mapping
del unique_users_list_with_indecies

#next step is to initialize the predictor
#callign with similarity measure as  cosine for now
music_predictor = Song_Based_Predictor.SongBasedPredictor(song_user_map=song_to_user_index_map, alpha=0.5,
                                                          simialrity_measure=0);
#load the test data as dictionary of users with the set of songs the user has listened to as user vector
print("Loading the test data")
user_song_map_test_data = Music_Recommender_Utils.get_user_songs_map(testingFile)

#initialise the recommender required with top 50 songs as output desired
music_recommender = Music_Recommender.MusicRecommender(songs_ordered_by_popularity=popular_songs_by_id,
                                                       music_predictor=music_predictor, N=50)

if(users_list[user_id]):
    top_recommended_songs = music_recommender.recommend_songs_for_user(user_id,user_song_map_test_data)
else:
    print("Invalid UserId")
    exit(0)

Music_Recommender_Utils.save_results(top_recommended_songs, out_put_filename)




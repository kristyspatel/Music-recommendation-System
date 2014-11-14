__author__ = 'pejakalabhargava'
#TODO
class UserBasedPredictor:
    def __init__(self, item_map, alpha = 0.5):
        print("Creation of user based predictor")
        self.item_map = item_map
        self.alpha = alpha

    def find_similarity(self, user1, user2):
        print("calling similarity function")

    def find_score(self,users_for_item, all_users):
         print("Calculating the score")
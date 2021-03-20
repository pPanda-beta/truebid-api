class UserRating:
    def __init__(self, rating_id, user_id, rating):
        self.rating_id = rating_id
        self.user_id = user_id
        self.rating = rating

    def get_rating(self):
        return self.rating

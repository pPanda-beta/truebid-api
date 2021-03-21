from constants.Domains import *
from constants.Users import *
from models.User import User
from models.UserRating import UserRating


class UserRepository:
    def __init__(self):
        self.users = {
            user_1_id: User(user_1_id, "Ritabrata Moitra", [
                UserRating("rating_id_1", user_1_id, GROCERIES_DOMAIN, 4),
                UserRating("rating_id_1", user_1_id, GROCERIES_DOMAIN, 3),
                UserRating("rating_id_1", user_1_id, CLASSIFIEDS_DOMAIN, 4)
            ]),
            user_2_id: User(user_2_id, "Palash Das", []),
            user_3_id: User(user_3_id, "Sabyasachi Nandy", [])
        }

    def get_user(self, user_id):
        return self.users.get(user_id)

    def add_user(self, new_user: User):
        self.users[new_user.user_id] = new_user

    def add_rating(self, new_rating: UserRating):
        user_for_rating: User = list(
            filter(lambda user: user[1].user_id == new_rating.user_id, self.users.items())
        )[0][1]

        user_for_rating.ratings.append(new_rating)

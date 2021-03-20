from models.User import User
from models.UserRating import UserRating


class UserRepository:
    def __init__(self):
        user_1_id = "User_1"
        user_2_id = "User_2"
        user_3_id = "User_3"

        self.users = {
            user_1_id: User(user_1_id, "Ritabrata Moitra", [
                UserRating("rating_id_1", user_1_id, 4),
                UserRating("rating_id_1", user_1_id, 3),
                UserRating("rating_id_1", user_1_id, 4)
            ]),
            user_2_id: User(user_2_id, "Palash Das", []),
            user_3_id: User(user_3_id, "Sabyasachi Nandy", [])
        }

    def get_user(self, user_id):
        return self.users.get(user_id)

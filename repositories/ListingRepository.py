from constants.Skus import SKU_MILK_ID
from constants.Users import user_1_id
from models.Listing import Listing


class ListingRepository:
    def __init__(self):
        self.listings = {
            "listing_1": Listing("listing_1", "open", user_1_id, SKU_MILK_ID, 100, 200, 1616259606795, 1616259630598)
        }

    def get_all_listings(self):
        return self.listings

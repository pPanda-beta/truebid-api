from constants.Skus import *
from constants.Users import user_1_id, user_2_id, user_3_id
from models.Bid import Bid
from models.Listing import Listing


class ListingRepository:
    def __init__(self):
        listing_id_1 = "listing_1"
        listing_id_2 = "listing_2"
        self.listings = {
            listing_id_1: Listing(listing_id_1, "open", user_1_id, SKU_MILK_ID, 100, 200, 1616259600000, 1616346000000,
                                  [Bid("bid_id_1", listing_id_1, user_2_id, 110, 1616281200000),
                                   Bid("bid_id_2", listing_id_1, user_3_id, 120, 1616299200000)]
                                  ),
            listing_id_2: Listing(listing_id_2, "open", user_3_id, SKU_HAIRCUT_ID, 500, 900, 1616259600000,
                                  1616346000000, [])
        }

    def get_all_listings(self):
        return self.listings

    def get_listing_by_creator(self, creator_id):
        return dict(filter(lambda listing: listing[1].creator_id == creator_id, self.listings.items()))

    def get_listing_by_bidder(self, bidder_id):
        return dict(
            filter(lambda listing:
                   [d for d in listing[1].bids if bidder_id == d.user_id],
                   self.listings.items())
        )

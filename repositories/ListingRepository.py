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

    def get_listing_by_id(self, listing_id):
        return self.listings.get(listing_id)

    def get_listing_by_creator(self, creator_id):
        return dict(filter(lambda listing: listing[1].creator_id == creator_id, self.listings.items()))

    def get_listing_by_bidder(self, bidder_id):
        return dict(
            filter(lambda listing:
                   [d for d in listing[1].bids if bidder_id == d.user_id],
                   self.listings.items())
        )

    def add_listing(self, new_listing: Listing):
        self.listings[new_listing.listing_id] = new_listing

    def edit_listing(self, listing_id, request_body):
        listing: Listing = list(
            filter(lambda listing: listing[1].listing_id == listing_id, self.listings.items())
        )[0][1]

        for k, v in request_body.items():
            setattr(listing, k, v)

    def add_bid(self, new_bid: Bid):
        listing: Listing = list(
            filter(lambda listing: listing[1].listing_id == new_bid.listing_id, self.listings.items())
        )[0][1]

        listing.bids.append(new_bid)

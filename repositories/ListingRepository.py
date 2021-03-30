from constants.Skus import *
from constants.Users import user_1_id, user_2_id, user_3_id
from models.Bid import Bid
from models.Listing import Listing


class ListingRepository:
    def __init__(self):
        listing_id_1 = "listing_1"
        self.listings = {
            listing_id_1: Listing(listing_id_1, "open", user_1_id, SKU_ACCOMMODATION_ID, SKU_ACCOMMODATION, 30000,
                                  40000,
                                  1619715600000,
                                  1619820000000,
                                  [
                                      Bid("bid_id_1", listing_id_1, user_2_id, 31000, 1619794800000),
                                      Bid("bid_id_2", listing_id_1, user_3_id, 32000, 1619791200000)
                                  ])
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
            if k == 'bids':
                v = [Bid(**d) for d in v]
            if k == 'sku':
                v = Sku(**v)
            if k == 'accepted_bid':
                v = v and Bid(**v)
            setattr(listing, k, v)

    def add_bid(self, new_bid: Bid):
        listing: Listing = list(
            filter(lambda listing: listing[1].listing_id == new_bid.listing_id, self.listings.items())
        )[0][1]

        listing.bids.append(new_bid)

    def edit_bid(self, listing_id, bid_id, request_body):
        listing: Listing = list(
            filter(lambda listing: listing[1].listing_id == listing_id, self.listings.items())
        )[0][1]

        bid: Bid = next(filter(lambda bid: bid.bid_id == bid_id, listing.bids))

        for k, v in request_body.items():
            setattr(bid, k, v)

class Bid:
    def __init__(self, bid_id, listing_id, user_id, bid_amount, timestamp,
        **kwargs):
        self.bid_id = bid_id
        self.listing_id = listing_id
        self.user_id = user_id
        self.bid_amount = bid_amount
        self.timestamp = timestamp

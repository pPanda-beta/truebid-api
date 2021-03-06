class Listing:
    def __init__(self, listing_id, state, creator_id, sku_id, sku, min_price, max_price, created_time, expiration_time,
                 bids):
        self.listing_id = listing_id
        self.state = state
        self.sku_id = sku_id
        self.sku = sku
        self.creator_id = creator_id
        self.min_price = min_price
        self.max_price = max_price
        self.created_time = created_time
        self.expiration_time = expiration_time
        self.bids = bids
        self.accepted_bid = None

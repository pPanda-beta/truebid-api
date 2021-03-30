from constants.Skus import *


class SkuRepository:
    def __init__(self):
        self.skuList = {
            SKU_FLIGHT_ID: SKU_FLIGHT,
            SKU_ACCOMMODATION_ID: SKU_ACCOMMODATION
        }

    def get_all_sku(self):
        return self.skuList

    def get_sku(self, sku_id):
        return self.skuList[sku_id]

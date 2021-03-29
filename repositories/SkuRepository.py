from constants.Skus import *


class SkuRepository:
    def __init__(self):
        self.skuList = {
            SKU_MILK_ID: SKU_MILK,
            SKU_HAIRCUT_ID: SKU_HAIRCUT,
            SKU_FLIGHT_ID: SKU_FLIGHT
        }

    def get_all_sku(self):
        return self.skuList

    def get_sku(self, sku_id):
        return self.skuList[sku_id]

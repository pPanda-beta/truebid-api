from constants.Domains import GROCERIES_DOMAIN, CLASSIFIEDS_DOMAIN
from constants.Skus import *
from models.Sku import Sku


class SkuRepository:
    def __init__(self):
        self.skuList = {
            SKU_MILK_ID: Sku(SKU_MILK_ID, SKU_MILK_NAME, GROCERIES_DOMAIN, SKU_MILK_DESCRIPTION),
            SKU_HAIRCUT_ID: Sku(SKU_HAIRCUT_ID, SKU_HAIRCUT_NAME, CLASSIFIEDS_DOMAIN, SKU_HAIRCUT_DESCRIPTION)
        }

    def get_all_sku(self):
        return self.skuList

    def get_sku(self, sku_id):
        return self.skuList[sku_id]

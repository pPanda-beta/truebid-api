from constants.Domains import *
from models.Sku import Sku

SKU_MILK_NAME = 'Milk'
SKU_MILK_ID = "sku_milk"
SKU_MILK_DESCRIPTION = "Fresh Amul Milk 2 Litres ( 500ml * 4 )"
SKU_MILK = Sku(SKU_MILK_ID, SKU_MILK_NAME, GROCERIES_DOMAIN, SKU_MILK_DESCRIPTION)

SKU_HAIRCUT_NAME = 'Haircut'
SKU_HAIRCUT_ID = "sku_haircut"
SKU_HAIRCUT_DESCRIPTION = "Professional Haircut by Habib's stylist"
SKU_HAIRCUT = Sku(SKU_HAIRCUT_ID, SKU_HAIRCUT_NAME, CLASSIFIEDS_DOMAIN, SKU_HAIRCUT_DESCRIPTION)

SKU_FLIGHT_NAME = 'Business Class Flight Seat B2B'
SKU_FLIGHT_ID = 'Business Class Flight Seat B2B'
SKU_FLIGHT_DESCRIPTION = 'Boeing 737 flight from New Delhi to Brussels. Accepting B2B bids for business class seats.'
SKU_FLIGHT = Sku(SKU_FLIGHT_ID, SKU_FLIGHT_NAME, TRAVEL_DOMAIN, SKU_FLIGHT_DESCRIPTION)

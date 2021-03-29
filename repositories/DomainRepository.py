from constants.Domains import *
from models.Domain import Domain


class DomainRepository:
    def __init__(self):
        self.domains = {
            GROCERIES_DOMAIN: Domain(GROCERIES_DOMAIN, GROCERIES),
            SERVICES_DOMAIN: Domain(SERVICES_DOMAIN, SERVICES),
            CLASSIFIEDS_DOMAIN: Domain(CLASSIFIEDS_DOMAIN, CLASSIFIEDS),
            TRAVEL_DOMAIN: Domain(TRAVEL_DOMAIN, B2B_FLIGHTS)
        }

    def get_domains(self):
        return self.domains

from injector import singleton

from repositories.DomainRepository import DomainRepository
from repositories.ListingRepository import ListingRepository
from repositories.SkuRepository import SkuRepository
from repositories.UserRepository import UserRepository


def configure(binder):
    binder.bind(DomainRepository, to=DomainRepository, scope=singleton)
    binder.bind(SkuRepository, to=SkuRepository, scope=singleton)
    binder.bind(ListingRepository, to=ListingRepository, scope=singleton)
    binder.bind(UserRepository, to=UserRepository, scope=singleton)

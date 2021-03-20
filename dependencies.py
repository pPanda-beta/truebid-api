from injector import singleton

from repositories.DomainRepository import DomainRepository


def configure(binder):
    binder.bind(DomainRepository, to=DomainRepository, scope=singleton)

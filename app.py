import json

from flask import Flask
from flask_injector import FlaskInjector
from injector import inject

from dependencies import configure
from repositories.DomainRepository import DomainRepository
from repositories.ListingRepository import ListingRepository
from repositories.SkuRepository import SkuRepository
from repositories.UserRepository import UserRepository

app = Flask(__name__)


@inject
@app.route('/api/domains', methods=['GET'])
def get_domains(domainRepository: DomainRepository):
    return json.dumps(domainRepository.get_domains(), default=vars)


@inject
@app.route('/api/sku', methods=['GET'])
def get_sku(skuRepository: SkuRepository):
    return json.dumps(skuRepository.get_all_sku(), default=vars)


@inject
@app.route('/api/sku/<sku_id>', methods=['GET'])
def get_all_sku(skuRepository: SkuRepository, sku_id):
    return json.dumps(skuRepository.get_sku(sku_id), default=vars)


@inject
@app.route('/api/listing', methods=['GET'])
def get_all_listings(listingRepository: ListingRepository):
    return json.dumps(listingRepository.get_all_listings(), default=vars)


@inject
@app.route('/api/user/<user_id>', methods=['GET'])
def get_user(userRepository: UserRepository, user_id):
    return json.dumps(userRepository.get_user(user_id), default=vars)


FlaskInjector(app=app, modules=[configure])

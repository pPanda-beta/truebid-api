from flask import Flask, request, jsonify
from flask.json import JSONEncoder
from flask_injector import FlaskInjector
from injector import inject

from dependencies import configure
from repositories.DomainRepository import DomainRepository
from repositories.ListingRepository import ListingRepository
from repositories.SkuRepository import SkuRepository
from repositories.UserRepository import UserRepository


# TODO: Use dataclass instead, as JSONEncoder supports that
class ObjectJSONEncoder(JSONEncoder):
    default = vars


app = Flask(__name__)
app.json_encoder = ObjectJSONEncoder


@inject
@app.route('/api/domains', methods=['GET'])
def get_domains(domainRepository: DomainRepository):
    return jsonify(domainRepository.get_domains())


@inject
@app.route('/api/sku', methods=['GET'])
def get_sku(skuRepository: SkuRepository):
    return jsonify(skuRepository.get_all_sku())


@inject
@app.route('/api/sku/<sku_id>', methods=['GET'])
def get_all_sku(skuRepository: SkuRepository, sku_id):
    return jsonify(skuRepository.get_sku(sku_id))


@inject
@app.route('/api/listing', methods=['GET'])
def get_all_listings(listingRepository: ListingRepository):
    if 'creator_id' in request.args.keys():
        creator_id = request.args.get('creator_id')
        return jsonify(listingRepository.get_listing_by_creator(creator_id))
    elif 'bidder_id' in request.args.keys():
        bidder_id = request.args.get('bidder_id')
        return jsonify(listingRepository.get_listing_by_bidder(bidder_id))
    else:
        return jsonify(listingRepository.get_all_listings())


@inject
@app.route('/api/listing/<listing_id>', methods=['GET'])
def get_listing_by_id(listingRepository: ListingRepository, listing_id):
    return jsonify(listingRepository.get_listing_by_id(listing_id))


@inject
@app.route('/api/user/<user_id>', methods=['GET'])
def get_user(userRepository: UserRepository, user_id):
    return jsonify(userRepository.get_user(user_id))


FlaskInjector(app=app, modules=[configure])

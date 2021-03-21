import uuid

from flask import Flask, request, jsonify, abort
from flask.json import JSONEncoder
from flask_injector import FlaskInjector
from injector import inject

from dependencies import configure
from models.Bid import Bid
from models.Listing import Listing
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
@app.route('/api/listing', methods=['POST'])
def create_listing(listingRepository: ListingRepository):
    abort_if_body_not_found()

    body = request.json
    new_listing = Listing(
        str(uuid.uuid1()),
        "open",
        body['creator_id'],
        body['sku_id'],
        body['min_price'],
        body['max_price'],
        body['created_time'],
        body['expiration_time'],
        bids=[]
    )
    listingRepository.add_listing(new_listing)
    return jsonify({new_listing.listing_id: new_listing})


@inject
@app.route('/api/listing/<listing_id>', methods=['GET'])
def get_listing_by_id(listingRepository: ListingRepository, listing_id):
    return jsonify(listingRepository.get_listing_by_id(listing_id))


@inject
@app.route('/api/user/<user_id>', methods=['GET'])
def get_user(userRepository: UserRepository, user_id):
    return jsonify(userRepository.get_user(user_id))


@inject
@app.route('/api/bid', methods=['POST'])
def create_bid(listingRepository: ListingRepository):
    abort_if_body_not_found()

    body = request.json
    new_bid = Bid(
        str(uuid.uuid1()),
        body['listing_id'],
        body['user_id'],
        body['bid_amount'],
        body['timestamp']
    )
    listingRepository.add_bid(new_bid)
    return jsonify({new_bid.bid_id: new_bid})


def abort_if_body_not_found():
    if not request.json:
        abort(400)


FlaskInjector(app=app, modules=[configure])

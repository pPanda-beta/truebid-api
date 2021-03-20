import json

from flask import Flask
from flask_injector import FlaskInjector
from injector import inject

from dependencies import configure
from repositories.DomainRepository import DomainRepository
from repositories.SkuRepository import SkuRepository

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


FlaskInjector(app=app, modules=[configure])

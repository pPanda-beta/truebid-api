import json

from flask import Flask
from flask_injector import FlaskInjector
from injector import inject

from dependencies import configure
from repositories.DomainRepository import DomainRepository

app = Flask(__name__)


@inject
@app.route('/domains', methods=['GET'])
def get_domains(domainRepository: DomainRepository):
    return json.dumps(domainRepository.get_domains(), default=vars)


FlaskInjector(app=app, modules=[configure])

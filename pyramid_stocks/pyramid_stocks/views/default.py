# from pyramid.response import Response
from pyramid.view import view_config

# from sqlalchemy.exc import DBAPIError

from pyramid.httpexceptions import HTTPFound, HTTPNotFound, HTTPException

import requests
import json
from ..models import Stock
from . import DB_ERR_MSG
from sqlalchemy.exc import DBAPIError, IntegrityError
# from ..sample_data import MOCK_DATA
API_URL = 'https://api.iextrading.com/1.0'


@view_config(route_name='home',
    renderer='../templates/index.jinja2',
    request_method='GET')
def home_view(request):
    return{}


@view_config(route_name='portfolio',
    renderer='../templates/portfolio.jinja2')
def portfolio_view(request):
    """portfolio view"""
    try:
        query = request.dbsession.query(Stock)
        all_stocks = query.all()
    except DBAPIError:
        return DBAPIError(DB_ERR_MSG, content_type='text/plain', status=500)

    return {'stocks': all_stocks}


@view_config(route_name='detail',
    renderer='../templates/stock-detail.jinja2')
def detail_view(request):
    """single stock detail view"""
    try:
        symbol = request.matchdict['symbol']
    except KeyError:
        return HTTPNotFound()

    try:
        query = request.dbsession.query(Stock)
        stock_detail = query.filter(Stock.symbol == symbol).first()
    except DBAPIError:
        return DBAPIError(DB_ERR_MSG, content_type='text/plain', status=500)

    return {'stock': stock_detail}

    # for stock in MOCK_DATA:
    #     if stock['symbol'] == symbol:
    #         return {'stock': stock}


@view_config(route_name='auth',
    renderer='../templates/auth.jinja2')
def get_auth_view(request):
    if request.method == 'GET':
        try:
        # take a look at the data in the GET req
        # access form data
            username = request.GET['username']
            password = request.GET['password']
            print('User: {}, Pass: {}'.format(username, password))

            return HTTPFound(location=request.route_url('portfolio'))

        except KeyError:
            return {}

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        print('User: {}, Pass: {}, Email: {}'.format(username, password, email))

        return HTTPFound(location=request.route_url('portfolio'))

    return HTTPNotFound()  # some exception, probs a 404


@view_config(route_name='stock',
renderer='../templates/stock-add.jinja2')
def add_view(request):
    """stock view"""
    if request.method == 'POST':
        symbol = request.POST['symbol']
        response = requests.get('{}/stock/{}/company'.format(API_URL, symbol))
        company = response.json()

        model = Stock(**company)
        try:
            request.dbsession.add(model)
        except IntegrityError:
            pass

        return HTTPFound(location=request.route_url('portfolio'))


    if request.method == 'GET':
        try:
            symbol = request.GET['symbol']
        except KeyError:
            return {}

        response = requests.get('{}/stock/{}/company'.format(API_URL, symbol))
        try:
            data = response.json()
            return {'company': data}
        except json.decoder.JSONDecodeError:
            return {'err': 'Invalid Symbol'}

    return HTTPNotFound()







# @view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
# def my_view(request):
#     try:
#         query = request.dbsession.query(MyModel)
#         one = query.filter(MyModel.name == 'one').first()
#     except DBAPIError:
#         return Response(db_err_msg, content_type='text/plain', status=500)
#     return {'one': one, 'project': 'pyramid_stocks'}


# db_err_msg = """\
# Pyramid is having a problem using your SQL database.  The problem
# might be caused by one of the following things:

# 1.  You may need to run the "initialize_pyramid_stocks_db" script
#     to initialize your database tables.  Check your virtual
#     environment's "bin" directory for this script and try to run it.

# 2.  Your database server may not be running.  Check that the
#     database server referred to by the "sqlalchemy.url" setting in
#     your "development.ini" file is running.

# After you fix the problem, please restart the Pyramid application to
# try it again.
# """

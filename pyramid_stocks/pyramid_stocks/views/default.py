# from pyramid.response import Response
from pyramid.view import view_config

# from sqlalchemy.exc import DBAPIError
# from ..models import MyModel

from pyramid.httpexceptions import HTTPFound, HTTPNotFound, HTTPException

import requests
from ..sample_data import MOCK_DATA
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
    return {'stocks': MOCK_DATA}


@view_config(route_name='detail',
    renderer='../templates/stock-detail.jinja2')
def detail_view(request):
    """single stock detail view"""
    try:
        symbol = request.matchdict['symbol']
    except KeyError:
        return HTTPNotFound()

    for stock in MOCK_DATA:
        if stock['symbol'] == symbol:
            return {'stock': stock}

    return HTTPNotFound()


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
        print('User: {}, Pass: {}'.format(username, password, email))

        return HTTPFound(location=request.route_url('portfolio'))

    return HTTPNotFound()  # some exception, probs a 404


# @view_config(route_name='stock',
# renderer='../templates/stock-add.jinja2')
# def stock_view(request):
#     """stock view"""
#     if request.method == 'POST':
#         fields = ['companyName', 'symbol']

#     if not all([field in request.POST for field in fields]):
#         return HTTPBadRequest()

#     try:
#         stock = {
#             'companyName': request.POST['companyName'],
#             'symbol': request.POST['symbol'],
#             'exchange': request.POST['exchange'],
#             'website': request.POST['website'],
#             'CEO': request.POST['CEO'],
#             'industry': request.POST['industry'],
#             'sector': request.POST['sector'],
#             'issueType': request.POST['issueType'],
#             'description': request.POST['description']
#         }

#     except KeyError:
#         pass

#     MOCK_DATA.append(stock)
#     return HTTPFound(request.route_url('portfolio'))

#     if request.method == 'GET':
#         try:
#             symbol = request.GET['symbol']
#         except KeyError:
#             return {}

#         response = requests.get(API_URL + '/stock/{}/company'.format(symbol))
#         data = response.json()
#         return {'company': data}

#     else:
#         raise HTTPNotFound()







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

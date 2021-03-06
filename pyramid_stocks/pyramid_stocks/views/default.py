from pyramid.response import Response
from pyramid.view import view_config

# from sqlalchemy.exc import DBAPIError

# from ..models import MyModel


@view_config(route_name='home', renderer='../templates/index.jinja2')
def home_view(request):
    return{}


@view_config(route_name='auth', renderer='../templates/login.jinja2')
def get_auth_view(request):
    return {}


# @view_config(route_name='register', renderer='../templates/register.jinja2')
# def get_register_view(request):
#     return {}


@view_config(route_name='stock', renderer='../templates/stock_add.jinja2')
def get_stock_view(request):
    return{}


@view_config(route_name='portfolio', renderer='../templates/portfolio.jinja2')
def get_portfolio_view(request):
    return{}


# @view_config(route_name='portfolio/{symbol}', renderer='../templates/stock_detail.jinja2')
# def get_detail_view(request):
#     symbol = 'test'
#     return{}




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

from pyramid.view import notfound_view_config


@notfound_view_config(renderer='../templates/404.jinja2')
def notfound_view(request):
    '''view for 404'''
    request.response.status = 404
    return {}

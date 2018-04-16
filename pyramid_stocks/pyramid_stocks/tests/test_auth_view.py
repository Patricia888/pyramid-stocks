def test_default_behavior_of_auth_view(dummy_request):
    """test auth view"""
    from ..views.auth import auth_view

    response = auth_view(dummy_request)
    assert isinstance(response, dict)
    assert response == {}


def test_signin_to_auth_view(dummy_request, db_session, test_user):
    """test auth view sign-in"""
    from ..views.auth import auth_view
    from pyramid.httpexceptions import HTTPFound
    db_session.add(test_user)

    dummy_request.method = 'GET'
    dummy_request.GET = {'username': 'testtest', 'password': 'testpass'}
    response = auth_view(dummy_request)
    assert isinstance(response, HTTPFound)


def test_auth_view_sign_up(dummy_request):
    """test auth view sign-up"""
    from ..views.auth import auth_view
    from pyramid.httpexceptions import HTTPFound

    dummy_request.method = 'POST'
    dummy_request.POST = {'username': 'scott', 'password': 'schmit', 'email': 'scott@schmit.com'}
    response = auth_view(dummy_request)
    assert isinstance(response, HTTPFound)
    assert response.status_code == 302


def test_auth_view_sign_up_bad_request(dummy_request):
    """test auth view sign-up without username"""
    from ..views.auth import auth_view
    from pyramid.httpexceptions import HTTPBadRequest

    dummy_request.method = 'POST'
    dummy_request.POST = {'password': 'schimt', 'email': 'scott@schmit.com'}
    response = auth_view(dummy_request)
    assert isinstance(response, HTTPBadRequest)
    assert response.status_code == 400


def test_auth_view_sign_up_wrong_method(dummy_request):
    """test auth view sign-up without username"""
    from ..views.auth import auth_view
    from pyramid.httpexceptions import HTTPFound

    dummy_request.method = 'PUT'
    response = auth_view(dummy_request)
    assert isinstance(response, HTTPFound)
    assert response.status_code == 302

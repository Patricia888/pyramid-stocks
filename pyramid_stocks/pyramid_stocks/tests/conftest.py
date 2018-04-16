import pytest
from pyramid import testing
import os
from ..models.meta import Base
from ..models import Stock
from ..models import Account


@pytest.fixture
def dummy_request(db_session):
    """Create a dummy request"""
    return testing.DummyRequest(dbsession=db_session)


@pytest.fixture
def test_stock():
    """Set up a test stock"""
    return Stock(
        symbol="GE",
        companyName="General Electric Company",
        exchange="New York Stock Exchange",
        industry="Industrial Products",
        website="http://www.ge.com",
        description="General Electric Co is a digital industrial company. It operates in various segments, including power and water, oil and gas, energy management, aviation, healthcare, transportation, appliances and lighting, and more.",
        CEO="John L. Flannery",
        issueType="cs",
        sector="Industrials"
    )


@pytest.fixture
def configuration(request):
    """Setup a database for testing purposes"""
    config = testing.setUp(settings={
        'sqlalchemy.url': os.environ['TEST_DATABASE_URL']
    })
    config.include('..models')
    config.include('..routes')

    def teardown():
        testing.tearDown()

    request.addfinalizer(teardown)
    return config


@pytest.fixture
def db_session(configuration, request):
    """Create a database session for interacting with the test database"""
    SessionFactory = configuration.registry['dbsession_factory']
    session = SessionFactory()
    engine = session.bind
    Base.metadata.create_all(engine)

    def teardown():
        session.transaction.rollback()
        Base.metadata.drop_all(engine)

    request.addfinalizer(teardown)
    return session


@pytest.fixture
def add_stock(dummy_request, test_stock):
    """Add a stock to database"""
    dummy_request.dbsession.add(test_stock)
    return test_stock


@pytest.fixture
def test_user():
    """Set up a test user"""
    return Account(
        username="testtest",
        password="testpass",
        email="test@testthis.com",
    )


@pytest.fixture
def add_user(dummy_request, test_user):
    """Add a user to database"""
    dummy_request.dbsession.add(test_user)
    return test_user

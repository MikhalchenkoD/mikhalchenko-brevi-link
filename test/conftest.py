

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.routes import create_app
from src.models import Base

test_engine = create_engine('sqlite:///test.db')
Session = sessionmaker(test_engine)
test_session = Session()


@pytest.fixture(scope='session')
def app():
    Base.metadata.create_all(test_engine)
    _app = create_app(test_session)

    yield _app

    Base.metadata.drop_all(test_engine)


@pytest.fixture
def client(app):
    client = app.test_client()
    yield client


from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey
)

from .meta import Base


# include all necessary categories of each stock
class Stock(Base):
    __tablename__ = 'stock'
    id = Column(Integer, primary_key=True)
    symbol = Column(String(10), nullable=False, unique=True)
    companyName = Column(String, nullable=False)
    exchange = Column(String)
    industry = Column(String)
    website = Column(String)
    description = Column(String)
    CEO = Column(String)
    issueType = Column(String)
    sector = Column(String)

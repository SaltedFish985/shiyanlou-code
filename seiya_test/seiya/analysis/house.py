import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO
from sqlalchemy import func, desc, and_, select
from ..db import session, House, engine

def housing_estate_top10():
    query = session.query(
            House.housing_estate,              
            func.count(House.housing_estate).label('count')     
    ).group_by(House.housing_estate).order_by(desc('count')).limit(10)    
    return [i._asdict() for i in query] 

def apartment_stat():
    rows = session.query(
        House.apartment,
        func.count(House.apartment).label('count')
    ).group_by('apartment').order_by(desc('count')).limit(5)
    print([row._asdict() for row in rows])
    return [row._asdict() for row in rows]

def rent_by_apartment():
    apartment_list = apartment_stat()
    five_apartment = []
    for x in apartment_list:
        five_apartment.append(x['apartment'])
    rows = session.query(
        House.housing_estate,
        House.apartment,
        House.rent
    ).filter(House.apartment in five_apartment
    ).group_by('apartment').order_by(desc('rent')) 
    return [row._asdict() for row in rows] 


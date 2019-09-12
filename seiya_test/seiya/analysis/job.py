import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO
from sqlalchemy import func, desc, and_, select
from ..db import session, Job, engine

def count_top10():
    query = session.query(
            Job.city,              
            func.count(Job.city).label('count')     
    ).group_by(Job.city).order_by(desc('count')).limit(10)    
    return [i._asdict() for i in query]  

def salary_top10():
    query = session.query(
            Job.city,
            func.avg((Job.salary_low+Job.salary_up)/2).label('salary')
    ).filter(and_(Job.salary_low>0, Job.salary_up>0)
    ).group_by(Job.city).order_by(desc('salary')).limit(10)
    query_dict_list = [i._asdict() for i in query]
    for i in query_dict_list:
        i['salary'] = float(format(i['salary'], '.1f'))
    return query_dict_list

def hot_tags():
    df = pd.read_sql(select([Job.tags]), engine)
    tags_list = [i.split() for i in df.tags if i != '""']
    tags_df = pd.DataFrame([i for l in tags_list for i in l], columns=['tags'])
    return tags_df.groupby('tags').size().sort_values(ascending=False).head(10)

def hot_tags_plot(format='png'):
    mpl.rcParams['font.sans-serif'] = ['simhei']
    mpl.rcParams['axes.unicode_minus'] = False
    mpl.rcParams['figure.figsize'] = 10, 5
    tags_series = hot_tags()
    xlabel_list = [x for x in range (1,11)]
    plt.bar(xlabel_list, tags_series.values)
    plt.xticks([index for index in xlabel_list], tags_series.index)
    img = BytesIO()
    plt.savefig(img, format=format)
    return img.getvalue()

def experience_stat():
    rows = session.query(        
        func.concat(
            Job.experience_low, '-', Job.experience_up, '年'
        ).label('experience'),
        func.count('experience').label('count')
    ).group_by('experience').order_by(desc('count'))
    return [row._asdict() for row in rows]

def education_stat():
    rows = session.query(
        Job.education,
        func.count(Job.education).label('count')
    ).group_by('education').order_by(desc('count'))
    return [row._asdict() for row in rows]

def salary_by_city_and_edu():
    rows = session.query(
        Job.city,
        Job.education,
        func.avg((Job.salary_low+Job.salary_up)/2).label('salary')
    ).filter(and_(Job.salary_low>0, Job.salary_up>0)
    ).group_by('city', 'education').order_by(desc('city'))
    rows = [row._asdict() for row in rows]
    for row in rows:
        row['salary'] = float('{:.2f}'.format(row['salary']))
    return rows



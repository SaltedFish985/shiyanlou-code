from flask import Blueprint, render_template
from simpledu.models import Live

live = Blueprint('live', __name__, url_prefix='/live')


@live.route('/')
def index():
    the_data = Live.query.order_by(Live.id.desc()).first()
    return render_template('live/index.html', data=the_data)


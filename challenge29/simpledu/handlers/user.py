from flask import Blueprint, render_template, abort
from simpledu.models import User

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/<username>')
def user_index(username):
    users = User.query.filter_by(username=username).all()
    if len(users) == 0: 
        abort(404)
    return render_template('user/detail.html', users=users)
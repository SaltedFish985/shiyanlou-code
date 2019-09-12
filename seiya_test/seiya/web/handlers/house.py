from flask import render_template, Blueprint, Response, jsonify
import seiya.analysis.house as house_

house = Blueprint('house', __name__, url_prefix='/house')

@house.route('/')
def index():
    return render_template('house/index.html')

@house.route('/housing_estate_top10')
def housing_estate_top10():
    return render_template('house/housing_estate_top10.html', query=house_.housing_estate_top10())

@house.route('/apartment_stat')
def apartment_stat():
    return render_template('house/apartment_stat.html', rows=house_.apartment_stat())

@house.route('/apartment_stat.json')
def apartment_stat_json():
    return jsonify(house_.apartment_stat())

@house.route('/rent_by_apartment')
def rent_by_apartment():
    rows = house_.rent_by_apartment()
    return render_template('house/rent_by_apartment.html', rows=rows)

@house.route('/rent_by_apartment.json')
def rent_by_apartment_json():
    return jsonify(house_.rent_by_apartment())
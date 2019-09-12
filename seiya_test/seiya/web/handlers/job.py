from flask import render_template, Blueprint, Response, jsonify
import seiya.analysis.job as job_

job = Blueprint('job', __name__, url_prefix='/job')

@job.route('/')
def index():
    return render_template('job/index.html')

@job.route('/count_top10')
def count_top10():
    return render_template('job/count_top10.html', query=job_.count_top10())

@job.route('/salary_top10')
def salary_top10():
    return render_template('job/salary_top10.html', query=job_.salary_top10())

@job.route('/hot_tags')
def hot_tags():
    query = [{'tag': i, 'count': j} for i, j in job_.hot_tags().items()]
    return render_template('job/hot_tags.html', query=query)

@job.route('/hot_tags.png')
def hot_tags_plot():
    return Response(job_.hot_tags_plot(), content_type='image/png')

@job.route('/hot_tags.json')
def hot_tags_json():
    d = {key: int(value) for key, value in job_.hot_tags().to_dict().items()}
    return jsonify(d)

@job.route('/experience_stat')
def experience_stat():
    return render_template('job/experience_stat.html', rows=job_.experience_stat())

@job.route('/experience_stat.json')
def experience_stat_json():
    return jsonify(job_.experience_stat())

@job.route('/education_stat')
def education_stat():
    return render_template('job/education_stat.html', rows=job_.education_stat())

@job.route('/education_stat.json')
def education_stat_json():
    return jsonify(job_.education_stat())

@job.route('/salary_by_city_and_edu')
def salary_by_city_and_edu():
    rows = job_.salary_by_city_and_edu()
    return render_template('job/salary_by_city_and_edu.html', rows=rows)

@job.route('/salary_by_city_and_edu.json')
def salary_by_city_and_edu_json():
    return jsonify(job_.salary_by_city_and_edu())
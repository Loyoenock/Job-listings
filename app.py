from flask import Flask, render_template, jsonify
app = Flask(__name__)

JOBS = [
{
	'id': 1,
'title': 'Data Analyst',
'location': 'Entebbe, Uganda',
'salary': 'Ugx. 2,500,000'
},

{
        'id': 2,
'title': 'Data Scientist',
'location': 'Gulu, Uganda',
'salary': 'Ugx. 2,300,000'
},

{
        'id': 3,
'title': 'Frontend Engineer',
'location': 'Remote'
},

{
        'id': 1,
'title': 'Backend Engineer',
'location': 'San Francisco USA',
'salary': 'usd.500,000'
}


]
@app.route('/')
def index():
    return render_template('home.html', 
			jobs = JOBS,
			company_name='Hanok')
@app.route('/api/jobs')
def list_jobs():
	return jsonify(JOBS)

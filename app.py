from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'Location': 'Bengaluru,India',
    'salary': '10lac'
}, {
    'id': 2,
    'title': 'Scientist',
    'Location': 'Bengaluru,India',
    'salary': '10lac'
}]


@app.route('/')
def Hello_ship():
  return render_template('Dummy2.html', jobs=JOBS, company_name='Shipping')


@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(debug=True)

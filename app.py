from flask import Flask, render_template
import pandas as pd
import json

app = Flask(__name__)

@app.route("/")
def index():
    data = 10
    return render_template('index2.html', data = data)

@app.route('/results', methods = ['GET', 'POST'])
def results():
    form = ProjectForm()
    if request.method == 'POST' and form.validate():

        variable1 = request.form['variable1']
        variable2 = request.form['variable2']
        variable3 = request.form['variable3']
        
        return redirect(url_for('project_result', variable1= variable1, variable2 = variable2,
                                                variable3 = variable3))    
    
    return render_template('results.html', form = form)

if __name__ == '__main__':
    app.run(debug=True, port = 5000)        
    

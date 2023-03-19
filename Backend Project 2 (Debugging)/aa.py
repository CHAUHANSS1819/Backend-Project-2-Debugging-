from flask import Flask, request, render_template

app = Flask(__name__)
notes = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        note = request.form['note']
        notes.append(note)
    return render_template('home.html', notes=notes)

@app.route('/submit-form', methods=['POST'])
def submit():
    if request.method == 'POST':
        note = request.form['note']
        notes.append(note)
        return render_template('home.html', notes=notes)
    
@app.route('/delete-note', methods=['POST'])
def delete():
    if request.method == 'POST':
        note = request.form['note']
        notes.remove(note)
    return render_template('home.html', notes=notes)
    	

if __name__ == '__main__':
    app.run(debug=True)

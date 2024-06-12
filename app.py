from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory database for simplicity
memberships = {}

@app.route('/')
def index():
    return render_template('index.html', memberships=memberships)

@app.route('/add_membership', methods=['GET', 'POST'])
def add_membership():
    if request.method == 'POST':
        membership_number = request.form['membership_number']
        duration = request.form['duration']
        memberships[membership_number] = {
            'duration': duration,
            'status': 'active'
        }
        return redirect(url_for('index'))
    return render_template('add_membership.html')

@app.route('/update_membership', methods=['GET', 'POST'])
def update_membership():
    if request.method == 'POST':
        membership_number = request.form['membership_number']
        if membership_number in memberships:
            action = request.form['action']
            if action == 'extend':
                memberships[membership_number]['duration'] = str(int(memberships[membership_number]['duration']) + 6)
            elif action == 'cancel':
                memberships[membership_number]['status'] = 'cancelled'
        return redirect(url_for('index'))
    return render_template('update_membership.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock databases
users = []
listings = []

# Helper function to check if email is valid for NUST students
def is_nust_email(email):
    return email.endswith('@edu.pk')

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Registration Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if is_nust_email(email):
            # Add user to mock database
            users.append({'email': email, 'password': password})
            return redirect(url_for('create_profile'))
        else:
            return "Invalid NUST Email!", 400

    return render_template('register.html')

# Profile Creation Route
@app.route('/create_profile', methods=['GET', 'POST'])
def create_profile():
    if request.method == 'POST':
        item = request.form['item']
        skill = request.form['skill']
        
        # Add item/skill to mock listings
        listings.append({'item': item, 'skill': skill})
        return redirect(url_for('view_listings'))

    return render_template('create_profile.html')

# View Listings Route
@app.route('/listings')
def view_listings():
    return render_template('listings.html', listings=listings)

if __name__ == '__main__':
    app.run(debug=True)


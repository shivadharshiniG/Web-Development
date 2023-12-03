from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        login_name = request.form['name']
        login_pwd = request.form['pwd']

        return f"Login successful! Username: {login_name}"
    else:
        return render_template('home.html')
    
@app.route("/signup", methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form['name']
        email = request.form['email']
        password = request.form['pwd']
        
        
        return f"Signup successful! Username: {username}, Email: {email}"
    else:
        return render_template('home.html')

    
@app.route("/forgot_password", methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email_or_username = request.form['email']
        return redirect(url_for('login'))

    return render_template('forgot_password.html')


if __name__ == "__main__":
    app.run(debug=True)

import os
from flask import Flask, render_template, url_for, flash, redirect, request, send_from_directory
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

posts = [
    {
        'Food_name': 'Traditional Meals',
        'title': 'Ugali',
        'content': 'First post content',
        'order_id': 'qwer098'
    },
    {
        'Food_name': 'Cuisines',
        'title': 'Matooke',
        'content': 'Second post content',
        'order_id': 'qwer099'
    },
    
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    image_names = os.listdir('./images')
    print(image_names)
    return render_template("about.html", image_names=image_names)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    '''check if form validate when submitted'''
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        '''redirect user after form validation'''
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)


if __name__ == '__main__':
    app.run(debug=True)
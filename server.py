from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__, static_folder='static', static_url_path='/static')

print(__name__)



@app.route("/")
def homepage():
    return render_template('./index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open ('database.txt', mode='a') as database:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{name}, {email}, {subject}, {message}')

def write_to_csv(data):
    with open ('database.csv', mode='a', newline='') as database2:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            print(data)
            return redirect('/thankyou.html')
        except:
            return'did not save to database'
    else:
        return 'something went wrong. try again'





'''
error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    render_template('login.html', error=error)
'''

'''
@app.route("/left-sidebar.html")
def leftsidebar():
    return render_template('./left-sidebar.html')

@app.route("/right-sidebar.html")
def rightsidebar():
    return render_template('./right-sidebar.html')

@app.route("/no-sidebar.html")
def nosidebar():
    return render_template('./no-sidebar.html')

@app.route("/<username>")
def user(username=None):
    #print(url_for('static', filename='lollipop.ico'))
    return render_template('./index.html', name=username)

@app.route("/<username>/<int:post_id>")
def post_id(username=None, post_id=None):
    #print(url_for('static', filename='lollipop.ico'))
    return render_template('./index.html', name=username, post_id=post_id)

@app.route("/about")
def about():
    return render_template('./about.html')

@app.route("/blog")
def blog():
    return "These are my thoughts on blogs"

@app.route("/favicon.ico")
def icon():
    return send_from_directory(app.root_path, 'lollipop.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/blog/2020/dogs")
def blog2():
    return "This is my dog"

# https://flask.palletsprojects.com/en/2.0.x/quickstart/ follow this to run

'''
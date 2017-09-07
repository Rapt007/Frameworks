from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
username = ''

@app.route('/', methods=['GET', 'POST'])
def show_index():
    global username
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        username = request.form.get('username', 'none')
        return redirect(url_for('show_user_home'))

@app.route('/homepage')
def show_user_home():
    # use global username
    return render_template('userhome.html', user=username)

if __name__ == '__main__':
    app.run()
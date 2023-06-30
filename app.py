from flask import Flask, render_template, request
import subprocess
from code_twitter_user_info import TwitterOps

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run():
    service = request.form['service']
    if service == 'service1':
        #result = subprocess.check_output(['python', 'code_twitter_user_info.py'])
        #result = result.decode()
        #twitter_user()
        result = "twitter code !"
    elif service == 'service2':
        result = subprocess.check_output(['python', 'code_tweeter_hashtag.py'])
        result = result.decode()

    return render_template('form_user.html', result=result)

@app.route('/get_user', methods=['POST'])
def get_user():
    username = request.form["username"]
    twitter_api = TwitterOps()
    info = twitter_api.get_user_info(username)
    if info is not None:
        all_tweets = twitter_api.get_user_tweets(username)
        result = {
            "user_info": info,
            "all_tweets": all_tweets["tweets"]
        }
        return render_template('result.html', result=result)
    else:
        return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)

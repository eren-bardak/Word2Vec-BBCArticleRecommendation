# Launch with
#
# python app.py

from flask import Flask, render_template
import sys
import pickle

app = Flask(__name__)


@app.route("/")
def articles():
    """Show a list of article titles"""
    ## YOUR CODE HERE
    host = 'http://127.0.0.1:5000'
    with open('articles.pkl', 'rb') as f:
        articles = pickle.load(f)
        article_titles = [(host + '/article/'+ i[0] + '/' + i[1].split('/')[-1], i[2]) for i in articles]
        return render_template('articles.html', titles=article_titles)

@app.route("/article/<topic>/<filename>")
def article(topic, filename):
    """
    Show an article with relative path filename. Assumes the BBC structure of
    topic/filename.txt so our URLs follow that.
    """
    ## YOUR CODE HERE
    with open('recommended.pkl', 'rb') as file:
        recommended = pickle.load(file)
        with open('articles.pkl', 'rb') as f:
            articles = pickle.load(f)
            for a in articles:
                if a[1].split('/')[-1] == filename and a[0] == topic:
                    return render_template('article.html', title=a[2], text = a[3], recommendations=recommended[topic, filename])

# f = open('articles.pkl', 'rb')
# articles = pickle.load(f)
# f.close()

# f = open('recommended.pkl', 'rb')
# recommended = pickle.load(f)
# f.close()

# you may need more code here or not


# for local debug
if __name__ == '__main__':
    app.run(debug=True)
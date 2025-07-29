from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)



@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    all_posts = requests.get(blog_url).json()
    # print("hello")
    # print(all_posts)
    return render_template("index.html", posts=all_posts)

@app.route('/post/<id>')
def blog_post(id):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    all_posts = requests.get(blog_url).json()
    for post in all_posts:
        print(type(post['id']))
        if post['id'] == int(id):
            title=post['title']
            subtitle=post['subtitle']
            body=post['body']
    print(id)
    return render_template('post.html', title=title, subtitle=subtitle, body=body)

if __name__ == "__main__":
    app.run(debug=True)

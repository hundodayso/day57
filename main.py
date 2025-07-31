from flask import Flask, render_template, url_for
import requests




app = Flask(__name__)

@app.route("/")
def get_all_posts():
    blog_data_ep = "https://api.npoint.io/45c4981c26ffed6e4fad"
    all_posts = requests.get(blog_data_ep).json()
    return render_template("index.html", posts=all_posts)
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.config['EXPLAIN_TEMPLATE_LOADING'] = True
    app.run(debug=True)
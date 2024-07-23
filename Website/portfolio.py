from flask import Flask ,render_template
portfolio=Flask(__name__)
@portfolio.route("/")
def home():
    # return "My Home page!!!!"
    return render_template("portfolio.html")
@portfolio.route('/education')
def education():
    return render_template("education.html")
@portfolio.route('/experience')
def experience():
    return render_template("experience.html")
@portfolio.route('/project')
def project():
    return render_template("project.html")
@portfolio.route('/skills')
def skills():
    return render_template("skills.html")
@portfolio.route('/contact_me')
def contact_me():
    return render_template("contact_me.html")
@portfolio.route('/profile')
def profile():
    return render_template("profile.html")

if __name__=="__main__":
    portfolio.run(debug=True)
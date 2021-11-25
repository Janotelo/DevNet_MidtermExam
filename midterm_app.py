from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route("/")
def loginpage():
    return render_template("login.html")

@app.route("/", methods = ["GET","POST"])
def user_cred():
    reqUserLog = request.form['Username']
    if request.method == "POST":
        return "Hi {0}! You are logged in!".format(reqUserLog)

@app.route("/register", methods = ["GET", "POST"])
def user_register():
    if request.method == "POST":
        return redirect("/")
    return render_template("registration.html")

if __name__== "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
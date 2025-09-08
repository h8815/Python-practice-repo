from flask import Flask, render_template, request

app = Flask(__name__)

# using template folder from the current directory 
@app.route("/")
def index():
    return render_template("index.html", data=[i for i in range(11)])

@app.route("/about")
def about():
    return render_template("about.html", data=[i for i in range(11)])

@app.route("/postdata", methods=["POST"])
def postdata():
    if request.method == "POST":
        first_name = request.form["Firstname"]
        last_name = request.form["Lastname"]
        return f"Thankyou {first_name} {last_name}"
    else:
        print("Something went wrong")
    
    
# using Variable Rules to pass values to the URL
# @app.route("/sum/<int:num1>/<int:num2>")
# def sum(num1, num2):
#     return f"<h1>{num1} + {num2} = {num1+num2}</h1>"

# @app.route("/sum/<name>")
# def name(name):
#     return f"<h1>Hello {name}</h1>"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
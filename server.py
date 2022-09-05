from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/") #decorator
def my_home():
    return render_template("index.html")

@app.route("/<string:filename>.html")
def route(filename):
    return render_template(f"{filename}.html")

def write_to_file(data):
    with open("database.txt", mode="a") as database:
        database.write(f"\n{str(data)}")

def write_to_csv(data):
    with open("database.csv", mode="a", newline="") as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=",", quotechar='"', quoting= csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thanks.html")
        except:
            return "did not save to database"
    else:
        return "nope"
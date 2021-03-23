from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from scrape_mars import scrape 

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def home():
    destination_data = mongo.db.collection.find_one()

    
    return render_template("index.html", mars=destination_data)

@app.route("/scrape")
def scrape_all():
    mars_data = scrape()

    mongo.db.collection.update({}, mars_data, upsert = True)

    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)

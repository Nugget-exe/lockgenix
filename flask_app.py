from flask import Flask, render_template # Import Flask Class
app = Flask(__name__) # Create an Instance

@app.route("/")
def home(): # Run the function
	return render_template("index.html")

@app.route("/Fileless_attacks")
def Fileless_attacks():
  return render_template("Fileless.html")

@app.route("/prevention")
def prevention():
  return render_template("prevention.html")

@app.route("/whattodo")
def whattodo():
  return render_template("whattodo.html")

if  __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True) # Run the Application (in debug mode)
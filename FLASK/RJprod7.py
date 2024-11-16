from flask import Flask, render_template

#route da pagina principal: RJprod7.com/
app = Flask(__name__, template_folder="tamplate")

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

if __name__ == "__main__":
    app.run(debug=True)
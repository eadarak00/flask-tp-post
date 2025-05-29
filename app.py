from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    erreur = None
    if request.method == "POST":
        nom = request.form.get("nom")
        if not nom.strip():
            erreur = "Le nom ne peut pas être vide."
        else:
            return render_template("result.html", nom=nom)
    return render_template("index.html", erreur=erreur)

if __name__ == "__main__":
    app.run(debug=True)

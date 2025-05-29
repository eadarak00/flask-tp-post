from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'  # Clé secrète pour sécuriser les formulaires

class NomForm(FlaskForm):
    nom = StringField("Nom", validators=[DataRequired(message="Le nom est requis.")])
    submit = SubmitField("Envoyer")

@app.route("/", methods=["GET", "POST"])
def index():
    form = NomForm()
    if form.validate_on_submit():
        nom = form.nom.data
        return render_template("result.html", nom=nom)
    return render_template("index.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)

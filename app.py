
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def accueil():
    return render_template("accueil.html")


@app.route("/resumes")
def resumes():
    return render_template("resumes.html")


@app.route("/resume/<int:numero>")
def resume_chapitre(numero):
    if numero < 1 or numero > 5:
        return "Chapitre introuvable", 404

    return render_template("chapitre.html", numero=numero)


@app.route("/quiz")
def quiz():
    return render_template("index.html")
@app.route("/qcm")
def qcm():
    return render_template("qcm.html")

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

from flask import Flask, render_template, request

app = Flask(__name__)

alunos = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form["nome"]
        n1 = float(request.form["n1"])
        n2 = float(request.form["n2"])
        n3 = float(request.form["n3"])

        media = (n1 + n2 + n3) / 3

        if media >= 7:
            status = "Aprovado"
        else:
            status = "Reprovado"

        aluno = {
            "nome": nome,
            "n1": n1,
            "n2": n2,
            "n3": n3,
            "media": round(media, 2),
            "status": status
        }

        alunos.append(aluno)

    return render_template("index.html", alunos=alunos)

if __name__ == "__main__":
    app.run(debug=True)

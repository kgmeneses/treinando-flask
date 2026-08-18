from flask import Flask, render_template, request

app = Flask(__name__)

class Postagem:
    def __init__(self, pessoa, frase):
        self.pessoa = pessoa
        self.frase = frase

postagens = []

@app.route("/", methods=["GET", "POST"])
def inicio():
    if request.method == "POST":
        nome = request.form['nomee']
        frase = request.form['frasee']
        postizinho = Postagem(nome, frase)
        postagens.append(postizinho)

    return render_template("index.html", postagens = postagens)



app.run(debug=True)
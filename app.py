from flask import Flask, render_template

app = Flask ("Meu App")

posts = [ # Banco de Dados MOCKADO (Mock)
    {
        "titulo": "Minha primeira postagem",
        "texto": "teste"
    },
    {
        "titulo": "Segundo Post",
        "texto": "Outro teste"
    }
]

@app.route('/') # rota principal
def exibir_entradas():
    entradas = posts # Mock das postagens
    return render_template ('exibir_entradas.html', entradas=entradas)
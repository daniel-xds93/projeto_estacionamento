from flask import Flask, render_template

# a linha abaixo eu crio a variavel responsavel por rodar meu projeto
app = Flask(__name__)

# a linha abaixo cria uma rota, que será indicada no navegador
@app.route('/ola')
def primeira():
    return "<h1>Iniciando o Flask</h1>"


@app.route('/lista')
def lista():
    listaVeiculos = ['Onix', 'Jetta', 'Civic', 'Gol']
    return render_template('lista.html', tituloPagina = 'Lista de Veículos',
                            carros = listaVeiculos)


app.run(debug=True)
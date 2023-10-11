from flask import Flask, render_template

# a linha abaixo eu crio uma classe
class Veiculo:
        # todos os parametros após o self ,
        # são obrigatorios 
    def __init__(self, placa, modelo, cor, proprietario):
        self.placa = placa
        self.modelo = modelo
        self.cor = cor
        self.proprietario = proprietario



# a linha abaixo eu crio a variavel responsavel por rodar meu projeto
app = Flask(__name__)

# a linha abaixo cria uma rota, que será indicada no navegador
@app.route('/ola')
def primeira():
    return "<h1>Iniciando o Flask</h1>"


@app.route('/lista')
def lista():
    # listaVeiculos = ['Onix', 'Jetta', 'Civic', 'Gol']

    carro01 = Veiculo('ABC-1234', 'Gol', 'Preto', 'Daniel')
    carro02 = Veiculo('DEF-5678', 'Civic', 'Prata', 'Denis')
    carro03 = Veiculo('GHI-9012', 'Golf', "Azul", "José")

    # a linha abaixo adiciona uma lista com os veiculos
    listaVeiculos = [carro01, carro02, carro03]


    return render_template('lista.html', tituloPagina = 'Lista de Veículos',
                            carros = listaVeiculos)


app.run()
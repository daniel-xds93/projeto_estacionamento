from flask import Flask, render_template, request, redirect

# a linha abaixo eu crio uma classe
class Veiculo:
        # todos os parametros após o self ,
        # são obrigatorios 
    def __init__(self, placa, modelo, cor, proprietario):
        self.placa = placa
        self.modelo = modelo
        self.cor = cor
        self.proprietario = proprietario

carro01 = Veiculo('ABC-1234', 'Gol', 'Preto', 'Daniel')
carro02 = Veiculo('DEF-5678', 'Civic', 'Prata', 'Denis')
carro03 = Veiculo('GHI-9012', 'Golf', "Azul", "José")

# a linha abaixo adiciona uma lista com os veiculos
listaVeiculos = [carro01, carro02, carro03]


# a linha abaixo eu crio a variavel responsavel por rodar meu projeto
app = Flask(__name__)

# a linha abaixo cria uma rota, que será indicada no navegador
@app.route('/ola')
def primeira():
    return "<h1>Iniciando o Flask</h1>"


@app.route('/lista')
def lista():
    # listaVeiculos = ['Onix', 'Jetta', 'Civic', 'Gol']

    


    return render_template('lista.html', tituloPagina = 'Lista de Veículos',
                            carros = listaVeiculos)


# a linha abaixo é a rota para abrir uma a tela de cadastro
@app.route('/novo')
def cadastra_novo(): # este método apenas chama o arquivo novo.html
    return render_template('novo.html')

# a rota abaixo é responsavel por cadastrar os dados
@app.route('/criar', methods=['POST',])
def cadastra_informacao():
    # para a proxima etapa é necessario importar o "request"
    placa = request.form['placa']
    modelo = request.form['modelo']
    cor = request.form['cor']
    proprietario = request.form['proprietario']

    # a linha abaixo cria uma variavel usando a classe criada
    carroAdd = Veiculo(placa, modelo, cor, proprietario)

    # a linha abaixo adiciona o veículo digitado pelo usuario 
    # na lista de veiculos
    listaVeiculos.append(carroAdd)

    # a linha abaixo direciona para a tela de lista.html
    #return render_template('lista.html', 
    #                       tituloPagina = 'Lista de Veículos',
    #                        carros = listaVeiculos)

    # a linha abaixo necessita adicionar o redirect
    return redirect('/lista')

app.run()
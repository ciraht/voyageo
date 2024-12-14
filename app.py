from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

USUARIO_CORRETO = "alexmartinscarvalho566@gmail.com"
SENHA_CORRETA = "05fev2007ju@"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        if email == USUARIO_CORRETO and senha == SENHA_CORRETA:
            return redirect('/home')
        else:
            return render_template('index.html', mensagem="Email ou senha inválidos. Tente novamente.")

    return render_template('index.html', mensagem=None)


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        return render_template('cadastro.html',
                               mensagem="A Voyageo não está mais operando. Agradecemos pelo interesse.")

    return render_template('cadastro.html', mensagem=None)


@app.route('/home', methods=['GET', 'POST'])
def pagina_secreta():
    if request.method == 'POST':
        entrada = request.form.get('entrada', '')
        if entrada.lower() == 'maçã':
            resultado = 'banana'
        elif entrada.lower() == 'auol':
            resultado = '@tales_____________'
        elif entrada.lower() == 'socorro':
            resultado = 'isso não vai te ajudar em nada'
        elif entrada.lower() == 'teste':
            resultado = 'eu já testei isso'
        elif entrada.lower() == 'dica':
            resultado = 'simples assim? tenta de outro jeito'
        elif entrada.lower() == 'banana':
            resultado = 'maçã'
        elif entrada.lower() == 'caos':
            resultado = 'energia'
        elif entrada.lower() == 'stephanie':
            resultado = '<3'
        elif entrada.lower() == 'por favor':
            resultado = 'A expressão "por favor" é usada para mostrar delicadeza quando se faz um pedido.'
        elif entrada.lower() == 'rullaluistimet':
            resultado = 'isso ae já foi já, esquece isso'
        elif entrada.lower() == 'oi':
            resultado = 'oi! como vai?'
        elif entrada.lower() == 'bem, e você?':
            resultado = 'bem também!'
        elif entrada.lower() == 'quem é você?':
            resultado = 'alguém'
        elif entrada.lower() == 'enigma':
            resultado = 'quanto tempo será que vcs vão passar nisso? kkkk'
        elif entrada.lower() == 'cu':
            resultado = 'sem palavrões no meu site'
        elif entrada.lower() == 'porra':
            resultado = 'sem palavrões no meu site'
        elif entrada.lower() == 'caralho':
            resultado = 'sem palavrões no meu site'
        elif entrada.lower() == 'buceta':
            resultado = 'sem palavrões no meu site'
        elif entrada.lower() == 'puta':
            resultado = 'sem palavrões no meu site'
        elif entrada.lower() == 'arrombado':
            resultado = 'sem palavrões no meu site'
        elif entrada.lower() == 'ordem':
            resultado = 'e caos'
        elif entrada.lower() == 'jogo':
            resultado = 'eu perdi'
        elif entrada.lower() == 'energia':
            resultado = 'caos'
        elif entrada.lower() == 'eae':
            resultado = 'olá'
        elif entrada.lower() == 'gado':
            resultado = 'sim'
        elif entrada.lower() == 'bom dia':
            resultado = 'bom dia'
        elif entrada.lower() == 'boa tarde':
            resultado = 'boa tarde'
        elif entrada.lower() == 'boa noite':
            resultado = 'boa noite'
        elif entrada.lower() == 'canivete':
            resultado = 'canivete é a chave'
        elif entrada.lower() == 'aibofobia':
            resultado = 'aibofobia'
        elif entrada.lower() == 'palíndromo':
            resultado = 'sator arepo tenet opera rotas'
        elif entrada.lower() == 'sator arepo tenet opera rotas':
            resultado = 'https://website-p6ae.onrender.com'
        elif entrada.lower() == 'eu gosto de batata frita':
            resultado = '...wait! they dont love you like i love you'
        else:
            resultado = None

        return render_template('home.html', resultado=resultado)

    return render_template('home.html', resultado=None)


if __name__ == '__main__':
    app.run(debug=True)

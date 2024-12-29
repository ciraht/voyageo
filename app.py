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
        elif entrada.lower() == 'atil':
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
        elif entrada.lower() in ['obrigado', 'obrigada', 'obg']:
            resultado = 'de nada'
        elif entrada.lower() == 'tchau':
            resultado = 'adeus'
        elif entrada.lower() == 'bom trabalho':
            resultado = 'obrigado!'
        elif entrada.lower() in ['tudo bem', 'como você está']:
            resultado = 'estou bem, e você?'
        elif entrada.lower() == 'que horas são?':
            resultado = 'hora de você me dizer algo interessante'
        elif entrada.lower() == 'nada':
            resultado = 'nada? tem certeza?'
        elif entrada.lower() == 'pq':
            resultado = 'porque sim'
        elif entrada.lower() == 'sim':
            resultado = 'não'
        elif entrada.lower() == 'não':
            resultado = 'sim'
        elif entrada.lower() == 'talvez':
            resultado = 'decida-se!'
        elif entrada.lower() == 'ok':
            resultado = 'ok então'
        elif entrada.lower() == 'ai':
            resultado = 'o que houve?'
        elif entrada.lower() == 'sério?':
            resultado = 'sério'
        elif entrada.lower() == 'claro':
            resultado = 'com certeza!'
        elif entrada.lower() == 'verdade':
            resultado = 'mentira'
        elif entrada.lower() == 'mentira':
            resultado = 'verdade'
        elif entrada.lower() == 'fome':
            resultado = 'vai comer algo!'
        elif entrada.lower() in ['frio', 'calor']:
            resultado = 'o tempo é imprevisível, não?'
        elif entrada.lower() == 'café':
            resultado = 'quero um também'
        elif entrada.lower() == 'chocolate':
            resultado = 'delícia!'
        elif entrada.lower() == 'que legal':
            resultado = 'eu sei'
        elif entrada.lower() == 'zzz':
            resultado = 'está com sono?'
        elif entrada.lower() == 'parabéns':
            resultado = 'obrigado!'
        elif entrada.lower() == 'amigo':
            resultado = 'sim, sou seu amigo'
        elif entrada.lower() == 'internet':
            resultado = 'sempre online'
        elif entrada.lower() in ['gato', 'cachorro']:
            resultado = 'amo animais!'
        elif entrada.lower() == 'poesia':
            resultado = 'a vida é poesia'
        elif entrada.lower() == 'canção':
            resultado = 'o que você gosta de ouvir?'
        elif entrada.lower() == 'bom':
            resultado = 'ótimo!'
        elif entrada.lower() == 'ruim':
            resultado = 'pode melhorar'
        elif entrada.lower() == 'saudade':
            resultado = 'quem nunca?'
        elif entrada.lower() == 'esperança':
            resultado = 'nunca perca!'
        elif entrada.lower() == 'dinheiro':
            resultado = 'quem não quer mais?'
        elif entrada.lower() == 'estudo':
            resultado = 'conhecimento é poder!'
        elif entrada.lower() == 'jantar':
            resultado = 'comida é vida'
        elif entrada.lower() == 'sonho':
            resultado = 'nunca deixe de sonhar'
        elif entrada.lower() == 'medo':
            resultado = 'enfrente-o!'
        elif entrada.lower() in ['alegria', 'tristeza']:
            resultado = 'faz parte da vida'
        elif entrada.lower() == 'você está aí?':
            resultado = 'sempre aqui!'
        elif entrada.lower() == 'certeza':
            resultado = 'tenho certeza absoluta!'
        elif entrada.lower() == 'vida':
            resultado = 'uma jornada fascinante'
        elif entrada.lower() == 'mundo':
            resultado = 'tão grande e misterioso'
        elif entrada.lower() == 'tempo':
            resultado = 'ele voa, não?'
        elif entrada.lower() == 'livro':
            resultado = 'adoro boas histórias'
        elif entrada.lower() == 'vídeo':
            resultado = 'o que você quer assistir?'
        elif entrada.lower() == 'filme':
            resultado = 'me diga um bom título!'
        elif entrada.lower() == 'novidade':
            resultado = 'sempre há algo novo'
        elif entrada.lower() in ['risada', 'risos']:
            resultado = 'kkkkk'
        elif entrada.lower() == 'brincadeira':
            resultado = 'adoro brincar também!'
        else:
            resultado = None

        return render_template('home.html', resultado=resultado)

    return render_template('home.html', resultado=None)


if __name__ == '__main__':
    app.run(debug=True)

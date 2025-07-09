from app import app, db
from flask import render_template, url_for, request, redirect
from app.forms import ContatoForm
from app.models import Contato

@app.route('/')
def homepage():
    usuario = 'Renan'
    idade = 17
    
    context = {
        'usuario':usuario,
        'idade':idade
    }
    return render_template('index.html', context=context)

@app.route('/contato/', methods=['GET','POST'])
def contato():
    form = ContatoForm()
    context={}
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))
    return render_template('contato.html',context=context,form=form)

@app.route('/contato/lista/', methods=['GET','POST'])
def contatoLista():
    if request.method=='GET':
        pesquisa=request.args.get('pesquisa','')

    dados = Contato.query.order_by()
    if pesquisa != '':
        dados = dados.filter_by(nome=pesquisa)
    context={'dados': dados.all()}

    for linha in dados:
        print(linha)
        print(linha.email)
        print(linha.assunto)
        print(linha.respondido)


    return render_template('contato_lista.html',context=context)
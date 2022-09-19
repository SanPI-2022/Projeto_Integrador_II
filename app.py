from flask import Flask, render_template, request, url_for, redirect, session
from flask_sqlalchemy import SQLAlchemy
import os
import sqlite3 as sql
from werkzeug.exceptions import abort


dir_path = os.path.dirname(os.path.realpath(__file__))

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "problemas.db"))

app = Flask(__name__, template_folder='templates')

app.config['SECRET_KEY'] = 'colocar_1_senha'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
db = SQLAlchemy(app)


class Poste(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    codigo = db.Column(db.String(20), nullable=False)
    rua = db.Column(db.String(50), nullable=False)
    bairro = db.Column(db.String(50), nullable=False)
    cidade = db.Column(db.String(300), nullable=False)


class Problema(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    codigo = db.Column(db.String(20), nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.String(14), nullable=False)
    telefone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(300), nullable=False)

    def __init__(self, codigo, nome, cpf, telefone, email, descricao):
        self.codigo = codigo
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.descricao = descricao


def register_user_to_db(username, password):
    con = sql.connect('problemas.db')
    cur = con.cursor()
    cur.execute('INSERT INTO users(username,password) VALUES (?,?)', (username, password))
    con.commit()
    con.close()


def check_user(username, password):
    con = sql.connect('problemas.db')
    cur = con.cursor()
    cur.execute('Select username,password FROM users WHERE username=? and password=?', (username, password))

    result = cur.fetchone()
    if result:
        return True
    else:
        return False


@app.route("/")
def telaa():
    return render_template("telaa.html")


@app.route("/login")
def index():
    return render_template('login.html')


@app.route("/errologin")
def errorlogin():
    return render_template('errologin.html')


@app.route('/register', methods=["POST", "GET"])
def register():
    if 'username' in session:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            register_user_to_db(username, password)
            return redirect(url_for('index'))

        else:
            return render_template('register.html')
    else:
        return render_template('errologin.html')


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(check_user(username, password))

        if check_user(username, password):
            session['username'] = username
            session['password'] = password

            return redirect(url_for('tela_admin')) #tela certa
        else:
            return render_template('errologin.html')


@app.route('/administrativa', methods=['POST', "GET"])
def tela_admin():
    if 'username' in session:
        return render_template('administrativa.html', username=session['username'])
    else:
        return render_template('errologin.html')


@app.route("/cadastraposte")
def tela_cad_poste():
    if 'username' in session:
        return render_template('cadastraposte.html', username=session['username'])
    else:
        return render_template('errologin.html')


@app.route("/cadastraposte", methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        try:
            Codigo = request.form['codigo']
            Rua = request.form['rua']
            Bairro = request.form['bairro']
            Cidade = request.form['cidade']

            with sql.connect("problemas.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO Poste(Codigo, Rua, Bairro, Cidade)"
                            "VALUES(?, ?, ?, ?)", (Codigo, Rua, Bairro, Cidade))

                con.commit()

        except:
            con.rollback()

        finally:
            con.close()
            return render_template("cadastraposte.html")


@app.route("/reclamacoes")
def add():
    if 'username' in session:
        problemas = Problema.query.all()
        return render_template("reclamacoes.html", problemas=problemas)
    else:
        return render_template('errologin.html')


@app.route("/postescadastrados")
def addp():
    if 'username' in session:
        postes = Poste.query.all()
        return render_template("postescadastrados.html", postes=postes)
    else:
        return render_template('errologin.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route("/telab")
def telab():
    posts = Poste.query.all()
    return render_template("telab.html", posts=posts)


def get_post(post_id):
    post = Poste.query.filter_by(id=post_id).first()
    if post is None:
        abort(404)
    return post


@app.route('/telac/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('telac.html', post=post)#prenche o formulario na telac


@app.route('/<id>')
def informa_pelo_id(id):
    if 'username' in session:
        informa = Problema.query.get(id)
        return render_template('reclamacoes.html', informa=informa)
    else:
        return render_template('errologin.html')


@app.route('/<id>')
def mostra_pelo_id(id):
    if 'username' in session:
        mostra = Poste.query.get(id)
        return render_template('postescadastrados.html', mostra=mostra)
    else:
        return render_template('errologin.html')


@app.route('/telad/<int:post_id>', methods=['GET', 'POST'])
def telad(post_id):
    post = get_post(post_id)
    if request.method == 'POST':
        informa = Problema(request.form['codigo'], request.form['nome'], request.form['cpf'], request.form['telefone'], request.form['email'], request.form['descricao'])
        db.session.add(informa)
        db.session.commit()
        return redirect(url_for('telae'))#telae
    return render_template("telad.html", post=post)


@app.route('/telae')
def telae():
    return render_template("telae.html")


@app.route('/telaqrs')
def telaqrs():
    return render_template("telaqrs.html")


@app.route('/visualizareclamacoes/<int:id>', methods=['GET', 'POST'])
def ver(id):
    if 'username' in session:
        informa = Problema.query.get(id)
        if request.method == 'POST':
            informa.codigo = request.form['codigo']
            informa.nome = request.form['nome']
            informa.cpf = request.form['cpf']
            informa.telefone = request.form['telefone']
            informa.email = request.form['email']
            informa.descricao = request.form['descricao']
            db.session.commit()
            return redirect(url_for('telad'))
        return render_template('visualizareclamacoes.html', informa=informa)
    else:
        return render_template('errologin.html')


@app.route('/visualizapostes/<int:id>', methods=['GET', 'POST'])
def verp(id):
    mostra = Poste.query.get(id)
    if request.method == 'POST':
        mostra.codigo = request.form['codigo']
        mostra.rua = request.form['rua']
        mostra.bairro = request.form['bairro']
        mostra.cidade = request.form['cidade']

        db.session.commit()
        return redirect(url_for('cadastraposte'))
    return render_template('visualizapostes.html', mostra=mostra)


@app.route('/apaga/<int:id>', methods=['GET', 'POST'])
def apaga(id):
    if 'username' in session:
        mostra = Poste.query.get(id)
        if request.method == 'POST':
            mostra.codigo = request.form['codigo']
            mostra.rua = request.form['rua']
            mostra.bairro = request.form['bairro']
            mostra.cidade = request.form['cidade']
            db.session.commit()
            return redirect(url_for('cadastraposte'))
        return render_template('apaga.html', mostra=mostra)
    else:
        return render_template('errologin.html')


@app.route('/delete/<int:id>')
def delete(id):
    if 'username' in session:
        mostra = Poste.query.get(id)
        db.session.delete(mostra)
        db.session.commit()
        return redirect(url_for('addp'))
    else:
        return render_template('errologin.html')


if __name__ == '__main__':
    app.run(debug=True)
# db.create_all()

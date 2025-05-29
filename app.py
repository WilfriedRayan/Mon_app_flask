from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'votre_cle_secrete'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['nom'] = request.form['nom']
        session['prenom'] = request.form['prenom']
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/home')
def home():
    nom = session.get('nom')
    prenom = session.get('prenom')
    if not nom or not prenom:
        return redirect(url_for('login'))
    return render_template('home.html', nom=nom, prenom=prenom)

@app.route('/calculatrice', methods=['GET', 'POST'])
def calculatrice():
    if request.method == 'POST':
        session['operation'] = request.form['operation']
        return redirect(url_for('calcul'))
    return render_template('choose_operation.html')

@app.route('/calcul', methods=['GET', 'POST'])
def calcul():
    result = None
    op = session.get('operation')
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                result = num1 / num2 if num2 != 0 else "Erreur : division par zéro"
        except ValueError:
            result = "Entrée invalide"
    return render_template('calculatrice.html', operation=op, result=result)

@app.route('/meteo')
def meteo():
    return "<h2>Fonctionnalité météo à venir</h2>"

if __name__ == '__main__':
    app.run(debug=True)

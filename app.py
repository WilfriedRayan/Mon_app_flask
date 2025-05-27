from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'ma_cle_secrete'  # à modifier en prod

# Page de connexion
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        prenom = request.form['prenom']
        nom = request.form['nom']
        session['user'] = {'prenom': prenom, 'nom': nom}
        return redirect(url_for('home'))
    return render_template('login.html')

# Page d'accueil
@app.route('/home')
def home():
    user = session.get('user')
    if not user:
        return redirect(url_for('login'))
    return render_template('home.html', user=user)

# Page de calculatrice
@app.route('/calculatrice', methods=['GET', 'POST'])
def calculatrice():
    result = None
    if request.method == 'POST':
        try:
            a = float(request.form['a'])
            b = float(request.form['b'])
            op = request.form['operation']
            if op == '+':
                result = a + b
            elif op == '-':
                result = a - b
            elif op == '*':
                result = a * b
            elif op == '/':
                result = a / b if b != 0 else "Erreur : division par zéro"
        except Exception as e:
            result = f"Erreur : {str(e)}"
    return render_template('calculatrice.html', result=result)

# Déconnexion
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

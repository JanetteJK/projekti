from flask import Flask, render_template, request, redirect, url_for
import game_logic

app = Flask(__name__)

@app.route('/')
def etusivu():
    return render_template('index.html')

@app.route('/peli')
def peli():
    pelitila = game_logic.hae_pelitila()

    return render_template('game.html', tila=pelitila)

@app.route('/vastaa', methods=['POST'])
def vastaa():

    vastaus = request.form.get('vastaus', '')

    game_logic.tarkista_vastaus(vastaus)

    return redirect('/peli')

@app.route('/uusi_peli')
def uusi_peli():

    game_logic.aloita_peli()

    return redirect('/peli')



if __name__ == '__main__':

    game_logic.aloita_peli()

    app.run(debug=True)
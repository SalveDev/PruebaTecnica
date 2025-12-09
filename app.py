from flask import Flask, render_template, Blueprint
import pandas as pd
from pathlib import Path

app = Flask(__name__)

@app.route("/alertas")
def alertas():

    # TODO:
    # - cargar data
    # - calcular rotacion
    # - unir con stock
    # - calcular DOI
    # - filtrar <= 7
    # - ordenar
    # - pasar al template

    alertas = []  # lista de dicts o DataFrame convertido a dict

    return render_template("alertas.html", alertas=alertas)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False, use_reloader=True)
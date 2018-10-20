from flask import Flask, render_template
app = Flask(__name__)

@app.route("/iniciarSesion")
def iniciarSesion():
    return render_template("login.html", title="iniciarSesion")


@app.route("/crearCuenta")
def crearCuenta():
    return render_template("crearCuenta.html", title="crearCuenta")
if __name__=="__main__":
    app.run(debug=True)

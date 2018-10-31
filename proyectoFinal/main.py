from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)
import ast
def actualizarDatos():
    listaUsuarios=[]
    archivo=open("baseDeDatos.txt","r")
    if archivo.readline()=="":
        listaUsuarios=[]
    else:
        with open("baseDeDatos.txt","r")as f:
                listaUsuarios=ast.literal_eval(f.read())

    return listaUsuarios

@app.route("/iniciarSesion", methods=["GET","POST"])
def iniciarSesion():
    if request.method == "POST":
        listaUsuarios=actualizarDatos()
        ID=request.form["iniciarSesion"]
        contraseña=request.form["contraseña"]
        contador=0
        while contador<len(listaUsuarios):
            print(listaUsuarios[contador]["ID"])
            print(listaUsuarios[contador]["contraseña"])
            print(ID)
            print(contraseña)
            if listaUsuarios[contador]["ID"]==ID and listaUsuarios[contador]["contraseña"]==contraseña:
                print("hi")
                return redirect(url_for("paginaPrincipal"))
            else:
                flash("nombre de usuario o contraseña incorrectos")
                return redirect(url_for("iniciarSesion"))
            contador+=1
            
    
    return render_template("login.html", title="iniciarSesion")

@app.route("/crearCuenta", methods=["GET","POST"])
def crearCuenta():

    
    if request.method == "POST":
        listaUsuarios=actualizarDatos()
        ID=request.form["nombreUsuario"]
        contraseña=request.form["contraseña"]
        preferencias=request.form["preferencias"]
        usuario={"ID":ID,"contraseña":contraseña,"preferencias":preferencias}            
        contador=0
        n=False
        while contador<len(listaUsuarios):
            if listaUsuarios[contador]["ID"]==ID:
                flash=("el nombre de usuario ya esta en uso")
                n=True
                return redirect(url_for("crearCuenta"))
                break
            contador+=1
        if n==False:
            listaUsuarios.append(usuario)
            archivo=open("baseDeDatos.txt", mode="w")
            archivo.write(str(listaUsuarios))
            archivo.close()
            return redirect(url_for("paginaPrincipal"))
        
        
    return render_template("crearCuenta.html", title="crearCuenta")

@app.route("/", methods=["GET","POST"])
def paginaPrincipal():
                                
    return render_template("paginaPrincipal.html", title="paginaPrincipal")
    
if __name__=="__main__":
    app.secret_key = 'holaMundoCruel'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)

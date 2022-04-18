from flask import Flask, request, render_template, redirect, url_for, json, jsonify
import requests
import data.InfoBasic

import json

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("createUsers.html")


@app.route("/create", methods=["POST"])
def create():
    identificacion = request.form["identificacion"]
    nombre = request.form["Usuario"]
    celular = request.form["Celular"]
    email = request.form["Email"]
    genero = request.form["selector_genero"]
    status = "active"

    datas = data.InfoBasic.dataRequest(identificacion, nombre, email, genero, status)
    json_data = json.dumps(datas.__dict__)

    # print(data.InfoBasic.info().base_uri)
    # print(json_data)
    response = requests.post(data.InfoBasic.info().base_uri + data.InfoBasic.info().endpoint, data=json_data,
                             headers=data.InfoBasic.info().headers)
    if response.status_code == 201 or response.status_code == 200:
        return "El usuario se ha creado"
    else:
        return "ocurrio un error"


@app.route("/users")
def get():
    response = requests.get(data.InfoBasic.info().base_uri + data.InfoBasic.info().endpoint,
                            headers=data.InfoBasic.info().headers).json()

    return render_template('users.html', title='Users',
                           users=response)


@app.route("/update")
def update():
    print(request.args)
    #response_get = requests.get(data.InfoBasic.info().base_uri + data.InfoBasic.info().endpoint + "/" + id,
    #                            headers=data.InfoBasic.info().headers)
    #print(response_get.text)

    #response = requests.put(data.InfoBasic.info().base_uri + data.InfoBasic.info().endpoint + "/" + id,
    #                        headers=data.InfoBasic.info().headers)

    # datas = data.InfoBasic.dataRequest(identificacion, nombre, email, genero, status)
    return ""


@app.route("/delete/<id>")
def delete(id):
    response = requests.delete(data.InfoBasic.info().base_uri + data.InfoBasic.info().endpoint + "/" + id,
                               headers=data.InfoBasic.info().headers)
    print(response)
    if response.status_code == 204:
        return redirect("/users")
    else:
        return "Ocurrio un error al eliminar"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3800)

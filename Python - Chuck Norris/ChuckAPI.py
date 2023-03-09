from flask import Flask, json, make_response
import Chuck;

app = Flask(__name__)

@app.route('/api/piada')
def getPiada():
    textoDaPiada = Chuck.GetPiada()
    piadaObjetoJson = {'piada':f'{textoDaPiada}'}
    piadaSerializada=json.dumps(piadaObjetoJson, ensure_ascii=False).encode('utf8')
    response=make_response(piadaSerializada)
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response

if __name__ == '__main__':
    app.run(debug=True)


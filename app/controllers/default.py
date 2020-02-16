from app import app

@app.route('/')
def index():
    return '<html><form><label for="teste">Nome: <input type="text" name="teste" id="teste"/></form></html>'
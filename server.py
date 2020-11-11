'''
flask es un framework. más complejo que un modulo, ya que un framework es casi un lenguaje nuevo
flask es más sencillo, django es más complejo, posee más reglas

terminal:
creamos el enviroment python3 -m venv venv(puede reemplazarse por la carpeta donde tenemos todos nuestros archivos)
y activamos . web_server(nombrecarpeta)/bin/activate
export FLASK_APP=hello.py
flask run

debug mode:
export FLASK_ENV = development
'''



'''
static files --> archivos que nunca cambiarán (css, js) carpeta "static"
'''

'''
template language = {{}} (en html) --> significa que hay una expresión en python. lenguaje jinja.
parámetros url --> en rout(/<variable>)
'''

'''
MIME TYPE (una vez que abramos la consola y pongamos "network" nos aparece los tipos de datos que se encuentran)
Multipurpose Internet Mail extension
'''

#render_template --> devuelve html HAY QUE TENER CARPETA templates
from flask import Flask, render_template

app = Flask(__name__)
print(__name__) #main file que se cargará




@app.route('/')
def home():
    return render_template('index.html')


#DINAMICO Y EVITAMOS COPIAR EL CÓDIGO MUCHAS VECES
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)





'''
@app.route('/<username>/<int:age>') #decorator. entregamos como parametros un username y un entero
def hello_world(username = None, age = 18): #por default
    if age >= 18:
        return render_template('./index.html', name = username, edad = age)
    else:
        return 'El sitio es apto solo para mayores de 18 años'
'''


'''
FORMULARIO: OBTENER INFORMACIÓN INGRESADA EN HTML.

en HTML buscamos forms --> action = /submit_form (concordar con la ruta que le hemos dado abajo). le asignamos la ruta
method= post get. en este caso para enviar información, es post.

capturamos la data a traves del email.

redirect = redirige a una pagina
'''

from flask import request, redirect
import csv

'''
guardaremos todo en un txt (email, subject y message)
'''
def write_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write('/n' + email + subject + message)


#para escribir en csv
def write_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writter = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, newline='') #damos formatos al csv.deliminter = qué separa a los valores
        csv_writter.writerow([email,subject,message]) #escribimos las filas


    

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    #obtenemos la información desde los name del form. request.method()
    if request.method == 'POST':
        #obtenemos por diccionario
        data = request.form.to_dict()
        write_csv(data)
        return redirect('/thank_you.html')
    else:
        return 'algo salió mal'
    

    
    '''
    pythonanywhere.com --> nos permite tener python 

    '''
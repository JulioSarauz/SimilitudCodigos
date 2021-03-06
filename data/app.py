from flask import Flask, render_template, request
import procesos 
from werkzeug.utils import secure_filename
import os

app = Flask (__name__, template_folder='template') 
app.config['UPLOAD_FOLDER'] = "data"
nombre = "SIMILITUD DE CODIGOS"
detalle = "Para los programadores que a menudo escriben código y cambian el código, si el código escrito antes necesita cambiarse después de mucho tiempo, es bastante difícil encontrar la diferencia."



#INICIO DE LA PAGINA WEB
@app.route ('/', methods=['GET','POST']) 
def home (): 
   contenido = procesos.buscarArchivos()
   return render_template ('index.html',nombre=nombre, detalle=detalle,contenido=contenido) 

@app.route ('/prueba', methods=['GET','POST']) 
def prueba(): 
   contenido = procesos.buscarArchivos()
   nombres = request.args['nombres']
   coseno = procesos.comparar(nombres)
   return render_template ('index.html',nombre=nombre, detalle=detalle,contenido=contenido, coseno=coseno) 


@app.route('/upload', methods=['POST'])
def uploadFile():
    if request.method == "POST":
        contenido = procesos.buscarArchivos()
        f = request.files['archivoRecibido']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        return render_template ('index.html',nombre=nombre, detalle=detalle,contenido=contenido) 

if __name__=="__main__":
    app.run(debug=True)
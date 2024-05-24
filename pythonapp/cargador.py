# Importamos "render_template"
import os
import errno
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

# Creamos la instancia de Flask y adjuntamos el nombre raiz de la carpeta de las vistas
app = Flask(__name__,template_folder='templates')

# valida si existe la carpeta si no la crea
try:
    os.mkdir('archivosdbf')
except OSError as e:
    if e.errno != errno.EEXIST:
        os.mkdir('archivosdbf')
        raise

# Carpeta de subida
app.config['UPLOAD_FOLDER'] = './archivosdbf'

# Definemos el route
@app.route("/")
# Un segundo route con el nombre del parametro
@app.route('/<nombre>')
def render(nombre=None): #Inicializamos "nombre"
 # Retornamos la plantilla "index.html"
 # y tambien Le pasamo el parametro a el método render_template
 return render_template("view.html", nombre=nombre)



@app.route("/upload_studioa", methods=['POST'])
def uploader():
 if request.method == 'POST':
  # obtenemos el archivo del input "archivo"
  f = request.files['fileavg']
  filename = secure_filename(f.filename)
  # Guardamos el archivo en el directorio "Archivos PDF"
  f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
  # Retornamos una respuesta satisfactoria
  #return "<h1>Archivo subido exitosamente</h1>"
  # retornas una vista de nuevo del mismo pero tambien un mensaje por url de archivosubido
  return render_template("view.html", nombre='archivosubido')

# Iniciamos la aplicación
if __name__ == '__main__':
    app.run(debug=True)

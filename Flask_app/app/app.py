from flask import Flask, render_template, request
app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello',methods=['POST'])
def sesion():
    """
    nombres=['Jossein','Paolo','Abel','Carlos']
    nombre=request.form.get("nombre")
    verify=False
    for a in nombres:
        if a==nombre:
            verify=True    
    if not verify:
        pyautogui.alert(text="Tu nombre no esta registrado, intenta nuevamente",title="OH, NO!",button="ok") 
    """
    nombre=request.form.get("nombre")
    return render_template('sesion.html',nombre=nombre)
    
@app.route('/formulario',methods=['POST'])
def formulario():
    nombre=request.form.get("firstname")
    apellido=request.form.get("lastname")
    telefono=request.form.get("telefono")
    pais=request.form.get("country")
    gmail=request.form.get("gmail")
    formacion=[request.form.get("grado1"),request.form.get("grado2")]
    idiomas=[request.form.get("idiomas1"),request.form.get("idiomas2"),request.form.get("idiomas3")]
    habilidades=[request.form.get("habilidades1"),request.form.get("habilidades2"),request.form.get("habilidades3"),request.form.get("habilidades4")]
    aptitudes=[request.form.get("aptitudes1"),request.form.get("aptitudes2"),request.form.get("aptitudes3"),request.form.get("aptitudes4"),request.form.get("aptitudes5")]
    experiencia=[request.form.get("experiencia1"),request.form.get("experiencia2"),request.form.get("experiencia1")]
    descripcion=request.form.get("descripcion")
    
    return render_template('form.html',nombre=nombre,apellido=apellido,telefono=telefono,pais=pais,gmail=gmail,formacion=formacion,idiomas=idiomas,habilidades=habilidades,aptitudes=aptitudes,experiencia=experiencia,descripcion=descripcion)

if __name__=='__main__':
    app.run(debug=True)

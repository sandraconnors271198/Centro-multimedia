from flask import Flask, render_template,send_file,request,url_for
import datetime
import cv2
import pywhatkit as rep
import numpy as np
import os
import sys
import shutil

server = Flask(__name__)

def createNewConnection(name, SSID, password):
    config = """<?xml version=\"1.0\"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>"""+name+"""</name>
    <SSIDConfig>
        <SSID>
            <name>"""+SSID+"""</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>"""+password+"""</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>"""
    command = "netsh wlan add profile filename=\""+name+".xml\""+" interface=Wi-Fi"
    with open(name+".xml", 'w') as file:
        file.write(config)
    os.system(command)
 
# function to connect to a network   
def connect(name, SSID):
    command = "netsh wlan connect name=\""+name+"\" ssid=\""+SSID+"\" interface=Wi-Fi"
    os.system(command)

def html(content):  # Also allows you to set your own <head></head> etc
   return '<!doctype html><html><head><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous"><title>{% block title %}{% endblock %}</title></head><body style="background-color:#e19cd3;"><nav class="navbar navbar-expand-lg navbar-light bg-light"><a class="navbar-brand" href="#">Lumière</a><button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button><div class="collapse navbar-collapse" id="navbarNav"><ul class="navbar-nav"><li class="nav-item active"><a class="nav-link" href="/">Home <span class="sr-only">(current)</span></a></li><li class="nav-item"><a class="nav-link" href="'+chr(92)+'red">Red</a></li><li class="nav-item"><a class="nav-link" href="'+chr(92)+'funcionalidades">Funcionalidades</a></li><li class="nav-item"><a class="nav-link" href="'+chr(92)+'tutorial">Tutorial</a></li><li class="nav-item"><a class="nav-link" href="'+chr(92)+'recom">Recomendaciones</a></li><li class="nav-item"><a class="nav-link" href="'+chr(92)+'\cuenta">Cuenta</a></li></ul></div></nav> <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script> <center>' + content + '</center></body></html>'

@server.route('/')
def home():
   today = datetime.datetime.now()
   print("Bienvenido al servidor. Fecha actual: "+str(today))
   return render_template('index.html')

@server.route('/tutorial')
def tuto():
   today = datetime.datetime.now()
   print("Bienvenido al servidor. Fecha actual: "+str(today))
   return render_template('tutorial.html')

@server.route('/recom')
def recom():
   today = datetime.datetime.now()
   print("Bienvenido al servidor. Fecha actual: "+str(today))
   return render_template('recomendaciones.html')

@server.route('/you')
def you():
   today = datetime.datetime.now()
   print("Bienvenido al servidor. Fecha actual: "+str(today))
   return render_template('youtube.html')

@server.route('/yo_robot')
def yo_robot():
	return send_file('static\libros\Yo, robot - Isaac Asimov.pdf')

@server.route('/quijote')
def quijote():
	return send_file('static\libros\donquijote.pdf')

@server.route('/diablo')
def diablo():
	return send_file('static\libros\El diablo de los numeros - Hans Magnus Enzensberger.pdf')

@server.route('/miserables')
def miserables():
	return send_file('static\libros\Víctor Hugo - Los miserables.pdf')

@server.route('/lenguas')
def lenguas():
	return send_file('static\libros'+chr(92)+'1 Veinte mil leguas de viaje submarino autor Julio Verne.pdf')

@server.route('/viaje')
def viaje():
	return send_file('static\libros'+chr(92)+'2 Viaje al centro de la Tierra autor Julio Verne.pdf')

@server.route('/luna')
def luna():
	return send_file('static\libros'+chr(92)+'5 De la Tierra a la Luna autor Julio Verne.pdf')

@server.route('/fe')
def fe():
	return send_file('static\libros'+chr(92)+'Fe y Razón.pdf')

@server.route('/antro')
def antro():
	return send_file('static\libros'+chr(92)+'Antropologia-Teologica-Juan-Luis-Lorda.pdf')

@server.route('/pneu')
def pneu():
	return send_file('static\libros'+chr(92)+'Pneumatología.pdf')

@server.route('/pneum')
def pneum():
	return send_file('static\libros'+chr(92)+'pmeu.pdf')

@server.route('/bibli')
def bibli():
	return send_file('static\libros'+chr(92)+'Teología Bíblica.pdf')

@server.route('/sein')
def sein():
	return send_file('static\libros'+chr(92)+'sein_und_zeit.pdf')

@server.route('/ser')
def ser():
	return send_file('static\libros'+chr(92)+'ser y nada.pdf')

@server.route('/critica')
def critica():
	return send_file('static\libros'+chr(92)+'critica.pdf')

@server.route('/bana')
def bana():
	return send_file('static\libros'+chr(92)+'eichmann.pdf')

@server.route('/red')
def red():
   today = datetime.datetime.now()
   print("Bienvenido al servidor. Fecha actual: "+str(today))
   return render_template('red.html')

@server.route('/camara')
def camara():
	return render_template('camara.html')

@server.route('/busc_youtube',methods=['GET'])
def busc_youtube():
	video = request.args.get('nom')
	rep.playonyt(video)
	output="El video " +video +" está siendo reproducido."
	return html('<div class="message"><p> '+output+' </p><i class="message-close-btn">&times;</i></div>')

@server.route('/libros_desc')
def libros_desc():
	return render_template('libros.html')

@server.route('/tomar_fotos',methods=['GET'])
def tomar_fotos():
	url = request.args.get('url')
	cap = cv2.VideoCapture(0)
	direc=os.getcwd()+chr(92)+"static"+chr(92)+"imagenes"
	filtro = np.ones((5,5),np.float32)/25
	# Trabajamos frame a frame
	while(cap.isOpened()):
		ret, frame = cap.read()   
		cv2.imshow('frame',frame)
		time=0
		for i in range(10000):
			time=time+1
		if(time==10000):
			print('Guardando la foto')
			cv2.imwrite('img.png',frame)
			img_to_yuv = cv2.cvtColor(frame,cv2.COLOR_BGR2YUV)
			img_to_yuv[:,:,0] = cv2.equalizeHist(img_to_yuv[:,:,0])
			hist_equalization_result = cv2.cvtColor(img_to_yuv, cv2.COLOR_YUV2BGR)
			dst = cv2.filter2D(hist_equalization_result,-1,filtro)
			cv2.imwrite('ecualizada.png',hist_equalization_result)
			cv2.imwrite('suavizada.png',dst)
			gray_image = cv2.cvtColor(hist_equalization_result, cv2.COLOR_BGR2GRAY) 
			cv2.imwrite('foto_old.png',gray_image)
			
			shutil.copy('foto_old.png', direc+chr(92)+"foto_old.png")
			shutil.copy('ecualizada.png', direc+chr(92)+'ecualizada.png')
			shutil.copy('suavizada.png', direc+chr(92)+'suavizada.png')
			shutil.copy('img.png', direc+chr(92)+'img.png')


			cap.release()
			cv2.destroyAllWindows()
	return render_template('fotos.html')

@server.route('/b_n')
def b_n():
   return send_file('foto_old.png', as_attachment=True)

@server.route('/suav')
def suav():
   return send_file('suavizada.png', as_attachment=True)

@server.route('/norm')
def norm():
   return send_file('img.png', as_attachment=True)

@server.route('/contr')
def contr():
   return send_file('ecualizada.png', as_attachment=True)

@server.route('/conect',methods=['GET'])
def conect():
	name = request.args.get('nom_red')
	password = request.args.get('contra_red')
	createNewConnection(name, name, password)
	connect(name, name)

	output="Ya se ha hecho la conexión con "+name+ "cuyo password introducido fue "+password+". Si aún no te has podido conectar verifica nuevamente tu contraseña. "
	return html('<div class="message"><p> '+output+' </p><i class="message-close-btn">&times;</i></div>')

@server.route('/funcionalidades')
def funcionali():
   today = datetime.datetime.now()
   print("Bienvenido al servidor. Fecha actual: "+str(today))
   return render_template('funcionalidades.html')

@server.route('/cuenta')
def cuenta():
   today = datetime.datetime.now()
   print("Bienvenido al servidor. Fecha actual: "+str(today))
   return render_template('cuenta.html')

if __name__ == '__main__':
   server.run(debug=True)
  
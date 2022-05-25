#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## #############################################################
# usb_access.py
#
# Authors: Sandra Susana Pérez Gutiérrez
#	   Brandon Silva Barrera
#	   Javier Adán Troncoso Moreno
# Licence: MIT
# Date:    2022.04.03
# 

# Functions to play the multimedia of an USB memory. 
#
# ## #############################################################

import os
import time
import tkinter
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import vlc
import ctypes
import math

x11 = ctypes.cdll.LoadLibrary('libX11.so')
x11.XInitThreads()
"""
def play_music(path_usb):
	usb_files = get_files_name(path_usb)
	for arch in usb_files:
		if (arch[-4:]=='.mp3'):
			try:
				media = vlc.MediaPlayer(path_usb + "/" + arch)
				media.play()
				time.sleep(0.1)
				duration = player.get_length()
				time.sleep(duration)
			except:
				raise RuntimeError('Failed to play the music')

def play_videos(vid_mod_presentation, path_usb):
	for arch in files_usb:
		if (arch[-4:]=='.mp4') or (arch[-5:]=='.mpeg') or (arch[-4]=='.3gp'):
			try:
				#instancia = vlc.Instance()
				#reproductor = instancia.media_player_new()
				#multimedia = instancia.media_new(ruta + "/" + archivo)
				#reproductor.set_media(multimedia)
				#reproductor.play()
				#Se mantiene la reproducción del video
				#while reproductor.get_state() != vlc.State.Ended:
				#	time.sleep(1)
				media=vlc.MediaPlayer(path_usb + "/" + arch)
				media.play()
				while media.get_state() != vlc.State.Ended:
					time.sleep(1)
			except:
				raise RuntimeError('Failed to play the videos')

def show_photos(path_usb):
	for arch in files_usb:
		if (arch[-4:]=='.png'): #or (archivo[-4:]=='.jpg'):
			try:
				media = vlc.MediaPlayer(path_usb + "/" + arch)
				media.play()
			except:
				raise RuntimeError('Failed to show the photos')

def get_files_name(path_usb):
	#Se revisa el contenido de la memoria
	try:
		#Se espera una sola memoria USB conectada a un puerto
		#Se obtienen los nombres sólo de los archivos
		names_usb_files = [arch for arch in os.listdir(path_usb) if os.path.isfile(os.path.join(path_usb, arch))]
		usb_conected = True
	except FileNotFoundError:
		raise RuntimeError('Failed to open USB and know its files')
	except:
		raise RuntimeError('Failed to open USB')
	
	return names_usb_files

#Según el contenido de la memoria se activa determinado funcionamiento del centro multimedia
		 
"""
def play(player, root, button):
	player.play()
	button.destroy()
	button_pause = tkinter.Button(root, text = "Pausar", width = 30, command = lambda: pause(player, root, button_pause))
	button_pause.pack()
	
def pause(player, root, button):
	player.pause()
	button.destroy()
	button_play = tkinter.Button(root, text = "Reproducir", width = 30, command = lambda: play(player, root, button_play))
	button_play.pack()
	
def stop(player, root, path_usb):
	player.stop()
	relaunch(root, path_usb)

def play_multimedia(path_multimedia, root, path_usb):
	root.destroy()
	playing = tkinter.Tk()
	playing.title("Reproduciendo " + path_multimedia)
	playing.geometry("500x100")
	
	try:
		player = vlc.MediaPlayer(path_multimedia)
		player.play()
		"""
		label_playing = tkinter.Label(root, text = "Reproduciendo " + path_multimedias)
		label_playing.pack()
		"""
		button_stop = tkinter.Button(playing, text = "Escoger otro archivo", width = 30, command = lambda: stop(player, playing, path_usb))
		button_stop.pack()
		
		button_pause = tkinter.Button(playing, text = "Pausar", width = 30, command = lambda: pause(player, playing, button_pause))
		button_pause.pack()
		
		
		if player.get_state() == vlc.State.Ended:
			button_end = tkinter.Button(playing, text = "Escoger otro archivo", width = 30, command = lambda: relaunch(playing, path_multimedia))
	except: 
		label_error = tkinter.Label(root, text = "Error al reproducir el video, intente nuevamente por favor.")
		label_error.pack()
		raise RuntimeError('Fallo al reproducir multimedia')

def play_music(path_usb, root):
	files = get_files_name(path_usb)
	audio_files = []
	for arch in files:
		if arch[-4:] == ".mp3":
			audio_files.append(arch)
			
	for audio in audio_files:
		play_multimedia(path_usb + audio)
	"""	
	label_playing = tkinter.Label(root, text = "Iniciando reproducción")
	label_playing.pack()
				
	for audio in audio_files:
		try:
			player = vlc.MediaPlayer(path_usb + audio)
			#playing.protocol("WM_DELETE_WINDOW", stop(player, playing))
				
			player.play()
			time.sleep(5)
			time.sleep((player.get_length()/1000)-4)
			#duration = player.get_length()
			#time.sleep(duration/1000)
			player.stop()
			#duration = player.get_length()
			
			#while player.is_playing():
			#	time.sleep(duration)
		except:
			continue
	if n > 1:
		button_stop = tkinter.Button(playing, text = "Volver al menú anterior", width = 30, command = lambda: stop(player, root))
		button_stop.pack()
			#button_stop.destroy()
		
		
		button_pause = tkinter.Button(playing, text = "Pausar", width = 30, command = lambda: pause(player, root, button_pause))
		button_pause.pack()
		
		label_playing.configure(text = "Reproduciendo " + audio)
			

def play_videos(path_usb, root):
	label_select = tkinter.Label(root, text = "No se ha seleccionado un video")
	label_select.pack()
	path_video = filedialog.askopenfilename(filetypes = [
		("all video format", ".mp4"),
		("all video format", ".avi")])
		
	if len(path_video) > 0:
		label_select.configure(text = path_video)
		if (path_video[-4:] == ".mp4") or (path_video[-4] == ".avi"):
			try:
				player = vlc.MediaPlayer(path_video)
				player.play()	 
			except:
				label_video = tkinter.Label(root, text = "Error al reproducir el video, intente nuevamente por favor.")
				label_video.pack()
		"""
def play_video(path_video, root):
	root.destroy()
	playing = tkinter.Tk()
	playing.title("Reproduciendo " + path_multimedia)
	playing.geometry("500x100")
	
	try:
		player = vlc.MediaPlayer(path_multimedia)
		player.play()
	except:
		pass

def show_image(path_image, root, path_usb):
	size_max_width = 750
	size_max_height = 500
	root.destroy()
	window = tkinter.Tk()
	window.attributes("-zoomed", True)
	window.title("Mostrando imagen " + path_image)
	image_unprepared = Image.open(path_image)
	size = image_unprepared.size
	if size[0] > size_max_width:
		image_unprepared = image_unprepared.resize((size_max_width, math.floor((size_max_width/size[0])*size[1])))
		size = image_unprepared.size
	if size[1] > size_max_height:
		image_unprepared = image_unprepared.resize((math.floor((size_max_height/size[1])*size[0]), size_max_height))
	window.image_unprepared = ImageTk.PhotoImage(image_unprepared)
	image_prepared = tkinter.Label(window, image = window.image_unprepared)
	image_prepared.pack()
	button_stop = tkinter.Button(window, text = "Escoger otro archivo", width = 30, command = lambda: relaunch(window, path_usb))
	button_stop.pack()
	window.mainloop()

#Global variable 
index = None


def change_index(window, image_duration ,len_list, image_prepared, path_usb, image_files):
	global index
	if index >= len_list - 1:
		index = 0
	else:
		index = index + 1
		#print(index)
	path_image = path_usb + image_files[index]
	size_max_width = 750
	size_max_height = 750
	image_unprepared = Image.open(path_image)
	size = image_unprepared.size
	if size[0] > size_max_width:
		image_unprepared = image_unprepared.resize((size_max_width, math.floor((size_max_width/size[0])*size[1])))
		size = image_unprepared.size
	if size[1] > size_max_height:
		image_unprepared = image_unprepared.resize((math.floor((size_max_height/size[1])*size[0]), size_max_height))
	window.image_unprepared = ImageTk.PhotoImage(image_unprepared)
	image_prepared.config(image = window.image_unprepared)
	window.after(image_duration*1000, change_index, window, image_duration, len(image_files), image_prepared, path_usb, image_files)

def show_images(path_usb, root):
	global index
	index = 0
	image_duration = 1
	root.destroy()
	#aux_window = tkinter.Tk() #To adapt to parameters of show_image
	files = get_files_name(path_usb)
	image_files = []
	# Save the names of images in a list
	for image in files:
		if (image[-4:] == ".png") or (image[-4:] == ".jpg") or (image[-5:] == ".jpeg"):
			image_files.append(image)
			
	#Show all the images in certain time interval
	path_image = path_usb + image_files[index]
	size_max_width = 750
	size_max_height = 750
	window = tkinter.Tk()
	window.attributes("-zoomed", True)
	window.title("Mostrando imágenes ")
	image_unprepared = Image.open(path_image)
	size = image_unprepared.size
	if size[0] > size_max_width:
		image_unprepared = image_unprepared.resize((size_max_width, math.floor((size_max_width/size[0])*size[1])))
		size = image_unprepared.size
	if size[1] > size_max_height:
		image_unprepared = image_unprepared.resize((math.floor((size_max_height/size[1])*size[0]), size_max_height))
	window.image_unprepared = ImageTk.PhotoImage(image_unprepared)
	image_prepared = tkinter.Label(window, image = window.image_unprepared)
	image_prepared.pack()
	window.after(image_duration*1000, change_index, window, image_duration, len(image_files), image_prepared, path_usb, image_files)
	window.mainloop()
	
	
def choose_multimedia(path_usb, root):
	label_select = tkinter.Label(root, text = "No se ha seleccionado un archivo multimedia")
	label_select.pack()
	path_multimedia = filedialog.askopenfilename(initialdir = path_usb, filetypes = [
		("image", ".jpg"),
		("image", ".jpeg"),
		("image", ".png"),
		("all video format", ".mp4"),
		("all video format", ".avi"),
		("audio files", ".mp3")])
	
	if len(path_multimedia) > 0:
		label_select.configure(text = path_multimedia)
		if (path_multimedia[-4:] == ".mp4") or (path_multimedia[-4] == ".avi"):
			play_multimedia(path_multimedia, root, path_usb)
		elif (path_multimedia[-4:] == ".jpg") or (path_multimedia[-5] == ".jpeg") or (path_multimedia[-4:] == ".png"):
			show_image(path_multimedia, root, path_usb)
		elif (path_multimedia[-4:] == ".mp3") or (path_multimedia[-4] == ".avi"):
			play_multimedia(path_multimedia, root, path_usb)
	else:
		label_select.configure(text = "No se ha seleccionado un archivo multimedia")
	
def get_USBs_name():
	#Se revisan las memorias USB conectadas
	try:
		names_usb_files = os.listdir("/media/centro_multimedia/")
	except FileNotFoundError:
		raise RuntimeError('Failed to open USB and know its files')
	except:
		raise RuntimeError('Failed to open USB')
	
	return names_usb_files

def get_files_name(path_usb):
	#Se revisa el contenido de la memoria
	try:
		#Se obtienen los nombres sólo de los archivos
		names_usb_files = [arch for arch in os.listdir(path_usb) if os.path.isfile(os.path.join(path_usb, arch))]
	except FileNotFoundError:
		raise RuntimeError('Failed to open USB and know its files')
	except:
		raise RuntimeError('Failed to open USB')
	
	return names_usb_files
	
def identify_files_type(names_usb_files):
	is_music, is_video, is_photo = False, False, False 
	for arch in names_usb_files:
		if arch[-4:]=='.mp3':
			is_music = True
		if (arch[-4:]=='.mp4') or (arch[-4:]=='.avi'):
			is_video = True
		if (arch[-4:]=='.png') or (arch[-4:]=='.jpg'):
			is_photo = True
		if (is_music == True) and (is_video == True) and (is_photo == True):
			break
	flags = [is_music, is_video, is_photo]
	return flags

def play_mode(path_usb):
	names_usb_files = get_files_name(path_usb)
	flags_files_type = identify_files_type(names_usb_files) #[is_music, is_video, is_photo]
	if (flags_files_type[0]==False) and (flags_files_type[1]==False) and (flags_files_type[2]==False):
		return "no_media_in_usb"#no_media_in_usb()
	elif (flags_files_type[0]==True) and (flags_files_type[1]==False) and (flags_files_type[2]==False):
		return "music"
	elif (flags_files_type[0]==False) and (flags_files_type[1]==True) and (flags_files_type[2]==False):
		return "video"
	elif (flags_files_type[0]==False) and (flags_files_type[1]==False) and (flags_files_type[2]==True):
		return "photo"
	else:
		return "multimedia"
	
def interface_usb(path_usb, usb_connected):
	root = tkinter.Tk()
	root.geometry("500x200")
	root.title("Reproductor multimedia")
	if usb_connected==True:
		label_root = tkinter.Label(root, text = "Memoria USB conectada")
		label_root.pack()
		action = play_mode(path_usb)
	else:
		label_root = tkinter.Label(root, text = "No se ha detectado una memoria USB conectada")
		label_root.pack()
	#Check type of files and execute the correct function	
	if action == "multimedia":
		button1 = tkinter.Button(root, text = "Elegir archivo", width = 30, command = lambda: choose_multimedia(path_usb, root))
		button1.pack()
	elif action == "music":
		#label1 = tkinter.Label(root, text = "Sólo se encontró audio")
		#label1.pack()
		button1 = tkinter.Button(root, text = "Reproducir audios en bucle infinito", width = 30, command = lambda: play_music(path_usb, root))
		button1.pack()
	elif action == "video":
		label1 = tkinter.Label(root, text = "Reproduciendo video")
		label1.pack()
		play_videos()
	elif action == "photo":
		label1 = tkinter.Label(root, text = "Reproduciendo imágenes")
		label1.pack()
		show_images(path_usb, root)
	else:
		label1 = tkinter.Label(root, text = "No se detectó algún archivo multimedia en la USB")
		label1.pack()
		
	root.mainloop()
	
def relaunch(root, path_usb):
	#print(path_usb + "re")
	root.destroy()
	interface_usb(path_usb, True)	
	
def start_usb_function():
	pre_path_usb = "/media/centro_multimedia/"
	list_usb = get_USBs_name()
	if len(list_usb) == 0:
		root = tkinter.Tk()
		root.geometry("300x100")
		root.title("No se detectó alguna USB conectada")
		root.mainloop()
	elif len(list_usb) == 1:
		interface_usb(pre_path_usb + list_usb[0] + "/", True)
	elif len(list_usb) > 1:
		root = tkinter.Tk()
		root.geometry("500x200")
		root.title("Escoja la USB desde donde se reproducirá la multimedia")
		for i in range(0, len(list_usb)):
			tkinter.Button(root, text = list_usb[i], width = 30, command = lambda i=i: relaunch(root, pre_path_usb + list_usb[i] + "/")).pack()
			#print(pre_path_usb + list_usb[i] + "/")
		root.mainloop()
	else:
		root = tkinter.Tk()
		root.geometry("300x100")
		root.title("Ocurrió un error, intente de nuevo por favor")
		root.mainloop()
		

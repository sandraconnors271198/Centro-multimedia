from selenium import webdriver

path='C:'+chr(92)+'Users'+chr(92)+'SANDRA SUSANA PEREZ'+chr(92)+'Documents'+chr(92)+'Escuela Fi'+chr(92)+'Código'+chr(92)+'centro_multimedia'+chr(92)+'static'+chr(92)+'chromedriver.exe'

login=input('Indica tu cuenta: ')
pasword=input('Indica tu password: ')
pasword=input('Nombre de la película: ')

driver=webdriver.Chrome(path)
driver.get('https://netflix.com')
time.sleep(10)
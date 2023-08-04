from selenium import webdriver #Framework selenium
from selenium.webdriver.chrome.service import Service #Elimina error problema de DeprecationWarning: executable_path has been deprecated, please pass in a Service object
from selenium.webdriver.common.by import By #Buscar Xpath
from selenium.webdriver.common.keys import Keys #Mandar texto a paginas
import time #Tiempo de espera

pathDriverChrome = "/Users/nicolasminato/Desktop/RPA/chromedriver" #Ubicación del driver de chrome
s = Service(pathDriverChrome) #Linea para que funcione 
driver = webdriver.Chrome(service=s) #Linea para que funcione 
driver.get('https://www.santandermovil.cl/UI.Web.HB/Private_new/frame/#/public/login?returnUrl=%2Fprivate%2Fmain') # URL Pagina
driver.maximize_window() #maximizar ventana
time.sleep(5)
id = "RUT"
contrasena = "CONTRASENA"
Rut = driver.find_element(By.XPATH, '//*[@id="rut"]') #Xpath Rut
Rut.click() #Click en Rut
Rut.send_keys(id) #enviar texto a rut
time.sleep(2)



Password = driver.find_element(By.XPATH, '//*[@id="pass"]') #Xpath Password
Password.click() #Click en password
Password.send_keys(contrasena) #enviar texto a password
time.sleep(2)

driver.find_element(By.XPATH, '/html/body/app-root/ng-component/div/div/div[4]/div[1]/form/div[3]/button').click() #Click en Xpath de Ingresar
time.sleep(10) #Esperar Nueva ventana

driver.find_element(By.XPATH, '//*[@id="mat-expansion-panel-header-3"]/span[2]').click() #Click en Xpath en Cuentas
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="cdk-accordion-child-3"]/div/div[3]/p').click() #Click en Xpath en Cartolas
time.sleep(10)

driver.find_element(By.XPATH, '//*[@id="cartolas"]/div/div[2]/div/div/button').click()
time.sleep(10)

driver.quit()

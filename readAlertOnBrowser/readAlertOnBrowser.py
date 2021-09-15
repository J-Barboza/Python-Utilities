from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Comente essa linha caso vá rodar em 2º plano
driver = webdriver.Chrome()

# para rodar o chrome em 2º plano / descomente as 4 linhas abaixo
#from selenium.webdriver.chrome.options import Options
#chrome_options = Options()
#chrome_options.headless = True 
#driver = webdriver.Chrome(options=chrome_options)

try:
    WebDriverWait(driver, 5).until(EC.alert_is_present(), 'Timed out waiting for simple alert to appear')
    alert = driver.switch_to.alert
    # time.sleep(2)
    print(alert.text)
except TimeoutException:
    print("Time out ao ler o Alert do Browser")


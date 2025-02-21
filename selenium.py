from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.detacoop.cl/")

button_text_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "elementor-button-text"))
)

assert button_text_element.text == "Solicite su Crédito", "El texto no coincide"
print("Verificación exitosa: El texto es 'Solicite su Crédito'.")

driver.quit()
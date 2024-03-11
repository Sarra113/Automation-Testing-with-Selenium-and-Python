from selenium import webdriver
import chromedriver_autoinstaller
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def configurare_driver():
    """
    Configureaza webdriver

    :return: un obiect webdriver
    """
    chromedriver_autoinstaller.install()
    # define options
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless') - ruleaza browserul in fundal
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    return driver


driver = configurare_driver()

try:
    driver.get('https://olx.ro')
    search_button_cookie = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'onetrust-accept-btn-handler'))).click()
    input_label = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, "input"))).send_keys('imobiliare')
    sleep(1)
    location_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'location-input'))).send_keys('cluj')
    sleep(2)
    location_dropdown = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'css-7lx9dr'))).click()
    sleep(2)
    search_button = driver.find_element(By.CLASS_NAME, 'css-1xla5xw').click()
    sleep(3)
    # Varianta I pentru scroll:
    # aflam lungimea totala a paginii
    # height = driver.execute_script('return document.body.scrollHeight')
    # print(height)
    # driver.execute_script('window.scrollTo(0, 500)')
    # sleep(1)
    # poate face screenshot-uri specifice elementelor
    # driver.get_screenshot_as_file('olx.png')

    # Varianta a II-a pentru scroll:
    # gasim elementul pana la care vrem sa dam scroll
    element_scroll = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, '259885748')))

    # folosim JS pentru a derula pana cand elementul devine vizibil
    '''
    arguments[0].scrollIntoView() este o instrucțiune JavaScript care 
    este utilizată pentru a derula pagina astfel încât elementul 
    specificat să devină vizibil în cadrul ferestrei browserului
    Elementul ar trebui sa apara afisat in partea de sus a ferestrei browserului
    '''
    driver.execute_script('arguments[0].scrollIntoView();', element_scroll)

    #  screenshot intreaga fereastra a browserului
    # driver.save_screenshot('olx2.png')

except Exception as e:
    print(e)
finally:
    sleep(5)
    driver.close()

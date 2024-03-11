from selenium import webdriver
import chromedriver_autoinstaller
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def configurare_driver():
    """
    Configureaza webdriver

    :return: obiectul webdriver.Chrome
    """
    # instaleaza si actualizeaza automat driverul Chrome
    chromedriver_autoinstaller.install()
    # initializeaza optiunile pt driverul Chrome
    options = webdriver.ChromeOptions()
    # [options.add_argument('--headless')]
    # adauga o optiune pt a maximiza fereastra browserului la deschiderea lui
    options.add_argument("--start-maximized")

    # creeaza un obiect webdriver.Chrome cu optiunile specificate
    driver = webdriver.Chrome(options=options)

    return driver

# apelam functia creata:


driver = configurare_driver()

try:
    # Acceseaza pagina web specificata
    driver.get('https://peviitor.ro')

    # Asteapta max 10 sec pana cand elem input (localizat prin tag name input) este vizibil si trimite cheia aecom
    input_label = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, "input"))).send_keys('aecom')  # (By tag, input) = tuplu

    # Asteapta 3 sec
    sleep(3)

    # Gaseste butonul de cautare dupa class name si da click pe el
    search_button = driver.find_element(By.CLASS_NAME, 'btn-yellow.btn').click()
    sleep(3)

    # Functia find.elements() returneaza o lista de elemente
    vezi_postul_buttons = driver.find_elements(By.CSS_SELECTOR, 'a.btn-yellow.btn')

    # iteram prin fiecare buton vezi postul
    for button in vezi_postul_buttons:
        # da scroll astfel incat butonul sa fie in centru vizibil
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});", button)
        sleep(1)
        button.click()
        sleep(1)

        # se obtine o lista cu toate ferestrele deschise in browser
        tabs = driver.window_handles

        # se comută la fereastra deschisă recent
        driver.switch_to.window(tabs[1])

        # se gaseste elementul de titlu al paginii deschise
        title = driver.find_element(By.CSS_SELECTOR, 'span[itemprop="title"]')

        # se da scroll astfel incat titlul sa fie in centri vizibil
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});", title)
        sleep(2)

        # se inchide fereastra curenta
        driver.close()

        # se comuta inapoi la fereastra originala
        driver.switch_to.window(tabs[0])

        # asteapta o sec intre iteratiile buclei for
        sleep(1)

    sleep(3)

except Exception as e:
    print(e)

    # Se executa intotdeauna chiar daca avem o exceptie sau nu
finally:
    sleep(5)
    driver.close()



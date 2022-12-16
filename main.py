import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium.webdriver.common.keys import Keys
import win32clipboard
import re
from datetime import date
import datetime
global panel
global opthead
def option_sleep():
    options = webdriver.ChromeOptions()
    ua = UserAgent( browsers=["chrome","edge"])
    user = ua.random
    options.add_argument('--disable-extensions')
    options.add_argument('--profile-directory=Default')
    options.add_argument("--incognito")
    options.add_argument("--disable-plugins-discovery")
    options.add_argument("--start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(f'user-agent={user}')
    print(f'Юзер-агент: {user}')
    options.headless = True
    return options

def option():
    options = webdriver.ChromeOptions()
    ua = UserAgent( browsers=["chrome","edge"])
    user = ua.random
    options.add_argument('--disable-extensions')
    options.add_argument('--profile-directory=Default')
    options.add_argument("--incognito")
    options.add_argument("--disable-plugins-discovery")
    options.add_argument("--start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(f'user-agent={user}')
    print(f'Юзер-агент: {user}')
    options.headless = False
    return options

lis = []
info = 1

def data(url):
    global opthead
    global inf
    driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe', options=option_sleep())
    driver.set_window_size(1920, 1080)
    try:
        driver.get('https://www.google.com/')
        #time.sleep(200)
        driver.find_element(By.XPATH, '//div/div/input').send_keys(url)
        driver.find_element(By.XPATH, '//input[@type="submit"]').click()
        print(url)
        h = 1
        while h != 0:
            captcha = driver.find_element(By.XPATH, '//*[@id="captcha-form"]')
            print('Введите капчу')
            info = input('Вы ввели капчу?')
            if bool(captcha) == True:
                h = 1
            else:
                h = 0
    except Exception as e:
        print(e)
        print('Капчи нет')
        info = 3
        while info != 0:
            try:
                #time.sleep(50)
                tags = driver.find_elements(By.XPATH, '//div/div/h3/div')
                for tag in tags:
                    if bool(re.search('[а-яА-Я]', tag.text)) == True:
                        continue
                    elif bool(tag.text.find(' ...')) == True:
                        g = tag.text.replace(' ...', '')
                        lis.append(g)
                    else:
                        lis.append(tag.text)
                sear = driver.find_element(By.XPATH,'//div/div/div/a[text() = "Следующая >"]')
                if bool(sear) == 1:
                    info = 1
                    sear.click()
                else:
                    info = 0
                print(lis)
            except Exception as e:
                try:
                    sear2 = driver.find_element(By.XPATH, '//span[text() = ">"]')
                    if bool(sear2) == 1:
                        info = 1
                        sear2.click()
                    else:
                        print(e)
                        #time.sleep(400)
                except:
                    print(e)
                    driver.close()
                    current_date = date.today()
                    c = datetime.datetime.now()
                    time1 = c.time()
                    c1 = time1.strftime('%H.%M.%S')
                    with open(f'Все Ключи - {current_date} - {c1}.txt', 'a', encoding="utf-8") as f:
                        f.writelines(f'{lis}\n')
                        f.close()
                    search(lis, url)

def search(lis, url):
    print(len(lis))
    sites1 = []
    iter = len(lis) - 1
    driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe', options=option_sleep())
    driver.set_window_size(1920, 1080)
    driver.get('https://www.google.com/')
    while iter != -1:
        try:
            print('2')
            panel = driver.find_element(By.XPATH, '//style/input')
            panel.clear()
            panel.send_keys(lis[iter])
            driver.find_element(By.XPATH, '//*[@type="submit"]').click()
        except:
            try:
                print('3')
                panel = driver.find_element(By.XPATH, '//div/div/input')
                #print('1dfdsfs')
                panel.clear()
                print(lis[iter])
                #time.sleep(20)
                panel.send_keys(lis[iter])
                g1 = driver.find_element(By.XPATH, '//*[@type="submit"]').click()
            except:
                try:
                    print('Новый')
                    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()
                except:
                    print('4')
                    #time.sleep(24)
                    driver.find_element(By.XPATH, '//div/img[@alt="Google"]').click()
                    time.sleep(4)
                    driver.find_element(By.XPATH, '//*[@type="submit"]').click()
            print('0')
        i = 0
        while i != 2:
            try:
                h = 1
                while h != 0:
                    captcha = driver.find_element(By.XPATH, '//*[@id="captcha-form"]')
                    print('Обнаружена капча. Введите капчу')
                    info = input('Вы ввели капчу?')
                    if bool(captcha) == True:
                        h = 1
                    else:
                        h = 0
            except:
                #print('Капча введена')
                sites = driver.find_elements(By.XPATH,'//a/div/div[2]/div')
                for site in sites:
                    glob = site.text
                    print(glob)
                    if url.find(glob.split()[0]) >= 0:
                        print(f'Запись первого ключа: {lis[iter]}\nСтраница: {i+1}')
                        file = f'Ключ: {lis[iter]} - Страница: {i + 1}'
                        current_date = date.today()
                        c = datetime.datetime.now()
                        time1 = c.time()
                        c1 = time1.strftime('%H')
                        sit = url[url.find('//')+2:url.find('.')]
                        with open(f'Ключи {sit} - {current_date } {c1} hours.txt', 'a', encoding="utf-8") as f:
                            f.write(f'{file}\n')
                            f.close()
                        continue
                    else:
                        continue
                #print(glob)

                i += 1
            #time.sleep(300)
            try:
                time.sleep(1)
                driver.find_element(By.XPATH, '//div/div/div/a[text() = "Следующая >"]').click()
            except:
                continue
        iter -= 1

def main():
    url1 = input('Введите домен: ')
    url = f'site:{url1}'
    data(url)
if '__main__' == __name__:
    #url = 'https://www.google.com/'
    #lis = ['google', 'facebook', 'adwords']
    #search(lis, url)
    main()
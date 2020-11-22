from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

mail='cefah27545@ummoh.com'
passwordd='a123456'

browser=webdriver.Chrome("chromedriver.exe")  # chrome webdriver'ı çalıştırır
browser.maximize_window()  # açılan pencereyi büyütür
browser.get("https://www.trendyol.com/")  # siteye gider
time.sleep(3)  # bekleme

popup=browser.find_element_by_xpath("/html/body/div[8]/div/div/a")  # gelen popup'ı kapar
popup.click()
time.sleep(1)


def giris():
    login=browser.find_element_by_xpath("//*[@id='accountBtn']")  # login butonuna basar
    login.click()
    time.sleep(1)

    email=browser.find_element_by_xpath("//*[@id='login-email']")  # emaili şecer
    email.send_keys(mail)  # emaili gönderir
    time.sleep(1)

    password=browser.find_element_by_xpath("//*[@id='login-password-input']")  # şifreyi seçer
    password.send_keys(passwordd)  # şifreyi gönderir
    time.sleep(1)

    login_button=browser.find_element_by_xpath(
        "//*[@id='login-register']/div[3]/div[1]/form/button").click()  # login butonuna basıp login olur
    time.sleep(3)


giris()


popup1=browser.find_element_by_xpath("//*[@id='modal-root']/div/div/div[1]").click()  # gelen popup'ı kapatır
time.sleep(1)

search=browser.find_element_by_xpath("//*[@id='auto-complete-app']/div/div/input")  # arama kısmını seçer
search.send_keys("Samsung")  # aranacak kelimeyi gönderir
time.sleep(1)

searchbutton=browser.find_element_by_xpath("//*[@id='auto-complete-app']/div/div/i")  # arama yapar
searchbutton.click()
time.sleep(1)

page2=browser.get(
    "https://www.trendyol.com/tum--urunler?q=Samsung&qt=Samsung&st=Samsung&os=1&pi=2")  # ikinci sayfaya gider
time.sleep(2)

product3=browser.find_element_by_xpath("//*[@id='search-app']/div/div[1]/div[2]/div[3]/div/div[3]")  # 3. ürünü açar
product3.click()
time.sleep(2)


def favs():
    fav=browser.find_element_by_xpath(
        "//*[@id='product-detail-app']/div/div[2]/div[2]/div[2]/div[6]/button[2]")  # fav butonuna basar
    fav.click()
    time.sleep(1)

    fav_hesabim=browser.find_element_by_xpath("//*[@id='favoritesButton']")  # favorilerim ekranına gider
    fav_hesabim.click()
    time.sleep(2)

    myfavdelete=browser.find_element_by_xpath(
        "//*[@id='account-gw-favorites']/div/div[2]/div/div/div[4]/i")  # favoriyi siler
    myfavdelete.click()
    time.sleep(5)


favs()

browser.close()  # pencereyi kapatır

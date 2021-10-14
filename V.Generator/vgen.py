from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
###
#proxy_ip_port = "115.200.0.170:8908"

#proxy = Proxy()
#proxy.proxy_type = ProxyType.MANUAL
#proxy.https_proxy = proxy_ip_port
#proxy.ssl_proxy = proxy_ip_port

#capabilities = webdriver.DesiredCapabilities.CHROME
#proxy.add_to_capabilities(capabilities)
###
driver = webdriver.Chrome(executable_path="chromedriver.exe")#, desired_capabilities=capabilities)
driver.execute_script("window.open('about:blank', 'tab2');")
driver.switch_to.window("tab2")
driver.get('https://temp-mail.org/fr/')
time.sleep(10)
mail = driver.find_element_by_id("mail")

mail.click()

mail.send_keys(Keys.CONTROL, 'c')

print(mail)
driver.execute_script("window.open('about:blank', 'tab1');")
driver.switch_to_window("tab1")
driver.get("https://discord.com/register")




search_bar = driver.find_element_by_name("email")
search_bar.send_keys(Keys.CONTROL, "v")

search_bar = driver.find_element_by_name("username")
search_bar.send_keys("0x00.V")


search_bar = driver.find_element_by_name("password")
search_bar.send_keys("0x00leakajeur")

dropdown = driver.find_element_by_class_name("css-gvi9bl-control")
dropdown.click()
zizi = driver.find_element_by_class_name("css-1rel15f")
ck = driver.find_element_by_id("react-select-2-option-4")
ck.click()

dropdown2 = driver.find_element_by_class_name("css-17e1tep-control")
dropdown2.click()
zizi2 = driver.find_element_by_class_name("css-1rel15f")
ck2 = driver.find_element_by_id("react-select-3-option-4")
ck2.click()

dropdown3 = driver.find_element_by_class_name("css-17e1tep-control")
dropdown3.click()
zizi3 = driver.find_element_by_class_name("css-1rel15f")
ck3 = driver.find_element_by_id("react-select-4-option-19")
ck3.click()

bouton_valide = driver.find_element_by_css_selector("input[type='checkbox']")
bouton_valide.click()

creer = driver.find_element_by_class_name("button-3k0cO7")
creer.click()
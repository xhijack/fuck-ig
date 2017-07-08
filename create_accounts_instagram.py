from random import choice
from time import sleep

from selenium.webdriver.common.keys import Keys
from selenium import webdriver


PROXY = "101.255.51.146:3128"

# Create a copy of desired capabilities object.
desired_capabilities = webdriver.DesiredCapabilities.INTERNETEXPLORER.copy()
# Change the proxy properties of that copy.
desired_capabilities['proxy'] = {
    "httpProxy":PROXY,
    "ftpProxy":PROXY,
    "sslProxy":PROXY,
    "noProxy":None,
    "proxyType":"MANUAL",
    "class":"org.openqa.selenium.Proxy",
    "autodetect":False
}

first_names = ['Azmya', 'Assyfa', 'Azka', 'Ashalina', 'Arsyila', 'Aqilla', 'Azahra', 'Annasya', 'Azrina']
middle_names = ['Yasna', 'Kirei', 'Adinda', 'Ashalina', 'Nasha', 'Shahin', 'Mysha', 'Salsabela', 'Naifa']
last_names = ['Fadheela', 'Alnaira', 'Nazeefah', 'Rafailah', 'Mahveen', 'Shakeera', 'Shafana', 'Anindita']


browser = webdriver.Chrome(desired_capabilities=desired_capabilities)
browser.maximize_window()
browser.get('https://instagram.com')

for i in range(1, 2):
    f = choice(first_names)
    m = choice(middle_names)
    l = choice(last_names)
    name_ = "{} {} {}".format(f, m, l)
    username_ = "{}{}{}".format(f, m, l)
    email_ = 'botinstagram.maker+1{}@gmail.com'.format(i)

    email = browser.find_element_by_name('emailOrPhone')
    fullname = browser.find_element_by_name('fullName')

    username = browser.find_element_by_name('username')
    password = browser.find_element_by_name('password')


    email.send_keys(email_)
    fullname.send_keys(name_)
    username.send_keys(username_)
    password.send_keys('master88' + Keys.RETURN)


    sleep(360)
    browser.close()



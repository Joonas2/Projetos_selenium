#!/usr/bin/env python
# coding: utf-8

# In[4]:


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()
driver.get('https://br.investing.com/currencies/usd-brl-historical-data')
sleep(5)

'''Esperando carregar pop-ups'''
while len(driver.find_elements_by_xpath('//*[@id="onetrust-accept-btn-handler"]')) == 0:
    sleep(1)
    

'''Fechando os pop-ups'''

driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()


'''Aguardando aparecer propaganda'''
elemento =  WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="PromoteSignUpPopUp"]/div[2]/i')))
sleep(1)
elemento.click()


'''Clicando para fazer download'''
driver.find_element_by_xpath('//*[@id="column-content"]/div[4]/div/a').click()


'''Fazendo login'''
email = driver.find_elements_by_id('loginFormUser_email')
email[0].send_keys('emailteste@gmail.com')

senha = driver.find_elements_by_id('loginForm_password')
senha[0].send_keys('senhateste')

driver.find_element_by_xpath('//*[@id="signup"]/a').click()


'''Fazendo Download'''
driver.find_element_by_xpath('//*[@id="column-content"]/div[4]/div/a').click()


# In[ ]:





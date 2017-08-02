from selenium import webdriver

driver = webdriver.Chrome(r'C:\Users\HunPC\Downloads\chromedriver_win32\chromedriver.exe')
driver.get('https://nid.naver.com/nidlogin.login')
driver.find_element_by_name('id').send_keys('hunman23')
driver.find_element_by_name('pw').send_keys('tjdgnse1')

driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()


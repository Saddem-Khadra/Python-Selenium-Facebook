from selenium import webdriver

your_email = ''
your_password = ''
send_to = ''
your_message = ''

chrome_browser = webdriver.Chrome()
chrome_browser.get('https://www.facebook.com')
# chrome_browser.minimize_window()

chrome_browser.implicitly_wait(10)

assert 'Facebook - ' in chrome_browser.title

email = chrome_browser.find_element_by_id('email')
email.clear()
email.send_keys(your_email)
password = chrome_browser.find_element_by_id('pass')
password.clear()
password.send_keys(your_password)

chrome_browser.implicitly_wait(10)

login = chrome_browser.find_element_by_id('u_0_b')
login.click()

chrome_browser.implicitly_wait(10)

messenger = chrome_browser.find_element_by_xpath("//div[@aria-label='Messenger']")
messenger.click()

chrome_browser.implicitly_wait(10)

search = chrome_browser.find_element_by_xpath("//label[input/@aria-label='Rechercher dans Messenger']")
search.send_keys(send_to)

chrome_browser.implicitly_wait(10)

result = chrome_browser.find_element_by_xpath(f"//div[div/@aria-label='{send_to}']")
result.click()

chrome_browser.implicitly_wait(10)

message = chrome_browser.find_element_by_xpath("//div[@class='pfnyh3mw']//br[@data-text='true']")
message.send_keys(your_message)

send = chrome_browser.find_element_by_css_selector(".pfnyh3mw > form")
send.submit()

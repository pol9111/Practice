import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.PhantomJS()
driver.get("http://www.douban.com")

# 输入账号密码
driver.find_element_by_name("form_email").send_keys("#")
driver.find_element_by_name("form_password").send_keys("#")

driver.save_screenshot('douban.png')

# 输入验证码
captcha = input("请输入验证码:")

driver.find_element_by_id("captcha_field").send_keys(captcha)

# 模拟点击登录
driver.find_element_by_xpath("//input[@class='bn-submit']").click()

time.sleep(3)

# 生成登陆后快照
driver.save_screenshot('douban.png')

print(driver.page_source)

with open('douban.html', 'wb') as f:
    f.write(driver.page_source.encode('utf-8'))

print('登入成功!!!')

driver.quit()



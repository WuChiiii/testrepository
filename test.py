from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
# 创建一个浏览器实例
driver = webdriver.Chrome()

# 打开目标网页
driver.get("https://codis.cwa.gov.tw/StationData")
button_xpath = "//*[@id='switch_display']/button[2]/i"
button = driver.find_element(By.XPATH, button_xpath)

# 模拟点击按钮
button.click()
time.sleep(2)
# 定位图标元素
text_to_match = "宜蘭"
xpath_td = f"//td[div[text()='{text_to_match}']]"

# 找到對應的<i>元素
ixpath = f"{xpath_td}/following-sibling::td//i[@class='fas fa-chart-line cursor-pointer']"
# //*[@id="station_table"]/table/tbody/tr[3]/td[6]/div/i
icon_element = driver.find_element(By.XPATH, ixpath)
# //*[@id="station_table"]/table/tbody/tr[3]/td[6]/div
icon_element.click()
time.sleep(1)
month_button_xpath = "//*[@id='main_content']/section[2]/div/div/aside/div/div[5]/img"
month_button = driver.find_element(By.XPATH, month_button_xpath)

# 模拟点击按钮
month_button.click()
time.sleep(1)
date_input_xpath = "//*[@id='main_content']/section[2]/div/div/section/div[6]/div[1]/div[1]/label/div/div[2]/input"
date_input = driver.find_element(By.XPATH, date_input_xpath)

# 使用 JavaScript 设置输入框的值
new_date_value = "2022/01"
driver.execute_script("arguments[0].value = arguments[1]", date_input, new_date_value)
# 等待一段时间（可選）
time.sleep(1)

# 关闭浏览器
driver.quit()
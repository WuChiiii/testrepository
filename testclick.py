from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
# 创建一个浏览器实例
driver = webdriver.Chrome()

# 打开目标网页
driver.get("https://codis.cwa.gov.tw/StationData")
time.sleep(5)
button_xpath = "//*[@id='switch_display']/button[2]/i"
button = driver.find_element(By.XPATH, button_xpath)

# 模拟点击按钮
button.click()
time.sleep(1)
# 定位图标元素

text_to_match = "宜蘭"
xpath_td = f"//td[div[text()='{text_to_match}']]"

# 找到對應的<i>元素
ixpath = f"{xpath_td}/following-sibling::td//i[@class='fas fa-chart-line cursor-pointer']"
# //*[@id="station_table"]/table/tbody/tr[3]/td[6]/div/i
icon_element = driver.find_element(By.XPATH, ixpath)
icon_element.click()
time.sleep(1) 
month_button_xpath = "//*[@id='main_content']/section[2]/div/div/aside/div/div[5]/img"
month_button = driver.find_element(By.XPATH, month_button_xpath)
month_button.click()
time.sleep(0.5)
##以下要模擬2020~2022的1月到12月的宜蘭資料蒐集
# 模拟点击按钮
flag=1
for year in range(2020, 2023):
    flag=1
    for month in range(1, 13):
        date_input_xpath = "//*[@id='main_content']/section[2]/div/div/section/div[6]/div[1]/div[1]/label/div/div[2]/input"
        date_input = driver.find_element(By.XPATH, date_input_xpath)
        date_input.click()#點blank
        time.sleep(0.5)
        year_input_xpath = "//*[@id='main_content']/section[2]/div/div/section/div[6]/div[1]/div[1]/label/div/div[2]/div/div[2]/div[1]/div[1]"
        year_input = driver.find_element(By.XPATH, year_input_xpath)
        year_input.click()#點title
        time.sleep(0.5)
        if year == 2020 and flag ==1 :
            year_select=98
            flag=0
        elif flag ==1:
            year_select=102
            flag=0
        else:
            year_select=101
        year_input_xpath = "//*[@id='main_content']/section[2]/div/div/section/div[6]/div[1]/div[1]/label/div/div[2]/div/div[2]/div[2]/div/div/div[{}]".format(year_select)
        year_input = driver.find_element(By.XPATH, year_input_xpath)
        year_input.click()#點year
        time.sleep(0.5)
        month_input_xpath = "//*[@id='main_content']/section[2]/div/div/section/div[6]/div[1]/div[1]/label/div/div[2]/div/div[2]/div[2]/div/div/div[{}]".format(month)
        month_input = driver.find_element(By.XPATH, month_input_xpath)
        month_input.click()#點month1
        time.sleep(15)
        # 定位 table 元素
        table_xpath = "//*[@id='report_month']/table"
        table_element = driver.find_element(By.XPATH, table_xpath)
        time.sleep(0.5)
        # 使用 Pandas 讀取表格
        table_html = table_element.get_attribute('outerHTML')
        time.sleep(0.5)
        df = pd.read_html(table_html)[0]  # 假設只有一個表格，你可以根據實際情況選擇索引
        filename="{}-{}_data.csv".format(year,month)
        df.to_csv(filename, index=False)
        # 顯示 DataFrame
        # print(df)
        time.sleep(0.5)
# 关闭浏览器
driver.quit()


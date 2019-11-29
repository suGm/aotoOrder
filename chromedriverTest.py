from selenium import webdriver
import time
 
chromedriver = "C:\\Users\\sgm\\Desktop\\sgm\\autoOrderTMall\\chromedriver.exe"
 
#设置不加载图片
chrome_opt = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_opt.add_experimental_option("prefs", prefs)
 
dirver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_opt)
 
dirver.get("https://detail.tmall.com/item.htm?spm=a1z10.4-b-s.w5003-22082778529.6.3f001e00vAe7Tn&id=603123506400")
 
#获取页面HTML
html = driver.page_source
 
dirver.find_element_by_xpath("//div[@class='SignContainer-switch']/span").click()
 
dirver.find_element_by_xpath("//div[@class='SignFlow-accountInput Input-wrapper']/input").send_keys("")
 
dirver.find_element_by_xpath("//div[@class='SignFlow-password']/div/div[@class='Input-wrapper']/input").send_keys("")
 
dirver.find_element_by_xpath("//button[@class='Button SignFlow-submitButton Button--primary Button--blue']").click()
 
cookie = [item["name"] + "=" + item["value"] for item in dirver.get_cookies()]
 
cookiestr = ';'.join(item for item in cookie)
 
print(cookiestr)
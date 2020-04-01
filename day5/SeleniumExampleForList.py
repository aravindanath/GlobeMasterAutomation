from selenium.webdriver import  Chrome
import time

from webdriver_manager.chrome import ChromeDriverManager
driver= Chrome(ChromeDriverManager().install())

# path = "../driver/chromedriver"
# driver = Chrome(executable_path=path)
driver.get("https://www.wikipedia.org/")


lang = driver.find_elements_by_xpath("//select[@id='searchLanguage']/option")

print("Total no of lang: ", len(lang))

emptyLang = []

for i in lang:
    emptyLang.append(i.text)

print("Un-Sorted lang: ",emptyLang)
emptyLang.sort(reverse=False)
print("Sorted lang: ",emptyLang)

time.sleep(3)
driver.quit()


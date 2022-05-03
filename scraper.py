from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options


chrome_options = Options()
chrome_options.add_argument("--headless")

URL_TO_SCRAPE = "https://www.trading212.com/trading-instruments/invest"

#driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()),options=chrome_options)
driver.get(URL_TO_SCRAPE)
#output html to file to examine what elements need to be scraped
with open("html_output.log",'w',encoding='utf-8') as external_file:
    print(driver.page_source,file=external_file)
    external_file.close()
driver.quit()
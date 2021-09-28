from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
class BOT():
    def __init__(self,url):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.url = url
        self.login()
        
    def login(self):
        self.driver.get(self.url)
    
        try: 
            sleep(1)
            cookie = self.driver.find_element_by_xpath('//*[@id="sp-cc-accept"]')
            cookie.click()
            self.check()
        except Exception as ex:
            self.check()
            self.driver.quit()
        
    def check(self):
        try:      
            instant = self.driver.find_element_by_xpath('//*[@id="buy-now-button"]')
            try:
                instant.click()
                sleep(1.25)
                instant.click()
                sleep(2)
                try:
                    assurancetxt = self.driver.find_element_by_xpath('//*[@id="attachSiNoCoverage-announce"]').text
                    sleep(1.25)
                    if(assurancetxt == "Non, merci." or assurancetxt == "No, Thanks."):
                        assr = self.driver.find_element_by_xpath('//*[@id="attachSiNoCoverage"]') 
                        assr.click()
                except Exception as ex: 
                    instant.click()
                    self.check()
            except Exception as ex: 
                print("Problème durant le paiement? Peut-être pas connecté?\n 1 minute le temps de vous connecter");
                sleep(60);
                self.driver.quit()
        except Exception as ex: 
            print("INDISPO")
            sleep(2)
            self.check()
amazon = BOT("https://www.amazon.fr/gp/product/B08B3TYX1H?pf_rd_r=GKDPS0WD6T69P80CNKA9&pf_rd_p=ed1ef413-005c-474d-837a-434c7d76d0d9&pd_rd_r=b44baa92-e539-48c9-9006-596e95af4546&pd_rd_w=9OnMu&pd_rd_wg=Qympw&ref_=pd_gw_unk&th=1")

from web_auto import *

driver = web_auto()
driver.open_url("https://www.google.com/")
driver.enterTextInXpath("//*[@id='lst-ib']", "length of highway SR-3")
if driver.CheckIfXpathExist("/html/body/div[6]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div[1]"):
    driver.clickXpath("/html/body/div/div[3]/form/div[2]/div[3]/center/input[1]")
    text = driver.GetTextInXpath("/html/body/div[6]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div[1]")
    print(text)
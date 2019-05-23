import pandas
from web_auto import *
df1 = pandas.read_csv('accident_2015.csv')
df2 = pandas.read_csv('accident_2016.csv')

temp = df1.append(df2, ignore_index=True)
# print(df1)
df = temp.groupby(['TWAY_ID']).size().reset_index(name='counts')
df = df.sort_values(by='counts', ascending=False)
# print(df)

road_name = df['TWAY_ID'].tolist()
road_accidents = df['counts'].tolist()

driver = web_auto()
f = open("road_data.csv", 'a')
for i in range(0, 188):
    print(road_name[i] + " "+ str(road_accidents[i]))
    driver.open_url("https://www.google.com/")
    driver.waitForXpath("//*[@id='lst-ib']")
    driver.enterTextInXpath("//*[@id='lst-ib']", road_name[i]+" road length")
    driver.SendEnterKey("/html/body/div/div[3]/form/div[2]/div[3]/center/input[1]")
    time.sleep(2)
    # driver.clickXpath("/html/body/div/div[3]/form/div[2]/div[3]/center/input[1]")
    text = ""
    if driver.CheckIfXpathExist(
            "/html/body/div[6]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div[1]"):
        text += driver.GetTextInXpath(
            "/html/body/div[6]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div[1]")

    if driver.CheckIfXpathExist("/html/body/div[6]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div/div[1]"):
        text += ","
        text += driver.GetTextInXpath(
            "/html/body/div[6]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div/div[1]")


    f.write(','.join([road_name[i], str(road_accidents[i]), text] )+"\n")
    print(','.join([road_name[i], str(road_accidents[i]), text] ))

# t = df1['TWAY_ID'].unique()

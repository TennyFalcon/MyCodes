from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import time
import pandas as pd
import csv

class TestWD():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="H:\Softwares\Selenium\chromedriver_win32\chromedriver.exe")
        driver.get("https://wd3-impl.workday.com/wday/authgwy/jlp2/login.htmld?redirect=n")
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(
            '//*[@id="noImageRequiredForLoadTime"]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div[3]/div[1]/div/input').send_keys(
            '83384782')
        driver.find_element_by_xpath(
            '//*[@id="noImageRequiredForLoadTime"]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div[3]/div[2]/div/input').send_keys(
            'Tenny@888')
        driver.find_element_by_xpath(
            '//*[@id="noImageRequiredForLoadTime"]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div[3]/button').click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//input[@type='checkbox']").click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//button[@data-automation-id='button']").click()
        driver.implicitly_wait(10)
        yield
        driver.close()
        driver.quit()

    def test_coveragebegindate(self,test_setup):
        #source = pd.read_csv('H:/Automation/Python/Selenium/Input file/Source.csv',encoding = "ISO-8859-1", error_bad_lines = False)
        y = []
        z = []
        y = ['76030547', '77137035', '83358579']
        z = ['13/03/2000','08/12/2003','10/06/2018']
        source = []
        i = 0
        OutputCsv = 'H:/Automation/Python/Selenium/Output file/Output.csv'
        OutputFile = open(OutputCsv, 'w')
        OutputFile.write('Primary key' + ',' + 'Field name' + ',' + 'Source Value' + ',' + 'Workday Value' + ',' + 'Result' )
        OutputFile.write('\n')

        #y = source['Emp_Id']
        #z = source['Original_Coverage_Begin_Date']
        for x in y:
            driver.find_element_by_xpath('//*[@id="wd-searchInput"]/div[1]/input').send_keys(x,
                                                                                                  Keys.ENTER)
            driver.implicitly_wait(10)
            driver.find_element_by_xpath("//div[@data-automation-id='compositeHeader']").click()
            time.sleep(3)
            driver.find_element_by_xpath('//button[@type="button"]').click()
            time.sleep(3)
            driver.find_element_by_xpath("//div[@data-automation-label='Benefits']").click()
            time.sleep(3)
            a = driver.find_element_by_xpath("//div[@data-automation-id='textView']")
            b = driver.find_element_by_xpath("//div[@aria-label='Discount Card - John Lewis Partnership (Partnership Discount)']")
            av = a.text
            bv = b.text
            if av == z[i]:
                wv = str(x)  +','+ str(bv) +',' + str(av)+',' + str(z[i]) + ','+ str('PASS')
            else:
                wv = str(x)  +','+ str(bv) + ','+ str(av) +','+ str(z[i]) + ',' + str('FAIL')
            i = i + 1
            OutputFile.write(str(wv))
            OutputFile.write('\n')
            driver.find_element_by_xpath('//*[@id="wd-searchInput"]/div[1]/input').send_keys(Keys.CONTROL + "a")
            driver.find_element_by_xpath('//*[@id="wd-searchInput"]/div[1]/input').send_keys(Keys.DELETE)
        OutputFile.close()

    def test_deductionbegindate(self, test_setup):
        # source = pd.read_csv('H:/Automation/Python/Selenium/Input file/Source.csv',encoding = "ISO-8859-1", error_bad_lines = False)
        y = []
        z = []
        y = ['76030547', '77137035', '83358579']
        z = ['13/03/2000', '08/12/2003', '10/06/2018']
        source = []
        i = 0
        OutputCsv = 'H:/Automation/Python/Selenium/Output file/Output.csv'
        OutputFile = open(OutputCsv, 'a')
        OutputFile.write(
            'Primary key' + ',' + 'Field name' + ',' + 'Source Value' + ',' + 'Workday Value' + ',' + 'Result')
        OutputFile.write('\n')

        # y = source['Emp_Id']
        # z = source['Original_Coverage_Begin_Date']
        for x in y:
            driver.find_element_by_xpath('//*[@id="wd-searchInput"]/div[1]/input').send_keys(x,
                                                                                             Keys.ENTER)
            driver.implicitly_wait(10)
            driver.find_element_by_xpath("//div[@data-automation-id='compositeHeader']").click()
            time.sleep(3)
            driver.find_element_by_xpath('//button[@type="button"]').click()
            time.sleep(3)
            driver.find_element_by_xpath("//div[@data-automation-label='Benefits']").click()
            time.sleep(3)
            a = driver.find_element_by_xpath("//div[@data-automation-id='textView']")
            b = driver.find_element_by_xpath(
                "//div[@aria-label='Discount Card - John Lewis Partnership (Partnership Discount)']")
            av = a.text
            bv = b.text
            if av == z[i]:
                wv = str(x) + ',' + str(bv) + ',' + str(av) + ',' + str(z[i]) + ',' + str('PASS')
            else:
                wv = str(x) + ',' + str(bv) + ',' + str(av) + ',' + str(z[i]) + ',' + str('FAIL')
            i = i + 1
            OutputFile.write(str(wv))
            OutputFile.write('\n')
            driver.find_element_by_xpath('//*[@id="wd-searchInput"]/div[1]/input').send_keys(Keys.CONTROL + "a")
            driver.find_element_by_xpath('//*[@id="wd-searchInput"]/div[1]/input').send_keys(Keys.DELETE)
        OutputFile.close()







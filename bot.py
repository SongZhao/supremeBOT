import time
try:  
    from selenium import webdriver
    from selenium.webdriver.support.ui import Select
except ImportError:
    print "Selenium module is not installed...Exiting program."
    exit(1)
     
def Check(keywords, text):
    for i in keywords:
        if i not in text:
            return False
    return True
 
def searchCommodity(browser, category, name, color):    
    print ("Searching for %s \t color: %s in %s" % (name, color, category))
    browser.get("http://www.supremenewyork.com/shop/all/" + category)
    links = browser.find_elements_by_class_name("name-link")
    i = 0
    while i < len(links):
        if (Check(name, links[i].text) & (color in links[i+1].text)):
            print "Description : " + links[i].text
            print "Color : " + links[i+1].text
            links[i].click()
            print " Buying"
            return True
        i += 2
    print " not found"
    return False

def fillForm(browser):
    billing_name = "Song Zhao"
    email = " "
    tel = " "
    billing_address = "xxxxxxxxx"
    billing_city = "Madison"
    billing_zip = "53705"
    billing_state = "FL"
    billing_country = "USA"
    nlb = "9999 999 999 9999"
    month = "02"
    year = "2018"
    rvv = "888"
    name = browser.find_element_by_name("order[billing_name]").send_keys(billing_name)
    email = browser.find_element_by_name("order[email]").send_keys(email)
    tel = browser.find_element_by_name("order[tel]").send_keys(tel)
    address = browser.find_element_by_name("order[billing_address]").send_keys(billing_address)
    address = browser.find_element_by_name("order[billing_city]").send_keys(billing_city)
    postCode = browser.find_element_by_name("order[billing_zip]").send_keys(billing_zip)
    billing_state = browser.find_element_by_name('order[billing_state]').send_keys(billing_state)
    countrySelect = Select(browser.find_element_by_name("order[billing_country]")).select_by_visible_text(billing_country)
    creditCardSelect = browser.find_element_by_name('credit_card[nlb]').send_keys(nlb)
    monthExpirationSelect = Select(browser.find_element_by_name("credit_card[month]")).select_by_visible_text(month)
    yearExpirationSelect = Select(browser.find_element_by_name("credit_card[year]")).select_by_visible_text(year)
    cvv = browser.find_element_by_name("credit_card[rvv]").send_keys(rvv)
    browser.find_element_by_class_name("terms").click()

def main():                     
    print " Opening Browser ..."
    browser = webdriver.Firefox()
    browser.implicitly_wait(5)  
    category = "accessories"  
    keywords = []
    keywords.append("shirt") 
    color = "pink"  
    size = 'small'

    if searchCommodity(browser, category, keywords, color) == False:
        return -1
    if size != "":
        try:
            sizeSelect = Select(browser.find_element_by_id("s"))
            sizeSelect.select_by_visible_text(size)
        except:
            print "[/i][/i][/i][i][i][i] Commodity sold out......."
            return -1
    try:
        browser.find_element_by_name("commit").click()
    except:
         print "[/i][/i][/i][i][i][i] Commodity sold out"
         return -1
    time.sleep(1)  
    browser.find_element_by_class_name("checkout").click()
    print "Filling in the information"
    fillForm(browser)
    print "Filled..."
    print "Prepare to buy a bill....."
    browser.find_element_by_name("commit").click()
    print "Finshed,congratulations on your favorite things!!!!!"
    brower.close()
 
if __name__ == '__main__':
    main()
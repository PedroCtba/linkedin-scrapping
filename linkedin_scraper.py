from selenium import webdriver

if __name__ == "__main__":
    ## make driver
    gldr = webdriver.Chrome(executable_path=r"C:\Users\PedroMiyasaki\AppData\Local\SeleniumBasic\chromedriver.exe")

    ## sleep
    gldr.implicitly_wait(10)

    ## oepn link
    gldr.get(r'https://www.linkedin.com/jobs/search/?geoId=106057199&keywords=dados&location=Brasil')


    ## login
    login_button = gldr.find_element_by_class_name('nav__button-secondary')
    login_button.click()

    l = gldr.find_element_by_xpath('//*[@id="username"]')
    l.send_keys('miyasakigazola@gmail.com')

    s = gldr.find_element_by_xpath('//*[@id="password"]')
    s.send_keys('Senha@322')

    e = gldr.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
    e.click()

    ## get results and loop
    result = gldr.find_element_by_class_name('jobs-seacrh-results__list')

    descriptions = []
    for r in result:
        r.click()
        description = gldr.find_element_by_class_name('description')
        descriptions.append(description)


    print(description)
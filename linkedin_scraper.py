from selenium import webdriver
from time import sleep


if __name__ == '__main__':
    ## make driver, sleep, and open site
    gldr = webdriver.Chrome(executable_path=r"C:\Users\PedroMiyasaki\AppData\Local\SeleniumBasic\chromedriver.exe")
    gldr.implicitly_wait(10)
    gldr.get(r'https://www.linkedin.com/jobs/search/?geoId=106057199&keywords=dados&location=Brasil')


    ## login on Linkedin and wait
    login_button = gldr.find_element_by_class_name('nav__button-secondary')
    login_button.click()

    l = gldr.find_element_by_xpath('//*[@id="username"]')
    l.send_keys('SEU USUÁRIO AQUI')
    s = gldr.find_element_by_xpath('//*[@id="password"]')
    s.send_keys('SUA SENHA AQUI')
    e = gldr.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
    e.click()


    # get first jobs and do while loop to save description
    result = gldr.find_elements_by_class_name('job-card-container')
    initial_leght = True

    # empty descriptios
    descriptions = [ ]
    while True:
        

        # if it is the firt loop
        if initial_leght:
            for i in result[::-1]:
                sleep(1)
                i.click()
                descriptions.append(i.text)
                
            initial_leght = False

        # if it is not
        else:
            for i in result[lenght:]:
                sleep(1)
                i.click()
                descriptions.append(i.text)
            

        # save last lenht
        lenght = len(result)
        result = gldr.find_elements_by_class_name('job-card-container')

        # stop when actual lenght is equal to the last
        if lenght == len(result):
            break
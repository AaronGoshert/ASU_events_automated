from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pyshadow.main import Shadow
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep



def expand_shadow_element(element):
    shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
    return shadow_root



userReader = open('username.txt', 'r')
user_name = userReader.read()
userReader.close()
passReader = open('password.txt', 'r')
pass_word = passReader.read()
passReader.close()
reader = open("eventinfo.txt", 'r')
eventName = reader.readline()
description = reader.readline()
room_name = reader.readline()
street_address = reader.readline()
city = reader.readline()
state = reader.readline()
reader.close()
reader = open('clubeventurl.txt', 'r')
club_mange_url = reader.read()
reader.close()

def login():
 sleep(5)
 driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(user_name)
 driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(pass_word)
 driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/section[2]/div[1]/input').click()
 
def duo(): 
 driver.switch_to.frame('duo_iframe')
 sleep(2)
 auth_bar = driver.find_element(By.CSS_SELECTOR, 'div.row-label:nth-child(2)')
 auth_bar.find_element(By.CSS_SELECTOR, 'div.row-label:nth-child(2) > button:nth-child(3)').click()
 input('Press enter when done with duo: ')


#SDS
driver = webdriver.Chrome()
driver.get("https://asu.campuslabs.com/engage")
shadow = Shadow(driver)
shadow.set_explicit_wait(20, 5)
login_bar = shadow.find_element("#top-tool-bar")
shadow.find_element(login_bar, "a.MuiButtonBase-root:nth-child(6)").click()

login()
duo()

sleep(10)

driver.get(club_mange_url)
sleep(10)


driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]").click()


driver.find_element(By.XPATH, '//*[@id="Name"]').send_keys(eventName)
selectTheme = Select(driver.find_element(By.ID, 'Theme'))
selectTheme.select_by_value('GroupBusiness')
descrip_frame = driver.switch_to.frame('Description_ifr')
driver.find_element(By.XPATH, '/html/body/p').send_keys(description)
driver.switch_to.default_content()

driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/form/div[2]/fieldset/div[1]/fieldset/div[2]/div[1]/input').click()
sleep(5)
driver.find_element(By.XPATH, '//*[@id="Instances[0].ExternalLocation"]').send_keys(room_name)
sleep(1)
driver.find_element(By.ID, 'Instances[0].Address').send_keys(street_address)
sleep(1)
driver.find_element(By.XPATH, '//*[@id="city_0"]').send_keys(city)
sleep(1)
driver.find_element(By.XPATH, '//*[@id="state_0"]').send_keys(state)
sleep(1)
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/form/div[2]/fieldset/div[1]/fieldset/div[6]/div[2]/div/button[1]/span').click()
sleep(2)

driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/form/div[2]/fieldset/div[1]/fieldset[2]/div[1]/span/a/span').click()
sleep(5)


sleep(5)
selectCategory = Select(driver.find_element(By.XPATH, '//*[@id="bsmSelectbsmContainer0"]'))
selectCategory.select_by_value('12887')
sleep(3)
input('Press enter after date is selected: ')
sleep(3)
driver.find_element(By.CSS_SELECTOR, ".mdl-button").click()
sleep(15)

driver.find_element(By.XPATH, '//*[@id="SendGroupMemberInvitationsAfterApproval"]').click()
driver.find_element(By.XPATH, '//*[@id="ShouldAllowGuests"]').click()
driver.find_element(By.XPATH, '//*[@id="GroupRepresentationEnabled"]').click()
driver.find_element(By.XPATH, '//*[@id="submitRsvpSettings"]').click()
sleep(5)
driver.find_element(By.XPATH, '//*[@id="submitPostEventSettings"]').click()
sleep(5)
driver.find_element(By.XPATH, '//*[@id="skip-cover-photo-button"]').click()
sleep(5)

driver.find_element(By.XPATH, '//*[@id="46139144"]').click()
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/form/div/div[2]/button').click()
sleep(3)
driver.find_element(By.XPATH, '//*[@id="review-btn"]').click()
sleep(5)


#Event Registry
eventregreader = open('EventReg.txt', 'r')
event_description = eventregreader.readline()
club_name = eventregreader.readline()
club_url = eventregreader.readline()
room_num = eventregreader.readline()
adv_name = eventregreader.readline()
adv_email = eventregreader.readline()
adv_number = eventregreader.readline()
cord_phone = eventregreader.readline()
cord_name = eventregreader.readline()
cord_email = eventregreader.readline()
officer_name = eventregreader.readline()
officer_email = eventregreader.readline()
eventregreader.close()
driver.get('https://eventreg.asu.edu/home')
driver.find_element(By.XPATH, '/html/body/div[1]/div/header/div/div/div/div[1]/div[2]/div/div/header/div[1]/div/div[1]/div/a').click()
login()
duo()
sleep(5)
driver.get('https://eventreg.asu.edu/node/add/event-registration-form')
sleep(2)

driver.find_element(By.XPATH, '//*[@id="edit-title"]').send_keys(club_name)
type = driver.find_element(By.XPATH, '//*[@id="edit_field_special_event_type_und_chosen"]').click()
sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/form/div/div[3]/div/div/fieldset[1]/div/fieldset[1]/div/div[1]/div/div[2]/div/div/input').send_keys('Meeting')
sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/form/div/div[3]/div/div/fieldset[1]/div/fieldset[1]/div/div[1]/div/div[2]/div/ul/li').click()
sleep(2)

driver.find_element(By.XPATH, '//*[@id="edit-field-description-und-0-value"]').send_keys(event_description)
driver.find_element(By.XPATH, '//*[@id="edit-field-event-producing-orgs-und-0-value"]').send_keys(club_name)
sleep(2)

orgQ = Select(driver.find_element(By.XPATH, '//*[@id="edit-field-stu-org-q-und"]'))
orgQ.select_by_value('2')

driver.find_element(By.XPATH, '//*[@id="edit-field-event-stu-org-name-und-0-value"]').send_keys(club_name)
driver.find_element(By.XPATH, '//*[@id="edit-field-orgsync-url-und-0-url"]').send_keys(club_url)
driver.find_element(By.XPATH, '//*[@id="edit-field-room-number-location-und-0-value"]').send_keys(room_num)
driver.find_element(By.XPATH, '//*[@id="edit-field-reservation-contact-name-und-0-value"]').send_keys(adv_name)
driver.find_element(By.XPATH, '//*[@id="edit-field-reservation-contact-phone-und-0-value"]').send_keys(adv_number)
driver.find_element(By.XPATH, '//*[@id="edit-field-reservation-contact-e-mail-und-0-email"]').send_keys(adv_email)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/form/div/div[3]/div/div/fieldset[1]/div/fieldset[5]/div/fieldset[1]/div/div[2]/div/div[2]/div[2]/label').click()
driver.find_element(By.XPATH, '//*[@id="edit-field-event-general-public-und"]').click()
sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/form/div/div[3]/div/div/fieldset[1]/div/fieldset[5]/div/fieldset[2]/div/div[1]/div/select/option[2]').click()
driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/div[1]/div[1]/fieldset[1]/div[1]/fieldset[5]/div[1]/fieldset[2]/div[1]/div[4]/div[1]/div[2]/div[2]/label[1]').click()
sleep(2)
driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/div[1]/div[1]/fieldset[1]/div[1]/fieldset[5]/div[1]/fieldset[2]/div[1]/div[4]/div[1]/div[2]/div[3]/label[1]').click()
sleep(3)
for i in range(125):
    ActionChains(driver).send_keys(Keys.TAB).perform() 
ActionChains(driver).send_keys(Keys.ENTER).perform() 


driver.find_element(By.XPATH, '//*[@id="edit-field-primary-contact-name-und-0-value"]').clear()
driver.find_element(By.XPATH, '//*[@id="edit-field-primary-contact-name-und-0-value"]').send_keys(cord_name)
driver.find_element(By.XPATH, '//*[@id="edit_field_asu_affiliation_und_chosen"]').click()
sleep(2)
input_bar = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/form/div/div[3]/div/div/fieldset[2]/div/fieldset[1]/div/div[3]/div/div/div/div/input')
input_bar.send_keys('Student')
input_bar.send_keys(Keys.DOWN)
input_bar.send_keys(Keys.ENTER)
driver.find_element(By.XPATH, '//*[@id="edit-field-primary-contact-email-und-0-email"]').clear()
driver.find_element(By.XPATH, '//*[@id="edit-field-primary-contact-email-und-0-email"]').send_keys(cord_email)
driver.find_element(By.XPATH, '//*[@id="edit-field-primary-contact-cell-phone-und-0-value"]').send_keys(cord_phone)
driver.find_element(By.XPATH, '//*[@id="edit-field-stu-org-officer-name-und-0-value"]').send_keys(officer_name)
driver.find_element(By.XPATH, '//*[@id="edit-field-stu-org-officer-emai-und-0-email"]').send_keys(officer_email)
driver.find_element(By.XPATH, '//*[@id="edit-field-stu-org-advisor-name-und-0-value"]').send_keys(adv_name)
driver.find_element(By.XPATH, '//*[@id="edit-field-stu-org-advisor-email-und-0-email"]').send_keys(adv_email)

for i in range(119):
    ActionChains(driver).send_keys(Keys.TAB).perform() 
sleep(5)
ActionChains(driver).send_keys(Keys.ENTER).perform() 

driver.find_element(By.XPATH, '//*[@id="edit-field-event-signature-und-0-value"]').send_keys(cord_name)
input('Enter event URL, Location, and Date then press enter: ')
driver.find_element(By.CSS_SELECTOR, '#edit-submit').click()
sleep(5)
SER = input("enter SER number: ")


#Rooms
driver.get('https://azstateu.aaiscloud.com/AZStateU/events/EventReqIntroForm.aspx')
sleep(5)
input_bar = driver.find_element(By.CSS_SELECTOR, '#EventReqForm_FormSelectorDialog_EventRequestFormSelectBox-inputEl')
input_bar.click()
sleep(2)
input_bar.send_keys('west')
sleep(3)
input_bar.send_keys(Keys.ENTER)
sleep(3)
driver.find_element(By.CSS_SELECTOR, '#EventReqForm_FormSelectorDialog_OKBtn').click()
sleep(5)
driver.find_element(By.CSS_SELECTOR, "#checkboxfield-1052-inputEl").click()
driver.find_element(By.CSS_SELECTOR, "#textfield-1054-inputEl").send_keys(eventName)
driver.find_element(By.CSS_SELECTOR, "#textfield-1056-inputEl").send_keys(club_name)
driver.find_element(By.CSS_SELECTOR, "#textfield-1058-inputEl").send_keys('Yes')
driver.find_element(By.CSS_SELECTOR, "#textfield-1060-inputEl").send_keys(cord_name)
driver.find_element(By.CSS_SELECTOR, "#textfield-1062-inputEl").send_keys(cord_email)
driver.find_element(By.CSS_SELECTOR, "#textfield-1064-inputEl").send_keys(cord_phone)
driver.find_element(By.CSS_SELECTOR, "#numberfield-1066-inputEl").send_keys('30')
event_type = driver.find_element(By.CSS_SELECTOR, '#browsecombo-1069-inputEl')
event_type.send_keys('student')
sleep(5)
event_type.send_keys(Keys.ENTER)
driver.find_element(By.CSS_SELECTOR, '#textfield-1071-inputEl').send_keys('No')
driver.find_element(By.CSS_SELECTOR, '#textfield-1073-inputEl').send_keys('No')
driver.find_element(By.CSS_SELECTOR, '#textfield-1075-inputEl').send_keys('No')
driver.find_element(By.CSS_SELECTOR, '#textareafield-1077-inputEl').send_keys(SER)
driver.find_element(By.CSS_SELECTOR, '#button-1082-btnEl').click()
input('Press Enter when meeting added: ')

sleep(3)
driver.find_element(By.CSS_SELECTOR, '#button-1085').click()
input('Press enter when room is selected: ')
sleep(2)
driver.find_element(By.CSS_SELECTOR, '#button-1043').click()

print('Event Created check email')
sleep(10)











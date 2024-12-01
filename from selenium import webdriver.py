from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("start-maximized")
versionid = "1.0.0"
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--log-level=3")  # Suppress console output
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://auth.edmentum.com/elf/login")

textbox = driver.find_element(By.ID, "AccountLogin")
usernamebox = driver.find_element(By.ID, "PlatoName")
passwordbox = driver.find_element(By.ID, "Password")



# Open the config.cfg file and read the account settings
with open("config.cfg", "r") as config_file:
    config_data = config_file.read()

# Extract the account, username, and password from the config data
account = config_data.split("account = ")[1].split("\n")[0].strip('"')
username = config_data.split("username = ")[1].split("\n")[0].strip('"')
password = config_data.split("password = ")[1].split("\n")[0].strip('"')

# Enter the username and password into the textbox
textbox.send_keys(account)
usernamebox.send_keys(username)
passwordbox.send_keys(password)
login_button = driver.find_element(By.ID, "loginButton")
login_button.click()
# Inject JavaScript code into the webpage

def reset(key):
    if key == "reset":
        driver.switch_to.default_content()
    elif key == "same":
        pass
    else:
        driver.switch_to.default_content()
        driver.switch_to.frame(key)
def checksname(frameofelement,elementname,resetkey):
    global driver
    reset(frameofelement)

    try:

        if driver.find_element(By.NAME, elementname):
            reset(resetkey)
            return True
    except:
        reset(resetkey)
        return False
def checkquestion():
    global driver
    try:
        reset("content-iframe")
        if driver.find_element(By.ID, "responseText_ifr"):

            return True
    except:

        return False
def next(element):
    global driver
    driver.switch_to.default_content()
    try:
        z = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/nav/button[3]")

    
    
        if z.get_attribute("class") == "tutorial-nav-next disabled":
            reset(element)
            return False
        elif z.get_attribute("class") == "tutorial-nav-next":
            reset(element)
            return True    
    except:
        pass
def checkfrq(element):
    global driver
    try:
        reset("content-iframe")
        
        if driver.find_elements(By.XPATH, "//span[@class='explanationMessage']"):
            reset(element)
            return True
            
    except:
        
        pass

while True:
    if "home" in driver.current_url:
        driver.execute_script('''
    // Create a new div element
    var messageBox = document.createElement("div");

    // Set the HTML content of the message box for multiple lines
    messageBox.innerHTML = "Please select a course,<br>made by bruhkeys<br>version ''' + versionid + '''<br>";

    // Apply styles to position it at the top right corner
    messageBox.style.position = "fixed";
    messageBox.style.top = "10px";
    messageBox.style.right = "10px";
    messageBox.style.padding = "10px";
    messageBox.style.backgroundColor = "lightblue";
    messageBox.style.border = "1px solid #000";
    messageBox.style.zIndex = 1000;

    // Append the message box to the body
    document.body.appendChild(messageBox);
''')
    if "courseware-delivery" in driver.current_url:

        

        try:
            
            WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/header/div/nav/button[3]")))
        except:
            pass
        if next("content-iframe") == False:
            print("done")
            try:
                driver.execute_script("""
for(let nav of document.getElementsByClassName('SampleAnswerNav')){
    nav.style = {}
    nav.firstElementChild.style.display = 'inline-block'
}

for(let nav of document.getElementsByClassName('buttonCorrectToggle')){
    nav.style.display = 'inline'
    nav.style.visibility = 'visible'
}""")
                a1 = driver.find_elements(By.CLASS_NAME, "buttonCorrectToggle")
                for i in range(len(a1)):
                    
                    a1[i].click()
                
            except:
                pass
            
            reset("content-iframe")
            
            buttons = driver.find_elements(By.CLASS_NAME, "buttonDone")
            for i in range(len(buttons)):
                try:
                    buttons[i].click()
                except:
                    pass
            try:
                driver.execute_script("arguments[0].click();", buttons[0])
            except:
                pass
                
            


        


            

        else:
            try:

                reset("reset")
                next_button = driver.find_element(By.CLASS_NAME, "tutorial-nav-next")
                next_button.click()
            except:
                pass
        
            

            
        

        

    pass
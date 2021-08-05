import pandas as pd
from selenium import webdriver
import pickle
from datetime import date
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


       
driver = webdriver.Chrome('chrome/chromedriver.exe')

#get cookies
# pickle.dump(driver.get_cookies() , open("chrome/chromedata/cookies.pkl","wb"))

#go to linkedin
driver.get('https://www.linkedin.com')

#add cookies
cookies = pickle.load(open('chrome/chromedata/cookies.pkl', 'rb'))

for cookie in cookies:
    driver.add_cookie(cookie)
    

driver.get('https://www.linkedin.com/jobs/search/?distance=25&geoId=108739038&keywords=software&location=Buenos%20Aires%2C%20Buenos%20Aires%20Province%2C%20Argentina')

#get value
val = driver.find_elements_by_css_selector('small')[0].text

# parse value

val_parsed = int(''.join([digit for digit in val if digit.isdigit()]))
date_today = date.today()

#set pandas DF
df= pd.DataFrame({'date':[date_today],
                  'software_jobs_caba': [val_parsed]})


driver.close()

#auth to Google Drive
gauth = GoogleAuth()

# Try to load saved client credentials
gauth.LoadCredentialsFile('mycreds.txt')
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
    
# Save the current credentials to a file
gauth.SaveCredentialsFile('mycreds.txt')

gauth.LocalWebserverAuth()


drive = GoogleDrive(gauth)

# create file
# file1 = drive.CreateFile({"title" : 'software_emp.csv',
#                           "mimeType": "text/csv"})
# file1.SetContentFile("file/software_emp.csv")
# file1.Upload()

#read file
file1 = drive.CreateFile({'id': '1eX7BYCDEMPynodr5KWeu5JUWzgkiu-C7'})
file1.GetContentFile('file/software_emp.csv')

df_old = pd.read_csv('file/software_emp.csv')

# add scrap

df_appended = df_old.append(df)
df_appended.to_csv("file/software_emp.csv", index=False)

#update file
file2 = drive.CreateFile({'id': '1eX7BYCDEMPynodr5KWeu5JUWzgkiu-C7'})
file2.SetContentFile('file/software_emp.csv')
file2.Upload() 


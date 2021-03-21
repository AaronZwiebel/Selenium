import os.path
import platform
import requests
import zipfile

platString = (str(platform.platform()))

#Checks if either the chromedriver or chromedriver.exe files exist in your files
if ((os.path.exists("Resources/chromedriver.exe")) == False) or ((os.path.exists("Resources/chromedriver")) == False):
        if "Window" in platString:
            url = ("https://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_win32.zip")
        elif "Linux" in platString:
            url = ("https://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_linux64.zip")
        elif "Mac" in platString:
            url = ("https://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_mac64.zip")

            if ((os.path.exists("Resources/chromedriver.exe")) == False) or (
                    (os.path.exists("Resources/chromedriver")) == False):
                if "Window" in platString:
                    url = ("https://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_win32.zip")
                elif "Linux" in platString:
                    url = ("https://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_linux64.zip")
                elif "Mac" in platString:
                    url = ("https://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_mac64.zip")

target_path = 'DesignatedDriver.zip'
response = requests.get(url, stream=True)
handle = open(target_path, "wb")
for chunk in response.iter_content(chunk_size=512):
    if chunk:  # filter out keep-alive new chunks
        handle.write(chunk)
handle.close()
with zipfile.ZipFile("DesignatedDriver.zip", "r") as zip_ref:
    zip_ref.extractall("Resources")
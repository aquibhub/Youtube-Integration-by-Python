import time
import random
from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\Assemblage\Documents\chromedriver.exe")

videos = [
'https://www.youtube.com/watch?v=gnUQZI3d5XQ',
]

sleep_time = 0

for i in range(100):
    print("Watching for {} time".format(i))
    #random_video = random.randint(0,5)
    #driver.get(videos[random_video])
    time.sleep(sleep_time) # Let the user actually see something!
    sleep_time = random.randint(60, 130)

time.sleep(5) # Let the user actually see something!
driver.quit()

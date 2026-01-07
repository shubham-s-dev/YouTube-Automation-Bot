import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# SETUP
# your search input
query = input("What do you like to search on YouTube:  ")
if not query:
    print("didn't provide input.")
    exit()
print("opening chrome")

options = Options()
# options.add_argument("--headless=new") # it's your choice agar chrome window dekhi hai toh (demo only)
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15) # youtube take time so add 15 sec time

# ek empty list data store ke liye
your_data = []

try:

    print("Opening YouTube...")
    driver.get("https://www.youtube.com/")

    # YouTube ka search box ka name="search_query" hota hai
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "search_query")))
    
    print(f"Typing: '{query}'...") 
    search_box.click()
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN) # Enter button dabaya
    
    print("wait for result")
    
    # YouTube par video title ka ID "video-title" hota hai
    wait.until(EC.presence_of_element_located((By.ID, "video-title")))
    
    time.sleep(3) 

    videos = driver.find_elements(By.ID, "video-title")
    
    print(f"Found {len(videos)} videos. Extracting Top 5...")
    

    for video in videos[:5]:
        title = video.get_attribute("title")
        link = video.get_attribute("href")

        if title and link:
            print(f"   {title[:30]}...")
            your_data.append({
                "Title": title,
                "Link": link
            })

except Exception as e:
    print(f" Error: {e}")

finally:
    driver.quit()

# export to excel file(csv)
print("-" * 30)
if len(your_data) > 0:
    df = pd.DataFrame(your_data)
    # file mei _ add na ho isliye replace(e.g., youtube_Python.csv)
    filename = f"youtube_{query.replace(' ', '_')}.csv"
    df.to_csv(filename, index=False)
    print(f" Success! Data saved to '{filename}'")
else:
    print(" No data found.")
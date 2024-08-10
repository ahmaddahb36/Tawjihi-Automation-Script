import requests
import time
import pygame
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def check_website(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers, verify=False)  # Disable SSL verification for testing
        if response.status_code in [200, 304]:
            return True
        else:
            print(f"Unexpected status code {response.status_code} received from {url}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error checking {url}: {e}")
        return False

def play_sound(file_path):
    pygame.mixer.init()
    sound = pygame.mixer.Sound(file_path)
    sound.play()

def interact_with_page():
    # Initialize the Chrome WebDriver (update if using a different driver or path)
    driver = webdriver.Chrome()  # Replace with the path if needed && you can change the brawser to other brawser like Firefox()

    try:
        while True:  # Retry loop
            driver.get("https://tawjihi.jo")  # Replace with the actual URL

            try:
                # Wait for the page to load
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "number")))

                # Find and interact with the input fields
                driver.find_element(By.ID, "number").send_keys("123456") # replace it to your tawjihi ID <-----------

                # Select the day
                day_input = driver.find_element(By.ID, "day")
                day_input.click()
                time.sleep(1)
                day_input.send_keys(Keys.ARROW_DOWN)
                time.sleep(1)
                day_input.send_keys("25") # replace it to your barth day <-----------
                day_input.send_keys(Keys.ENTER)

                # Select the month
                month_input = driver.find_element(By.ID, "month")
                month_input.click()
                time.sleep(1)
                month_input.send_keys(Keys.ARROW_DOWN)
                time.sleep(1)
                month_input.send_keys("7") # replace it to your barth month <-----------
                month_input.send_keys(Keys.ENTER)

                # Select the year
                year_input = driver.find_element(By.ID, "year")
                year_input.click()
                time.sleep(1)
                year_input.send_keys(Keys.ARROW_DOWN)
                time.sleep(1)
                year_input.send_keys("2000") # replace it to your barth year <-----------
                year_input.send_keys(Keys.ENTER)
                # Find and click the button
                button = driver.find_element(By.XPATH, "//button[@type='button' and contains(@class, 'action-btn')]")
                if button.is_enabled():
                    button.click()
                else:
                    print("The button is disabled.")

                # Wait to see the result
                time.sleep(15)

                # Take a screenshot and save it
                screenshot_path = "Path_to_save_screenshot.png" # Enter the path to save the screenshot to <-----------
                driver.save_screenshot(screenshot_path)
                print(f"Screenshot saved to {screenshot_path}")
                 # Keep the browser open
                print("Browser will remain open. You can manually close it when done.")
                input("Press Enter to close the browser...")  # Wait for user input to close
                play_sound("Path_to_sound.wav")# Replace with the path to your WAV file || if you not need it makr the line as a comment <-----------

                break  # Exit the retry loop if successful

            except Exception as e:
                print(f"Error during page interaction: {e}")
                print("Refreshing the page...")
                driver.refresh()
                time.sleep(5)  # Wait before retrying

    finally:
        # Close the browser only after user input
        driver.quit()

if __name__ == "__main__":
    website_url = "https://tawjihi.jo"  # URL to check
    sound_file = "Path_to_sound.wav"  # Replace with the path to your WAV file  <-----------
        
    while True:
        if check_website(website_url):
            print(f"The website {website_url} is active.")
            play_sound(sound_file) # play sound if the site is active
            interact_with_page()  # Perform web interactions if the site is active
            break  # Exit loop after performing actions
        else:
            print(f"The website {website_url} is not active.")
        time.sleep(10) # Time to recheck the site 

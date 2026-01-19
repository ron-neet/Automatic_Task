from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# -------------------------------
# Generate 100 test users
# -------------------------------
test_data = [
    {
        "username": f"testUser{i:03}",
        "password": "Test@1234",
        "creditCard": f"4111111111111{i:03}",
        "telephone": f"(999) 888-{i:04}",
        "valid": True
    }
    for i in range(1, 101)
]

# -------------------------------
# Function to submit one user's form
# -------------------------------
def submit_form(data, index):
    # Headless Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run without UI
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1200,800")
    
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get("https://chulo-solutions.github.io/qa-internship/")
        time.sleep(1)
        
        # Fill form fields
        driver.find_element(By.ID, "username").send_keys(data["username"])
        driver.find_element(By.ID, "password").send_keys(data["password"])
        driver.find_element(By.ID, "creditCard").send_keys(data["creditCard"])
        driver.find_element(By.ID, "telephone").send_keys(data["telephone"])
        
        # Submit the form
        driver.find_element(By.TAG_NAME, "button").click()
        time.sleep(1)
        
        # Validate success message
        if data["valid"]:
            try:
                success_msg = driver.find_element(By.ID, "successMessage").text
                if "successful" in success_msg.lower():
                    print(f"✅ User {index}: {data['username']} submitted successfully")
                else:
                    print(f"❌ User {index}: {data['username']} submission failed")
            except:
                print(f"❌ User {index}: {data['username']} no success message")
        else:
            # Negative test placeholder
            print(f"⚠️ User {index}: {data['username']} submitted (invalid data)")
    except Exception as e:
        print(f"❌ User {index}: {data['username']} error -> {e}")
    finally:
        driver.quit()

# -------------------------------
# Run users in batches concurrently
# -------------------------------
batch_size = 1  # Number of concurrent users at a time

with ThreadPoolExecutor(max_workers=batch_size) as executor:
    futures = [executor.submit(submit_form, user, i+1) for i, user in enumerate(test_data)]
    
    # Wait for all submissions to complete
    for future in as_completed(futures):
        pass  # Just ensure all threads finish

print("✅ All 100 user submissions completed!")

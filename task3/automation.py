from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://chulo-solutions.github.io/qa-internship/")
time.sleep(2)

test_data = [
    # 1-20: Valid data
    {"username": "testUser01", "password": "Test@1234", "creditCard": "4111111111111111", "telephone": "(999) 888-0001", "valid": True},
    {"username": "testUser02", "password": "Pass@5678", "creditCard": "4111111111111112", "telephone": "(999) 888-0002", "valid": True},
    {"username": "userAlice03", "password": "Alice@123", "creditCard": "4111111111111113", "telephone": "(999) 888-0003", "valid": True},
    {"username": "userBob04", "password": "Bob@4567", "creditCard": "4111111111111114", "telephone": "(999) 888-0004", "valid": True},
    {"username": "johnDoe05", "password": "John@890", "creditCard": "4111111111111115", "telephone": "(999) 888-0005", "valid": True},
    {"username": "marySue06", "password": "Mary@234", "creditCard": "4111111111111116", "telephone": "(999) 888-0006", "valid": True},
    {"username": "samSmith07", "password": "Sam@678", "creditCard": "4111111111111117", "telephone": "(999) 888-0007", "valid": True},
    {"username": "lindaLee08", "password": "Linda@901", "creditCard": "4111111111111118", "telephone": "(999) 888-0008", "valid": True},
    {"username": "charlie09", "password": "Char@345", "creditCard": "4111111111111119", "telephone": "(999) 888-0009", "valid": True},
    {"username": "emmaWatson10", "password": "Emma@678", "creditCard": "4111111111111120", "telephone": "(999) 888-0010", "valid": True},
    {"username": "oliver11", "password": "Oliv@123", "creditCard": "4111111111111121", "telephone": "(999) 888-0011", "valid": True},
    {"username": "ava12", "password": "Ava@456", "creditCard": "4111111111111122", "telephone": "(999) 888-0012", "valid": True},
    {"username": "liam13", "password": "Liam@789", "creditCard": "4111111111111123", "telephone": "(999) 888-0013", "valid": True},
    {"username": "sophia14", "password": "Soph@234", "creditCard": "4111111111111124", "telephone": "(999) 888-0014", "valid": True},
    {"username": "mason15", "password": "Maso@567", "creditCard": "4111111111111125", "telephone": "(999) 888-0015", "valid": True},
    {"username": "isabella16", "password": "Isab@890", "creditCard": "4111111111111126", "telephone": "(999) 888-0016", "valid": True},
    {"username": "jacob17", "password": "Jac@123", "creditCard": "4111111111111127", "telephone": "(999) 888-0017", "valid": True},
    {"username": "mia18", "password": "Mia@456", "creditCard": "4111111111111128", "telephone": "(999) 888-0018", "valid": True},
    {"username": "ethan19", "password": "Eth@789", "creditCard": "4111111111111129", "telephone": "(999) 888-0019", "valid": True},
    {"username": "charlotte20", "password": "Char@234", "creditCard": "4111111111111130", "telephone": "(999) 888-0020", "valid": True},

    # 21-60: Invalid usernames or passwords
    {"username": "a", "password": "Test@1234", "creditCard": "4111111111111131", "telephone": "(999) 888-0021", "valid": False},
    {"username": "ab", "password": "123", "creditCard": "4111111111111132", "telephone": "(999) 888-0022", "valid": False},
    {"username": "user!", "password": "pass", "creditCard": "4111111111111133", "telephone": "(999) 888-0023", "valid": False},
    {"username": "test#", "password": "pwd", "creditCard": "4111111111111134", "telephone": "(999) 888-0024", "valid": False},
    {"username": "invalid$", "password": "1234", "creditCard": "4111111111111135", "telephone": "(999) 888-0025", "valid": False},
    {"username": "longusername"*5, "password": "pass@1", "creditCard": "4111111111111136", "telephone": "(999) 888-0026", "valid": False},
    {"username": "", "password": "Test@1234", "creditCard": "4111111111111137", "telephone": "(999) 888-0027", "valid": False},
    {"username": "user21", "password": "", "creditCard": "4111111111111138", "telephone": "(999) 888-0028", "valid": False},
    {"username": "user22", "password": "nopass", "creditCard": "4111111111111139", "telephone": "(999) 888-0029", "valid": False},
    {"username": "user23", "password": "123", "creditCard": "4111111111111140", "telephone": "(999) 888-0030", "valid": False},
    {"username": "user24", "password": "aaaa", "creditCard": "4111111111111141", "telephone": "(999) 888-0031", "valid": False},
    {"username": "user25", "password": "bbbb", "creditCard": "4111111111111142", "telephone": "(999) 888-0032", "valid": False},
    {"username": "user26", "password": "cccc", "creditCard": "4111111111111143", "telephone": "(999) 888-0033", "valid": False},
    {"username": "user27", "password": "dddd", "creditCard": "4111111111111144", "telephone": "(999) 888-0034", "valid": False},
    {"username": "user28", "password": "eeee", "creditCard": "4111111111111145", "telephone": "(999) 888-0035", "valid": False},
    {"username": "user29", "password": "ffff", "creditCard": "4111111111111146", "telephone": "(999) 888-0036", "valid": False},
    {"username": "user30", "password": "gggg", "creditCard": "4111111111111147", "telephone": "(999) 888-0037", "valid": False},
    {"username": "user31", "password": "hhhh", "creditCard": "4111111111111148", "telephone": "(999) 888-0038", "valid": False},
    {"username": "user32", "password": "iiii", "creditCard": "4111111111111149", "telephone": "(999) 888-0039", "valid": False},
    {"username": "user33", "password": "jjjj", "creditCard": "4111111111111150", "telephone": "(999) 888-0040", "valid": False},
    {"username": "user34", "password": "kkkk", "creditCard": "4111111111111151", "telephone": "(999) 888-0041", "valid": False},
    {"username": "user35", "password": "llll", "creditCard": "4111111111111152", "telephone": "(999) 888-0042", "valid": False},
    {"username": "user36", "password": "mmmm", "creditCard": "4111111111111153", "telephone": "(999) 888-0043", "valid": False},
    {"username": "user37", "password": "nnnn", "creditCard": "4111111111111154", "telephone": "(999) 888-0044", "valid": False},
    {"username": "user38", "password": "oooo", "creditCard": "4111111111111155", "telephone": "(999) 888-0045", "valid": False},
    {"username": "user39", "password": "pppp", "creditCard": "4111111111111156", "telephone": "(999) 888-0046", "valid": False},
    {"username": "user40", "password": "qqqq", "creditCard": "4111111111111157", "telephone": "(999) 888-0047", "valid": False},
    {"username": "user41", "password": "rrrr", "creditCard": "4111111111111158", "telephone": "(999) 888-0048", "valid": False},
    {"username": "user42", "password": "ssss", "creditCard": "4111111111111159", "telephone": "(999) 888-0049", "valid": False},
    {"username": "user43", "password": "tttt", "creditCard": "4111111111111160", "telephone": "(999) 888-0050", "valid": False},
    {"username": "user44", "password": "uuuu", "creditCard": "4111111111111161", "telephone": "(999) 888-0051", "valid": False},
    {"username": "user45", "password": "vvvv", "creditCard": "4111111111111162", "telephone": "(999) 888-0052", "valid": False},
    {"username": "user46", "password": "wwww", "creditCard": "4111111111111163", "telephone": "(999) 888-0053", "valid": False},
    {"username": "user47", "password": "xxxx", "creditCard": "4111111111111164", "telephone": "(999) 888-0054", "valid": False},
    {"username": "user48", "password": "yyyy", "creditCard": "4111111111111165", "telephone": "(999) 888-0055", "valid": False},
    {"username": "user49", "password": "zzzz", "creditCard": "4111111111111166", "telephone": "(999) 888-0056", "valid": False},
    {"username": "user50", "password": "aaaa", "creditCard": "4111111111111167", "telephone": "(999) 888-0057", "valid": False},

    # 51-100: Invalid credit card or telephone numbers
    {"username": "user51", "password": "Test@123", "creditCard": "1234", "telephone": "(999) 888-0058", "valid": False},
    {"username": "user52", "password": "Test@123", "creditCard": "abcd", "telephone": "(999) 888-0059", "valid": False},
    {"username": "user53", "password": "Test@123", "creditCard": "4111", "telephone": "9998880060", "valid": False},
    {"username": "user54", "password": "Test@123", "creditCard": "0000000000000000", "telephone": "9998880061", "valid": False},
    {"username": "user55", "password": "Test@123", "creditCard": "4111111111111170", "telephone": "abcd", "valid": False},
    {"username": "user56", "password": "Test@123", "creditCard": "4111111111111171", "telephone": "123", "valid": False},
    {"username": "user57", "password": "Test@123", "creditCard": "4111111111111172", "telephone": "", "valid": False},
    {"username": "user58", "password": "Test@123", "creditCard": "", "telephone": "(999) 888-0062", "valid": False},
    {"username": "user59", "password": "Test@123", "creditCard": "4111111111111174", "telephone": "9998880063", "valid": False},
    {"username": "user60", "password": "Test@123", "creditCard": "4111111111111175", "telephone": "9998880064", "valid": False},
    {"username": "user61", "password": "Pass@123", "creditCard": "4111111111111176", "telephone": "9998880065", "valid": False},
    {"username": "user62", "password": "Pass@123", "creditCard": "4111111111111177", "telephone": "9998880066", "valid": False},
    {"username": "user63", "password": "Pass@123", "creditCard": "4111111111111178", "telephone": "9998880067", "valid": False},
    {"username": "user64", "password": "Pass@123", "creditCard": "4111111111111179", "telephone": "9998880068", "valid": False},
    {"username": "user65", "password": "Pass@123", "creditCard": "4111111111111180", "telephone": "9998880069", "valid": False},
    {"username": "user66", "password": "Pass@123", "creditCard": "4111111111111181", "telephone": "9998880070", "valid": False},
    {"username": "user67", "password": "Pass@123", "creditCard": "4111111111111182", "telephone": "9998880071", "valid": False},
    {"username": "user68", "password": "Pass@123", "creditCard": "4111111111111183", "telephone": "9998880072", "valid": False},
    {"username": "user69", "password": "Pass@123", "creditCard": "4111111111111184", "telephone": "9998880073", "valid": False},
    {"username": "user70", "password": "Pass@123", "creditCard": "4111111111111185", "telephone": "9998880074", "valid": False},
    {"username": "user71", "password": "Pass@123", "creditCard": "4111111111111186", "telephone": "9998880075", "valid": False},
    {"username": "user72", "password": "Pass@123", "creditCard": "4111111111111187", "telephone": "9998880076", "valid": False},
    {"username": "user73", "password": "Pass@123", "creditCard": "4111111111111188", "telephone": "9998880077", "valid": False},
    {"username": "user74", "password": "Pass@123", "creditCard": "4111111111111189", "telephone": "9998880078", "valid": False},
    {"username": "user75", "password": "Pass@123", "creditCard": "4111111111111190", "telephone": "9998880079", "valid": False},
    {"username": "user76", "password": "Pass@123", "creditCard": "4111111111111191", "telephone": "9998880080", "valid": False},
    {"username": "user77", "password": "Pass@123", "creditCard": "4111111111111192", "telephone": "9998880081", "valid": False},
    {"username": "user78", "password": "Pass@123", "creditCard": "4111111111111193", "telephone": "9998880082", "valid": False},
    {"username": "user79", "password": "Pass@123", "creditCard": "4111111111111194", "telephone": "9998880083", "valid": False},
    {"username": "user80", "password": "Pass@123", "creditCard": "4111111111111195", "telephone": "9998880084", "valid": False},
    {"username": "user81", "password": "Pass@123", "creditCard": "4111111111111196", "telephone": "9998880085", "valid": False},
    {"username": "user82", "password": "Pass@123", "creditCard": "4111111111111197", "telephone": "9998880086", "valid": False},
    {"username": "user83", "password": "Pass@123", "creditCard": "4111111111111198", "telephone": "9998880087", "valid": False},
    {"username": "user84", "password": "Pass@123", "creditCard": "4111111111111199", "telephone": "9998880088", "valid": False},
    {"username": "user85", "password": "Pass@123", "creditCard": "4111111111111200", "telephone": "9998880089", "valid": False},
    {"username": "user86", "password": "Pass@123", "creditCard": "4111111111111201", "telephone": "9998880090", "valid": False},
    {"username": "user87", "password": "Pass@123", "creditCard": "4111111111111202", "telephone": "9998880091", "valid": False},
    {"username": "user88", "password": "Pass@123", "creditCard": "4111111111111203", "telephone": "9998880092", "valid": False},
    {"username": "user89", "password": "Pass@123", "creditCard": "4111111111111204", "telephone": "9998880093", "valid": False},
    {"username": "user90", "password": "Pass@123", "creditCard": "4111111111111205", "telephone": "9998880094", "valid": False},
    {"username": "user91", "password": "Pass@123", "creditCard": "4111111111111206", "telephone": "9998880095", "valid": False},
    {"username": "user92", "password": "Pass@123", "creditCard": "4111111111111207", "telephone": "9998880096", "valid": False},
    {"username": "user93", "password": "Pass@123", "creditCard": "4111111111111208", "telephone": "9998880097", "valid": False},
    {"username": "user94", "password": "Pass@123", "creditCard": "4111111111111209", "telephone": "9998880098", "valid": False},
    {"username": "user95", "password": "Pass@123", "creditCard": "4111111111111210", "telephone": "9998880099", "valid": False},
    {"username": "user96", "password": "Pass@123", "creditCard": "4111111111111211", "telephone": "9998880100", "valid": False},
    {"username": "user97", "password": "Pass@123", "creditCard": "4111111111111212", "telephone": "9998880101", "valid": False},
    {"username": "user98", "password": "Pass@123", "creditCard": "4111111111111213", "telephone": "9998880102", "valid": False},
    {"username": "user99", "password": "Pass@123", "creditCard": "4111111111111214", "telephone": "9998880103", "valid": False},
    {"username": "user100", "password": "Pass@123", "creditCard": "4111111111111215", "telephone": "9998880104", "valid": False},
]


for i, data in enumerate(test_data, start=1):
    # Clear the form or refresh the page
    driver.refresh()
    time.sleep(1)
    
    # Fill the form
    driver.find_element(By.ID, "username").send_keys(data["username"])
    driver.find_element(By.ID, "password").send_keys(data["password"])
    driver.find_element(By.ID, "creditCard").send_keys(data["creditCard"])
    driver.find_element(By.ID, "telephone").send_keys(data["telephone"])
    
    # Submit the form
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    
    # Check result
    if data["valid"]:
        try:
            success_msg = driver.find_element(By.ID, "successMessage").text
            assert "successful" in success_msg.lower()
            print(f"✅ Test {i}: Passed (valid data)")
        except:
            print(f"❌ Test {i}: Failed (valid data)")
    else:
        try:
            error_msg = driver.find_element(By.CLASS_NAME, "error-message").text
            print(f"✅ Test {i}: Correctly caught invalid data")
        except:
            print(f"❌ Test {i}: Invalid data was accepted!")

driver.quit()

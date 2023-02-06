# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# import re
class ProfileScraper():
    def __init__(self):
        print ("here")
        
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)
        
        self.profiles = {
            "codechef": {"https://www.codechef.com/users/sanchita170676": "//h5[contains(text(), 'Fully Solved')]"},
            "codeforces": {"https://codeforces.com/profile/sanchita170676": "//div[contains(@class, '_UserActivityFrame_counterValue')]"},
            "spoj": {"https://www.spoj.com/users/sanchita170676/": "//dl[contains(@class, 'profile-info-data')]/dd"},
            "leetcode": {"https://leetcode.com/sanchitamishra170676/": "//div[contains(@class, 'total-solved-count')]"},
            "gfg": {"https://auth.geeksforgeeks.org/user/sanchitamishra170676/practice": "//a[contains(text(), 'Problems Solved')]"},
        }
#         print(self.profiles)
        print( self.getProfiles())
        
        
    
    def getProfiles(self):
        print("here2")
        totalQuestions = 0
        for platform, data in self.profiles.items():
            for profile, query in data.items():
#                 print(profile," -> ", query)
                questions = self.runQuery(profile, query)
                print(profile, " ", questions, end="\n")
                totalQuestions += int(questions)
        return totalQuestions
    
    
    def runQuery(self, profile, query):
        try:
            self.driver.get(profile)
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, query))
            )
            questions = int(re.search(r'\d+', element.text).group())
            return questions
        except:
            return '0'
        
ProfileScraper()
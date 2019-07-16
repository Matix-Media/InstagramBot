from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os


class msgs:
    def welcome():
        print('---====::::INSTAGRAM BOT::::====---')
        print('                                   ')
        print('                 by                ')
        print('         Matix Media, Inc.         ')
        print('                                   ')
        print('        created: 15.07.2019        ')
        print('===================================')
        print('')
        print('')

class InstagramBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        print("IB-C:: Starting Firefox Browser...")
        self.bot = webdriver.Firefox()
        print("IB-C:: Firefox Browser started!")

    def login(self):
        bot = self.bot
        print("IB-C:: Navigate to the login page of Instagram...")
        bot.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)
        print("IB-C:: Successfully navigated to the login page of Instagram!")
        username_box = bot.find_element_by_name('username')
        password_box = bot.find_element_by_name('password')
        username_box.clear()
        password_box.clear()
        username_box.send_keys(self.username)
        password_box.send_keys(self.password)
        password_box.send_keys(Keys.RETURN)
        print("IB-C:: Try to login...")
        time.sleep(3)
        print("IB-C:: Login data sent!")
    
    def gettag(self,hashtag,scrolls):
        bot = self.bot
        print("IB-C:: Navigate to the hashtag '#"+hashtag+"'...")
        bot.get('https://www.instagram.com/explore/tags/'+hashtag+'/')
        time.sleep(3)
        print("IB-C:: Successful to hashtag '#"+hashtag+"' navigated!")
        
        

    def likeImages(self,scrolls):
        done_scrolls = 0
        bot = self.bot
        print("IB-C:: Search for all Links...")
        links = []
        for i in range(1,scrolls):
            print("IB-C:: Scroll to the bottom of the page (" + str(done_scrolls + 1) + " of " + str(scrolls) + " Scrolls)...")
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            print("IB-C:: At the end of the page!", end='\r')
            done_scrolls = done_scrolls + 1
            time.sleep(1)

            found_links = bot.find_elements_by_tag_name('a')

            for elem in found_links:
                links.append(elem.get_attribute('href'))
            #links.extend = found_links

            found_links_count = 0
            for elem in found_links:
                found_links_count = found_links_count + 1
                print("IB-C:: " + str(elem.get_attribute('href')), end='\r')

            print("IB-C:: Found links: " + str(found_links_count) + " Links                                                ")
        time.sleep(3)

        links_count = 0
        links_used_count = 0
        links_used = []
        print("IB-C:: ALL LINKS:")
        for elem2 in links:
            links_count = links_count + 1
            
            link_str = elem2
            if "/p/" in link_str:
                if not link_str in links_used:
                    print(link_str, end='\r')
                    links_used_count = links_used_count + 1
                    links_used.append(link_str)

        print('')
        print("IB-C:: Found links: " + str(links_count) + " Links")
        print('')
        print("IB-C:: Links to posts: " + str(links_used_count) + "Links")
        print('')
        print('')
        print("IB-C:: Start working on links...")
        liked_posts = 0
        links_error = 0
        for link in links_used:
            print('')
            print('__________________________________________________________')
            print('IB-C:: Post ' + str(liked_posts + 1) + ' of ' + str(links_used_count) + ' Posts:')
            print('IB-C:: Lädt...', end='\r')
            bot.get(link)
            time.sleep(4)
            print("IB-C:: Try to Like Post '" + link + "'...")
            try:
                bot.find_element_by_class_name('glyphsSpriteHeart__outline__24__grey_9').click()
                print("IB-C:: Post '" + link + "' Successfully liked!")
                time.sleep(1)
                liked_posts = liked_posts + 1
            except Exception as ex:
                print("IB-C:: Error while liking the post (Maybe the post was deleted or the link is not available anymore or you already liked this post): ")
                print(ex)
                print("IB-C:: Previous mistakes when liking " + str(liked_posts) + " Posts: " + str(links_error) + " Errors")
                print("IB-C:: Try again in 30 seconds at the next post!", end='\r')
                time.sleep(1)
                links_error = links_error + 1
                for i in range(1,29):
                    time.sleep(1)
                    print("IB-C:: Try again in " + str(30 - i) + " seconds at the next post!", end='\r')
                    
                    
                print('')
        print('')
  
        msgs.welcome()
        print(str(links_used_count - links_error) + ' of ' + str(links_used_count) + ' Posts liked successfully!')
        bot.get('https://www.instagram.com/'+self.username+'/')
        input("IB-C <<>>")
        bot.quit()





#welcome massage
msgs.welcome()
time.sleep(2)

#inputs
input_username = input("Your username: ")
print("Your username is '"+input_username+"'")

print('')
input_password = input("Your password for '"+input_username+"': ")
print("Your password for the user '"+input_username+"' is '"+input_password+"'")

print('')
print('The 15 most popular hashtags on Instagram (as of 15.07.2019):')
fav_hashtags = ['#love', '#instagood', '#photooftheday', '#fashion', '#beautiful', '#happy', '#cute', '#tbt', '#like4like', '#followme', '#picoftheday', '#follow', '#me', '#selfie', '#summer']
for hashtag in fav_hashtags:
    print('  ★ '+hashtag)

print('')
input_hashtag = input("Hashtag: #")
print("Your entered hashtag is '#"+input_hashtag+"'")

print('')
input_scrolls = round(int(input("Posts to be liked (At least 3): ")) / 5)
print("It will be about " + str(input_scrolls * 6) + " Liked posts!")
print('')
print('')
print('Starting InstagramBot by Matix Media, Inc. ...')
time.sleep(3)


msgs.welcome()
print('')

#run code
mx = InstagramBot(input_username, input_password)

mx.login()

mx.gettag(input_hashtag, input_scrolls)

mx.likeImages(input_scrolls)
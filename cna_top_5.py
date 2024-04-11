from bs4 import BeautifulSoup
import requests


class CNATop5:
    def __init__(self):
        #setting up instance variables
        self.website = requests.get("https://www.channelnewsasia.com/")
        self.soup = BeautifulSoup(self.website.text, 'html.parser')

        #core program loop
        self.get_top5()
        self.display_top5()


    def get_top5(self):
        #this gives us all the large headlines
        headlines = self.soup.find_all('a', attrs= {'class':'h3__link list-object__heading-link'})

        #now let's reformat them as just a list of words without the fluff. the string splitting is for newline and whitespace removal.
        headlines_top5 = [headline.text[7:len(headline)-4] for headline in headlines[0:5]]

        #the next task is to number them, let's use a dictionary and save it as an instance variable.
        self.top5_dict = {}
        for num, line in zip(range(1,6), headlines_top5):
            self.top5_dict[num] = line
        
        return
        
    
    #we are seperating out the display method because we don't want to create a new top 5 list every time we want to display it.
    def display_top5(self):
        print("Below are the top 5 articles on CNA right now!\n")

        for num, line in self.top5_dict.items():
            print(f"{str(num)}. {line}")
        
        return
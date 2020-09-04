from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from chatterbot import ChatBot
'''from chatterbot.trainers import ChatterBotCorpusTrainer''' #Training the chatbot on corpus mode
from chatterbot.trainers import ListTrainer #Training the chatbot on Listening mode
import logging
logging.basicConfig(level=logging.CRITICAL) #remove logs from terminal
from time import sleep




class scrapping_massages():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='/home/cleomenezes/Projetos/Autochatbox/chromedriver_linux64/chromedriver')
        self.driver.get("https://web.whatsapp.com/")
        sleep(10)

            
    def get_person(self):
        person = self.driver.find_element_by_xpath(f"//span[@title='{str('BotTest')}']") #BotTest was a contact that I created to test this. 
        sleep(3)                                                                             # ^ replace with the desired contact name. Next version I will put a easier and auto way to do it
        person.click()


    def get_msg(self):
        msg = self.driver.find_elements_by_class_name('z_tTQ')
        self.last_massage = len(msg) -1

        text_msg = msg[self.last_massage].find_elements_by_css_selector('span.selectable-text')
        self.text_msg = text_msg[len(text_msg) -1].text
        return self.text_msg


    def chat_bot(self):
        
        bot = ChatBot("Mr.MenezesBot")
        #Training the chatbot on Listening mode
        conversation = ["Opa", "diga", "valeu", "falou"] #Here a put some different words, nothing especial
        trainer = ListTrainer(bot)
        trainer.train(conversation)

        #Training the chatbot on corpus mode
        '''trainer = ChatterBotCorpusTrainer(bot)
        trainer = ListTrainer(bot)
        trainer.train("chatterbot.corpus.portuguese")'''


        while True:
            text_msg = self.get_msg()
            text_msg = str(text_msg)

            if text_msg != self.last_massage and text_msg[0] != '⠀':
                self.last_massage = text_msg
                user_input = text_msg

                self.bot_answer = bot.get_response(user_input)

                chatbox = self.driver.find_element_by_class_name("_3uMse")
                sleep(2)
                chatbox.click()
                chatbox.send_keys("⠀" + str(self.bot_answer))
                send_botton = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                sleep(2)

                send_botton.click()
                sleep(5)



run = scrapping_massages()
run.get_person()
sleep(8)
run.chat_bot()
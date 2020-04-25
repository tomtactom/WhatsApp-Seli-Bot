#!/usr/bin/python python
# -*- coding: utf-8 -*-

class WaBot():
    # Libraries importieren
    import urllib.request
    import urllib.parse
    import time
    from selenium import webdriver
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By

    from bs4 import BeautifulSoup
    
    def __init__(self, data_dir):
        # Webdriver Einstellungen
        options = self.webdriver.ChromeOptions()
        options.add_argument("--user-data-dir=" + data_dir)
        #options.add_argument("--window-size=1920,5000")
        #options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
        #options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        self.driver = self.webdriver.Chrome(options=options)
        #self.driver.set_window_size(512, 100000)
        
        # Seite aufrufen und QR-Code Scannen
        self.driver.get('https://web.whatsapp.com/')
        #self.driver.execute_script("document.body.style.zoom='15%'")# Seite verkleinern, damit alle Chats angezeigt werden und so auch alle ausgelesen werden können
        self.time.sleep(3)
        
    
        self.wait = self.WebDriverWait(self.driver, 100)
        
    
    def stop(self):
        self.driver.close()
		
    # Funktionen
    def select_user(self, name=False, index=False):
        # User auswählen
        element  = self.wait.until(self.EC.element_to_be_clickable((self.By.XPATH, '//span[@title = "{}"]'.format(name))))
        element.click()
        #self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(name)).click()
        #self.driver.execute_script('document.querySelector(\'span[title="' + name + '"]\').click()')
        #self.time.sleep(0.5)
        
    def select_user_by_index(self, index = 0):
        pass
    
    def read_messages(self, group = False):
        print('#################################################')
        messages = self.driver.find_elements_by_css_selector('div._1_keJ div._1ays2 div.FTBzM')
        messages_dicts = []
        if messages:
            for message in messages[::-1]:
                message = self.BeautifulSoup(message.get_attribute("outerHTML"), "html.parser")#.prettify()
                classes = []
                for element in message.find_all(class_=True):
                    classes.extend(element["class"])
                    break
                    
                #class_detector = message.text.split('FTBzM ')#[1].split('"')[0]
                #print(class_detector)
                # message in
                if "message-in" in classes:
                    #print("\n", message.select_one(".-N6Gq .woe4f"))
                     # Erste Nachricht
                    if message.select_one(".-N6Gq .woe4f"):
                        # Emojis richtig formatieren
                        print('+++++++++++++++++++')
                        text = str(message.select_one("._F7Vk span")).replace('<span>', '').replace('</span>', '')
                        if not '<img' in text:
                            text_message = message.select_one("._F7Vk span").text
                        else:
                            text_message = ''
                            for i in text.split('<img'):
                                part = i.split('alt="')
                                if len(part) > 1:
                                    text_message += part[1][0] + part[1].split('>')[-1]
                                elif len(part) == 1:
                                    text_message += part[0]
                                
                        messages_dicts.append({"class": "message-in",
                                               "name" : message.select_one("._F7Vk").text,
                                               "message": text_message,
                                               "date": str(message.select_one(".-N6Gq .woe4f")).split('[')[1].split(']')[0]
                                })
                    # nächste Nachrichen
                    elif message.select_one(".-N6Gq .copyable-text"):
                        # Emojis richtig formatieren
                        text = str(message.select_one("._F7Vk span"))
                        text_message = ''
                        for i in text.split('<img'):
                            part = i.split('alt="')
                            if len(part) > 1:
                                text_message += part[1][0] + part[1].split('>')[-1]
                            elif len(part) == 1:
                                text_message += part[0]
                                
                        messages_dicts.append({"class": "message-in",
                                               "name" : message.select_one(".-N6Gq .copyable-text")['data-pre-plain-text'].split("] ", 1)[1][:-2],
                                               "message": text_message,
                                               "date": str(message.select_one(".-N6Gq .copyable-text")).split('[')[1].split(']')[0]
                                })
                    elif message.select_one("._12pGw"):
                        messages_dicts.append({"class": "message-in",
                                               "name" : message.select_one("._F7Vk").text,
                                               "message": message.select_one('._12pGw').text,
                                               "date": message.select_one('._3MYI2 ._3fnHB').text,
                                               "info": "deleted message"
                            })
                    elif message.select_one("._1zGQT.a81-s"): # Sticker
                        messages_dicts.append({"class": "message-in",
                                               "name" : message.select_one("._1uQFN._18GNg._F7Vk").text,
                                               "message": False,
                                               "date": message.select_one('._3MYI2 ._3fnHB').text,
                                               "info": "sticker"
                            })
                        
                # message out
                elif "message-out" in classes:
                    # Erste Nachricht
                    if str(message.select_one(".-N6Gq .copyable-text")) and message.select_one("._F7Vk span"):
                        # Emojis richtig formatieren
                        text = str(message.select_one("._F7Vk span"))
                        text_message = ''
                        for i in text.split('<img'):
                            part = i.split('alt="')
                            if len(part) > 1:
                                text_message += part[1][0] + part[1].split('>')[-1]
                            elif len(part) == 1:
                                text_message += part[0]
                            
                        messages_dicts.append({"class": "message-out",
                                               "name" : False,
                                               "message" : text_message,
                                               "date" : str(message.select_one(".-N6Gq .copyable-text")).split('[')[1].split(']')[0],
                                               "status" : message.select_one('._370iZ span')['data-icon']
                                })
                    # nächste Nachrichen
                    elif message.select_one('._F7Vk span'):
                        # Emojis richtig formatieren
                        text = str(message.select_one("._F7Vk span"))
                        text_message = ''
                        for i in text.split('<img'):
                            part = i.split('alt="')
                            if len(part) > 1:
                                text_message += part[1][0] + part[1].split('>')[-1]
                            elif len(part) == 1:
                                text_message += part[0]
                        
                        messages_dicts.append({"class": "message-out",
                                               "name" : False,
                                               "message": text_message,
                                               "date" : str(message.select_one(".-N6Gq .woe4f")).split('[')[1].split(']')[0],
                                               "status" : message.select_one('._370iZ span')['data-icon']
                                })
                    elif message.select_one("._1zGQT.a81-s"): # Sticker
                        messages_dicts.append({"class": "message-out",
                                               "name" : False,
                                               "message": False,
                                               "date": message.select_one('._3MYI2 ._3fnHB').text,
                                               "status": message.select_one('._370iZ span')['data-icon'],
                                               "info": "sticker"
                            })
                    elif message.select_one("._12pGw"):
                        messages_dicts.append({"class": "message-out",
                                               "name": False,
                                               "message": message.select_one('._12pGw').text,
                                               "date": message.select_one('._3MYI2 ._3fnHB').text,
                                               "info": "deleted message"
                            })
                # events
                else:
                    messages_dicts.append({"class": "event",
                                           "message": message.select_one('._F7Vk').text
                            })
                
                #print(message)
            print(messages_dicts)
                #break
    
    def send_img(self):
        pass
    
    def download_pp(self):
        pass
    
    def send_msg(self, msg):
        # Nachricht ins Textfeld eingeben
        self.driver.find_element_by_xpath('//div[@class = "_3u328 copyable-text selectable-text"]').send_keys(msg)
        # Nachricht absenden
        self.driver.execute_script('document.querySelector(\'span[data-icon="send"]\').click()')
        self.time.sleep(0.5)
        
    def read_data(self):
        self.time.sleep(2)
        chatfields = self.driver.find_elements_by_class_name('X7YrQ')
        if chatfields == []:
            print('Es wurde kein Chat gefunden...')
        else:
            self.main_data = {
                    'time': self.time.strftime('%d.%m.%Y-%H:%M:%S'),
                    }
            chats = []
            for field in chatfields:
                field = self.BeautifulSoup(field.get_attribute("outerHTML"), "html.parser")
                name = field.select_one("div._3H4MS span._19RFN").text
                if field.select_one("span._3NWy8 span._19RFN"):
                    is_group = False
                elif field.select_one('div._3H4MS span._19RFN'):
                    is_group = True
                    
                zeit = field.select_one('div._0LqQ').text# Zeit
                dictionary = {
                    'name': name,
                    'is_group': is_group,
                    'time': zeit
                    }
                    
                if is_group:
                    status = field.select_one('div._3VIru span[data-icon^="status"]')
                    if status:# letzte Nachricht von einem selber
                        dictionary['sender'] = False
                        dictionary['status'] = status.attrs['data-icon']# Status der eigenen letzten Nachricht
                        if field.select_one('span._1Wn_k'):
                            dictionary['last_message'] = field.select_one('span._1Wn_k').attrs['title'][1:-1] # Letzte Nachricht
                            
                    else:
                        if field.select_one('div._2Bw3Q span._1Wn_k ._1ovWX._F7Vk'):
                            dictionary['sender'] = field.select_one('div._2Bw3Q span._1Wn_k span._1ovWX._F7Vk').text# Sender
                            if field.select_one('span._1Wn_k'):
                                dictionary['last_message'] = field.select_one('span._1Wn_k').attrs['title'][1:-1] # Letzte Nachricht
                                
                        else:
                            if field.select_one('span._1_8_q > span'):
                                dictionary['event'] = field.select_one('span._1_8_q > span').text# Event
                            
                    if field.select_one('div._0LqQ span div._1ZMSM span.P6z4j'):
                        dictionary['new_messages'] = int(field.select_one('div._0LqQ span div._1ZMSM span.P6z4j').text)# Anzahl neuer Nachrichten
                            
                    if field.select_one('div._0LqQ span div._1ZMSM span[data-icon="muted"]'):
                        dictionary['is_muted'] = True# Stummgeschaltet
                        
                    if field.select_one('div._0LqQ span div._1ZMSM span[data-icon="pinned"]'):
                        dictionary['is_pinned'] = True# Fixiert
                        
                    if field.select_one('div._2Ol0p div._2UVJ5 div.yKiIK svg > path'):
                        dictionary['label'] = field.select_one('div._2Ol0p div._2UVJ5 div.yKiIK svg > path').attrs['fill']# Mit label versehen
                    elif field.select_one('div._2Ol0p div._2UVJ5 path:nth-of-type(2)'):
                        dictionary['label'] = field.select_one('div._2Ol0p div._2UVJ5 path:nth-of-type(2)').attrs['fill']# Mit mehreren Labeln versehen
                    
                    if field.select_one('div._3RWII div.B9BIa span[data-icon="default-group"]') and not field.select_one('div._3RWII img.jZhyM._13Xdg'):
                        dictionary['pp'] = False# Kein Profilbild
                    elif field.select_one('div._3RWII img.jZhyM._13Xdg'):
                        dictionary['pp'] = self.urllib.parse.unquote(field.select_one('div._3RWII img.jZhyM._13Xdg').attrs['src'].split('?e=')[1].split('&')[0])# Profilbild vorhanden

                else: # Einzelne Chats
                    status = field.select_one('div._3VIru span[data-icon^="status"]')
                    if status:# letzte Nachricht von einem selber
                        dictionary['sender'] = False
                        dictionary['status'] = status.attrs['data-icon']# Status der eigenen letzten Nachricht
                    else:
                        dictionary['sender'] = True# Sender
                        if field.select_one('div._0LqQ span div._1ZMSM span.P6z4j'):
                            dictionary['new_messages'] = int(field.select_one('div._0LqQ span div._1ZMSM span.P6z4j').text)# Anzahl neuer Nachrichten
                        
                    if field.select_one('span._1Wn_k > span'):
                        dictionary['last_message_or_event'] = field.select_one('div._2Bw3Q span._1Wn_k').attrs['title'][1:-1] # Letzte Nachricht
                        
                    if field.select_one('div._0LqQ span div._1ZMSM span[data-icon="muted"]'):
                        dictionary['is_muted'] = True  # Stummgeschaltet
        
                    if field.select_one('div._0LqQ span div._1ZMSM span[data-icon="pinned"]'):
                        dictionary['is_pinned'] = True  # Fixiert
        
                    if field.select_one('div._2Ol0p div._2UVJ5 div.yKiIK svg > path'):
                        dictionary['label'] = field.select_one('div._2Ol0p div._2UVJ5 div.yKiIK svg > path').attrs['fill']  # Mit label versehen
                    elif field.select_one('div._2Ol0p div._2UVJ5 path:nth-of-type(2)'):
                        dictionary['label'] = field.select_one('div._2Ol0p div._2UVJ5 path:nth-of-type(2)').attrs['fill']  # Mit mehreren Labeln versehen
        
                    if field.select_one('div._3RWII img.jZhyM._13Xdg'):
                        dictionary['pp'] = self.urllib.parse.unquote(field.select_one('div._3RWII img.jZhyM._13Xdg').attrs['src'].split('?e=')[1].split('&')[0])  # Profilbild vorhanden
                    else:
                        dictionary['pp'] = False  # Kein Profilbild
                        
                if field.select_one('div._2WP9Q div.xD91K div._2Bw3Q span._2ZAIy._19RFN'): # Screibt / Audio
                    dictionary['activity'] = field.select_one('div._2WP9Q div.xD91K div._2Bw3Q span._2ZAIy._19RFN').text
                    
                dictionary['index'] = int(int(field.select_one('div.X7YrQ').attrs['style'][:-33].split('(')[-1].split(': ')[1].split(';')[0]) / 72) # Nummer des Chats
                chats.append(dictionary)
                
            chats = sorted(chats, key = lambda i: i['index'])
            for dictionary in chats:
                del dictionary['index']
                
            self.main_data['chats'] = chats
            if self.driver.find_elements_by_css_selector('header._3Jvyf div._2rZZg div._3RWII img.jZhyM._13Xdg'):# eigenes Profielbild
                self.main_data['own_pp'] = self.urllib.parse.unquote(self.driver.find_element_by_css_selector('header._3Jvyf div._2rZZg div._3RWII img.jZhyM._13Xdg').get_attribute('src').split('?e=')[1].split('&')[0])
            else:
                self.main_data['own_pp'] = False
            
            if self.driver.find_elements_by_css_selector('div._3lq69 span div._3j8Pd:first-child div[role="button"] span[data-icon^=status]'): # Überprüfen ob neuer Status vorhanden ist
                if self.driver.find_element_by_css_selector('div._3lq69 span div._3j8Pd:first-child div[role="button"] span[data-icon^=status]').get_attribute('outerHTML').split('-')[3].split('"')[0] == 'unread':
                    self.main_data['new_status'] = True
                else:
                    self.main_data['new_status'] = False
            else:
                self.main_data['new_status'] = False
                
            if self.driver.find_elements_by_css_selector('span._3O0po div._25f0v div._2-Q3h._1puWZ div._3K1Z_ div._28Bny'): # Zeigt an ob der Computer oder das Telefon Verbindungsprobleme hat
                self.main_data['connection_error'] = self.driver.find_element_by_css_selector('span._3O0po div._25f0v div._2-Q3h._1puWZ div._3K1Z_ div._28Bny').get_attribute('innerHTML')

    def login(self):
        # 2 Sekunden Pause, damit die Seite geladen werden kann
        self.time.sleep(2)
        
        src_test = ""
        src= ""
        logout_or_tryagin = ""
        img = False
        
        # Anmeldevorgang
        if not self.driver.find_elements_by_css_selector('div._3WtUH div div._2UaNq div._3vpWv'):
            if self.driver.find_elements_by_css_selector('img[alt="Scan me!"]'):
                img = self.driver.find_element_by_xpath('//img[@alt = "Scan me!"]')
                src = img.get_attribute('src')
                self.urllib.request.urlretrieve(src, "qrcode.png")
                print('Scanne den QR-Code um dich Anzumelden')
        
            while not self.driver.find_elements_by_css_selector('div._3WtUH div div._2UaNq div._3vpWv'):
                if logout_or_tryagin == 'logout':
                    if self.driver.find_elements_by_css_selector('img[alt="Scan me!"]'):
                        img = self.driver.find_element_by_xpath('//img[@alt = "Scan me!"]')
                        src = img.get_attribute('src')
                        self.urllib.request.urlretrieve(src, "qrcode.png")
                        print('Scanne den QR-Code um dich Anzumelden')
                        logout_or_tryagin = False
        
                if self.driver.find_elements_by_css_selector('img[alt="Scan me!"]'):
                    if img == False:
                        img = self.driver.find_element_by_xpath('//img[@alt = "Scan me!"]')
                    else:
                        src_test = img.get_attribute('src')
        
                if src_test != src:
                    # QR-Code herunterladen
                    self.urllib.request.urlretrieve(src_test, "qrcode.png")
                    print('Es gibt einen neuen QR-Code')
                    src = src_test
                    self.time.sleep(2)
        
                # Wenn der QR-Code abgelaufen ist, kann man ENTER drücken um einen neuen anzufordern
                if self.driver.find_elements_by_css_selector('span div._1MOym'):
                    input("Der QR-Code ist abgelaufen. Drücke ENTER um einen neuen QR-Code anzufordern")
                    self.driver.find_element_by_class_name('_1MOym').click()
                    self.time.sleep(1)
                    img = self.driver.find_element_by_xpath('//img[@alt = "Scan me!"]')
        
                if self.driver.find_elements_by_css_selector('div._3RiLE div.aymnx div._13HPh'):
                    logout_or_tryagin = input('Versuche dein Telefon zu erreichen... gebe "logout" ein, um dich dauerhaft abzumelden oder drücke eine beliebige Taste, um es erneut zu probieren: ')
                    if logout_or_tryagin != 'logout':
                        print('Laden...')
        
                    if self.driver.find_elements_by_css_selector('div._2eK7W'):
                        if logout_or_tryagin == 'logout':
                            self.driver.find_element_by_xpath('//div[@class="_2eK7W _23_1v"]').click()
                            self.time.sleep(1)
                        else:
                            self.driver.find_element_by_xpath('//div[@class="_2eK7W _3PQ7V"]').click()
                    self.time.sleep(1)
        
        print('Du wurdest eingeloggt!')


bot = WaBot('./selenium')
bot.login()
bot.read_data()
#bot.driver.find_element_by_xpath('//span[@title = "{}"]'.format("Test1")).click()
print(bot.main_data)
#bot.select_user("Test1")
#bot.send_msg("test")
bot.select_user("Test")
#bot.send_msg("test")
bot.read_messages()



"""
    • Umfragefunktion
    • Bild senden
    • zu Gruppe hinzufügen
    • Gruppe erstellen 
    • read_messages_from()
    • Profilbild hinzufügen
    
"""
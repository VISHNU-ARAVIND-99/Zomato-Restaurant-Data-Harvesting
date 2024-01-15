from selenium import webdriver
import time
from bs4 import BeautifulSoup
import json


def scroll_down(t1, t2):
    """ 
    used to scroll down the chrome browser
    """
    start = time.time()
    initial_scroll = 0
    finals_sroll = 1000

    while True:
        driver.execute_script(f"window.scrollTo({initial_scroll},{finals_sroll})")
        time.sleep(t1)
        initial_scroll = finals_sroll
        finals_sroll += 1000
        end = time.time()
        if round(end - start) > t2:
            break


def restaurant_link_scraping(all_loc_links):
    """ 
    used to scrap all restaurant links from list of links from all_location() function as a input
    """
    restaurant_link = []
    count = 0
    for i in all_loc_links:
        driver.get(i)
        scroll_down(t1=0.8, t2=100)
        source = BeautifulSoup(driver.page_source, "html.parser")
        links = source.find_all('a', class_='sc-hSmEHG htzHpa')
        for j in links:
            restaurant_link.append(j['href'])
        count += 1
        if count == 1: # u can change here the count, want how many location u want to scrap
            return restaurant_link


def all_location():
    """
    given this links "https://www.zomato.com/delivery-cities" as input, which scrap links of all for different location around india.
    """
    all_loc_links = []
    driver.get("https://www.zomato.com/delivery-cities")
    time.sleep(1)
    source = BeautifulSoup(driver.page_source, "html.parser")
    links = source.find_all('a', class_='sc-chAAoq cvOfLa')
    for i in links:
        all_loc_links.append(i['href'])
    return all_loc_links


def scraping(link):
    """ 
    This function scraps details from given restaurant link
    """
    for lin in link:
        try:
            dis = {}
            result = lin.rstrip("order")
            driver.get(f"https://www.zomato.com{result}")
            time.sleep(1)
            source = BeautifulSoup(driver.page_source, "html.parser")

            name = source.find('h1', class_='sc-7kepeu-0 sc-iSDuPN fwzNdh')
            if name is not None:
                dis["restaurant name"] = name.get_text().strip()
            dis["restaurant_zomoto_link"] = f"https://www.zomato.com{result}"
            des = source.find('div', class_='sc-fgfRvd gBMRZZ')
            if des is not None:
                dis["description"] = des.get_text().strip()

            loc = source.find('a', class_='sc-clNaTc vNCcy')
            if loc is not None:
                dis["location"] = loc.get_text().strip()

            opening_time = source.find('span', class_='sc-kasBVs dfwCXs')
            if opening_time is not None:
                dis["opening_time"] = opening_time.get_text().strip()

            phone_num = source.find('p', class_='sc-1hez2tp-0 fanwIZ')
            if phone_num is not None:
                dis["phone_num"] = phone_num.get_text().strip()

            a = source.find('a', class_='sc-eetwQk jrslkY')
            if a is not None:
                dis["location_google_map_link"] = a['href']

            location_address = source.find('p', class_='sc-1hez2tp-0 clKRrC')
            if location_address is not None:
                dis["location_address"] = location_address.get_text().strip()

            c = source.find_all('div', class_='sc-1q7bklc-1 cILgox')
            if c is not None:
                dis["dining_rating"] = c[0].get_text().strip()
                dis["delivery_rating"] = c[1].get_text().strip()

            b = source.find_all('div', class_='sc-1q7bklc-8 kEgyiI')
            if c is not None:
                dis["dining_rating_count"] = b[0].get_text().strip()
                dis["delivery_rating_count"] = b[1].get_text().strip()

            driver.get(f"https://www.zomato.com{lin}")
            time.sleep(1)
            scroll_down(t1=0.8, t2=10)
            source = BeautifulSoup(driver.page_source, "html.parser")

            box = source.find_all('div', class_='sc-1s0saks-17 bGrnCu')
            food_dic = {}
            if box is not None:
                for i in box:
                    a = {}
                    food_name = i.find('h4', class_='sc-1s0saks-15 iSmBPS')
                    if food_name is not None:
                        food_name = food_name.get_text().strip()
                    food_price = i.find('span', class_='sc-17hyc2s-1 cCiQWA')
                    if food_price is not None:
                        a["food_price"] = food_price.get_text().strip()
                    food_rating_count = i.find('span', class_='sc-z30xqq-4 hTgtKb')
                    if food_rating_count is not None:
                        a["food_rating_count"] = food_rating_count.get_text().strip()
                    food_image_url = i.find('img', class_='sc-s1isp7-5 fyZwWD')
                    if food_image_url is not None:
                        li = food_image_url['src']
                        index = li.find('.jpeg')
                        a["food_image_url"] = li[:index + len('.jpeg')]
                    food_description = i.find('p', class_='sc-1s0saks-12 hcROsL')
                    if food_description is not None:
                        if food_description.get_text().strip():
                            a["food_description"] = food_description.get_text().strip()
                    food_dic[food_name] = a
            dis["food_item_list"] = food_dic
            try:
                with open("output.json", 'r', encoding='utf-8') as file:
                    data = json.load(file)
            except:
                data = []
            data.append(dis)
            json_data = json.dumps(data, indent=2, ensure_ascii=False)
            with open("output.json", 'w', encoding='utf-8') as file:
                file.write(json_data)
        except:
            pass


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
res_links = restaurant_link_scraping(all_loc_links=all_location())
scraping(link=res_links)

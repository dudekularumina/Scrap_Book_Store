from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver=webdriver.Chrome()
def Commonfields():
    data={
        'book_name':[],
        'image_url':[],
        'about_book_url':[],
        'price':[],
        'availability':[], 
    }
    return(data)
Commonfields()
def books_scrap(Commonfields):
    data=Commonfields
    for i in range(1,51):
       url="https://books.toscrape.com/catalogue/page-{}.html".format(i)
       driver.get(url)
       time.sleep(3)
       print("Books Store++++++++++++++++++++++++++++",url)

       ol_div=driver.find_elements(By.CLASS_NAME, 'product_pod')
       print("Length Of Books list--------------------------",len(ol_div))
       time.sleep(2)
       for b in ol_div:
           img_cont=b.find_element(By.CLASS_NAME, 'image_container')
        #    print("+++++++++++++++++++++++",img)
           img_tag=img_cont.find_element(By.TAG_NAME, 'a')
           about_book=img_tag.get_attribute('href')
        #    print("About Book--------------------", about_book)
           img_src=b.find_element(By.CLASS_NAME, 'thumbnail')
           img_src=img_src.get_attribute('src')
        #    print("Image Source-----------------",img_src)

           book_title=b.find_element(By.TAG_NAME, 'h3')
           book_title=book_title.find_element(By.TAG_NAME, 'a')
           book_title=book_title.get_attribute('title')
        #    print("Book Title...................", book_title)

           price=b.find_element(By.CLASS_NAME, 'price_color').text
        #    print("Price of the Book----------------------",price)

           availability=b.find_element(By.CLASS_NAME,'instock').text
        #    print("Availability------------------------",availability)
           time.sleep(2)
        #    print()

           data['book_name'].append(book_title)
           data['image_url'].append(img_src)
           data['about_book_url'].append(about_book)
           data['price'].append(price)
           data['availability'].append(availability)

    return data


books=books_scrap(Commonfields())

import pandas as pd

df=pd.DataFrame(books)
# print(df)

df.to_csv('books.csv', index=False)    #to CSV

df.to_excel('books.xlsx', engine='openpyxl')    #to Excel

print("data Saved............")
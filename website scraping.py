#!/usr/bin/env python
# coding: utf-8

# In[18]:


pip install bs4 --quiet


# In[19]:


from bs4 import BeautifulSoup


# In[20]:


import requests


# In[21]:


products_url="https://www.flipkart.com/search?q=mobiles%20under%2040000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"


# In[22]:


response=requests.get(products_url)


# In[23]:


response.status_code


# In[24]:


page_contents = response.text


# In[25]:


doc = BeautifulSoup(page_contents,'html.parser')


# In[26]:


heading_class = "_4rR01T"
heading_tags = doc.findAll('div',class_= heading_class)
name_text = []


# In[27]:


heading_tags[:5]


# In[14]:


price_class = "_30jeq3 _1_WHN1"
price_tags = doc.findAll('div', class_=price_class)
price_text = [] 


# In[15]:


price_tags[:4]


# In[16]:


stars_class= "_3LWZlK"
stars_tags = doc.findAll('div', class_=stars_class)
stars_text = [] 
stars_tags[:4]


# In[17]:


reviews_class = "_2_R_DZ"


# In[15]:


reviews_tags = doc.findAll('span', class_=reviews_class)
reviews_text = []
reviews_tags[:4]


# In[16]:


url_class = "_1fQZEK"
base_url = "https://www.flipkart.com"
url_tags = doc.findAll('a', class_=url_class)
url_product = []
for i in range(len(url_tags)):
    url_product.append(base_url+url_tags[i]['href'])


# In[17]:


for i in range(len(reviews_tags)):
        price_text.append(price_tags[i].text)
        name_text.append(heading_tags[i].text)
        stars_text.append(stars_tags[i].text)
        reviews_text.append(reviews_tags[i].text)
        reviews_text[i]=reviews_text[i].replace("\xa0"," ")


# In[18]:


product_dict={'name':name_text,'price':price_text,'stars':stars_text,'reviews':reviews_text,'url':url_product}
import pandas as pd
products_df=pd.DataFrame(product_dict)
products_df[:4]


# In[19]:


products_df.to_csv('products.csv')


# In[ ]:





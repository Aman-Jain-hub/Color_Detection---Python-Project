#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
import cv2


# In[31]:


Image_Path = 'pic_3.jpg'
Csv_Path = 'colors.csv'


# In[32]:


index = ['color', 'color_name', 'hex', 'R', 'G', 'B'] 


# In[33]:


# reading csv file
df = pd.read_csv(Csv_Path, names = index, header = None)
print(df.head(10))


# In[34]:


# reading image
read_image = cv2.imread(Image_Path)
read_image = cv2.resize(read_image, (1100,700))


# In[35]:


print(len(df))


# In[36]:


#declaring global variables
clicked = False
r = g = b = xpos = ypos = 0


# In[37]:


#function to calculate minimum distance from all colors and get the most matching color
def get_color_name(R,G,B):
    minimum = 1000
    for i in range(len(df)):
        d = abs(R - int(df.loc[i,'R'])) + abs(G - int(df.loc[i,'G'])) + abs(B - int(df.loc[i,'B']))
        if d <= minimum:
            minimum = d
            cname = df.loc[i, 'color_name']
            
    return cname 


# In[38]:


#function to get x,y coordinates of mouse double click
def draw_function(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, xpos, ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = read_image[y,x]
        b = int(b)
        g = int(g)
        r = int(r)


# In[39]:


# creating window
cv2.namedWindow('Display')
cv2.setMouseCallback('Display', draw_function)

while True:
    cv2.imshow('Display', read_image)
    if clicked:
        #cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle 
        cv2.rectangle(read_image, (20,20), (600,60), (b,g,r), -1)
        
        #Creating text string to display(Color name and RGB values)
        text = get_color_name(r,g,b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
        cv2.putText(read_image, text, (50,50), 2,0.8, (255,255,255),2,cv2.LINE_AA)
        if r+g+b >=600:
            cv2.putText(read_image, text, (50,50), 2,0.8, (0,0,0),2,cv2.LINE_AA)
    if cv2.waitKey(20) & 0xFF == 27:
        break
    
cv2.destroyAllWindows()


# In[ ]:





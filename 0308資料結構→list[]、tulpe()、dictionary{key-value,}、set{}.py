
# coding: utf-8

# In[1]:


weekdays = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
roles = ('張三','李四','王五')


# In[2]:


type(weekdays)


# In[3]:


type(roles)


# In[4]:


weekdays[0]='monday'


# In[5]:


weekdays


# In[7]:


roles[0] 


# In[8]:


roles[0]='kitty'


# In[9]:


roles


# In[10]:


a = [[[1,'apple',2,'banana'],'水果'],'籃子']


# In[11]:


a


# In[12]:


a[0]


# In[13]:


a[1]


# In[14]:


a[0,0,3]


# In[15]:


a[0][0][3]


# In[16]:


a[0][0]


# In[17]:


areas = ['台北','桃園','宜蘭']
names = [1,'lilias',2,'chang']


# In[18]:


areas +=names


# In[19]:


areas


# In[21]:


areas.extend(names)


# In[22]:


areas


# In[23]:


areas = ['台北','桃園','宜蘭']
names = [1,'lilias',2,'chang']


# In[24]:


areas.append(names)


# In[25]:


areas


# In[26]:


areas.insert(2,'羅東')
areas


# In[27]:


del areas[-2]
areas


# In[28]:


areas.remove('桃園')


# In[29]:


areas


# In[32]:


areas.index('桃園')


# In[33]:


areas.index('羅東')


# In[34]:


'羅東' in areas


# In[35]:


areas = ['台北','宜蘭','桃園','宜蘭']


# In[36]:


areas.count('宜蘭')


# In[37]:


areas.count('羅東')


# In[38]:


len(areas)


# In[39]:


areas.sort()


# In[40]:


areas


# In[42]:


areas.sort(reverse =True)
areas


# In[45]:


areas = ['台北','宜蘭','桃園','宜蘭']
sorted(areas)


# In[46]:


areas


# In[47]:


a = [1,2,3]
b = a
a[0] = 'x'
a


# In[48]:


b


# In[50]:


a = [1,2,3]
c = a.copy()
c


# In[51]:


a[0]='123'
a


# In[52]:


c


# In[53]:


tuple_1 = ('123','456','789')
a,b,c = tuple_1


# In[54]:


a


# In[55]:


b


# In[56]:


c


# In[57]:


a = '123'
b = '456'
a,b = b,a


# In[58]:


a


# In[59]:


b


# In[60]:


school = [("班級","甲班"),("姓名","⽢甘道夫"),("學號","110999")]
dict(school)


# In[67]:


class_dict = {
    'a':'apple',
    'b':'banana',
}
class_dict


# In[68]:


class_dict['a']


# In[69]:


class_dict['a'] = 'XXX'


# In[70]:


class_dict


# In[71]:


A_dict = {
    'a':'apple',
    'b':'banana',
}
B_dict = {'i':'ins','d':'del','u':'update',}


# In[73]:


A_dict


# In[74]:


B_dict


# In[75]:


B_dict.update(A_dict)
B_dict


# In[76]:


A_dict


# In[77]:


del B_dict['u']


# In[78]:


B_dict


# In[79]:


B_dict['a'] = 'XXX'
B_dict


# In[80]:


B_dict.update(A_dict)


# In[81]:


B_dict


# In[82]:


A_dict


# In[83]:


B_dict.clear()
B_dict


# In[85]:


'a' in A_dict


# In[86]:


A_dict.get('a')


# In[87]:


A_dict.get('u','Not found!')


# In[88]:


A_dict.keys()


# In[89]:


A_dict.values()


# In[91]:


A_dict.items()


# In[92]:


A_dict = {
    'a':'apple',
    'b':'banana',
}
B_dict = {'i':'ins','d':'del','u':'update',}
B_dict  = A_dict
A_dict['a'] = 'XXX'
B_dict 


# In[93]:


A_dict = {
    'a':'apple',
    'b':'banana',
}
B_dict = {'i':'ins','d':'del','u':'update',}
B_dict  = A_dict.copy()
A_dict['a'] = 'XXX'
B_dict 


# In[94]:


set('lilias')


# In[99]:


drinks = {"item1":{"珍珠奶茶","紅茶"},
         "item2":{"蘋果紅茶","綠茶"},
         "item3":{"紅茶","烏龍茶"},}


# In[100]:


drinks['item1']


# In[101]:


drinks.items()


# In[102]:


for name,contents in drinks.items():
    if '紅茶' in contents:
        print(name,contents)


# In[105]:


for name,contents in drinks.items():
    if '紅茶' in contents and not ('烏龍茶' in contents):
        print(name,contents)


# In[106]:


a={1,2,3}
b={3,4,5}
a&b


# In[107]:


a|b


# In[108]:


a - b


# In[109]:


a^b


# In[110]:


n = ['a','d','c']
n.append('k')
n


# In[111]:


n.pop()


# In[112]:


n


# In[113]:


n.insert(0,'G')
n


# In[114]:


n.pop(0)


# In[115]:


n


# In[116]:


days = [0,1,2,3,4,5,6]
weeks = ['w1','w2','w3','w4']
mons = ['1月','2月']
tulpelist = days,weeks,mons
tulpelist


# In[ ]:


x = [1,2,3,4,5,4]
len(set(x))!=len(x)


# In[ ]:


x = input("請輸入數字:");len(set(x))!=len(x)


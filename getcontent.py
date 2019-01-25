from requests_html import HTMLSession
session = HTMLSession()
# tlist=[]
# mylist = [ ]
# i=1
# while i<3:
# 	url='http://www.snqbbs.co/forum.php?mod=forumdisplay&fid=2&orderby=dateline&orderby=dateline&filter=author&page='+str(i)
# 	i=i+1
# 	print("正在查询第",i,"页")
# 	r = session.get(url)
# 	sel = 'tr > th > div > div.messBox > div.fromText > a'
# 	#results = r.html.find(sel)
# 	#print(results)
# 	#results[0].text
# 	#print(results[0].text)
# 	def get_text_link_from_sel(sel):
# 		  #mylist = [ ]
# 		  try:
# 			  results=r.html.find(sel)
# 			  for result in results:
# 				  mytext=result.text
# 				  mylink = list(result.absolute_links)[0]
# 				  mylist.append((mytext,mylink))
# 			  return mylist
# 		  except:
# 			  return none
# 	tlist.append(get_text_link_from_sel(sel))
# print(tlist)
# import pandas as pd
# #df = pd.DataFrame(get_text_link_from_sel(sel))
# def func3(mylist):
#     '''
#     使用列表推导的方式
#     '''
#     temp_list=[]
#     for one in mylist:
#         if one not in temp_list:
#             temp_list.append(one)
#     return temp_list
# df = pd.DataFrame(func3(mylist))
# #df.columns = ['username']
# print (df)
# df.to_excel('e:/code/username.xlsx', encoding='gbk', index=False)
from typing import Any


def getcontent(base_url,sel,page_num):
    mylist = []
    for i in range (1,page_num):
        #base_url+=str(i)
        url =  base_url + str(i)
        print (url)
        print("正在查询第", i, "页")
        try:
            results = session.get(url).html.find(sel)
            #print (results)
            for result in results:
                mytext = result.text
                mylink = list(result.absolute_links)[0]
                print (mylink)
                mylist.append((mytext,mylink))
                print (mylist)
            #return mylist
        except:
            print ("第", i, "页查询错误")
    #print (mylist)
    return mylist
if __name__ == '__main__' :
    getcontent('http://www.snqbbs.co/forum.php?mod=forumdisplay&fid=2&orderby=dateline&orderby=dateline&filter=author&page=',' tr > th > div > div.messBox > div.fromText > a',2)
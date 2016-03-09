#!/usr/bin/env python
#coding:utf-8
from django.utils.safestring import mark_safe
class PageInfo:
	def __init__(self,current_page,all_count,per_item=5):
		self.CurrentPage = current_page
		self.AllCount = all_count
		self.PerItem = per_item
	@property
	def start(self):
		return (self.CurrentPage-1)*self.PerItem
	@property
	def end(self):
		return self.CurrentPage*self.PerItem
	
	@property
	def all_page_count(self):
		temp =divmod( self.AllCount,self.PerItem)
		if temp[1] == 0:
			all_page_count = temp[0]
		else:
			all_page_count = temp[0] + 1
		return all_page_count

def Pager(page,all_page_count):
	# page：当前页
	#all_page_count:总页数

	page_html = [] 
    	first_html = "<a href = '/index/%d'>首页</a>"%1     #首页
    	page_html.append(first_html)

    	if page <= 1:
		prev_html = "<a href='#'>上一页</a>"      #上一页
    	else:
    		prev_html ="<a href='/index/%d'>上一页</a>"%(page-1)
    	page_html.append(prev_html)
    
 	if all_page_count <=11:
		start = 0
		end = all_page_count
    	else:
		if page <= 6:
			start = 0
			end = 11
		elif page>6 and page+5 < all_page_count:
			start =page - 6
			end = page + 5
		else:
			start = all_page_count -12
			end = all_page_count
    	for i in range(start,end):
        	if page == i+1 :
            		a_html = "<a  style='color:red' href = '/index/%d'>%d</a>"%(i+1,i+1)

        	else:                                  #用红色来标出当前页              
            		a_html = "<a  href = '/index/%d'>%d</a>"%(i+1,i+1)
        	page_html.append(a_html)               #分别生成a标签

    	if page>=all_page_count:
        	later_html = "<a href='#'>下一页</a>"
    	else:                                         
        	later_html ="<a href='/index/%d'>下一页</a>"%(page+1)
    	page_html.append(later_html)                     #下一页

    	last_html = "<a href = '/index/%d'>尾页</a>"%all_page_count
    	page_html.append(last_html)  
                                                                            #尾页

    	page_string = mark_safe(''.join(page_html))
    
   	return page_string

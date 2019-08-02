from django.shortcuts import render
from django.http import HttpResponse
import requests
import re
# Create your views here.

def index(request):
	# name='bdshadang@gmail.com'
	# passs='05061988'
	# link_Dnc='http://member.chothuesaigon.net/dang-nhap.htm?returnurl=%2fquan-ly-tin-rao.htm'
	# link_Qlc='http://member.chothuesaigon.net/quan-ly-tin-rao/p11.htm'
	# rq_referer = requests.get(link_Dnc)
	# #messagebox.showinfo("tb",rq_referer.text)
	# s_view = re.findall(r'id="__VIEWSTATE" value="(.*?)"',rq_referer.text)
	# # messagebox.showinfo("tb",s_view)
	# s_even = re.findall(r'id="__EVENTVALIDATION" value="(.*?)"',rq_referer.text)
	# # messagebox.showinfo("tb",s_even)

	
	# datasen={"__EVENTTARGET":"ctl00$MainContent$btnLogin","__EVENTARGUMENT":"","__VIEWSTATE":s_view,"__EVENTVALIDATION":s_even,'ctl00$MainContent$txtUserName':name,'ctl00$MainContent$txtPassword':passs}
	# s = requests.Session()
	# rq = s.post(link_Dnc,data=datasen)

	# result=s.get(link_Qlc)
	# s_viewTr = re.findall(r'VIEWSTATE" value="(.*?)" />',result.text)
	# s_evenTr = re.findall(r'EVENTVALIDATION" value="(.*?)" />',result.text)
	# datasen14={"__EVENTTARGET":"ctl00$MainContent$ctl00$rpProductManage$ctl"+'00$lbtUp',"__EVENTARGUMENT":"","__VIEWSTATE":s_viewTr,"__EVENTVALIDATION":s_evenTr}
	# kq_14 = s.post(link_Qlc,data=datasen14)
	
	return render(request,"pools/index.html")
def view_list(request):
	return render(request,'pools/question_list.html')
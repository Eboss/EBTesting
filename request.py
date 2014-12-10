
import urllib
import httplib2
# #url = 'http://www.example.com/login'   
body = {'USERNAME': 'admin@equityboss.com', 'PASSWORD': 'admin'}
http = httplib2.Http()
url = 'http://127.0.0.1:8000/api/eboss/wl/'   
response, content = http.request(url, 'GET', body=urllib.urlencode(body))
print response,content
#headers = {'Content-type': 'application/x-www-form-urlencoded'}
# import requests
#r = requests.get('http://127.0.0.1:8000/api/eboss/wl/',verify=False)
# r = requests.get('http://127.0.0.1:8000/watchlist/')
# print r
# url = 'http://127.0.0.1:8000/api/eboss/wl/'
# response = requests.get(url, headers={"USERNAME":'admin@equityboss.com',"PASSWORD":'admin2697'}, verify=False)
# print response
# res = requests.get('http://127.0.0.1:8000/api/eboss/wl/', auth=('admin@equityboss.com', 'admin2697'))
# print res
# r1 = r.get('http://127.0.0.1:8000/api/eboss/wl/')
# print r1
# import httplib
# conn = httplib.HTTPConnection("http://127.0.0.1:8000",name = 'admin@equityboss.com',password= 'admin2697')
# conn.request("GET", "/api/eboss/wl/")
# r1 = conn.getresponse()
# print r1.status, r1.reason

# import urllib2

# url = 'http://127.0.0.1:8000/'
# username = 'admin@equityboss.com'
# password = 'admin2697'
# p = urllib2.HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None, url, username, password)
# handler = urllib2.HTTPBasicAuthHandler(p)
# opener = urllib2.build_opener(handler)
# urllib2.install_opener(opener)
# page = urllib2.urlopen('http://127.0.0.1:8000/api/eboss/wl/').read()

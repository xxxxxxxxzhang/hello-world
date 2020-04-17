import requests
from lxml import html
import sys
def check(host):
    session = requests.Session()
    html_doc = session.get(host + '/admin/login').content.decode('utf-8')
    selector = html.fromstring(html_doc)
    csrf_token = selector.xpath('//*[@id="jstokenCSRF"]/@value')[0]
    user_payload = {'tokenCSRF': csrf_token, 'username': 'cuc', 'password': '111111'}
    login = session.post(host + '/admin/login', data=user_payload)
    print("login status£º",login.status_code)
    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: exp.py blog_host')
        exit(0)
    h=sys.argv[1]
    check(h)
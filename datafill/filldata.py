# -*- coding: utf-8 -*-
import requests
import sys
from lxml import html


def config(host):
    data_language = 'language=zh_CN'
    requests.post(host + '/install.php', data=data_language, verify=False)
    params = (
        ('language', 'zh_CN'),
    )
    data_reg = {'timezone': 'Asia', 'password': '111111', 'install': ''}
    requests.post(host + '/install.php', params=params, data=data_reg, verify=False)


def login_add_user_changelogo(host):
    session = requests.Session()
    html_doc = session.get(host + '/admin/login').content.decode('utf-8')

    selector = html.fromstring(html_doc)
    csrf_token = selector.xpath('//*[@id="jstokenCSRF"]/@value')[0]

    admin_payload = {'tokenCSRF': csrf_token, 'username': 'admin', 'password': '111111'}

    session.post(host + '/admin/login', data=admin_payload)


    user_html_doc = session.get(host + '/admin/new-user').content.decode('utf-8')


    selector_user = html.fromstring(user_html_doc)
    csrf_token_user = selector_user.xpath('//*[@id="jstokenCSRF"]/@value')[0]


    user_payload = {'save': '', 'tokenCSRF': csrf_token_user, 'new_username': 'cuc', 'new_password': '111111',
                    'confirm_password': '111111', 'role': 'author',
                    'email': ''}
    response=session.post(host + '/admin/new-user', data=user_payload)
    print('response_code', response.status_code)
    change_html_doc = session.get(host + '/admin/login').content.decode('utf-8')
    change_selector = html.fromstring(change_html_doc)

    change_csrf_token = change_selector.xpath('//*[@id="jstokenCSRF"]/@value')[0]
    change_payload = {'save': '', 'tokenCSRF': change_csrf_token, 'title':'hefeixin', 'slogan': 'wlecome to hefeixin',
                      'description': 'hello', 'Copyright': 'Copyright ? 2020', 'itemsPerPage': '6',
                      'orderBy': 'date', 'homepageTMP': '', 'pageNotFoundTMP': '', 'emailFrom': '',
                      'autosaveInterval': '2','url': host,'markdownParser': 'true',
                      'uriPage': '', 'uriTag': '/tag/', 'uriCategory': '/category/', 'extremeFriendly': 'true',
                      'titleFormatHomepage': '', 'titleFormatPages': 'titleFormatCategory', '': '',
                      'titleFormatTag': '', 'twitter': 'https://feixin.10086.cn/',
                      'facebook': 'https://www.facebook.com/pages/%E4%B8%AD%E5%9B%BD%E7%A7%BB%E5%8A%A8%E9%A3%9E%E4%BF%A1/104235166315815',
                      'thumbnailHeight': '400', 'thumbnailQuality': '100', 'language': 'zh_CN',
                      'timezone': 'Asia%2FShanghai', 'locale': 'zh_CN', 'dateFormat': 'F /C Y'
                      }
    session.post(host + '/admin/settings', data=change_payload)

    

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usages:exp.py blog_host')
        exit(0)
    h = sys.argv[1]
    config(h)
    login_add_user_changelogo(h)
    print("fill date success!!!")

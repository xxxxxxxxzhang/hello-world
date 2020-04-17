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
    re = requests.post(host + '/install.php', params=params, data=data_reg, verify=False)
    print("add user status",re.status_code)


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
    
    change_html_doc = session.get(host + '/admin/login').content.decode('utf-8')
    change_selector = html.fromstring(change_html_doc)

    change_csrf_token = change_selector.xpath('//*[@id="jstokenCSRF"]/@value')[0]
    change_payload = {'save': '', 'tokenCSRF': change_csrf_token, 'title':'和飞信', 'slogan': '欢迎来到和飞信论坛',
                      'description': '您好', 'Copyright': 'Copyright ? 2020', 'itemsPerPage': '6',
                      'orderBy': 'date', 'homepageTMP': '', 'pageNotFoundTMP': '', 'emailFrom': '',
                      'autosaveInterval': '2','url': host,'markdownParser': 'true',
                      'uriPage': '', 'uriTag': '/tag/', 'uriCategory': '/category/', 'extremeFriendly': 'true',
                      'titleFormatHomepage': '', 'titleFormatPages': 'titleFormatCategory', '': '',
                      'titleFormatTag': '', 'twitter': 'https://feixin.10086.cn/',
                      'facebook': '',
                      'thumbnailHeight': '400', 'thumbnailQuality': '100', 'language': 'zh_CN',
                      'timezone': 'Asia%2FShanghai', 'locale': 'zh_CN', 'dateFormat': 'F /C Y'
                      }
    check_mark = session.post(host + '/admin/settings', data=change_payload)
    print("Config Success?",check_mark.status_code) 
    if check_mark.status_code == 200:
      print("Config Success!")
    else:
         print("Config failed!")    
    

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usages:exp.py blog_host')
        exit(0)
    h = sys.argv[1]
    config(h)
    login_add_user_changelogo(h)

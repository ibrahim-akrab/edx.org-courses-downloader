# import useful modules
import re
from robobrowser import RoboBrowser
import sys


def main():
        # initialize a browser to be used in exploring the weebsite
        browser = RoboBrowser()

        # the url address of the login webpage
        login_url = 'https://courses.edx.org/login'
        # the url address that the POST request will be submitted to
        # you can get it using developer tools in your favourite web browser
        submission_url = 'https://courses.edx.org/user_api/v1/account/login_session/'
        # the url of the dashboard that contains all courses you are enrolled in
        dashboard_url = 'https://courses.edx.org/dashboard'
        
        
        # the header that will be used to when interacting with edx.org
        # to make it feel like the program is real browser
        # you can get it from browser developer tools as weel
        headers = {'Host': 'courses.edx.org',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
                   'Accept': '*/*',
                   'Accept-Language': 'en-US,en;q=0.5',
                   'Accept-Encoding': 'gzip, deflate, br',
                   'X-NewRelic-ID': 'XA4GVl5ACwAEV1JQAA==',
                   'X-CSRFToken': 'AAHYILL317VUPkCvSMtCZHdWGr4Kftvu',
                   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                   'x-requested-with': 'XMLHttpRequest',
                   'Referer': 'https://courses.edx.org/login',
                   'Content-Length': '56',
                   'Cookie': 'csrftoken=AAHYILL317VUPkCvSMtCZHdWGr4Kftvu; AWSELB=D1EF6B6510E347E5B895826CD53CF4FD55E0CFA9A95907C11F810E7D6972F2D556AAC01BD8A29EB6B5AC70EA7FC4728EA29366084A1515C55C7CE5AC04F11C67453CBBE860; optimizelyEndUserId=oeu1502448980573r0.11874445472471806; ajs_user_id=%2215574242%22; ajs_group_id=null; ajs_anonymous_id=%22fe4065de-90cf-4fc6-9ecb-23ea6e535a95%22; ki_t=1502448986838%3B1502448986838%3B1502452031949%3B1%3B9; ki_r=https%3A%2F%2Fwww.edx.org%2F; __cfduid=d868fba5a6a33fdfd0bdfe385619cf79c1502452898; sailthru_hid=59d37409bf443e8a6c45070abda3c375598d41df18ff438c048b5373a7723eadd21c865926edcb03072e3cb8; prod-edx-language-preference=en; prod-edx-sessionid="1|s6nvsyfukyb4a7x7t50bh3zgm7vs9n3q|qwwJrGVYc78j|ImNkN2RkOTY3NWU4NTMwYWQ4N2FlNWI5MjZkZjNiYjdhMGE0OTBiYzg5NWRlNDUzNDdkODEwOTIyOGUyNmEzOTEi:1dg9L8:vA7iN1elORpFIqRumagee4aYjXE"',
                   'DNT': '1',
                   'Connection': 'keep-alive'
                   }

        # the dict data that will be submitted for the website to log in the account
        # will add ways to enter these data dynamically
        payload = {'email': 'test@grr.la',
                   'password': "123456789",
                   'remember': 'true'
                   }

        # send POST request to the submission url with the data and the header
        response = browser.session.post(submission_url, data = payload, headers = headers)
        browser._update_state(response)

        if not browser.response.ok: sys.exit(1)     
        print(response)
        # update the state of the browser with the response
        # now that we are logged in
        browser.open(dashboard_url)
        if not browser.response.ok: sys.exit(1)
        print(browser.response)
	    








if __name__ == "__main__": main()

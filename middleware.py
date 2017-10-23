# encoding=utf-8
import random
from cookies import cookies
from user_agents import agents


class UserAgentMiddleware(object):
    """ 换User-Agent """

    def process_request(self, request, spider):
        agent = random.choice(agents)
        agent = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"
        request.headers["User-Agent"] = agent


class CookiesMiddleware(object):
    """ 换Cookie """

    def process_request(self, request, spider):
        cookie = random.choice(cookies)
        cookie = {'_T_WM': '429afd73f971665092dcbae39a752651', " \
                  "'SCF': 'AqJkmkm693P1Xjuhs0konfR7wHbxdB0-GN2Eoj-znitGvUDDCZF8IFiIWB-4xnegRPZSp60ghQ5KoeXKvw_vJ-k.', " \
                  "'SUB': '_2A2503Yp-DeRhGeVG71cU9CjMwj6IHXVUIRY2rDV6PUJbktBeLUrSkW1ZMT3d9-DqGrfunMEcza57kQKF1g..', " \
                  "'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9W5l.lDTnMBmA1j8F0Z2DkPr5JpX5K-hUgL.FoeRSh-fShq71Kz2dJLoIpjLxK-L12zLBo.LxK-LBoML1-eLxKnLB--LBK5t', " \
                  "'SUHB': '0WGc638d7IKb_c', " \
                  "'SSOLoginState': '1507457582', " \
                  "'ALF': '1510049559'}
        request.cookies = cookie

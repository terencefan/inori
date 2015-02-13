# -*- coding:utf-8 -*-

import requests
import json


class Invoker():

    HOST = {
        'US': 'us.battle.net',
        'Europe': 'eu.battle.net',
        'Korea': 'kr.battle.net',
        'Taiwan': 'tw.battle.net',
        'China': 'www.battlenet.com.cn',
    }

    def __init__(self, area):
        self.prefix = 'http://{}'.format(self.HOST[area])

    def get(self, url, params=None):
        url = '{}{}'.format(self.prefix, url)
        content = requests.get(url).content
        return json.loads(content)

    def get_achievement(self, uid):
        url = '/api/wow/achievement/{}'.format(uid)
        return self.get(url)

    def get_auction(self, realm):
        url = '/api/wow/auction/data/{}'.format(realm)
        return self.get(url)

    def get_battlepet_ability(self, uid):
        url = '/api/wow/battlePet/ability/{}'.format(uid)
        return self.get(url)

    def get_battlepet_species(self, uid):
        url = '/api/wow/battlePet/species/{}'.format(uid)
        return self.get(url)

    def get_battlepet_stats(self, uid, params):
        url = '/api/wow/battlePet/stats/{}'.format(uid)
        return self.get(url, params)

    def get_character(self, realm, name):
        url = '/api/wow/character/{}/{}'.format(realm, name)
        return self.get(url)

    def get_item(self, uid):
        url = '/api/wow/item/{}'.format(uid)
        return self.get(url)

    def get_item_set(self, uid):
        url = '/api/wow/item/set/{}'.format(uid)
        return self.get(url)

    def get_guild(self, realm, name):
        url = '/api/wow/guild/{}/{}'.format(realm, name)
        return self.get(url)

    def get_recipe(self, uid):
        url = '/api/wow/recipe/{}'.format(uid)
        return self.get(url)

    def get_spell(self, uid):
        url = '/api/wow/spell/{}'.format(uid)
        return self.get(url)


if __name__ == '__main__':
    invoker = Invoker('China')
    print invoker.get_guild('斯坦索姆', '白兔糖')

from locust import HttpLocust, TaskSet, task
import helper
from random import randint
import time, datetime
import json

hostname = helper.build_host_name()
trans_id = -1
names = ["Shiva", "Matthew", "Andy", "Nick", "Prof"]
sellers = ["Frank", "Bob", "Fred"]
product_names = ["MacBook Pro", "JBL 10 Inch Subwoofer", "Beats Solo2"]
sale_prices = [1299.99, 450.00, 200.00]


class MyTaskSet(TaskSet):
    @task
    def send(self):
	global trans_id, names, product_names, sale_prices, hostname, sellers
	trans_id += 1	
	user_id = randint(0, len(names)-1)
	item_id = randint(0, len(product_names)-1)
	seller_id = randint(0, len(sellers)-1)
	token = helper.token
	broker_props = {'ContentType' : 'application/json'}	
	headers = {
            'Authorization': token,
            'Content-Type': 'application/atom+xml;type=entry;charset=utf-8',
            'BrokerProperties': json.dumps(broker_props)
	}
	if (trans_id % 600 == 0):
		userParams = {'transaction_id': trans_id, 'user_id': 'Nil', 'seller_id': 'Nil', 'product_name':'Error', 'sale_price':-99.99, 'transaction_date':str(datetime.datetime.now())}
	else:
		userParams = {'transaction_id': trans_id, 'user_id': names[user_id], 'seller_id': sellers[seller_id], 'product_name':product_names[item_id], 'sale_price':sale_prices[item_id], 'transaction_date':str(datetime.datetime.now())}
	response = self.client.post(hostname + '/messages', data= json.dumps(userParams), headers= headers)

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 0
    max_wait = 0

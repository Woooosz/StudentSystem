# coding=utf-8
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, supports_credentials=True)
api = Api(app)
app.config.from_object('config')
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))


parser = reqparse.RequestParser()
parser.add_argument('username', type=str, location='form')
parser.add_argument('password', type=str, location='form')
class Login(Resource):
	def post(self):

		args = parser.parse_args()
		username = args['username']
		password = args['password']

		if username == 'admin' and password == 'admin':
			return {
				'code':0,
				'data':username,
				'message':"",
				'success':True,
				'total':'null'
			}
		else:
			return {
				'code': -1,
				'data':username,
				'message':"用户名不存在或用户名密码错误，请重试",
				'success':False,
				'total':'null'
			}

class getCurrentUser(Resource):
	def get(self):
		return {"code":10,"data":None,"message":"not login yet","success":False,"total":None};

api.add_resource(Login, '/api/login')
api.add_resource(getCurrentUser, '/api/getCurrentUser')

if __name__ == '__main__':
    app.run(debug=True)

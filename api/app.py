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
# 添加导师表相关信息
parser.add_argument('tutor_name')
parser.add_argument('tutor_phone')
parser.add_argument('tutor_id')

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

from dao.tutor import get_tutor, get_schema, add_tutor
class SchemaTutor(Resource):
	def get(self):
		return get_schema()

class SelectTutor(Resource):
	def post(self):
		args = parser.parse_args()
		return get_tutor(args['tutor_name'], args['tutor_phone'])

class Add_tutor(Resource):
	def post(self):
		args = parser.parse_args()
		return add_tutor(args['tutor_id'], args['tutor_name'], args['tutor_phone'])

api.add_resource(Login, '/api/login')
api.add_resource(getCurrentUser, '/api/getCurrentUser')
api.add_resource(SchemaTutor,'/api/tutor/schema')
api.add_resource(SelectTutor,'/api/tutor/select')
api.add_resource(Add_tutor,'/api/tutor/insert')

if __name__ == '__main__':
    app.run(debug=True)

# coding=utf-8
from flask import Flask
from flask_restful import Resource, Api, reqparse, request
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
parser.add_argument('tutor_name', location='json')
parser.add_argument('tutor_phone', location='json')
parser.add_argument('tutor_id', location='json')
parser.add_argument('id', location='json')

# 表项目
#parser.add_argument('keys', location='args')
parser.add_argument('page', location='json')
parser.add_argument('pageSize', location='json')

# 添加 workroom 信息
parser.add_argument('workroom_id', location='json')
parser.add_argument('roomname', location='json')
parser.add_argument('capacity', location='json')
parser.add_argument('support_name', location='json')
parser.add_argument('work_organization', location='json')
parser.add_argument('used', location='json')
parser.add_argument('used_rate', location='json')

# 添加 user 信息
parser.add_argument('xuehao', location='json')
parser.add_argument('xingming', location='json')
parser.add_argument('nianji', location='json')
parser.add_argument('shoujihaoma', location='json')
parser.add_argument('gongzuoshi', location='json')
parser.add_argument('xueweileixing', location='json')
parser.add_argument('peiyangfangshi', location='json')
parser.add_argument('zhengzhimianmao', location='json')
parser.add_argument('zhuanye', location='json')
class Login(Resource):
	def post(self):
		args = parser.parse_args()
		username = args['username']
		password = args['password']
		#
		# if username == 'admin' and password == 'admin':
		return {
			'code':0,
			'data':username,
			'message':"",
			'success':True,
			'total':'null'
		}
		# else:
		# 	return {
		# 		'code': -1,
		# 		'data':username,
		# 		'message':"用户名不存在或用户名密码错误，请重试",
		# 		'success':False,
		# 		'total':'null'
		# 	}

class getCurrentUser(Resource):
	def get(self):
		return {"code":0,"data":None,"message":"not login yet","success":True,"total":None};

# tutor表
from dao import tutor
class SchemaTutor(Resource):
	def get(self):
		return tutor.get_schema()

class SelectTutor(Resource):
	def post(self):
		args = parser.parse_args()
		return tutor.get_tutor(args['tutor_id'], args['tutor_name'], args['tutor_phone'], args['page'], args['pageSize'])

class Add_tutor(Resource):
	def post(self):
		args = parser.parse_args()
		return tutor.add_tutor(args['tutor_id'], args['tutor_name'], args['tutor_phone'])
class Delete_tutor(Resource):
	def get(self):
		return tutor.delete_tutor(request.values['keys'])

class Update_tutor(Resource):
	def post(self):
		args = parser.parse_args()
		# for k, v in args.items():
		# 	if v is None:
		# 		print(k)
		# 		args[k] = 'NULL'
		# 		print(str(k) + '  ' + str(v))
		return tutor.update_tutor(request.values['keys'], args['tutor_id'], args['tutor_name'], args['tutor_phone'])

# workroom表
from dao import workroom
class SchemaWorkroom(Resource):
	def get(self):
		return workroom.get_schema()

class SelectWorkroom(Resource):
	def post(self):
		args = parser.parse_args()
		return workroom.get_tutor(args['roomname'], args['support_name'], args['work_organization'], args['page'], args['pageSize'])

class DeleteWorkroom(Resource):
	def get(self):
		return workroom.delete_tutor(request.values['keys'])

class AddWorkroom(Resource):
	def post(selfself):
		args = parser.parse_args()
		return workroom.add_tutor(args['roomname'], args['capacity'],args['support_name'], args['work_organization'])

class UpdateWorkroom(Resource):
	def post(self):
		args = parser.parse_args()
		return workroom.update_tutor(request.values['keys'], args['roomname'], args['capacity'], args['support_name'], args['work_organization'])

# user表
from dao import user
class SchemaUser(Resource):
	def get(self):
		return user.get_schema()

class SelectUser(Resource):
	def list2str(self, a):
		ans = ''
		for i in a:
			ans = ans + ',' + i
		print(a[1:-1])
		return a[1:-1]
	def post(self):
		args = parser.parse_args()
		xuehao = '' if args['xuehao'] is None else args['xuehao']
		xingming = '' if args['xingming'] is None else args['xingming']
		nianji = '' if args['nianji'] is None else args['nianji']
		shoujihaoma = '' if args['shoujihaoma'] is None else args['shoujihaoma']
		gongzuoshi = 'select roomname from workroom group by roomname' if args['gongzuoshi'] is None else self.list2str(args['gongzuoshi'])
		xueweileixing = 'select xueweileixing from student group by xueweileixing' if args['xueweileixing'] is None else self.list2str(args['xueweileixing'])
		peiyangfangshi = 'select peiyangfangshi from student group by peiyangfangshi' if args['peiyangfangshi'] is None else self.list2str(args['peiyangfangshi'])
		zhengzhimianmao = 'select zhengzhimianmao from student group by zhengzhimianmao' if args['zhengzhimianmao'] is None else self.list2str(args['zhengzhimianmao'])
		zhuanye = 'select zhuanye from student group by zhuanye' if args['zhuanye'] is None else self.list2str(args['zhuanye'])
		page = args['page']
		pageSize = args['pageSize']
		return user.get_tutor(xuehao, xingming, nianji, shoujihaoma, gongzuoshi, xueweileixing, peiyangfangshi, zhengzhimianmao, zhuanye, page, pageSize)


api.add_resource(Login, '/api/login')
api.add_resource(getCurrentUser, '/api/getCurrentUser')
api.add_resource(SchemaTutor,'/api/tutor/schema')
api.add_resource(SelectTutor,'/api/tutor/select')
api.add_resource(Add_tutor,'/api/tutor/insert')
api.add_resource(Delete_tutor, '/api/tutor/delete')
api.add_resource(Update_tutor, '/api/tutor/update')
# workroom表
api.add_resource(SchemaWorkroom,'/api/workroom/schema')
api.add_resource(SelectWorkroom,'/api/workroom/select')
api.add_resource(DeleteWorkroom,'/api/workroom/delete')
api.add_resource(AddWorkroom, '/api/workroom/insert')
api.add_resource(UpdateWorkroom,'/api/workroom/update')
# user表
api.add_resource(SchemaUser,'/api/user/schema')
api.add_resource(SelectUser, '/api/user/select')

if __name__ == '__main__':
    app.run(debug=True)

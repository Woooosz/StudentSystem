#coding=utf8
import config
import pymysql

def mapping(x):
  if x is None:
    return None
  return {'key': x[0], 'value': x[1]}

def getSchema():
  with pymysql.connect(host=config.MYSQL_HOST, port=config.MYSQL_PORT, user=config.MYSQL_USRT,
                       password=config.MYSQL_PASSWD, db=config.MYSQL_DB) as conn:
    sql_get = "SELECT roomname,roomname FROM workroom GROUP BY roomname"
    conn.execute(sql_get)
    res = conn.fetchall()
    ans_jiaoyanshi = [mapping(y) for y in res]
    sql_get = "SELECT peiyangfangshi, peiyangfangshi FROM student GROUP BY peiyangfangshi"
    conn.execute(sql_get)
    res = conn.fetchall()
    ans_peiyangfangshi = [mapping(y) for y in res]
    sql_get = "SELECT roomname, roomname FROM workroom GROUP BY roomname"
    conn.execute(sql_get)
    res = conn.fetchall()
    ans_roomname = [mapping(y) for y in res]
    sql_get = "SELECT tutor_id, concat(concat(concat(tutor_id,'('),tutor_name),')') AS tutor_ids FROM tutor GROUP BY tutor_id"
    conn.execute(sql_get)
    res = conn.fetchall()
    ans_tutor = [mapping(y) for y in res]
  key = 'key'
  title = 'title'
  dataType='dataType'
  value='value'
  showType='showType'
  options='options'
  validator = 'validator'
  required = 'required'
  primary='primary'
  pattern = 'pattern'
  message = 'message'
  type = 'type'

  userQuerySchemaList=[
      {
          key: 'xuwhao',
          title: '学号',
          dataType: 'varchar',
      },
      {
          key: 'xingming',
          title: '姓名(支持全拼)',
          dataType: 'varchar',
      },
      {
          key: 'nianji',
          title: '年级',
          dataType: 'varchar',
      },
      {
          key: 'shoujihaoma',
          title: '手机号码',
          dataType: 'varchar',
      },
      {
          key: 'gongzuoshi',
          title: '教研室',
          dataType:'varchar',
          showType:'multiSelect',
          options:ans_jiaoyanshi,
      },
      {
          key: 'xueweileixing',
          title: '学位类型',
          dataType: 'varchar',
          showType: 'checkbox',
          options: [{key: '硕士', value: '硕士'}, {key: '博士', value: '博士'}]
      },
      {
          key: 'peiyangfangshi',
          title: '培养方式',
          dataType: 'varchar',
          showType: 'multiselect',
          options: [{key:'全日制非定向', value:'全日制定向'}, {key:'全日制定向', value:'全日制定向'},{key:'非全日制非定向', value:'非全日制非定向'}, {key:'非全日制定向', value:'非全日制定向'}]
      },
      {
          key: 'zhengzhimianmao',
          title: '政治面貌',
          dataType: 'varchar',
          showType: 'multiSelect',
          options: [{key: '中共党员', value: '中共党员'}, {key: '中共预备党员', value: '中共预备党员'}, {key: '共青团员', value: '共青团员'},{key: '群众', value: '群众'}, {key: '民主党派成员', value: '民主党派成员'}]
      },
      {
          key: 'zhuanye',
          title: '专业',
          dataType: 'varchar',
          showType: 'multiSelect',
          options: [{key: '管理科学与工程', value: '管理科学与工程'}, {key: '经济系统分析与管理', value: '经济系统分析与管理'},
                    {key: '信息管理与电子政务', value: '信息管理与电子政务'}, {key: '交通系统工程', value: '交通系统工程'},
                    {key: '系统工程', value: '系统工程'}, {key: '信息管理与电子政务', value: '信息管理与电子政务'}, {key: '会计学', value: '会计学'},
                    {key: '企业管理', value: '企业管理'}, {key: '旅游管理', value: '旅游管理'}, {key: '技术经济及管理', value: '技术经济及管理'},
                    {key: '项目管理', value: '项目管理'}, {key: '环境管理', value: '环境管理'}, {key: '投资学', value: '投资学'},
                    {key: '知识产权管理', value: '知识产权管理'}, {key: '物流工程', value: '物流工程'}, {key: '金融学', value: '金融学'},
                    {key: '产业经济学', value: '产业经济学'}, {key: '国际贸易学', value: '国际贸易学'}, {key: '金融专硕', value: '金融专硕'}]
      },
  ]
  userDataSchemaList = [
      {
          key: 'id',
          title: '序号',
          dataType: 'int',
          primary: True,
      },
      {
          key: 'xueweileixing',
          title: '学位类型',
          dataType: 'varchar',
          showType: 'radio',
          options: [{key: '硕士', value: '硕士'}, {key: '博士', value: '博士'}]
      },
      {
          key: 'peiyangfangshi',
          title: '培养方式',
          dataType: 'varchar',
          showType: 'select',
          options: [{key: '全日制非定向', value: '全日制定向'}, {key: '全日制定向', value: '全日制定向'}, {key: '非全日制非定向', value: '非全日制非定向'},
                    {key: '非全日制定向', value: '非全日制定向'}]
      },

      {
          key: 'xuehao',
          title: '学号',
          dataType: 'varchar',
      },
      {
          key: 'xingming',
          title: '姓名',
          dataType: 'varchar',
      },
      {
          key: 'nianji',
          title: '年级',
          dataType: 'varchar',

      },
      {
          key: 'zhuanye',
          title: '专业',
          dataType: 'varchar',
          showType: 'select',
          options: [{key: '管理科学与工程', value: '管理科学与工程'}, {key: '经济系统分析与管理', value: '经济系统分析与管理'},
                    {key: '信息管理与电子政务', value: '信息管理与电子政务'}, {key: '交通系统工程', value: '交通系统工程'},
                    {key: '系统工程', value: '系统工程'}, {key: '信息管理与电子政务', value: '信息管理与电子政务'}, {key: '会计学', value: '会计学'},
                    {key: '企业管理', value: '企业管理'}, {key: '旅游管理', value: '旅游管理'}, {key: '技术经济及管理', value: '技术经济及管理'},
                    {key: '项目管理', value: '项目管理'}, {key: '环境管理', value: '环境管理'}, {key: '投资学', value: '投资学'},
                    {key: '知识产权管理', value: '知识产权管理'}, {key: '物流工程', value: '物流工程'}, {key: '金融学', value: '金融学'},
                    {key: '产业经济学', value: '产业经济学'}, {key: '国际贸易学', value: '国际贸易学'}, {key: '金融专硕', value: '金融专硕'}]
      },
      {
          key: 'daoshibianhao',
          title: '导师编号',
          dataType: 'varchar',
          showType:'select',
          validator: [{required: True}],
          options: ans_tutor,
      },
      {
          key: 'biyeyuanxiao',
          title: '毕业院校',
          dataType: 'varchar',

      },
      {
          key: 'xingbie',
          title: '性别',
          dataType: 'varchar',
          showType: 'radio',
          options: [{key: '男', value: '男'}, {key: '女', value: '女'}]

      },
      {
          key: 'zhengzhimianmao',
          title: '政治面貌',
          showType: 'select',
          options: [{key: '中共党员', value: '中共党员'}, {key: '中共预备党员', value: '中共预备党员'}, {key: '共青团员', value: '共青团员'},
                    {key: '群众', value: '群众'}, {key: '民主党派成员', value: '民主党派成员'}]
      },
      {
          key: 'jiatinglianxiren',
          title: '家庭联系人',
          dataType: 'varchar',

      },
      {
          key: 'sos_relation',
          title: '与本人关系',
          dataType: 'varchar',
      },
      {
          key: 'jiatinglianxidianhua',
          title: '家庭联系电话',
          dataType: 'varchar',
      },
      {
          key: 'jiatingzhuzhi',
          title: '家庭住址',
          dataType: 'varchar',

      },
      {
          key: 'minzu',
          title: '民族',
          dataType: 'varchar',

      },
      {
          key: 'hunfou',
          title: '婚否',
          dataType: 'varchar',
          showType: 'radio',
          options: [{key: '是', value: '是'}, {key: '否', value: '否'}]
      },
      {
          key: 'chushengriqi',
          title: '出生日期',
          dataType: 'varchar',

      },
      {
          key: 'shenfenzhenghaoma',
          title: '身份证号码',
          dataType: 'varchar',

      },
      {
          key: 'shoujihaoma',
          title: '手机号码',
          dataType: 'varchar',
      },
      {
          key: 'email',
          title: '邮箱',
          dataType: 'varchar',
          validator: [{type: 'email', required: False, message: '邮箱地址有误'}],
      },
      {
          key: 'shifouzhuxiao',
          title: '是否住校',
          dataType: 'varchar',
          showType: 'radio',
          options: [{key: '是', value: '是'}, {key: '否', value: '否'}]
      },
      {
          key: 'xiaowaizhuzhi',
          title: '校外住址',
          dataType: 'varchar',

      },
      {
          key: 'susheid',
          title: '宿舍 ID',
          dataType: 'varchar',

      },
      {
          key: 'fangjianhao',
          title: '房间号',
          dataType: 'varchar',
      },
      {
          key: 'gongzuoshi',
          title: '教研室',
          dataType: 'varchar',
          showType: 'select',
          options: ans_roomname,
      },
      {
          key: 'gongweihao',
          title: '工作位',
          dataType: 'varchar',
      },
  ]
  return userDataSchemaList, userQuerySchemaList


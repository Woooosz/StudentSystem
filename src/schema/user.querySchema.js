// 定义某个表的querySchema
// schema的结构和含义参考下面的例子
// 注意: 所有的key不能重复

module.exports = [
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
    key:'nianji',
    title:'年级',
    dataType:'varchar',
  },
  {
    key: 'shoujihaoma',
    title: '手机号码',
    dataType: 'varchar',
  },
  {
    key: 'gongzuoshi',
    title: '教研室',
    dataType: 'varchar',
  },
  {
    key:'xueweileixing',
    title:'学位类型',
    dataType:'varchar',
    showType:'checkbox',
    options:[{key:'硕士', value:'硕士'},{key:'博士', value:'博士'}]
  },
  {
    key:'peiyangfangshi',
    title:'培养方式',
    dataType:'varchar',
    showType:'checkbox',
    options:[{key:'学硕', value:'学硕'},{key:'专硕', value:'专硕'},{key:'MBA', value:'MBA'}]
  },
  {
    key:'zhengzhimianmao',
    title:'政治面貌',
    dataType:'varchar',
    showType:'multiSelect',
    options:[{key:'中共党员', value:'中共党员'}, {key:'中共预备党员', value:'中共预备党员'},{key:'共青团员', value:'共青团员'}, {key:'群众', value:'群众'},{key:'民主党派成员', value:'民主党派成员'}]
  },
  {
    key:'zhuanye',
    title:'专业',
    dataType:'varchar',
    showType:'multiSelect',
    options:[{key:'管理科学与工程', value:'管理科学与工程'}, {key:'经济系统分析与管理', value:'经济系统分析与管理'}, {key:'信息管理与电子政务', value:'信息管理与电子政务'}, {key:'交通系统工程', value:'交通系统工程'}, {key:'系统工程', value:'系统工程'}, {key:'信息管理与电子政务', value:'信息管理与电子政务'}, {key:'会计学', value:'会计学'}, {key:'企业管理', value:'企业管理'}, {key:'旅游管理', value:'旅游管理'}, {key:'技术经济及管理', value:'技术经济及管理'}, {key:'项目管理', value:'项目管理'}, {key:'环境管理', value:'环境管理'}, {key:'投资学', value:'投资学'}, {key:'知识产权管理', value:'知识产权管理'}, {key:'物流工程', value:'物流工程'}, {key:'金融学', value:'金融学'}, {key:'产业经济学', value:'产业经济学'}, {key:'国际贸易学', value:'国际贸易学'}, {key:'金融专硕', value:'金融专硕'}]
  },
  
];

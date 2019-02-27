// 定义某个表的querySchema
// schema的结构和含义参考下面的例子
// 注意: 所有的key不能重复

module.exports = [
  {
    key:'tutor_id',
    title:'编号',
    dataType:'varchar',
    primary:true
  },
  {
    key:'tutor_name',
    title:'导师姓名',
    dataType:'varchar'
  },
  {
    key:'tutor_phone',
    title:'联系方式',
    dataType:'varchar'
  }
];

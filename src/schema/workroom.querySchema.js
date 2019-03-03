// 定义某个表的querySchema
// schema的结构和含义参考下面的例子
// 注意: 所有的key不能重复

module.exports = [
  {
    key:'roomname',
    title:'教研室',
    dataType:'varchar',
  },
  {
    key:'support_name',
    title:'负责人名称',
    dataType:'varchar',
  },
  {
    key:'work_organization',
    title:'研究所',
    dataType:'varchar'
  },
];

// 定义某个表的querySchema
// schema的结构和含义参考下面的例子
// 注意: 所有的key不能重复

module.exports = [
  {
    key:'ip',
    title:'IP',
    dataType:'varchar',
  },
  {
    key: 'date',
    title: '登录日期',
    dataType: 'datetime',  // 日期范围查询, 日期范围查询占用的显示空间会很大, 注意排版
    showType: 'between',
    defaultValueBegin: '2019-01-01 12:34:56',  // 注意日期类型defaultValue的格式
    defaultValueEnd: '2019-12-01 22:33:44',
  },
];

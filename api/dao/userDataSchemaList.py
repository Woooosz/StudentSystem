key = 'key'
title='title'
dataType='dataType'
userQuerySchema = [
  {
    key: 'xuwhao',
    title: '学号',
    dataType: 'varchar',
  },
  {
    key: 'xingming',
    title: '姓名',
    dataType: 'varchar',
  },
  {
    key: 'shoujihaoma',
    title: '手机号码',
    dataType: 'varchar',
  },
  {
    key: 'gongzuoshi',
    title: '工作室',
    dataType: 'varchar',
  },
  {
    key: 'daoshixingming',
    title: '工作室',
    dataType: 'varchar',
  },
  {
    key:'xueweileixing',
    title:'学位类型',
    dataType:'varchar',
    showType:'radio',
    options:[{key:'shuoshi', value:'硕士'},{key:'boshi', value:'博士'}]
  },
  {
    key: 'isNative',
    title: '是否住校',
    dataType: 'varchar',
    showType: 'radio',
    options: [{key: 'yes', value: '是'}, {key: 'no', value: '否'}],
  },
  {
    key: 'location',
    title: '地理位置',
    dataType: 'varchar',  // 一般而言dataType是字符串, 但也可以是数字
    showType: 'cascader',
    defaultValue: ['zhejiang', 'hangzhou', 'xihu'],
    options: [{
      value: 'zhejiang',   // option的value必须是字符串, 和select类似
      label: '浙江',
      children: [{
        value: 'hangzhou',
        label: '杭州',
        children: [{
          value: 'xihu',
          label: '西湖',
        }],
      }],
    }, {
      value: 'yuzhou',
      label: '宇宙中心',
      children: [{
        value: 'wudaokou',
        label: '五道口',
      }],
    }],
  },
];

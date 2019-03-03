import React from 'react';
import {Link} from 'react-router';

module.exports = [
  {
    key: 'id',
    title: '序号',
    dataType: 'int',
    primary: true,
    // 当前列如何渲染
    render(text) {
      // 只是一个例子, 说明下render函数中可以用this, 甚至可以this.setState之类的
      // 我会把this绑定到当前的InnerTable组件上
      // 但需要注意, 如果要使用this, render必须是普通的函数, 不能是箭头函数, 因为箭头函数不能手动绑定this
      // this不要滥用, 搞出内存泄漏就不好了
      // render应该尽量是一个纯函数, 不要有副作用
      // console.log(this.props.tableName);
      return text;
    },
    // 表格中根据这一列排序, 排序规则可以配置
    sorter: (a, b) => a.id - b.id,
  },
  {
    key:'xueweileixing',
    title:'学位类型',
    dataType:'varchar',
  },
  {
    key: 'peiyangfangshi',
    title: '培养方式',
    dataType: 'varchar',
  },

  {
    key:'stuid',
    title:'学号',
    dataType:'varchar',
  },
  {
    key:'xingming',
    title:'姓名',
    dataType:'varchar',
  },
  {
    key:'nianji',
    title:'年级',
    dataType:'varchar',

  },
  {
    key:'zhuanye',
    title:'专业',
    dataType:'varchar',

  },
  {
    key:'daoshi',
    title:'导师',
    dataType:'varchar',

  },
  {
    key:'daoshidianhua',
    title:'导师电话',
    dataType:'varchar',

  },
  {
    key:'biyeyuanxiao',
    title:'毕业院校',
    dataType:'varchar',

  },
  {
    key:'xingbie',
    title:'性别',
    dataType:'varchar',

  },
  {
    key:'zhengzhimianmao',
    title:'政治面貌',
    dataType:'varchar',

  },
  {
    key:'jiatinglianxiren',
    title:'家庭联系人',
    dataType:'varchar',

  },
  {
    key:'jiatinglianxidianhua',
    title:'家庭联系电话',
    dataType:'varchar',

  },
  {
    key:'jiatingzhuzhi',
    title:'家庭住址',
    dataType:'varchar',

  },
  {
    key:'minzu',
    title:'民族',
    dataType:'varchar',

  },
  {
    key:'hunfou',
    title:'婚否',
    dataType:'varchar',

  },
  {
    key:'chushengriqi',
    title:'出生日期',
    dataType:'varchar',

  },
  {
    key:'shenfengzhenghaoma',
    title:'身份证号码',
    dataType:'varchar',

  },
  {
    key: 'shoujihaoma',
    title: '手机号码',
    dataType: 'varchar',
    // 跳转其他组件的例子, 可以带参数, 一般用于关联查询之类的
    // 其实就是react-router的配置
    render: (text, record) => <Link to={`/index/option1?name=${record.id}`}>{'跳转其他组件'}</Link>,
    validator: [{type: 'string', pattern: /^[a-zA-Z0-9]+$/, message: '只能是数字+字母'}],
  },
  {
    key: 'email',
    title: '邮箱',
    dataType: 'varchar',
    validator: [{type: 'email', required: true, message: '邮箱地址有误'}],
    // 跳转邮箱地址例子
    render: (text) => <a href="mailto:wushizhe001@gmail.com" target="_blank">{'wushizhe001@gmail.com'}</a>,
  },
  {
    key:'shifouzhuxiao',
    title:'是否住校',
    dataType:'varchar',

  },
  {
    key:'xiaowaizhuzhi',
    title:'校外住址',
    dataType:'varchar',

  },
  {
    key:'susheid',
    title:'宿舍 ID',
    dataType:'varchar',

  },
  {
    key:'fangjianhao',
    title:'房间号',
    dataType:'varchar',

  },
  {
    key:'gongzuoshi',
    title:'工作室',
    dataType:'varchar',

  },
  {
    key:'gongzuowei',
    title:'工作位',
    dataType:'varchar',

  },
  {
    key:'suozaifuzeren',
    title:'所在负责人',
    dataType:'varchar',

  },
  {
    key:'yanjiusuo',
    title:'研究所',
    dataType:'varchar',

  },
  {
    key:'singleRecordActions',
    title:'操作',
    width:200,
    actions:[
      {
        name:'删除',
        type:'delete',
      },
    ],
  },
];

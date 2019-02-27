import React from 'react';
import {Link} from 'react-router';
import {UpdateGPA1, UpdateGPA2} from '../components/UpdateComponentDemo';

module.exports = [
  {
    key: 'tutor_id',
    title: '编号',
    dataType: 'varchar',
    primary: true,
    disable: false,
    render(text) {
      // 只是一个例子, 说明下render函数中可以用this, 甚至可以this.setState之类的
      // 我会把this绑定到当前的InnerTable组件上
      // 但需要注意, 如果要使用this, render必须是普通的函数, 不能是箭头函数, 因为箭头函数不能手动绑定this
      // this不要滥用, 搞出内存泄漏就不好了
      // render应该尽量是一个纯函数, 不要有副作用
      // console.log(this.props.tableName);
      return text;
    },
  },
  {
    key:'tutor_name',
    title:'导师姓名',
    dataType:'varchar',
  },
  {
    key:'tutor_phone',
    title:'导师联系方式',
    dataType:'varchar',
  },
];

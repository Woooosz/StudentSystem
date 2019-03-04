import React from 'react';
import {Link} from 'react-router';

module.exports = [
  {
    key: 'id',
    title: '编号',
    dataType: 'int',
    primary: true,
    showInTable: false,
  },
  {
    key:'username',
    title:'用户名',
    dataType:'varchar',
    disabled:true,
  },
  {
    key:'ip',
    title:'登录IP',
    dataType:'varchar',
    disabled:true,
  },
  {
    key:'date',
    title:'登录日期',
    dataType:'datetime',
    disabled:true,
  },
  {
    key:'platform',
    title:'登录平台',
    dataType:'varchar',
    disabled:true,
  },
  {
    key:'browser',
    title:'登录浏览器',
    dataType:'varchar',
    disabled: true,
  },
];

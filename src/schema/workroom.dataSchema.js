import React from 'react';
import {Link} from 'react-router';

module.exports = [
  {
    key: 'workroom_id',
    title: '编号',
    dataType: 'int',
    primary: true,
    showInTable: true,
  },
  {
    key:'roomname',
    title:'名称',
    dataType:'varchar',
  },
  {
    key:'capacity',
    title:'容量',
    dataType:'varchar',
  },
  {
    key:'support_name',
    title:'负责人姓名',
    dataType:'varchar',
  },
  {
    key:'work_organization',
    title:'研究所',
    dataType:'varchar',
  },
  {
    key:'used',
    title:'当前使用',
    dataType:'varchar',
    disabled: true,
  },
  {
    key:'rate',
    title:'利用率',
    dataType:'float',
    disabled:true,
  },
];

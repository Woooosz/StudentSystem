import React from 'react';
import {Link} from 'react-router';
import {UpdateGPA1, UpdateGPA2} from '../components/UpdateComponentDemo';

module.exports = [
  {
    key:'id',
    title:'编号',
    dataType:'int',
    primary:true,
  },
  {
    key: 'tutor_id',
    title: '教师编号',
    dataType: 'varchar',
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

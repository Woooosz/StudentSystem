import React from 'react';
import {Link} from 'react-router';
import {UpdateGPA1, UpdateGPA2} from '../components/UpdateComponentDemo';

module.exports = [
  {
    key: 'workroom_id',
    title: '编号',
    dataType: 'int',
    primary: true,
  },
  {
    key:'name',
    title:'名称',
    dataType:'varchar',
  },
  {
    key:'capacity',
    title:'容量',
    dataType:'int',
  },
  {
    key:'support_name',
    title:'负责人姓名',
    dataType:'varchar',
  },
  {
    key:'work_orgainzation',
    title:'研究所',
    dataType:'varchar'
  },
  {
    key:'remain',
    title:'剩余空位',
    dataType:'int',
  }
];

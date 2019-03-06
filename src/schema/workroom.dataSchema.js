import React from 'react';
import {Link} from 'react-router';

module.exports = [
  {
    key: 'workroom_id',
    title: '编号',
    dataType: 'int',
    primary: true,
    showInTable: false,
  },
  {
    key:'roomname',
    title:'教研室',
    dataType:'varchar',
  },
  {
    key:'capacity',
    title:'容量',
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
    // 这个key是我预先定义好的, 注意不要冲突
    key: 'singleRecordActions',
    title: '操作',  // 列名
    //width: 300,  // 宽度
    actions:[
      {
        // 如果不是预定义的type(update/delete/newLine/component), 就检查是否有render函数
        // 有render函数就直接执行
        render: (record) => <a href={`http://jxy.me?id=${record.id}`} target="_blank">{'使用情况'}</a>,
      },
    ],
  },
];

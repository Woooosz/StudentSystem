/**
 * 定义sidebar和header中的菜单项
 *
 * 一些约定:
 * 1.菜单最多3层;
 * 2.只有"叶子"节点才能跳转;
 * 3.所有的key都不能重复;
 */

// 其实理论上可以嵌套更多层菜单的, 但是我觉得超过3层就不好看了
// 可用的图标见这里: https://ant.design/components/icon-cn/

// 定义siderbar菜单
const sidebarMenu = [
  {
    key: 'index',  // route时url中的值
    name: '信息维护',  // 在菜单中显示的名称
    icon: 'smile',  // 图标是可选的
    child: [
      // {
      //   key: 'option1',
      //   name: '用户',
      //   icon: 'play-circle',   // 二级三级菜单也可以带图标
      // },
      // {
      //   key: 'option2',
      //   name: '图片DEMO',
      //   icon: 'android',
      // },
      // {
      //   key: 'option3',
      //   name: '自定义操作',
      //   icon: 'bulb',
      // },
      {
        key:'tutor',
        name:'导师信息',
        icon:'bulb',
      },
      {
        key:'workroom',
        name:'教研室信息',
        icon:'bulb',
      },
      {
        key:'student',
        name:'学生信息',
        icon:'bulb',
      },
    ],
  },
  {
    key:'shujuhuizong',
    name:'数据汇总',
    child:[
      {
        key: 'user',
        name: '学生信息汇总',
        icon: 'bulb',
      },
    ],
  },
  {
    key: 'alone',
    name: '权限管理',
    icon: 'clock-circle',
    child:[
      {
        key:'logInfo',
        name:'登录信息',
      },
    ],
  },
];

export default sidebarMenu;

// 定义header菜单, 格式和sidebar是一样的
// 特殊的地方在于, 我规定header的最右侧必须是用户相关操作的菜单, 所以定义了一个特殊的key
// 另外注意这个菜单定义的顺序是从右向左的, 因为样式是float:right
export const headerMenu = [
  {
    // 一个特殊的key, 定义用户菜单, 在这个submenu下面设置icon/name不会生效
    key: 'userMenu',
    child: [
      {
        key: 'modifyUser',
        name: '修改用户信息',
        icon: 'bulb',
        // 对于headerMenu的菜单项, 可以让它跳到外部地址, 如果设置了url属性, 就会打开一个新窗口
        // 如果不设置url属性, 行为和sidebarMenu是一样的, 激活特定的组件, 注意在index.js中配置好路由, 否则会404
      },
    ]
  },
];

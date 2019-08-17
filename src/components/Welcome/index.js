import React from 'react';
import './index.less';
// 引入 ECharts 主模块
import echarts from 'echarts/lib/echarts';
// 引入柱状图
import  'echarts/lib/chart/bar';
import  'echarts/lib/chart/pie';
import  'echarts/lib/chart/scatter';
import  'echarts/lib/chart/effectScatter';



// 引入提示框和标题组件
import 'echarts/lib/component/tooltip';
import 'echarts/lib/component/title';
import ajax from '../../utils/ajax';
import {Row, Col} from 'antd'

/**
 * 展示欢迎界面
 */
class Welcome extends React.PureComponent {
    async componentDidMount() {
    
    const res = await ajax.getechart();
    // 基于准备好的dom，初始化echarts实例
    var myChart1 = echarts.init(document.getElementById('main'));
    window.onresize = myChart1.resize;
    // 绘制图表
    myChart1.setOption({
        title : {
            text: '经济管理学院各年级学生人数',
            x:'center'
        },
        tooltip: {},
        xAxis: res.chart1.xAxis,
        yAxis: {},
        series: res.chart1.series
    });

    var myChart2 = echarts.init(document.getElementById('main2'));
    window.onresize = myChart2.resize;
    myChart2.setOption({
        title : {
            text: '经济管理学院各专业',
            x:'center'
        },
        tooltip : {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: {
            x : 'center',
            y : 'bottom',
            data:['管理科学与工程','经济系统分析与管理','信息管理域电子政务','系统工程','会计学','企业管理','旅游管理','项目管理']
        },
        toolbox: {
            show : true,
            feature : {
                mark : {show: true},
                dataView : {show: true, readOnly: false},
                magicType : {
                    show: true,
                    type: ['pie', 'funnel']
                },
                restore : {show: true},
                saveAsImage : {show: true}
            }
        },
        calculable : true,
        series : [
            {
                name:'经济管理学院',
                type:'pie',
                radius : [30, 110],
                roseType : 'area',
                data:[
                    {value:10, name:'管理科学与工程'},
                    {value:5, name:'经济系统分析与管理'},
                    {value:15, name:'信息管理与电子政务'},
                    {value:25, name:'系统工程'},
                    {value:20, name:'会计学'},
                    {value:35, name:'企业管理'},
                    {value:30, name:'旅游管理'},
                    {value:40, name:'项目管理'}
                ]
            }
        ]
    });



    var myChart3 = echarts.init(document.getElementById('main3'));
    window.onresize = myChart3.resize;
    myChart3.setOption( {
        tooltip : {
            trigger: 'axis',
            axisPointer : {            // 坐标轴指示器，坐标轴触发有效
                type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
            }
        },
        legend: {
            data: ['直接访问', '邮件营销','联盟广告','视频广告','搜索引擎']
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        xAxis:  {
            type: 'value'
        },
        yAxis: {
            type: 'category',
            data: ['2019级','2018级','2017级','2016级','2015级','2014级','2013级']
        },
        series: [
            {
                name: '直接访问',
                type: 'bar',
                stack: '总量',
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: [320, 302, 301, 334, 390, 330, 320]
            },
            {
                name: '邮件营销',
                type: 'bar',
                stack: '总量',
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: [120, 132, 101, 134, 90, 230, 210]
            },
            {
                name: '联盟广告',
                type: 'bar',
                stack: '总量',
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: [220, 182, 191, 234, 290, 330, 310]
            },
            {
                name: '视频广告',
                type: 'bar',
                stack: '总量',
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: [150, 212, 201, 154, 190, 330, 410]
            },
            {
                name: '搜索引擎',
                type: 'bar',
                stack: '总量',
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: [820, 832, 901, 934, 1290, 1330, 1320]
            }
        ]
    });

    var myChart4 = echarts.init(document.getElementById('main4'));
    window.onresize = myChart4.resize;
    myChart4.setOption(  {
        title : {
            text: '教研室使用情况',
            x:'center'
        },
        legend: {},
        tooltip: {},
        dataset: {
            source: [
                ['教研室', '301', '302', '303', '304', '311', '312'],
                ['已使用', 41.1, 30.4, 65.1, 53.3, 83.8, 98.7],
                ['未使用', 86.5, 92.1, 85.7, 83.1, 73.4, 55.1],
            ]
        },
        series: [ 
        {
            type: 'pie',
            radius: 60,
            title:{text:'dsafasdf'},
            name:'301',
            center: ['20%', '30%'],
            encode: {
                itemName: '教研室',
                value: '301'
            }
        }, {
            type: 'pie',
            radius: 60,
            name:'302',
            center: ['40%', '30%'],
            encode: {
                itemName: '教研室',
                value: '302'
            }
        }, {
            type: 'pie',
            radius: 60,
            name:'303',
            center: ['60%', '30%'],
            encode: {
                itemName: '教研室',
                value: '303'
            }
        },
        {
            type: 'pie',
            radius: 60,
            title:{text:'dsafasdf'},
            name:'301',
            center: ['80%', '30%'],
            encode: {
                itemName: '教研室',
                value: '301'
            }
        }
    ]
    });

    var myChart5 = echarts.init(document.getElementById('main5'));
    window.onresize = myChart5.resize;
    myChart5.setOption({
        tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b}: {c} ({d}%)"
        },
        legend: {
            orient: 'vertical',
            x: 'left',
            data:['直达','营销广告','搜索引擎','邮件营销','联盟广告','视频广告','百度','谷歌','必应','其他']
        },
        series: [
            {
                name:'访问来源',
                type:'pie',
                selectedMode: 'single',
                radius: [0, '30%'],
    
                label: {
                    normal: {
                        position: 'inner'
                    }
                },
                labelLine: {
                    normal: {
                        show: false
                    }
                },
                data:[
                    {value:335, name:'博士', selected:true},
                    {value:679, name:'MBA'},
                    {value:1548, name:'硕士'}
                ]
            },
            {
                name:'培养方式',
                type:'pie',
                radius: ['40%', '55%'],
                label: {
                    normal: {
                        formatter: '{a|{a}}{abg|}\n{hr|}\n  {b|{b}：}{c}  {per|{d}%}  ',
                        backgroundColor: '#eee',
                        borderColor: '#aaa',
                        borderWidth: 1,
                        borderRadius: 4,
                        // shadowBlur:3,
                        // shadowOffsetX: 2,
                        // shadowOffsetY: 2,
                        // shadowColor: '#999',
                        // padding: [0, 7],
                        rich: {
                            a: {
                                color: '#999',
                                lineHeight: 22,
                                align: 'center'
                            },
                            // abg: {
                            //     backgroundColor: '#333',
                            //     width: '100%',
                            //     align: 'right',
                            //     height: 22,
                            //     borderRadius: [4, 4, 0, 0]
                            // },
                            hr: {
                                borderColor: '#aaa',
                                width: '100%',
                                borderWidth: 0.5,
                                height: 0
                            },
                            b: {
                                fontSize: 16,
                                lineHeight: 33
                            },
                            per: {
                                color: '#eee',
                                backgroundColor: '#334455',
                                padding: [2, 4],
                                borderRadius: 2
                            }
                        }
                    }
                },
                data:[
                    {value:335, name:'直达'},
                    {value:310, name:'邮件营销'},
                    {value:234, name:'联盟广告'},
                    {value:135, name:'视频广告'},
                    {value:1048, name:'百度'},
                    {value:251, name:'谷歌'},
                    {value:147, name:'必应'},
                    {value:102, name:'其他'}
                ]
            }
        ]
    });
    

}


  
  render() {
    return (

      <div>
      <Row gutter={16}>
        <Col span={12}>
            <div  id='main' style={{width:'100%', height:300}}></div>
        </Col>
        <Col span={12}>
            <div  id='main2' style={{width:'100%', height:300}}></div>   
        </Col>
      </Row>

      <Row gutter={16}>
            <Col span={12}>
                <div  id='main3' style={{width:'100%', height:300}}></div>   
            </Col>
            <Col span={12}>
                <div  id='main5' style={{width:'100%', height:300}}></div>   
            </Col>
        </Row>

        <Row gutter={16}>
            <Col span={24}>
                <div  id='main4' style={{width:'100%', height:300}}></div>   
            </Col>
        </Row>


    </div>
      

        
    );
  }
}

export default Welcome;

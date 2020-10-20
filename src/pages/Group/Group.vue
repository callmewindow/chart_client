<template>
  <div class="PoliticsInfo">
    <Head :title="eventData.title" :showBack="showBack" :name="backTitle"></Head>
    <div class="PoliticsInfoBox">
      <div class="InfoWrap">
        <!-- 时间选择器 -->
        <div class="selectTime">
          <!-- <div>
            <span
              v-show="timeSum>0&&timeSum<60"
              style="color:rgba(255,255,255,0.68);display:inline-block;margin-right:10px"
            >({{timeSum}}s)</span>
            <el-date-picker
              v-model="timevalue"
              type="daterange"
              range-separator="至"
              start-placeholder="开始日期"
              end-placeholder="结束日期"
              @change="getDateValue()"
            ></el-date-picker>
          </div>-->
        </div>
        <div class="groupBox">
          <div class="gropTop">
            <div class="mesBase common">
              <Icon></Icon>
              <p class="title">事件基本属性</p>
              <div class="mesBaseBox">
                <div class="baseMes">
                  <table>
                    <tr>
                      <td class="td1" valign="top">关键词：</td>
                      <td class="td2" valign="top">
                        <ul class="news">
                          <li class="every_news" v-for="(item,index) in keyWordList" :key="index">
                            <p>{{item}}</p>
                          </li>
                        </ul>
                      </td>
                      <td class="td3" valign="top">
                        <div class="goleft">
                          <div class="leave">
                            <div class="effect">
                              <div v-if="eventData.grade==1">
                                <img src="../../assets/img/danger1.png" alt />
                                <span style="color:#741B33">一级</span>
                              </div>
                              <div v-if="eventData.grade==2">
                                <img src="../../assets/img/danger2.png" alt />
                                <span style="color:#773F3B">二级</span>
                              </div>
                              <div v-if="eventData.grade==3">
                                <img src="../../assets/img/danger3.png" alt />
                                <span style="color:#7B8744">三级</span>
                              </div>
                              <div v-if="eventData.grade==4">
                                <img src="../../assets/img/danger4.png" alt />
                                <span style="color:#B7F2F9">四级</span>
                              </div>
                              <div v-if="eventData.grade==5">
                                <img src="../../assets/img/danger5.png" alt />
                                <span style="color:#E6CCFF">五级</span>
                              </div>
                            </div>
                            <div class="per_box">
                              <p>影响力指标</p>
                              <div class="perbox">
                                <div class="per" :style="'width:'+eventData.impactIndicators+'%'"></div>
                              </div>
                              <p>{{eventData.impactIndicators}}</p>
                            </div>
                          </div>
                        </div>
                      </td>
                    </tr>
                    <tr>
                      <td class="td1" valign="top">标签：</td>
                      <td class="td2" colspan="2" valign="top">
                        <ul class="lables">
                          <li
                            class="every_lable"
                            v-for="(item,index) in labelWordList"
                            :key="index"
                          >
                            <p>{{item}}</p>
                          </li>
                        </ul>
                      </td>
                    </tr>
                  </table>
                </div>
                <p class="content">{{eventData.detailsynopsis}}</p>
              </div>
            </div>
            <div class="mesPredicted common">
              <Icon></Icon>
              <div class="mesPredicted_box">
                <p class="title" style="margin:0.3125rem 0 0.3125rem">事件发生地</p>
                <div id="myChartMap"></div>
              </div>
            </div>
          </div>
          <div class="gropBottom common">
            <Icon></Icon>
            <div style="display:flex;width:100%;height:100%">
              <div class="relation">
                <div class="select_local">
                  <div>
                    <el-select v-model="value" placeholder="请选择">
                      <el-option
                        v-for="item in options"
                        :key="item.value"
                        :label="item.label"
                        :value="item.label"
                      ></el-option>
                    </el-select>
                  </div>
                </div>
                <div id="myChartActive" class="myCharts" :style="{width:'100%',height:'80%'}"></div>
              </div>
              <div class="select_event">
                <template>
                  <div class="select_content" v-show="flag">
                    <div class="select_title">自媒体热度</div>
                    <div id="myChartZheHot" class="myChartZhe"></div>
                  </div>
                  <div class="select_content" v-show="flag">
                    <div class="select_title">自媒体参与度</div>
                    <div id="myChartZhePartIn" class="myChartZhe"></div>
                  </div>
                </template>
                <template>
                  <div class="select_content">
                    <div class="select_title">情感倾向</div>
                    <div id="myChartZheEmotion" class="myChartZhe"></div>
                  </div>
                  <div class="select_content">
                    <div class="select_title">用户活跃度</div>
                    <div id="myChartZheLive" class="myChartZhe"></div>
                  </div>
                </template>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import "../../../static/js/chinamap/china.js";
import Head from "../../components/Head/Head.vue";
import Icon from "../../components/Icon/Icon.vue";
import BMap from "BMap";
import * as eventAPI from "../../APIs/event.js";
import newsetDate from "../../untils/newsetDate.js"; //地图数据和列表页数据合计

var vm;
var timer;
export default {
  name: "Group",
  components: {
    Head,
    Icon
  },
  data() {
    return {
      showBack: true,
      backTitle: "返回",
      timeSum: 60,
      timevalue: ["2020-01-03", "2020-01-03"],
      options: [],
      value: "",
      linecolor: "#fb6237",
      eventData: "", // 事件的所有数据
      keyWordList: [], // 事件的关键词列表
      labelWordList: [], // 事件的标签列表
      mapData: {}, // 事件的位置信息
      // 自媒体热度
      selfMediaPopularity: {
        actual: [],
        predicted: []
      },
      // 自媒体参与度
      selfMediaParticipation: {
        actual: [],
        predicted: []
      },
      // 情感倾向
      emotional: {
        actual: [],
        predicted: []
      },
      // 用户活跃度
      liveness: {
        actual: [],
        predicted: []
      },
      one: false,
      two: true,
      three: true,
      four: true,
      //折线图横坐标的值
      xData: [],
      xActual: [],
      xPredicted: [],
      chartZheHot: "",
      chartZhePartIn: "",
      chartZheEmotion: "",
      chartZheLive: "",
      option: [],
      // 关系图数据
      currentRelation: [],
      node: [],
      relation: [],
      categories: [],
      optionActive: {},
      chart1: "",
      flag: true,
      flag2: false
    };
  },
  created() {
    this.getEventData();
  },
  mounted() {
    this.drowlineZheHot();
    this.drowlineZhePartIn();
    this.drowlineZheEmotion();
    this.drowlineZheLive();
    this.drowBaiduMap();
  },
  destroyed() {},
  watch: {
    value(newValue, oldValue) {
      if (newValue != oldValue) {
        this.updateRelation();
      }
    }
  },
  methods: {
    // 获取事件数据
    async getEventData() {
      this.eventData = this.$route.params.item;
      // // 提取第一个事件填充没有的数据
      // this.eventData = newsetDate.data.resultList[0];
      // let temp = await eventAPI.getEventById(this.$route.params.eventId);
      // let tempData = temp.data;
      // // 批量替换当前事件已有的字段，即尽可能更新实际的数据
      // for(let key in tempData){
      //   this.eventData[key] = tempData[key];
      // }
      // 关键词列表
      this.keyWordList = this.eventData.keyWord.split(",");
      this.labelWordList = this.eventData.labelWord.split(",");

      this.mapData = {
        name: this.eventData.title,
        value: [
          this.eventData.longitude,
          this.eventData.latitude,
          this.eventData.number
        ]
      };

      let dataBox = this.eventData.relation[0].effectList;
      for (let i = 0; i < dataBox.length; i++) {
        // console.log(dataBox[i]);
        this.xData.push(dataBox[i].dateTime);

        // // 自媒体热度
        this.selfMediaPopularity.actual.push(dataBox[i].selfMediaPopularity[0]);
        this.selfMediaPopularity.predicted.push(
          dataBox[i].selfMediaPopularity[1]
        );
        // 自媒体参与度
        this.selfMediaParticipation.actual.push(
          dataBox[i].selfMediaParticipation[0]
        );
        this.selfMediaParticipation.predicted.push(
          dataBox[i].selfMediaParticipation[1]
        );
        // 情感倾向
        this.emotional.actual.push(dataBox[i].emotional[0]);
        this.emotional.predicted.push(dataBox[i].emotional[1]);
        // 用户活跃度
        this.liveness.actual.push(dataBox[i].liveness[0]);
        this.liveness.predicted.push(dataBox[i].liveness[1]);
      }
      this.xActual = this.selfMediaPopularity.actual;
      this.xPredicted = this.selfMediaPopularity.predicted;

      // 关系图数据集合
      this.currentRelation = this.eventData.relation;
      // 获得下拉框数据

      for (let i = 0; i < this.currentRelation.length; i++) {
        let obj = {
          label: this.currentRelation[i].name,
          value: this.currentRelation[i].value
        };
        this.options.push(obj);
      }
      this.value = this.options[0].label;
    },

    // 绘制地图
    drowBaiduMap() {
      var map = new BMap.Map(document.getElementById("myChartMap")); // 创建Map实例
      var point = new BMap.Point(
        this.eventData.longitude,
        this.eventData.latitude
      );
      map.centerAndZoom(point, 12);
      var marker = new BMap.Marker(point); // 创建标注
      map.addOverlay(marker); // 将标注添加到地图中
      marker.disableDragging(); // 不可拖拽
      marker.setAnimation(BMAP_ANIMATION_BOUNCE); //跳动的动画
      map.enableScrollWheelZoom(true); //开启鼠标滚轮缩放
    },

    // 重置关系图数据
    updateRelation() {
      this.zheData(this.value);
      // 改变关系图数据
      this.node = [];
      this.relation = [];
      this.categories = [];
      this.optionActive = {};
      this.chart1 = "";
      for (let i = 0; i < this.currentRelation.length; i++) {
        if (this.value == this.currentRelation[i].name) {
          // 重置关系图数据
          let node = this.currentRelation[i].relationDetail.node;
          let relation = this.currentRelation[i].relationDetail.relation;
          for (let j = 0; j < node.length; j++) {
            let obj = {
              name: node[j].name,
              symbolSize: node[j].symbolSize / 3,
              category: node[j].category,
              itemStyle: {
                color: "#827EE4"
              }
            };
            this.node.push(obj);
          }
          for (let j = 0; j < relation.length; j++) {
            let obj = {
              source: relation[j].source,
              target: relation[j].target,
              label: {
                show: false
              }
            };
            this.relation.push(obj);
          }

          this.categories = this.currentRelation[i].relationDetail.categories;
        }
      }
      this.drowlineActive();
    },

    // 折线图数据处理
    zheData(e) {
      // console.log(e);
      for (let i = 0; i < this.currentRelation.length; i++) {
        if (this.value == this.currentRelation[i].name) {
          this.xData = [];
          this.xActual = [];
          this.xPredicted = [];
          // 自媒体热度
          this.selfMediaPopularity = {
            actual: [],
            predicted: []
          };
          // 自媒体参与度
          this.selfMediaParticipation = {
            actual: [],
            predicted: []
          };
          // 情感倾向
          this.emotional = {
            actual: [],
            predicted: []
          };
          // 用户活跃度
          this.liveness = {
            actual: [],
            predicted: []
          };
          let dataBox = this.currentRelation[i].effectList;
          for (let j = 0; j < dataBox.length; j++) {
            // console.log(dataBox[j]);
            this.xData.push(dataBox[j].dateTime);
            // // 自媒体热度
            this.selfMediaPopularity.actual.push(
              dataBox[j].selfMediaPopularity[0]
            );
            this.selfMediaPopularity.predicted.push(
              dataBox[j].selfMediaPopularity[1]
            );
            // 自媒体参与度
            this.selfMediaParticipation.actual.push(
              dataBox[j].selfMediaParticipation[0]
            );
            this.selfMediaParticipation.predicted.push(
              dataBox[j].selfMediaParticipation[1]
            );
            // 情感倾向
            this.emotional.actual.push(dataBox[j].emotional[0]);
            this.emotional.predicted.push(dataBox[j].emotional[1]);
            // 用户活跃度
            this.liveness.actual.push(dataBox[j].liveness[0]);
            this.liveness.predicted.push(dataBox[j].liveness[1]);
          }

          if (this.currentRelation[i].type == 1) {
            this.flag = true;
            this.drowlineZheHot();
            this.drowlineZhePartIn();
            this.drowlineZheEmotion();
            this.drowlineZheLive();
          } else if (this.currentRelation[i].type == 2) {
            this.flag = false;
            this.drowlineZheHot();
            this.drowlineZhePartIn();
            this.drowlineZheEmotion();
            this.drowlineZheLive();
          }
        }
      }
      // 折线图数据处理
    },

    //实例化折线图热度
    drowlineZheHot() {
      this.chartZheHot = this.$echarts.init(
        document.getElementById("myChartZheHot")
      );
      this.option = {
        xAxis: {
          type: "category",
          data: this.xData,
          boundaryGap: false,
          axisLine: {
            lineStyle: {
              color: "#ffffff"
            }
          },
          splitLine: {
            show: true,
            lineStyle: {
              type: "dashed"
            }
          }
        },
        yAxis: {
          type: "value",
          min: 0,
          max: 80,
          interval: 20,
          axisLine: {
            lineStyle: {
              color: "#ffffff"
            }
          },
          splitLine: {
            show: false
          }
        },
        series: [
          {
            data: this.selfMediaPopularity.actual,
            type: "line",
            lineStyle: {
              color: "#fb6237",
              width: 1
            },
            symbolSize: 0
          },
          {
            data: this.selfMediaPopularity.predicted,
            type: "line",
            lineStyle: {
              color: "#fb6237",
              width: 1,
              type: "dashed"
            },
            symbolSize: 0
          }
        ]
      };
      this.chartZheHot.clear();
      this.chartZheHot.setOption(this.option);
    },
    //实例化折线图参与度
    drowlineZhePartIn() {
      this.chartZhePartIn = this.$echarts.init(
        document.getElementById("myChartZhePartIn")
      );
      this.option = {
        xAxis: {
          type: "category",
          data: this.xData,
          boundaryGap: false,
          axisLine: {
            lineStyle: {
              color: "#ffffff"
            }
          },
          splitLine: {
            show: true,
            lineStyle: {
              type: "dashed"
            }
          }
        },
        yAxis: {
          type: "value",
          min: 0,
          max: 80,
          interval: 20,
          axisLine: {
            lineStyle: {
              color: "#ffffff"
            }
          },
          splitLine: {
            show: false
          }
        },
        series: [
          {
            data: this.selfMediaParticipation.actual,
            type: "line",
            lineStyle: {
              color: "#07e9db",
              width: 1
            },
            symbolSize: 0
          },
          {
            data: this.selfMediaParticipation.predicted,
            type: "line",
            lineStyle: {
              color: "#07e9db",
              width: 1,
              type: "dashed"
            },
            symbolSize: 0
          }
        ]
      };
      this.chartZhePartIn.clear();
      this.chartZhePartIn.setOption(this.option);
    },
    //实例化折线图情感
    drowlineZheEmotion() {
      this.chartZheEmotion = this.$echarts.init(
        document.getElementById("myChartZheEmotion")
      );
      this.option = {
        xAxis: {
          type: "category",
          data: this.xData,
          boundaryGap: false,
          axisLine: {
            lineStyle: {
              color: "#ffffff"
            }
          },
          splitLine: {
            show: true,
            lineStyle: {
              type: "dashed"
            }
          }
        },
        yAxis: {
          type: "value",
          min: 0,
          max: 80,
          interval: 20,
          axisLine: {
            lineStyle: {
              color: "#ffffff"
            }
          },
          splitLine: {
            show: false
          }
        },
        series: [
          {
            data: this.emotional.actual,
            type: "line",
            lineStyle: {
              color: "#827ee4",
              width: 1
            },
            symbolSize: 0
          },
          {
            data: this.emotional.predicted,
            type: "line",
            lineStyle: {
              color: "#827ee4",
              width: 1,
              type: "dashed"
            },
            symbolSize: 0
          }
        ]
      };
      this.chartZheEmotion.clear();
      this.chartZheEmotion.setOption(this.option);
    },
    //实例化折线图情感
    drowlineZheLive() {
      this.chartZheLive = this.$echarts.init(
        document.getElementById("myChartZheLive")
      );
      this.option = {
        xAxis: {
          type: "category",
          data: this.xData,
          boundaryGap: false,
          axisLine: {
            lineStyle: {
              color: "#ffffff"
            }
          },
          splitLine: {
            show: true,
            lineStyle: {
              type: "dashed"
            }
          }
        },
        yAxis: {
          type: "value",
          min: 0,
          max: 80,
          interval: 20,
          axisLine: {
            lineStyle: {
              color: "#ffffff"
            }
          },
          splitLine: {
            show: false
          }
        },
        series: [
          {
            data: this.liveness.actual,
            type: "line",
            lineStyle: {
              color: "#f2123c",
              width: 1
            },
            symbolSize: 0
          },
          {
            data: this.liveness.predicted,
            type: "line",
            lineStyle: {
              color: "#f2123c",
              width: 1,
              type: "dashed"
            },
            symbolSize: 0
          }
        ]
      };
      this.chartZheLive.clear();
      this.chartZheLive.setOption(this.option);
    },

    //实例化关系图
    drowlineActive() {
      this.chart1 = this.$echarts.init(
        document.getElementById("myChartActive")
      );
      this.optionActive = {
        backgroundColor: "transparent", // 背景颜色
        tooltip: {
          // 提示框的配置
          formatter: function(param) {
            return param.data.nameDetail;
          }
        },

        series: [
          {
            type: "graph", // 系列类型:关系图
            top: "10%", // 图表距离容器顶部的距离
            roam: true, // 是否开启鼠标缩放和平移漫游。默认不开启。如果只想要开启缩放或者平移，可以设置成 'scale' 或者 'move'。设置成 true 为都开启
            focusNodeAdjacency: true, // 是否在鼠标移到节点上的时候突出显示节点以及节点的边和邻接节点。[ default: false ]
            force: {
              // 力引导布局相关的配置项，力引导布局是模拟弹簧电荷模型在每两个节点之间添加一个斥力，每条边的两个节点之间添加一个引力，每次迭代节点会在各个斥力和引力的作用下移动位置，多次迭代后节点会静止在一个受力平衡的位置，达到整个模型的能量最小化。
              // 力引导布局的结果有良好的对称性和局部聚合性，也比较美观。
              repulsion: 150, // [ default: 50 ]节点之间的斥力因子(关系对象之间的距离)。支持设置成数组表达斥力的范围，此时不同大小的值会线性映射到不同的斥力。值越大则斥力越大
              edgeLength: [50, 20] // [ default: 30 ]边的两个节点之间的距离(关系对象连接线两端对象的距离,会根据关系对象值得大小来判断距离的大小)，
              // 这个距离也会受 repulsion。支持设置成数组表达边长的范围，此时不同大小的值会线性映射到不同的长度。值越小则长度越长。如下示例:
              // 值最大的边长度会趋向于 10，值最小的边长度会趋向于 50      edgeLength: [10, 50]
            },
            // layout: "circular", // 图的布局。[ default: 'none' ]
            layout: "force", // 图的布局。[ default: 'none' ]

            symbol: "circle",
            lineStyle: {
              // 关系边的公用线条样式。其中 lineStyle.color 支持设置为'source'或者'target'特殊值，此时边会自动取源节点或目标节点的颜色作为自己的颜色。
              normal: {
                // color: "target", // 线的颜色[ default: '#aaa' ]
                width: 2, // 线宽[ default: 1 ]
                type: "solid", // 线的类型[ default: solid ]   'dashed'    'dotted'
                opacity: 0.5, // 图形透明度。支持从 0 到 1 的数字，为 0 时不绘制该图形。[ default: 0.5 ]
                curveness: 0.2 // 边的曲度，支持从 0 到 1 的值，值越大曲度越大。[ default: 0 ]
              }
            },
            label: {
              // 关系对象上的标签
              normal: {
                show: true, // 是否显示标签
                position: "bottom", // 标签位置:'top''left''right''bottom''inside''insideLeft''insideRight''insideTop''insideBottom''insideTopLeft''insideBottomLeft''insideTopRight''insideBottomRight'
                textStyle: {
                  // 文本样式
                  fontSize: 12
                }
              }
            },
            edgeLabel: {
              // 连接两个关系对象的线上的标签
              normal: {
                show: true,
                textStyle: {
                  fontSize: 11
                },
                formatter: function(param) {
                  // 标签内容
                  return param.data.category;
                }
              }
            },
            data: this.node,
            links: this.relation,
            category: this.categories
          }
        ],
        animationEasingUpdate: "quinticInOut", // 数据更新动画的缓动效果。[ default: cubicOut ]    "quinticInOut"
        animationDurationUpdate: 100 // 数据更新动画的时长。[ default: 300 ]
      };
      this.chart1.clear();
      this.chart1.setOption(this.optionActive);
    }
  }
};
</script>

<style scoped lang="less">
@import url("./Group.less");
/deep/ .el-input {
  input {
    background: transparent;
    border: 1px solid #fff;
    color: #fff;
    padding: 0;
    padding-left: 0.625rem;
    border-radius: 0;
  }
}
/deep/ .el-range-editor--small.el-input__inner {
  background: transparent;
  border: none;
  color: #fff;
  padding: 0;
}
/deep/ .el-date-editor .el-range-input {
  background: transparent;
  border: none;
  color: #fff;
  padding: 0;
}
/deep/ .el-range-separator {
  margin-top: 6px !important;
  color: #fff !important;
}
/deep/ .myCharts input {
  font-size: 9px !important;
}
/deep/ .el-date-editor .el-range-input {
  width: 5.625rem;
}
.el-range-editor--small.el-input__inner {
  width: 15rem;
}
</style>

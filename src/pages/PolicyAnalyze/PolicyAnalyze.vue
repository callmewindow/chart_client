<template>
  <div class="PoliticsInfo">
    <Head :title="eventData.title" :showBack="showBack" :name="backTitle"></Head>
    <div class="PoliticsInfoBox">
      <div class="InfoWrap">
        <div class="groupBox">
          <div class="gropTop">
            <div class="mesBase common">
              <Icon></Icon>
              <p class="title">信息基本属性</p>
              <div class="mesBaseBox">
                <div class="baseMes">
                  <table>
                    <tr>
                      <td class="td1" valign="top">信息熵：</td>
                      <td class="td2" valign="top">{{eventData.informationEntropy}}</td>
                      <td rowspan="2" class="td3" valign="top">
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
                              <p>{{eventData.impactIndicators}}%</p>
                            </div>
                          </div>
                        </div>
                      </td>
                    </tr>
                    <tr>
                      <td class="td1" valign="top">关键词：</td>
                      <td class="td2" style="padding-top:0" valign="top">
                        <ul class="news">
                          <li class="every_news" v-for="(item,index) in keyWordList"  :key="index">
                            <p>{{item}}</p>
                          </li>
                        </ul>
                      </td>
                    </tr>
                    <tr>
                      <td class="td1" valign="top">参与人数：</td>
                      <td class="td2" style="padding-top:0px" valign="top">
                        主办方：
                        1642
                        ；警方：
                        327
                        ；预测总数：
                        3914
                        ；
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
              <p class="title">信息预测分析</p>
              <div class="select_event">
                
                <div>
                  <ul>
                    <li @click="clickOne(1)" v-show="!flag">
                      <div
                        class="colorset"
                        :style="one?'background-color:#fb6237':'background-color:#834635'"
                      ></div>
                      <p>自媒体热度</p>
                    </li>
                    <li @click="clickOne(2)" v-show="!flag">
                      <div
                        class="colorset"
                        :style=" two?'background-color:#07d9eb':'background-color:#217c76'"
                      ></div>
                      <p>自媒体参与</p>
                    </li>
                    <li @click="clickOne(3)" v-show="flag">
                      <div
                        class="colorset"
                        :style="three? 'background-color:#e5beef':'background-color:#7a6b7e'"
                      ></div>
                      <p>点赞量</p>
                    </li>
                    <li @click="clickOne(4)" v-show="flag">
                      <div
                        class="colorset"
                        :style="four? 'background-color:#4dfd87':'background-color:#3d8455'"
                      ></div>
                      <p>转发量</p>
                    </li>
                  </ul>
                </div>
                <div id="myChartZhe" class="myChartZhe" :style="{width:'100%',height:'80%'}"></div>
              </div>
            </div>
          </div>
          <div class="gropBottom common">
            <Icon></Icon>
            <p class="title">事件传播顺序与时效</p>
            <div class="time-line">
              <div style="white-space:nowrap;width:100%;height:100%;">
                <div
                  class="time-line-div"
                  v-for="(item,index) in eventData.forwardList"
                  :key="index"
                >
                  <div class="content_detail">
                    <div
                      style="height:100%; display:flex;justify-content:flex-end;flex-direction:column"
                    >
                      <div class="back_item_titel">
                        <p>{{item.websiteName}}</p>
                      </div>
                      <div class="back_item_content">
                        <ul>
                          <li
                            v-for="(ite,idx) in item.nameList"
                            :key="idx"
                            @click="changeData(ite.id)"
                          >{{ite.webName}}</li>
                        </ul>
                      </div>
                    </div>
                  </div>
                  <div ref="circular">
                    <div class="circle"></div>
                  </div>
                  <div>{{item.createTime}}</div>
                  <div class="img-dotted" ref="dotted"></div>
                </div>
              </div>
            </div>
            <div class="local-video">
              <video id="video-player" controls src="../../assets/video/lollipop_introduction.mp4"></video>
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
import effectList from "../../untils/effectList.js";

var vm;
export default {
  name: "PolicyAnalyze",
  components: {
    Head,
    Icon
  },
  data() {
    return {
      showBack: true,
      backTitle: "返回",
      title: "网络数据采集与分析系统", //页面标题
      timeSum: 60,
      // timevalue: ["2020-01-03", "2020-01-03"],
      video_src: "../../assets/video/lollipop_introduction.mp4",
      one: false,
      two: true,
      three: true,
      four: true,
      lineColor: "",
      eventData: "", // 事件的所有数据
      keyWordList: [], // 事件的关键词列表
      labelWordList: [], // 事件的标签列表
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
      // 点赞量
      clicks: {
        actual: [],
        predicted: []
      },
      // 转发量
      forwardingVolume: {
        actual: [],
        predicted: []
      },
      //折线图横坐标的值
      xData: [],
      xActual: [],
      xPredicted: [],
      chartZhe: "",
      option: [],
      effectList: [],
      flag: true,
      webId: ""
    };
  },
  created() {
    this.getEventData();
  },
  mounted() {
    // // 设置视频播放地址
    // let videoPlayer = document.getElementById("video-player");
    // videoPlayer.src = this.video_src;
    this.drowlineZhe();
  },
  destroyed() {},
  methods: {
    // 获取事件数据
    getEventData() {
      this.eventData = this.$route.params.item;
      this.eventData.detailsynopsis = this.eventData.detailsynopsis.substring(0,250);
      this.keyWordList = this.eventData.keyWord.split(",");
      // 最多显示四个关键词
      for(let i = this.keyWordList.length;i>4;i = this.keyWordList.length){
        this.keyWordList.pop();
      }
      this.labelWordList = this.eventData.labelWord.split(",");
      this.effectList = effectList.data.resultList;
      this.webId = this.eventData.forwardList[0].nameList[0].id;

      // 設置折线图默認数据
      for (let i = 0; i < this.effectList.length; i++) {
        if (this.webId == this.effectList[i].id) {
          this.zheData(i);
          // console.log(this.forwardingVolume);
        }
      }
    },
    // 折线图
    drowlineZhe() {
      this.chartZhe = this.$echarts.init(document.getElementById("myChartZhe"));
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
          axisTick: {
            show: false
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
          max: 160,
          interval: 20,
          axisLine: {
            lineStyle: {
              color: "#ffffff"
            }
          },
          splitLine: {
            show: false
          },
          axisTick: {
            show: false
          }
        },
        dataZoom: [
          {
            start: 0
          },
          {
            type: "slider",
            backgroundColor: "#09275D",
            fillerColor: "#09275D",
            borderColor: "#09275D"
          }
        ],
        series: [
          {
            data: this.xActual,
            type: "line",
            lineStyle: {
              color: this.lineColor,
              width: 1
            },
            symbolSize: 0
          },
          {
            data: this.xPredicted,
            type: "line",
            lineStyle: {
              color: this.lineColor,
              width: 1,
              type: "dashed"
            },
            symbolSize: 0
          }
        ]
      };
      this.chartZhe.clear();
      this.chartZhe.setOption(this.option);
    },
    // 点击切换折线图数据
    clickOne(e) {
      if (e == 1) {
        this.one = false;
        this.two = true;
        this.three = true;
        this.four = true;
        this.lineColor = "#fb6237";
        this.xActual = this.selfMediaPopularity.actual;
        this.xPredicted = this.selfMediaPopularity.predicted;
      } else if (e == 2) {
        this.one = true;
        this.two = false;
        this.three = true;
        this.four = true;
        this.lineColor = "#07e9db";
        this.xActual = this.selfMediaParticipation.actual;
        this.xPredicted = this.selfMediaParticipation.predicted;
      } else if (e == 3) {
        this.one = true;
        this.two = true;
        this.three = false;
        this.four = true;
        this.lineColor = "#7a6b7e";
        this.xActual = this.clicks.actual;
        this.xPredicted = this.clicks.predicted;
      } else {
        this.one = true;
        this.two = true;
        this.three = true;
        this.four = false;
        this.lineColor = "#3d8455";
        this.xActual = this.forwardingVolume.actual;
        this.xPredicted = this.forwardingVolume.predicted;
      }
      this.drowlineZhe();
    },
    // 折线图数据处理
    zheData(i) {
      let effectData = this.effectList[i].effectList;
      for (let j = 0; j < effectData.length; j++) {
        this.xData.push(effectData[j].dateTime);

        // 自媒体热度
        this.selfMediaPopularity.actual.push(
          effectData[j].selfMediaPopularity[0]
        );
        this.selfMediaPopularity.predicted.push(
          effectData[j].selfMediaPopularity[1]
        );
        // // 自媒体参与度
        this.selfMediaParticipation.actual.push(
          effectData[j].selfMediaParticipation[0]
        );
        this.selfMediaParticipation.predicted.push(
          effectData[j].selfMediaParticipation[1]
        );
        // // 点赞量
        this.clicks.actual.push(effectData[j].clicks[0]);
        this.clicks.predicted.push(effectData[j].clicks[1]);
        // // 转发量
        this.forwardingVolume.actual.push(effectData[j].forwardingVolume[0]);
        this.forwardingVolume.predicted.push(effectData[j].forwardingVolume[1]);
      }
      if (this.effectList[i].type == 1) {
        this.flag = true;
        this.xActual = this.clicks.actual;
        this.xPredicted = this.clicks.predicted;
        this.lineColor = "#7a6b7e";
        this.one = true;
        this.two = true;
        this.three = false;
        this.four = true;
      } else {
        this.flag = false;
        this.xActual = this.selfMediaPopularity.actual;
        this.xPredicted = this.selfMediaPopularity.predicted;
        this.lineColor = "#fb6237";
        this.one = false;
        this.two = true;
        this.three = true;
        this.four = true;
      }
    },
    changeData(id) {
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
      // 点赞量
      this.clicks = {
        actual: [],
        predicted: []
      };
      // 转发量
      this.forwardingVolume = {
        actual: [],
        predicted: []
      };
      //折线图横坐标的值
      this.xData = [];
      this.xActual = [];
      this.xPredicted = [];
      this.chartZhe = "";
      this.option = [];

      for (let j = 0; j < this.effectList.length; j++) {
        if (id == this.effectList[j].id) {
          this.webId = id;
          this.zheData(j);
          this.drowlineZhe();
        }
      }
      // console.log(this.selfMediaPopularity);
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
@import url("./PolicyAnalyze.less");
</style>

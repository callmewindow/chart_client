<template>
  <div class="PoliticsInfo">
    <Head :title="title" :showBack="showBack" :name="backTitle"></Head>
    <div class="PoliticsInfoBox">
      <div class="InfoWrap">
        <div class="edit_box common">
          <Icon></Icon>
          <div class="edit">
            <table cellpadding="0" cellspacing="0">
              <tr>
                <td valign="top">事件标题：</td>
                <td valign="top">
                  <input
                    type="text"
                    v-model="eventTitle"
                    placeholder="请输入标题"
                    class="titleInput"
                  />
                </td>
                <td valign="top">
                  <div class="search_input">
                    <input
                      type="text"
                      v-model="searchContent"
                      placeholder="请输入搜索内容"
                    />
                    <div class="btn" @click="searchEvent">
                      <img src="../../assets/img/juxing1.png" alt />
                      <p class="searchBtn">搜索</p>
                    </div>
                  </div>
                </td>
              </tr>
              <tr>
                <td valign="top">事件介绍：</td>
                <td valign="top" style="height: 150px">
                  <textarea
                    name
                    id
                    cols="30"
                    rows="10"
                    v-model="eventIntro"
                    placeholder="请输入内容"
                  ></textarea>
                </td>
                <td rowspan="4" valign="top">
                  <div class="search_result">
                    <div v-for="item in eventList" :key="item.id">
                      {{ item }}
                    </div>
                  </div>
                </td>
              </tr>
              <tr>
                <td valign="top">事件时间：</td>
                <td valign="top" style="height: 55px">
                  <!-- <el-date-picker
                    v-model="dateValue"
                    type="date"
                    placeholder="选择日期"
                  ></el-date-picker> -->
                  <input
                    style="cursor: not-allowed"
                    type="text"
                    disabled
                    placeholder="新建事件的时间会自动生成，不必填写"
                    class="titleInput"
                  />
                </td>
              </tr>
              <tr>
                <td valign="top">关键词：</td>
                <td valign="top" style="height: 80px">
                  <div class="news_div">
                    <el-select
                      v-model="keywords"
                      multiple
                      filterable
                      allow-create
                      default-first-option
                      placeholder="请选择或输入"
                    >
                      <el-option
                        v-for="item in news_options"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value"
                      ></el-option>
                    </el-select>
                  </div>
                </td>
              </tr>
              <tr>
                <td valign="top">事件类型：</td>
                <td valign="top" style="height: 80px">
                  <div class="lable_box">
                    <ul class="lable">
                      <li>
                        <input type="checkbox" v-model="groupEvent" />
                        <label for>群体性事件</label>
                      </li>
                      <!-- <li>
                        <input type="checkbox" v-model="politicEvent" />
                        <label for>新冠疫情</label>
                      </li> -->
                    </ul>
                  </div>
                </td>
              </tr>
            </table>
          </div>
          <div class="save">
            <div class="saveDiv" @click="uploadEvent">
              <img src="../../assets/img/juxing.png" alt />
              <p class="saveBtn">上传</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import newsetDate from "../../untils/newsetDate.js"; //地图数据和列表页数据合计
import "../../../static/js/chinamap/china.js";
import Head from "../../components/Head/Head.vue";
import Icon from "../../components/Icon/Icon.vue";
import * as eventAPI from "../../APIs/event.js";

var vm;
var timer;
export default {
  name: "AddMessage",
  components: {
    Head,
    Icon,
  },
  data() {
    return {
      showBack: true,
      backTitle: "返回",
      title: "网络数据采集与分析系统辅助工具", //页面标题
      eventTitle: "", // 事件的标题
      eventIntro: "", // 事件的介绍
      dateValue: "", // 事件的时间
      keywords: "", // 事件的关键词
      groupEvent: true, // 群体性事件
      politicEvent: false, // 涉政事件
      news_options: [
        // 事件的关键词列表
        {
          value: "人权",
          label: "人权",
        },
        {
          value: "游行",
          label: "游行",
        },
        {
          value: "示威",
          label: "示威",
        },
        {
          value: "诉讼",
          label: "诉讼",
        },
      ],
      newEvent: {}, // 上传新事件的基本内容
      searchContent: "", // 搜索的内容
      allEvent: {}, // 当前所有的事件信息
      eventList: [], // 搜索到的事件列表
    };
  },
  created() {
    this.allEvent = newsetDate;
    Date.prototype.Format = function (fmt) {
      //author: meizz
      var o = {
        "M+": this.getMonth() + 1, //月份
        "d+": this.getDate(), //日
        "h+": this.getHours(), //小时
        "m+": this.getMinutes(), //分
        "s+": this.getSeconds(), //秒
        "q+": Math.floor((this.getMonth() + 3) / 3), //季度
        S: this.getMilliseconds(), //毫秒
      };
      if (/(y+)/.test(fmt))
        fmt = fmt.replace(
          RegExp.$1,
          (this.getFullYear() + "").substr(4 - RegExp.$1.length)
        );
      for (var k in o)
        if (new RegExp("(" + k + ")").test(fmt))
          fmt = fmt.replace(
            RegExp.$1,
            RegExp.$1.length == 1
              ? o[k]
              : ("00" + o[k]).substr(("" + o[k]).length)
          );
      return fmt;
    };
  },
  mounted() {},
  destroyed() {},
  methods: {
    async uploadEvent() {
      if (this.eventTitle !== "") {
        if (this.eventIntro !== "") {
          if (this.dateValue === "") {
            if (this.keywords != []) {
              if (this.groupEvent) {
                this.newEvent = {
                  title: this.eventTitle,
                  brief:
                    this.eventIntro.length > 23
                      ? this.eventIntro.substr(0, 23) + "..."
                      : this.eventIntro,
                  intro: this.eventIntro,
                  // date: this.dateValue.Format("yyyy-MM-dd"),
                  label: this.keywords,
                };
                try {
                  this.$message({
                    showClose: true,
                    message:
                      "事件有关数据计算并上传中，请等待约一分钟时间，结束时会有弹框信息的提醒",
                    type: "info",
                    duration: 30000,
                  });
                  let temp = await eventAPI.createEvent(
                    this.newEvent.title,
                    this.newEvent.brief,
                    this.newEvent.intro,
                    // this.newEvent.date,
                    this.newEvent.label
                  );
                  if (temp) {
                    this.$message.success("新建事件成功，可以继续上传");
                    this.eventTitle = "";
                    this.eventIntro = "";
                    this.keywords = []
                    // this.$router.push({ path: "/Group/" + temp });
                  } else {
                    this.$message.error("上传新事件失败，请检查数据格式稍后再试");
                  }
                } catch (error) {
                  this.$message.error("上传新事件失败，请检查数据格式稍后再试");
                }
                return;
              }
            }
          }
        }
      }
      this.$message.warning("事件信息不完整，请全部填写完毕后再尝试上传");
    },
    searchEvent() {
      this.$message.info("功能建设中，敬请期待");
      return;
      console.log(this.searchCon);
      console.log(this.allEvent.data.resultList);
      this.eventList = [];
      let ae = this.allEvent.data.resultList;
      for (let i = 0; i < ae.length; i++) {
        if (ae[i].title.indexOf(this.searchCon) != -1) {
          this.eventList.push(ae[i]);
        }
      }
      console.log(this.eventList);
    },
  },
};
</script>

<style scoped lang="less">
@import url("./AddMessage.less");
/deep/ .el-input {
  input {
    background: transparent;
    border: 1px solid #fff;
    color: #fff;
    padding: 0;
    padding-left: 2.625rem;
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
/deep/ .el-date-editor.el-input,
.el-date-editor.el-input__inner {
  width: 100%;
}
/deep/ .el-select {
  width: 100% !important;
}
</style>

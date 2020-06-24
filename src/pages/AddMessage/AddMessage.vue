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
                  <input type="text" v-model="eventTitle" placeholder="请输入标题" class="titleInput" />
                </td>
                <td valign="top">
                  <div class="search_input">
                    <input type="text" v-model="searchContent" />
                    <div class="btn" @click="searchEvent">
                      <img src="../../assets/img/juxing1.png" alt />
                      <p class="searchBtn">搜索</p>
                    </div>
                  </div>
                </td>
              </tr>
              <tr>
                <td valign="top">事件介绍：</td>
                <td valign="top" style="height:150px">
                  <textarea name id cols="30" rows="10" v-model="eventIntro" placeholder="请输入内容"></textarea>
                </td>
                <td rowspan="4" valign="top">
                  <div class="search_resault">
                    <div v-for="item in eventList" :key="item.id">
                      {{ item }}
                    </div>
                  </div>
                </td>
              </tr>
              <tr>
                <td valign="top">事件时间：</td>
                <td valign="top" style="height:55px">
                  <el-date-picker v-model="dateValue" type="date" placeholder="选择日期"></el-date-picker>
                </td>
              </tr>
              <tr>
                <td valign="top">关键词：</td>
                <td valign="top" style="height:80px">
                  <div class="news_div">
                    <el-select v-model="keywords" multiple collapse-tags placeholder="请选择">
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
                <td valign="top">标签集：</td>
                <td valign="top" style="height:80px">
                  <div class="lable_box">
                    <ul class="lable">
                      <li>
                        <input type="checkbox" v-model="groupEvent" />
                        <label for>种族歧视</label>
                      </li>
                      <li>
                        <input type="checkbox" v-model="politicEvent" />
                        <label for>新冠疫情</label>
                      </li>
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

var vm;
var timer;
export default {
  name: "AddMessage",
  components: {
    Head,
    Icon
  },
  data() {
    return {
      showBack: true,
      backTitle: "返回",
      title: "网络信息分析系统", //页面标题
      eventTitle: "", // 事件的标题
      eventIntro: "", // 事件的介绍
      dateValue: "", // 事件的时间
      keywords: "", // 事件的关键词
      groupEvent: false, // 群体性事件
      politicEvent: false, // 涉政事件
      news_options: [
        // 事件的关键词列表
        {
          value: "选项1",
          label: "人权"
        },
        {
          value: "选项2",
          label: "游行"
        },
        {
          value: "选项3",
          label: "示威"
        },
        {
          value: "选项4",
          label: "诉讼"
        }
      ],
      newEvent: {}, // 上传新事件的基本内容
      searchContent: "", // 搜索的内容
      allEvent: {}, // 当前所有的事件信息
      eventList: [] // 搜索到的事件列表
    };
  },
  created() {
    this.allEvent = newsetDate;
  },
  mounted() {},
  destroyed() {},
  methods: {
    // nothing() {
    //   alert("功能开发中");
    // },
    uploadEvent() {
      if (this.eventTitle !== "") {
        if (this.eventIntro !== "") {
          if (this.dateValue !== "") {
            if (this.keywords != []) {
              if (this.groupEvent || this.politicEvent) {
                let newType = "";
                if (this.groupEvent) newType = "group";
                if (this.politicEvent) newType = "politic";
                this.newEvent = {
                  eventTitle: this.eventTitle,
                  eventIntro: this.eventIntro,
                  eventTime: this.dateValue,
                  eventKeywords: this.keywords,
                  eventType: newType
                };
                console.log(this.newEvent);
              }
            }
          }
        }
      }
      alert("事件信息不完整，请全部填写完毕后保存");
    },
    searchEvent() {
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
    }
  }
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

<template>
  <div id="all">
    <div id="echart2"></div>
    <div id="echart1"></div>
  </div>
</template>

<script>
export default {
  name: "test",
  data() {
    return {};
  },
  mounted() {
    this.getchart1();
    this.getchart2();
  },
  methods: {
    // 实例化柱状图1
    getchart1() {
      this.echart1 = this.$echarts.init(document.getElementById("echart1"));
      let option = {
        title: {
          text: "交易比例展示",
          subtext: "数据来源网络",
          left: "center"
        },
        tooltip: {
          trigger: "item",
          formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: {
          orient: "vertical",
          left: "left",
          data: ["小布丁", "可爱多", "冰淇凌", "芒果千层", "榴莲千层"]
        },
        series: [
          {
            name: "交易内容",
            type: "pie",
            radius: "55%",
            center: ["50%", "60%"],
            data: [
              { value: 635, name: "小布丁" },
              { value: 710, name: "可爱多" },
              { value: 834, name: "冰淇凌" },
              { value: 335, name: "芒果千层" },
              { value: 158, name: "榴莲千层" }
            ],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: "rgba(0, 0, 0, 0.5)"
              }
            }
          }
        ]
      };
      this.echart1.clear();
      this.echart1.setOption(option);
    },

    // 实例化柱状图1
    getchart2() {
      this.echart2 = this.$echarts.init(document.getElementById("echart2"));
      let option = {
        title: {
          text: "各类型交易数量展示",
          subtext: "数据来自网络"
        },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "shadow"
          }
        },
        legend: {
          data: ["2020年"]
        },
        grid: {
          left: "3%",
          right: "4%",
          bottom: "3%",
          containLabel: true
        },
        xAxis: {
          type: "value",
          boundaryGap: [0, 0.01]
        },
        yAxis: {
          type: "category",
          data: ["小布丁", "可爱多", "冰淇凌", "芒果千层", "榴莲千层"]
        },
        series: [
          {
            name: "2020年",
            type: "bar",
            data: [635, 710, 834, 335, 158]
          }
        ]
      };
      this.echart2.clear();
      this.echart2.setOption(option);
    }
  }
};
</script>

<style scoped lang="less">
#all {
  background-color: blanchedalmond;
  width: 100vw;
  height: 100vh;
  padding: 20px;
}
#echart1 {
  width: 500px;
  height: 500px;
}
#echart2 {
  width: 500px;
  height: 300px;
}
</style>

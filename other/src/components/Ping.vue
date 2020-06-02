<template>
  <div class="container">
    <button type="button" class="btn btn-primary">{{message}}</button>
  </div>
</template>
<script>
  import axios from 'axios'

  export default {
    name: 'Ping',
    data() {
      return {
        msg: 'Hello!',
      };
    },
    methods:{
      getMessage(){
        const path = 'http://localhost:5000/'
        var that = this
        axios.get(path).then(function (result) {
          that.msg = result.data
        })
      },
      created() {
      this.getMessage();
      },
    }
  };
</script>

<template>
  <div class="box">
    <img src="../../static/image/Loginbg.3377d0c.jpg" alt="">
    <div class="forget">
      <div class="forget_box">
        <div class="forget-title">忘记密码</div>
        <div class="inp">
          <input v-model="email" type="text" @blur="checkEmail" placeholder="邮箱" class="user">
          <div class="forget-box">
            <el-button class="forget_btn" @click="smsHandler" style="text-align: center; margin: auto auto; ">{{this.sms_text}}</el-button>
          </div>
          <p class="go_login">返回登陆
            <router-link to="/user/login">直接登录</router-link>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: 'Forget',
  data() {
    return {
      email: "",
      //  判断 是否发送过短信
      is_send_sms: false,
      sms_text:"点击发送邮箱"
    }
  },
  created() {
  },
  methods: {

    checkEmail() {

      if (this.email) {

      // 检查手机号的合法性[格式和是否已经注册]
      this.axios.get(`/basic/user/forget/${this.email}`).then().catch(error => {
        this.$message.error("邮箱校验错误");
        console.log(error.response.data.message)
      })

      } else {
        this.$message.error("请输入邮箱")
      }


    },

    smsHandler(){
       //1. 检查手机格式
      if (/.*?@.*\.com/.test(this.email)) {
        this.message.error("邮箱格式错误");
        return false;
      }

      //2. 判断短信间隔事件
      if (this.is_send_sms) {
        this.$message.error("请勿重复发送邮件 请稍后重试");
        return false;
      }

      // 如果没有短信间隔 就发送ajax
      this.axios.get(`/basic/user/forget/${this.email}`).then(res => {
        console.log(res.data)
        this.$notify.success(res.data);
        // alert(1)
        let interval_time = 60;

        // 此时发送短信成功  这个标识符标记为true
        this.is_send_sms = true;

        let timer = setInterval(() => {
          if (interval_time <= 1) {
            // 停止倒计时
            // 清除计时器
            clearInterval(timer);
            // 当时间过去 重新标志为 false
            this.is_send_sms = false;
            this.sms_text="点击发送邮件";
          } else {
            interval_time--;
            this.sms_text=`${interval_time}秒后重新发送短信`;

          }
        }, 1000)
      }).catch(error => {
        console.log(error.data)
        console.log(error.data.response)
      })
    }


  },

};
</script>

<style scoped>
.box {
  width: 100%;
  height: 100%;
  position: relative;
  overflow: hidden;
}

.box img {
  width: 100%;
  min-height: 100%;
}

.box .forget {
  position: absolute;
  width: 500px;
  height: 400px;
  top: 0;
  left: 0;
  margin: auto;
  right: 0;
  bottom: 0;
  top: -338px;
}

.forget-title {
  width: 100%;
  font-size: 24px;
  text-align: center;
  padding-top: 30px;
  padding-bottom: 30px;
  color: #4a4a4a;
  letter-spacing: .39px;
}

.register-title img {
  width: 190px;
  height: auto;
}

.register-title p {
  font-family: PingFangSC-Regular;
  font-size: 18px;
  color: #fff;
  letter-spacing: .29px;
  padding-top: 10px;
  padding-bottom: 50px;
}

.forget_box {
  width: 400px;
  height: auto;
  background: #fff;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, .5);
  border-radius: 4px;
  margin: 0 auto;
  padding-bottom: 40px;
}

.register_box .title {
  font-size: 20px;
  color: #9b9b9b;
  letter-spacing: .32px;
  border-bottom: 1px solid #e6e6e6;
  display: flex;
  justify-content: space-around;
  padding: 50px 60px 0 60px;
  margin-bottom: 20px;
  cursor: pointer;
}

.register_box .title span:nth-of-type(1) {
  color: #4a4a4a;
  border-bottom: 2px solid #84cc39;
}

.inp {
  width: 350px;
  margin: 0 auto;
}

.inp input {
  border: 0;
  outline: 0;
  width: 100%;
  height: 45px;
  border-radius: 4px;
  border: 1px solid #d9d9d9;
  text-indent: 20px;
  font-size: 14px;
  background: #fff !important;
}

.inp input.user {
  margin-bottom: 16px;
}

.inp .rember {
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
  margin-top: 10px;
}

.inp .rember p:first-of-type {
  font-size: 12px;
  color: #4a4a4a;
  letter-spacing: .19px;
  margin-left: 22px;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  /*position: relative;*/
}

.inp .rember p:nth-of-type(2) {
  font-size: 14px;
  color: #9b9b9b;
  letter-spacing: .19px;
  cursor: pointer;
}

.inp .rember input {
  outline: 0;
  width: 30px;
  height: 45px;
  border-radius: 4px;
  border: 1px solid #d9d9d9;
  text-indent: 20px;
  font-size: 14px;
  background: #fff !important;
}

.inp .rember p span {
  display: inline-block;
  font-size: 12px;
  width: 100px;
  /*position: absolute;*/
  /*left: 20px;*/

}


.forget_btn {
  width: 100%;
  height: 45px;
  background: #84cc39;
  border-radius: 5px;
  font-size: 16px;
  color: #fff;
  letter-spacing: .26px;
  margin-top: 30px;
}

.inp .go_login {
  text-align: center;
  font-size: 14px;
  color: #9b9b9b;
  letter-spacing: .26px;
  padding-top: 20px;
}

.inp .go_login span {
  color: #84cc39;
  cursor: pointer;
}

.forget-box {
  position: relative;
}

.sms-box .sms-btn {
  position: absolute;
  font-size: 14px;
  letter-spacing: 0.26px;
  top: 10px;
  right: 16px;
  border-left: 1px solid #484848;
  padding-left: 16px;
  padding-bottom: 4px;
  cursor: pointer;
  background: #ffffff;
}
</style>

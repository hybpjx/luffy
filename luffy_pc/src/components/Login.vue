<template>
  <div class="login box">
    <img src="../../static/image/Loginbg.3377d0c.jpg" alt="">
    <div class="login">
      <div class="login-title">
        <img src="../../static/image/Logotitle.1ba5466.png" alt="">
        <p>帮助有志向的年轻人通过努力学习获得体面的工作和生活!</p>
      </div>
      <div class="login_box">
        <div class="title">
          <span @click="login_type=0" :class="login_type==0?'current':''">密码登录</span>
          <span @click="login_type=1" :class="login_type==1?'current':''">短信登录</span>
        </div>
        <div class="inp" v-if="login_type==0">
          <input v-model="username" type="text" placeholder="用户名 / 手机号码" class="user">
          <input v-model="password" type="password" name="" class="pwd" placeholder="密码">
          <div id="geetest1"></div>
          <div class="rember">
            <p>
              <input type="checkbox" class="no" name="a" v-model="remember"/>

              <span>记住密码</span>
            </p>
            <router-link to="/user/forget">忘记密码</router-link>
          </div>
<!--          <button class="login_btn" @click="get_geetest_captcha">登录</button>-->
          <button class="login_btn" @click="loginHandler">登录</button>
          <p class="go_login">没有账号
            <router-link to="/user/register">立即注册</router-link>
          </p>
        </div>
        <div class="inp" v-show="login_type==1">
          <input v-model="username" type="text" placeholder="手机号码" class="user">
          <input v-model="password" type="text" class="pwd" placeholder="短信验证码">
          <button id="get_code">获取验证码</button>
          <button class="login_btn" @click="loginHandler">登录</button>
          <p class="go_login">没有账号
            <router-link to="/user/register">立即注册</router-link>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: 'Login',
  data() {
    return {
      login_type: 0,
      username: "",
      password: "",
      remember: false,
    }
  },

  methods: {
    // 账号密码登陆
    loginHandler() {
      this.axios.post('/basic/user/login/', {
        "username": this.username,
        "password": this.password
      }).then(res => {
        if (this.remember) {
          // 记住登陆状态
          sessionStorage.removeItem("user_token")
          sessionStorage.removeItem("user_id")
          sessionStorage.removeItem("user_name")
          localStorage.user_token = res.data.token;
          localStorage.user_id = res.data.id;
          localStorage.user_name = res.data.username;
        } else {
          // 不记住登陆状态
          localStorage.removeItem("user_token")
          localStorage.removeItem("user_id")
          localStorage.removeItem("user_name")
          sessionStorage.user_token = res.data.token;
          sessionStorage.user_id = res.data.id;
          sessionStorage.user_name = res.data.username;
        }


        let self = this;
        // 页面跳转
        this.$alert("登陆成功", "路飞学城", {
          callback() {
            // this.$router.push("/"); // 如果这里用了this 指代的当前的alert方法里面
            self.$router.push("/");
          }
        })


      }).catch(error => {
        this.$message.error("用户名或密码错误")
        console.log(error.response)
      })
    },


    // get_geetest_captcha(){
    //   console.log("hello")
    // },

    // 向后端发送极验验证码
    get_geetest_captcha() {
      // 获取极验验证码
      this.axios.get('/basic/user/captcha/', {
        params: {
          'username': this.username
        }
      },).then(response => {
        // 使用initGeetest接口
        // 参数1：配置参数
        // 参数2：回调，回调的第一个参数验证码对象，之后可以使用它做appendTo之类的事件
        let data = JSON.parse(response.data);
        // eslint-disable-next-line no-undef
        initGeetest({
          gt: data.gt,
          challenge: data.challenge,
          product: "popup",// 产品形式, 包括:float, embed, popup, 只对pc版验证码有效
          offline: !data.success// 表示用户后台检测极验服务器是否宕机, 一般无需关注
        }, this.handlerPopup);

      }).catch(error => {
        console.log(error.response)
      })
    },

    // 极验验证码的验证
    handlerPopup( captchaObj) {
      let self = this;

      captchaObj.onsuccess(function () {
        let validate = captchaObj.getValidate();
        // 当用户 点击验证码正确后执行操作
        self.axios.post("/basic/user/captcha/", {
          // 二次验证所需的三个值
          geetest_challenge: validate.geetest_challenge,
          geetest_validate: validate.geetest_validate,
          geetest_seccode: validate.geetest_seccode
        }).then(res=>{
          if (res.data.status){
            // 验证码通过后,才发送账号与密码进行登陆
            self.loginHandler();
          }
        }).catch(error=>{
          self.$message.error(error.response)
        })


      })

      // 优化验证码
      document.getElementById("#geetest1").innerHTML="";
      // 将验证码加到id为captcha的元素里
      captchaObj.appendTo("#geetest1");
      // 更多接口参考：http://www.geetest.com/install/sections/idx-client-sdk.html
    }
  }
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

.box .login {
  position: absolute;
  width: 500px;
  height: 400px;
  left: 0;
  margin: auto;
  right: 0;
  bottom: 0;
  top: -338px;
}

.login .login-title {
  width: 100%;
  text-align: center;
}

.login-title img {
  width: 190px;
  height: auto;
}

.login-title p {
  font-size: 18px;
  color: #fff;
  letter-spacing: .29px;
  padding-top: 10px;
  padding-bottom: 50px;
}

.login_box {
  width: 400px;
  height: auto;
  background: #fff;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, .5);
  border-radius: 4px;
  margin: 0 auto;
  padding-bottom: 40px;
}

.login_box .title {
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

.login_box .title .current {
  color: #4a4a4a;
  border-bottom: 2px solid #84cc39;
}

.inp {
  width: 350px;
  margin: 0 auto;
}

.inp input {
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

#geetest {
  margin-top: 20px;
}

.login_btn {
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
</style>


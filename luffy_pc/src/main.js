import { createApp } from 'vue'
import App from './App.vue'
import {router} from "@/router";

// // 导入gt极验
import "../static/js/gt.js";

// 导入 element-ui
import elementPlus from 'element-plus';
import 'element-plus/dist/index.css';

// 导入css 初始化
import "../static/css/reset.css";

const app=createApp(App);

import VueAxios from 'vue-axios';
import axios from "axios";
axios.defaults.withCredentials=false // 阻止ajax 附带cookie


app.config.productionTip=false


app.use(router)
// 直接引入对象属性

app.mount('#app')
app.use(elementPlus)

app.use(VueAxios, axios);




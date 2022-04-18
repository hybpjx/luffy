import { createApp } from 'vue'
import App from './App.vue'
import {router} from "@/router";
import settings from "@/settings";

// 导入 element-ui
import elementPlus from 'element-plus';
import 'element-plus/dist/index.css';

// 导入css 初始化
import "../static/css/reset.css";

const app=createApp(App)

app.config.productionTip=false


app.use(router)
// 直接引入对象属性
app.use(settings)
app.mount('#app')
app.use(elementPlus)
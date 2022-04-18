import {createRouter, createWebHistory} from "vue-router";
// 要导入 component 的内容 然后注册到路由中
import Home from "@/components/Home";

const routes=[
    {
        path:'/',
        name:"Home",
        component:Home
    }
]

export const router=createRouter({
    // history:createWebHashHistory(),
    // 去除 url 访问地址 # 号
    history:createWebHistory(),
    routes:routes
})
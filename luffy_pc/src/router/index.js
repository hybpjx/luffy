import {createRouter, createWebHistory} from "vue-router";
// 要导入 component 的内容 然后注册到路由中
import Home from "@/components/Home";
import Login from "@/components/Login";

const routes=[
    {
        path:'/',
        name:"Home",
        component:Home
    },
    // {
    //     path:'/home',
    //     name:"Home",
    //     component:Home
    // },
    {
        path:'/user/login',
        name:"Login",
        component:Login
    },
]

export const router=createRouter({
    // history:createWebHashHistory(),
    // 去除 url 访问地址 # 号
    history:createWebHistory(),
    routes:routes
})
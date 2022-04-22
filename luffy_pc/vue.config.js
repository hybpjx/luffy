const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})

module.exports = {
    // 基本路径
    // baseUrl: './',
    // 生产环境是否生成 sourceMap 文件
    productionSourceMap: false,
    // 服务器端口号
    devServer: {
        host:"http://www.luffy.cn",
        port: 8080,
       https: false,
      allowedHosts:[
          "api.luffy.cn",
          "www.luffy.cn",
      ],
             proxy:{
            '/api':{
                target: 'http://api.luffy.cn:8000/banner',
                changeOrigin:true,
                pathRewrite: {
                    '^/api': ''
                }
            }
        }
    },
}


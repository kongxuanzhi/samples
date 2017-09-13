[webpack sample](http://zhaoda.net/webpack-handbook/commonjs.html)

1. use webpack to package js, css or other resource file into js file.

2. package.json:
```json
"devDependencies": {
  "css-loader": "^0.28.7", #turn css file into javascript
  "style-loader": "^0.18.2", //make css in js into html tags
  "webpack": "^1.15.0", //webpack --progress --colors --watch 监听
  "webpack-dev-server": "^2.7.1" //webpack-dev-server --progress --colors监听
}
```

1. 配置webpack.config.js文件
2. 监听文件: 从入口文件开始递归依赖树, 打包文件为js

  > $ webpack-dev-server --progress --colors

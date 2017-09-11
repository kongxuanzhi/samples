// entry.js
// require("!style-loader!css-loader!./style.css") // 载入 style.cssx
require('./style.css')
document.write('It works.')
document.write(require('./module.js')) // 添加模块

/**
 * Created by faiyer on 2017/9/23.
 */
const sqrt = Math.sqrt;

module.exports = {
  port: 3000,
  square: function(x) {
    return x * x;
  }
  diag: function() {
    return sqrt(square(x) + square(y));
  }
}

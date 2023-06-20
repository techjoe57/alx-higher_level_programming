module.exports = {
  callMeMoby: function (x, f) {
    let i = 0;
    while (i < x) {
      f();
      i++;
    }
  }
};

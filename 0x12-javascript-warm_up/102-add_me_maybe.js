#!/usr/bin/node
module.exports = {
  addMeMaybe: function (nb, f) {
    return f(nb + 1);
  }
};

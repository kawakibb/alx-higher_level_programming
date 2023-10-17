#!/usr/bin/node
//comment
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};

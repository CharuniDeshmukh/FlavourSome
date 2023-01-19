function addItem(img, name, des, price) {
  var ind = parseInt(localStorage.length);
  if (ind == 0) {
    localStorage.setItem("index", ind + 1);
    localStorage.setItem("cartValue", 0);
  }
  var indexS = localStorage.getItem("index");
  var cartValue = localStorage.getItem("cartValue");
  localStorage.setItem("cartValue", parseInt(price) + parseInt(cartValue));
  for (i = 0; i < localStorage.length; i++) {
    const arr = JSON.parse(localStorage.getItem(localStorage.key(i)));
    if (arr.length == undefined) {
      continue;
    }
    if (arr[0] == img && arr[1] == name) {
      const temp = [img, name, des, price, arr[4] + 1];
      localStorage.setItem(localStorage.key(i), JSON.stringify(temp));
      document.location.reload();
      return;
    }
  }
  const temp = [img, name, des, price, 1];
  localStorage.setItem("item" + indexS.toString(), JSON.stringify(temp));
  localStorage.setItem("index", parseInt(indexS) + 1);
  document.location.reload();
}

function subItem(img, name, des, price) {
  var flag = false;
  if (localStorage.length < 1) {
    return;
  }
  for (i = 0; i < localStorage.length; i++) {
    const arr = JSON.parse(localStorage.getItem(localStorage.key(i)));
    if (arr[0] == img && arr[1] == name) {
      if (parseInt(arr[4]) == 1) {
        localStorage.removeItem(localStorage.key(i));
        var cartValue = localStorage.getItem("cartValue");
        localStorage.setItem("cartValue", parseInt(cartValue) - parseInt(price));
        document.location.reload();
      } else {
        const temp = [img, name, des, price, arr[4] - 1];
        localStorage.setItem(localStorage.key(i), JSON.stringify(temp));
        var cartValue = localStorage.getItem("cartValue");
        localStorage.setItem("cartValue", parseInt(cartValue) - parseInt(price));
        document.location.reload();
      }
      flag = true;
    }
  }
}

function increment(tid) {
    var txtQty = document.getElementById(tid);
    var x = parseInt(txtQty.value);
    if (!isNaN(x) && x < 5) {
        txtQty.value = x + 1;
    }
}

function decrement(tid) {
    var txtQty = document.getElementById(tid);
    var x = parseInt(txtQty.value);
    if (!isNaN(x) && x > 1) {
        txtQty.value = x - 1;
    }
}
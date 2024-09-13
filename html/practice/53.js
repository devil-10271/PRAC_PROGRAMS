console.log(`hello world`);

function gt(a = 0, b = 0) {
    if (a > b) {
        return a;
    }
    else {
        return b;
    }
}
function lt(a = 0, b = 0) {
    if (a < b) {
        return a;
    }
    else {
        return b;
    }
}

a = gt(11, 1);
console.log(a);
function ave(array) {
    let sum = 0;
    array.forEach(element => {
        sum+=element;
    });
    return sum/array.length;
}
module.exports={
    avg:ave,
    name:'dahil'
};

function soma(arr){
    if(arr.length === 0) return 0;
    return arr[0] + soma(arr.slice(1));
}
console.log(soma([1,2,3,4,5,6]));
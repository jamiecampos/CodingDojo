// Given an array, create and return a new one containing all the values of the
// provided array, made negative (not simply multiplies by -1). Given [1,-3,5],
// return [-1,-3,-5].

function negative(arr){
    arr2 = []
    for(var i = 0; i < arr.length; i++){
        if(arr[i] > 0){
            arr[i] = arr[i] * -1
            arr2.push(arr[i])
        }else{
            arr2.push(arr[i])
        }
    }
    console.log(arr2)
}

negative([1,-3,5])

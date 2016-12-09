// Given an array, find and print its largest element.

function findMax(arr){
    var max = 0
    for(i = 0; i < arr.length; i++){
        if (arr[i] > max){
            max = arr[i]
        }
    }
    console.log(max)
}

findMax([34,6,365,8,43])

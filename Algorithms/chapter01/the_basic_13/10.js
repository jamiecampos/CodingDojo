// Analyze an array's values and print the average.

function average(arr){
    var sum = 0
    for(i = 0; i < arr.length; i++){
        sum = sum + arr[i]
    }
    var avg = sum / arr.length
    console.log(avg)
}

average([5,3,8,54,1,76])

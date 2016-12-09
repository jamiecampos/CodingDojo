// Given an array, print the max, min and average values for that array.

function minMaxAvg(arr){
    var min = arr[0]
    var max = arr[0]
    var sum = 0
    for(i = 0; i < arr.length; i++){
        if(arr[i] < min){
            min = arr[i]
        }
        if(arr[i] > max){
            max = arr[i]
        }
        sum = sum + arr[i]
    }
    var avg = sum / arr.length
    console.log("Min = " + min)
    console.log("Max = " + max)
    console.log("Avg = " + avg)
}

minMaxAvg([4,3,9,6,7,1,0])

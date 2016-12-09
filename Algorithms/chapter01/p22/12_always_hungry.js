// Create a function that accepts an array and prints "yummy" each time one of
// the values is equal to "food". If no array elements are "food", then print
// "I'm hungry" once.

function hungry(arr){
    var foodCount = 0
    for(var i = 0; i < arr.length; i++){
        if(arr[i] == "food"){
            foodCount +=1
        }
    }
    if(foodCount > 0){
        console.log("yummy")
    }else{
        console.log("I'm hungry")
    }
}

hungry([1,2,3, "food"])

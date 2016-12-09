// Create a function that accepts an array. Every time that array has three odd
// values in a row, print "That's odd!" Every time the array has three evens in
// a row, print "Even more so!"

function evenOdd(arr){
    for(var i = 2; i < arr.length; i++){
        if((arr[i] % 2 == 1) && (arr[i-1] % 2 == 1) && (arr[i-2] % 2 == 1)){
            console.log("That's odd!")
        }else if((arr[i] % 2 == 0) && (arr[i-1] % 2 == 0) && (arr[i-2] % 2 == 0)){
            console.log("Even more so!")
        }
    }
}

evenOdd([1,3,7,5,7,8,5,4,2,8,9])

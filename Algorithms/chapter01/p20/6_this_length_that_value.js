// Given two numbers, return array of length num1 with each value num2. Print
// "Jinx!" if they are the same.


function lengthValue(num1,num2){
    var arr = []
    var i = 0
    for(var i = 0; i < num1; i+= 1){
        arr.push(num2);
    }
    console.log(arr)
    if(num1 == num2){
        console.log("Jinx!")
    }
}

lengthValue(3,3)

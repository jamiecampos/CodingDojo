// Stan learned something today: that reucing an array's .length immediately
// shortens it by that amount. Given array arr and number x, remove all except
// the last x elements, and return arr (changed and shorter). Given
// ([2,4,6,8,10],3), change the given array to [6,8,10] and return it.

function shorten(arr,x){
    for(var i = 0; i < arr.length; i++){
        if(i < arr.length + 1 - x){
            arr.shift()
        }
    }
    console.log(arr)
}

shorten([2,4,6,8,10],3)

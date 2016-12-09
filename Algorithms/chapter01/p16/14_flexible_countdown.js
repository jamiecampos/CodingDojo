// Based on earlier "Countdown By Fours", given lowNum, highNum, mult, print
// multiples of mult from highNum down to lowNum, using a FOR. For (2,9,3),
// print 9 6 3 (on successive lines).

function flexCount(lowNum,highNum,mult){
    while(highNum >= lowNum){
        if(highNum % mult == 0){
            console.log(highNum)
        }
        highNum -= 1

}

}

return(flexCount(1,2016,4))

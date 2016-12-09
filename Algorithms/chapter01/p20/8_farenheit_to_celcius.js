// Kelvin wants to convert between temperature scales. Create farenheitToCelcius
// (fDegrees) that accepts a number of degrees in Farenheit, and returns the
// equivalent tempareature as expressed in Celsius degrees. For review,
// Farenheit = (9/5 * Celcius) * 32.

function farenheitToCelcius(fDegrees){
    cDegrees = ((fDegrees - 32)*(5/9))
    console.log(cDegrees)
}

farenheitToCelcius(70)

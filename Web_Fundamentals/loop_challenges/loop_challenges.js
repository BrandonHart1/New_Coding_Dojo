//  Numbers 1 - 20, odds only  ###########################################################
for (var i = 0; i < 21; i++) {
    if (i % 2 == 1) 
    console.log(i);
}


//  all of the values divisible by 3, 100 down to  0  ####################################
for (var i = 100; i > 1; i--) {
    if (i % 3 == 0)
    console.log(i)
}


// Values in the sequence of 4, 2.5, 1, 0.5, -2, -3.5  ###################################
for (var i = 4; i > -4; i -= 1.5) {
    console.log(i)
}

// Write code that will add all of the values from 1-100 onto some variable sum and at the end console.log the result 1 + 2 + 3 + ... + 98 + 99 + 100. We should get back 5050 at the end.######################################################################################

var sum = 0
for(var i = 0; i < 101; i++) {
    sum = sum + i
}
console.log(sum)


// Write code that will multiply all of the values from 1-12 onto some variable product and at the end console.log the result 1 * 2 * 3 * ... * 10 * 11 * 12. We should get back 479001600 at the end.######################################################################

var product = 1

for(var i = 1; i <= 12; i++) {
    product *= i
}
console.log(product)
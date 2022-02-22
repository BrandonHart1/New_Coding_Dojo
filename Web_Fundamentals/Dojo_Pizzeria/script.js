// function pizzaOven(crustType, sauceType, cheeses, toppings) {
//     var pizza1 = {
//         pizza.crustType = "deep dish",
//         pizza.sauceType = "traditional",
//         pizza.cheeses = "mozzarella",
//         pizza.toppings = ["pepperoni", "sausage"],
//     };
    
//     var pizza2 = {
//         pizza.crustType = "hand tossed",
//         pizza.sauceType = "marinara",
//         pizza.cheeses = ["mozzarella", "feta"],
//         pizza.toppings = ["mushrooms", "olives", "onions"]
//     }
    
//     var myPizza = {
//         pizza.crustType = "thin n' crispy",
//         pizza.sauceType = "traditional", 
//         pizza.cheese = "extra mozzarella",
//         pizza.toppings = ["hamburger", "pepperoni", "extra mushrooms"]
//     }

//     var myPizza2 = {
//         pizza.crustType = "deep dish",
//         pizza.sauceType = "traditional", 
//         pizza.cheese = "extra mozzarella",
//         pizza.toppings = ["hamburger", "pepperoni", "extra mushrooms", "black olives"]
//     }
// }

// function randomPizza(crustType, sauceType, cheeses, toppings) {
//     var pizza1 = randomPizza.
// }

// ################################################################################################

function pizzaOven(crustType, sauceType, cheeses, toppings) {
    var pizza = {};
    pizza.crustType = crustType;
    pizza.sauceType = sauceType;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;
    return pizza;
}

var pizza1 = pizzaOven("deep dish", "traditional", ["mozzarella"], ["pepperoni", "sausage"]);
console.log(pizza1);

var pizza2 = pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"]);
console.log(pizza2);

var crustTypes = [
    "deep dish",
    "hand tossed",
    "thin and crispy",
    "cauliflower",
    "gluten free",
    "hawaiian bread"
];

var sauceTypes = [
    "traditional",
    "marinara",
    "bbq",
    "white sauce",
    "nacho cheese",
    "tikka masala"
];

var cheeses = [
    "mozzarella",
    "cheddar",
    "feta",
    "swiss cheese",
    "blue cheese",
    "goat cheese",
    "provolone",
    "parmesan",
    "vegan cheese"
];

var toppings = [
    "pepperoni",
    "sausage",
    "chicken",
    "corn",
    "olives",
    "bell peppers",
    "onions",
    "mushrooms",
    "anchovies"
];

function randomRange(max, min) {
    return Math.floor(Math.random() * max - min) + min;
}

function randomPick(arr) {
    var i = Math.floor(arr.length * Math.random());
    return arr[i];
}

// ################################################################################################

function randomPizza() {
    var pizza = {};
    pizza.crustType = randomPick(crustTypes);
    pizza.sauceType = randomPick(sauceTypes);
    pizza.cheeses = [];
    pizza.toppings = [];
    for(var i=0; i<randomRange(5, 1); i++) {
        pizza.cheeses.push(randomPick(cheeses));
    }
    for(var i=0; i<randomRange(4, 0); i++) {
        pizza.toppings.push(randomPick(toppings));
    }
    return pizza;
}

console.log(randomPizza());
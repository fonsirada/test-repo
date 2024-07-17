/*    Kelvin to celsius to fahrenheit practice project

    // this is the temperature in kelvin, it will not change
    const kelvin = 293;

    // this is the temperature in celsius, it is 273 degrees less than kelvin
    let celsius = kelvin - 273;

    // this is the temperature in fahrenheit
    let fahrenheit = celsius * (9/5) + 32;
    // rounding the value down to a whole number
    fahrenheit = Math.floor(fahrenheit);

    console.log(`The temperature is ${fahrenheit} degrees Fahrenheit.`);

*/

/* program that calculates your age in dog years

    let myAge = 18;
    let earlyYears = 2;
    earlyYears *= 10.5;
    let laterYears = myAge - 2;
    laterYears *= 4;
    let myAgeInDogYears = earlyYears + laterYears;
    let myName = "Alfonso".toLowerCase();
    console.log(`My name is ${myName}. I am ${myAge} years old in human years which is ${myAgeInDogYears} years old in dog years.`);

*/

/*  magic eight ball

    let username = "Alfonso";
    username ? console.log(`Hi ${username}! Nice to meet you!`) : console.log('Hi!');
    let userQuestion = "When will I become famous?";
    let randomNumber = Math.floor(Math.random() * 5);
    let eightBall = "";
    switch (randomNumber) {
        case 0:
            eightBall = "I don't know";
            break;
        case 1:
            eightBall = "Soon";
            break;
        case 2:
            eightBall = "It is certain";
            break;
        case 3:
            eightBall = "Patience is a virtue";
            break;
        default:
            eightBall = "Signs point to yes";
            break;
    }
    console.log(eightBall);

*/

/*   racetime generator

    let raceNumber = Math.floor(Math.random() * 1000);

    let earlyRegistration = true;
    let runnerAge = 18;
    if (runnerAge > 18) {
        if (earlyRegistration) {
            raceNumber += 1000;
            console.log(`${raceNumber}, your race will start at 9:30`);
        }
        else {
            console.log(`${raceNumber}, you will race at 11:00 am`);
        }
    } else if (runnerAge < 18) {
        console.log(`${raceNumber}, you will race at 12:30 pm`);
    } else {
        console.log(`${raceNumber}, please see the registration desk`);
    }
*/

/*  rock paper scissors

    function robotPlay() {
        let randomNum = Math.floor(Math.random() * 3);
        let robotChoice = "";
        switch (randomNum) {
            case 0:
                robotChoice = "Rock";
                break;
            case 1:
                robotChoice = "Paper";
                break;
            default:
                robotChoice = "Scissors";
                break;
        }
        return robotChoice;
    }

    function play(userChoice) {
        let robotChoice = robotPlay();
        console.log(`Robot chooses ${robotChoice}.`);
        switch (userChoice) {
            case "Rock":
                switch (robotChoice) {
                    case "Rock":
                        console.log("Draw.");
                        break;
                    case "Paper":
                        console.log("You lose.");
                        break;
                    default:
                        console.log("You win!");
                        break;
                }
                break;
            case "Paper":
                switch (robotChoice) {
                    case "Rock":
                        console.log("You win!");
                        break;
                    case "Paper":
                        console.log("Draw.");
                        break;
                    default:
                        console.log("You lose.");
                        break;
                }
                break;
            case "Scissors":
                switch (robotChoice) {
                    case "Rock":
                        console.log("You lose.");
                        break;
                    case "Paper":
                        console.log("You win!");
                        break;
                    default:
                        console.log("Draw.");
                        break;
                }
                break;
            default:
                console.log("That is not a valid choice.");
                break; 
        }
    }

    play("Paper");

*/

/*  FUNCTIONS
    //basic function syntax

    function funcName(param) {
        body;
        return returnVar;
    }

    //arrow function syntax

    let funcName = (param) => {
        body;
        return returnVar;
    }

*/

/*  Javascript Methods

    const groceryList = ['orange juice', 'bananas', 'coffee beans', 'brown rice', 'pasta', 'coconut oil', 'plantains'];

    groceryList.shift(); //pops first element in array and adjusts other elements down - mutates array
    console.log(groceryList);

    groceryList.unshift('popcorn'); //adds element to front of array and adjusts other elemnts up - mutates array
    console.log(groceryList);

    console.log(groceryList.slice(1,4)); // grabs snippet of array, first argument is beginning index (inclusive),
                                        // second arg is last index (exclusive), - does not mutate array
    console.log(groceryList);

    const pastaIndex = groceryList.indexOf("pasta"); //gets index of an element in the array, returns -1 if not found
    console.log(pastaIndex);

*/

/*  nested arrays

    let numberClusters = [[1,2], [3,4], [5,6]];
    const target = numberClusters[2][1];
    console.log(target);

*/

/*  for loops

    const vacationSpots = ['Bali', 'Paris', 'Tulum'];

    for (let i = 0; i < vacationSpots.length; i++) {
        console.log(`I would love to visit ${vacationSpots[i]}`);
    } 

*/

/*  nested for loops

    let bobsFollowers = ["Gley", "Aaron", "Juan", "Cole"];
    let tinasFollowers =  ["DJ", "Aaron", "Juan"];
    let mutualFollowers = [];

    for (let i = 0; i < bobsFollowers.length; i++) {
        for (let j = 0; j < tinasFollowers.length; j++) {
            if (bobsFollowers[i] === tinasFollowers[j]) {
                mutualFollowers.push(bobsFollowers[i]);
            }
        }
    }
    console.log(mutualFollowers);

*/

/* While loops - In situations when we want a loop to execute an undetermined number of times, while loops are the best choice.

    const cards = ['diamond', 'spade', 'heart', 'club'];

    let currentCard = undefined; 
    while (currentCard !== "spade") {
        currentCard = cards[Math.floor(Math.random() * 4)];
        console.log(currentCard);
    }
    
*/

/* Do...While loops - Unlike the while loop, do...while will run at least once whether or not the condition evaluates to true.

    const firstMessage = 'I will print!';
    const secondMessage = 'I will not print!'; 

    // A do while with a stopping condition that evaluates to false
    do {
        console.log(firstMessage)
    } while (true === false);

    // A while loop with a stopping condition that evaluates to false
    while (true === false){
        console.log(secondMessage)
    };

*/

/*  break keyword for getting out of loops

    const rapperArray = ["Lil' Kim", "Jay-Z", "Notorious B.I.G.", "Tupac"];

    for (let i = 0; i < rapperArray.length; i++) {
        console.log(rapperArray[i]);
        if (rapperArray[i] === "Notorious B.I.G.") {
            break;
        }
    }
    console.log("And if you don't know, now you know.");

*/

/*  functions as data, using variables to hold functions by reference, saving a lot of space

    const checkThatTwoPlusTwoEqualsFourAMillionTimes = () => {
    for(let i = 1; i <= 1000000; i++) {
        if ( (2 + 2) != 4) {
        console.log('Something has gone very wrong :( ');
        }
    }
    };

    // Write your code below

    const isTwoPlusTwo = checkThatTwoPlusTwoEqualsFourAMillionTimes

    console.log(isTwoPlusTwo.name);

*/

/* Higher order functions - param is the function passed, NO PARANTHESES, functions passed as parameters are CALLBACKS, callback functions
    // JavaScript functions are first-class objects, so they have properties and methods as well!

    const higherOrderFunc = param => {
        param();
        return `I just invoked ${param.name} as a callback function!`;
    }
 
    const anotherFunc = () => { //takes in no parameters (therefore the empty parantheses)
        return 'I\'m being invoked by the higher-order function!';
    }

    higherOrderFunc(anotherFunc); //passing a function as an argument

*/

/*  Iterators

    0. for - for loops are iterators, they iterate through an array with a given condition and incrementation
        //prints out each element of array
    for (let i = 0; i < array.length; i++) {
        console.log(array[i]);
    }
    
    1. .forEach() - iterates through each element in the array, always returns undefind

    const fruits = ['mango', 'papaya', 'pineapple', 'apple'];

    function printFruits(element) {
        console.log("I want to eat a " + element);
    }

    //calls printFruits function for each element in array
    fruits.forEach(printFruits);

    /// Arrow function syntax - does same thing, but simpler; for each element in the fruits array (fruit), console.log(etc.)

    fruits.forEach(fruit => console.log("I want to eat a " + fruit));

    2. .map() - iterates through each element in the array, returns an array with instructions from function body, doesn't mutate original array

    const bigNumbers = [100, 200, 300, 400, 500];
                                        //number is the identifier for each element in the array bigNumbers.
    const smallNumbers = bigNumbers.map(number => {
        return number / 100;
    });

    console.log(smallNumbers); // prints an array that has each element from bigNumbers divided by 100.

    3. .filter() - iterates through each element in the array, returns an array that make the conditional TRUE, doesn't mutate original array

    const randomNumbers = [375, 200, 3.14, 7, 13, 852];
                                    //number is the identifier for each element in the array randomNumbers
    const smallNumbers = randomNumbers.filter(number => {
        return number < 250;
    });

    console.log(smallNumbers); // prints an array that contains all the elements from randomNumbers that are greater than 250

    4. .findIndex() - iterates through each element in the array UNTIL first element that makes conditional TRUE is found, doesn't mutate original array
                                    //if an element that makes the conditional TRUE is not found, it returns -1.
    const animals = ['hippo', 'tiger', 'lion', 'seal', 'cheetah', 'monkey', 'salamander', 'elephant'];
                                        //animal is the identifier for each element in the array
    const foundAnimal = animals.findIndex(animal => {
        return animal === "elephant";
    });

    console.log(foundAnimal);

   5. .reduce() - iterates through each elemt in the array, grabbing the sum of the previous elements and the current, 
                                    //ultimately returning the sum of all the elements, doesn't mutate the og array

    const newNumbers = [1, 3, 5, 7];

                //accumulator is just the sum of the previous values, on first iteration it will be first element in array
                //currentValue is the value of current element in the array
                //accumulator will always be the sum of the accumulator and currentValue from previous iteration.
    const newSum = newNumbers.reduce((accumulator, currentValue) => {
        console.log("The value of accumulator:", accumulator);
        console.log("The value of currentValue:", currentValue);
        return accumulator + currentValue;
    });

        //returns total sum from all the elemnts in the array
    console.log("The sum of accumulator (previous value) and currentValue is:", newSum);

    6. .some() - iterates through each element in the array, returns true if atleast one of the elements makes the condition true

    const words = ['unique', 'uncanny', 'pique', 'oxymoron', 'guise'];
                // returns true
    console.log(words.some((word) => {
        return word.length < 6;
    }));

    7. .every() - iteraters through each element in the array, returns true if EVERY element in the array makes the condition true

    const interestingWords = ['unique', 'uncanny', 'oxymoron'];
        
    const interestingWords = words.filter(word => {
        return word.length > 5;
    });
                //returns true
    console.log(interestingWords);

*/

/*      Objects - non-primitive data types (can have multiple functions and purposes)

        //object literal - declaration of an object
    let spaceship = {
        //key       //value
        homePlanet: 'Earth',
        color: 'silver',
        'Fuel Type': 'Turbo Fuel',
        numCrew: 5,
        flightPath: ['Venus', 'Mars', 'Saturn']
    };

    //can call upon an objects properties, similar to how you'd call .length on a string (a string is also a non-primitive data type)
    let crewCount = spaceship.numCrew;
    console.log(crewCount);

    let planetArray = spaceship.flightPath;
    console.log(planetArray);

    //can also use bracket notation to call upon an object's properties. HAVE TO USE BRACKET NOTATION FOR KEYS THAT
    // ARE STRINGS, NUMBERS, SPECIAL CHARS, (ALMOST ALL KEYS - SHOULD PROB JUST USE THIS TO BE SAFE)
    spaceship["numCrew"];           //these all work the same
    let crewMembers = "numCrew";
    spaceship[crewMembers];


    //objects are mutable, we can change their properties, even if it is const (can't reassign const objects tho).
    let spaceship = {
        'Fuel Type' : 'Turbo Fuel',
        homePlanet : 'Earth',
        color: 'silver',
        'Secret Mission' : 'Discover life outside of Earth.'
    };

    spaceship.color = "glorious gold";  //changes color property value to glorious gold
    spaceship.numEngines = 7;   // adds a numEngines property with value 7

    delete spaceship["Secret Mission"];     //deletes "Secret Mission" property from object

    //METHODS - A function inside of an object (Ex: .floor - Math.floor(), .log - console.log()) - always followed by (), may incl params

    let retreatMessage = 'We no longer wish to conquer your planet. It is full of dogs, which we do not care for.';

    let alienShip = {
        // method declaration
        retreat: function () {
            console.log(retreatMessage);
        },
        takeOff: function () {
            console.log("Spim... Borp... Glix... Blastoff!");
        }
    }

    alienShip.retreat();
    alienShip.takeOff();

    //NESTED OBJECTS - Objects inside of objects

    let spaceship = {
        passengers: null,
        telescope: {
            yearBuilt: 2018,
            model: "91031-XLT",
            focalLength: 2032 
        },
        crew: {
            captain: { 
            name: 'Sandra', 
            degree: 'Computer Engineering', 
            encourageTeam() { console.log('We got this!') },
            'favorite foods': ['cookies', 'cakes', 'candy', 'spinach'] }
        },
        engine: {
            model: "Nimbus2000"
        },
        nanoelectronics: {
            computer: {
            terabytes: 100,
            monitors: "HD"
            },
            'back-up': {
            battery: "Lithium",
            terabytes: 50
            }
        }
    }; 
                        //how to iterate through nested objects
    let capFave = spaceship.crew.captain['favorite foods'][0];
    console.log(capFave);
                        //HOW TO ASSIGN AN ARRAY OF OBJECTS TO A PROPERTY VALUE
                        //Each object doesn't need an identifier, just list the keys and values (properties in {})
    spaceship['passengers'] = [{age: 30, job: "chef"}];

    let firstPassenger = spaceship.passengers[0];
    console.log(firstPassenger);

    //Passing by reference - anytime you pass an object as an argument, any changes to the parameters properties will also apply
    //to object in global scope - HOWEVER, you cannot reassign the object variable to a new object and apply to object in global scope

    //object properties are changed
    const spaceship = {
        homePlanet : 'Earth',
        color : 'silver'
    };
    
    let paintIt = obj => {
        obj.color = 'glorious gold'
    };
    
    paintIt(spaceship);
    
    spaceship.color // Returns 'glorious gold'

    //object cannot be reassigned when passed as arg - this is because even tho the object is passed by reference, the variable 
    // that holds the reference inside of the func has its own memory address as well. changing the reference of this variable in the func
    // doesn't change the reference of the 'spaceship' variable that was passed as an argument

    let spaceship = {
        homePlanet : 'Earth',
        color : 'red'
    };
    let tryReassignment = obj => {
    obj = {
        identified : false, 
        'transport type' : 'flying'
    }
    console.log(obj) // Prints {'identified': false, 'transport type': 'flying'}
    
    };
    tryReassignment(spaceship) // The attempt at reassignment does not work.
    spaceship // Still returns {homePlanet : 'Earth', color : 'red'};
    
    spaceship = {
    identified : false, 
    'transport type': 'flying'
    }; // Regular reassignment still works.

    ///// LOOPING THROUGH OBJECTS

    let spaceship = {
        crew: {
            captain: { 
                name: 'Lily', 
                degree: 'Computer Engineering', 
                cheerTeam() { console.log('You got this!') } 
            },
            'chief officer': { 
                name: 'Dan', 
                degree: 'Aerospace Engineering', 
                agree() { console.log('I agree, captain!') } 
            },
            medic: { 
                name: 'Clementine', 
                degree: 'Physics', 
                announce() { console.log(`Jets on!`) } 
            },
            translator: {
                name: 'Shauna', 
                degree: 'Conservation Science', 
                powerFuel() { console.log('The tank is full!') } 
            }
        }
    }; 

        //crewMember represents each key in object spaceship.crew -  crewMember IS A STRING
    for (let crewMember in spaceship.crew) {
                                        //since crewMember IS A STRING, we cannot just use crewMember.name, you have to treat it 
                                        //as a string ref to a property
        console.log(`${crewMember}: ${spaceship.crew[crewMember].name}`);
    }

    for (let crewMember in spaceship.crew) {
        console.log(`${spaceship.crew[crewMember].name}: ${spaceship.crew[crewMember].degree}`);
    }
*/

/* THIS keyword

            //cannot access an object's properties from within one of the object's methods, have to use THIS (keyword) to access them
                                                                                        //THIS references the calling object
                                    //THIS keyword does not work for arrow functions, avoid using arrow functions as much as possible
    const robot = {
        model: "1E78V2",
        energyLevel: 100,
        provideInfo() {
            return `I am ${this.model} and my current energy level is ${this.energyLevel}.`;
        },
    };

    console.log(robot.provideInfo())

*/

/*
    add _ to properties that should not be changed - think private properties and methods from c++ ex: _age or _amount

*/

/* GETTER & SETTER METHODS

    /// GETTER - similar to a normal method, returns something about data within the object, or a property

    const robot = {
        _model: '1E78V2',
        _energyLevel: 100,
        get energyLevel() {
            if (typeof this._energyLevel === "number") {
                return `My current energy level is ${this._energyLevel}`;
            } else {
                return "System malfunction: cannot retrieve energy level";
            }
        }
    }

    /// call upon the getter method without parantheses, almost like it's another property
    console.log(robot.energyLevel);

    ///SETTER - reassigns values of existing properties in an object

    const robot = {
        _model: '1E78V2',
        _energyLevel: 100,
        _numOfSensors: 15,
        get numOfSensors() {
            if (typeof this._numOfSensors === 'number'){
                return this._numOfSensors;
            } else {
                return 'Sensors are currently down.'
            }
        },
        //even though you are creating the method to pass an argument, when you call for the setter you set it equal to the arg.
        set numOfSensors(num) {
            if (typeof num === "number" && num >= 0) {
                this._numOfSensors = num;
            } else {
                console.log("Pass in a number that is greater than or equal to 0");
            }
        },
    };
    // pass the parameter by setting it equal to the setter method. ONCE AGAIN NO PARANTHESES
    //THE PARAMETERS PASSED MAKE IT DIFFERENT FROM THE GETTER METHOD
    robot.numOfSensors = 100;
    console.log(robot.numOfSensors);

*/

/* Factory functions - functions used to make multiple objects, all with the possibility of making multiple instances of the same object

    //the factory function returns an object that is customized using the parameters
    function robotFactory(model, mobile) {
        return {
            model: model,
            mobile: mobile,
            beep() {
                console.log("Beep Boop");
            },
        }
    }

    //arrow function syntax
    let robotFactory = (model, mobile) => {
        return {
            model: model,
            mobile: mobile,
            beep() {
                console.log("Beep Boop");
            },
        }
    }

    //can also use shorthand syntax - just directly assumes the parameters are being set for the properties, I would avoid this it's lazy.
    let robotFactory = (model, mobile) => {
        return {
            model,
            mobile,
            beep() {
                console.log("Beep Boop");
            },
        }
    }

    const tinCan = robotFactory("P-500", true);
    tinCan.beep();

    //destructured assignment - similar to shorthand syntax, grabs the property based on the name of the variable wrapped in curly brackets

    const robot = {
        model: '1E78V2',
        energyLevel: 100,
        functionality: {
            beep() {
                console.log('Beep Boop');
            },
            fireLaser() {
                console.log('Pew Pew');
            },
        }
    };

        //since variable is named 'functionality' and wrapped in curly brackets, it will look for 'functionality' property in 'robot' object
    const {functionality} = robot;
    //can call upon the 'beep' property within 'functionality' object
    functionality.beep()

    ///// Additional Methods

    const robot = {
        model: 'SAL-1000',
        mobile: true,
        sentient: false,
        armor: 'Steel-plated',
        energyLevel: 75
    };

    /// Object.keys(obj) - creates an array with the keys or properties within an object - the object is the parameter
    const robotKeys = Object.keys(robot);
    console.log(robotKeys);

    /// Object.entries(obj) - creates an array with the keys and value pairs within an object (tuples) - the object is the parameter
    const robotEntries = Object.entries(robot);
    console.log(robotEntries);

    ///  Object.assign(object1/target, object2/source1, object3/source2, ...) - creates a new object with a combination of the keys and value pairs of however 
                                                        //many other objects you add in the arguments
                                        - ALSO can transform the target object (object1) by adding the properties of object2 to it.
    let oldRobot = {
        laserBlaster: true,
        voiceRecognition: true,
    }

    const newRobot =  Object.assign({laserBlaster: true, voiceRecognition: true}, robot);
    Object.assign(oldRobot, robot);

        //BOTH of these would have the same answer.
    console.log(newRobot);
    console.log(oldRobot);

*/
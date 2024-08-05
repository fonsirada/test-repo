// String, numbers, boolean, null, undefined
// only numbers in js, not floats or ints

const name = "John";
const age = 32;
const number = 4;
const number_2 = 4.5;
const cond = true;
const y = undefined;
let z; // z = undefined

//formatted strings
const hello = `Hello! My name is ${name}, and I am ${age}`;

//object literals

const person = {
    firstName: "John",
    lastname: "Doe",
    age: 30,
    hobbies: ['music', 'movies', 'sports'],
    address: {
        street: "50 main st",
        city: "Boston",
        state: "MA"
    }
}

//classes

class Person {
    constructor(firstName, lastName, dob) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.dob = new Date(dob);
    }

    getBirthYear() {
        return this.dob.getFullYear();
    }

    getFullName() {
        return `${this.firstName} ${this.lastName}`;
    }
}

const person1 = new Person("Alfonso", "Rada", "07-29-2005");


// learning the DOM

//single element - # for ids, . for classes,
const buns = document.querySelector('#buns');

//multiple elements
const passwords = document.querySelectorAll('.passwords'); //returns a NodeList, which can be looped through just like an array
//passwords.forEach((password) => console.log(password)); //prints out each element in passwords NodeList
buns.textContent = "Balls"; //changes text content of element buns
passwords[1].innerText = "Bolitas" //changes inner text of first element in passwords NodeList

buns.style.color = "green"; //can change css methods as well

const button = document.querySelector(".btn");
// button.addEventListener('click', function (e) {
//     e.preventDefault();
//     button.textContent = "Submitted!";
//     console.log('click');
// });
const form = document.querySelector("#form");
const nameInput = document.querySelector("#name");
const passwordsList = document.querySelector(".passwords");
form.addEventListener('submit', function (event) {
    event.preventDefault();
    if (nameInput.value === '') {
        const msg = document.querySelector("#msg");
        //adds an element to a class - error class in css has error pop-up decorations
        msg.classList.add('error');
        msg.textContent = "Please enter a name.";
        //removes message after 3 seconds or 3000 milliseconds.
        setTimeout(function() {
            msg.remove();
        }, 3000);
        const div = document.createElement('div');
        //adds id attribute to div and the id is 'msg'
        div.setAttribute("id",'msg');
        form.appendChild(div);
    } else {
        //creates an html element 
        const li = document.createElement('li');
        //adds text to the html element
        li.appendChild(document.createTextNode(nameInput.value));
        //adds li as an element to list, passwordsList
        passwordsList.appendChild(li);

        //clears name field
        nameInput.value = '';
    }
})

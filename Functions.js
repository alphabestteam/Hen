function helloWorld(){
    return "Hello World";
}

function sayHi(name){
    return "Hello " + name;
}

const setSquared = (number)=> number**2;

const rectangleArea = (length,width) => length*width;

const circleValues = (radius) => {
    const circumference = 2*Math.PI * radius;
    const area = Math.PI * Math.pow(radius,2);
    return [circumference,area];
}

const countVowels = (sentence)=>{
    sentence = sentence.toUpperCase();
    const vowelPattern = /[AEOUI]/g;
    const vowelMatches = sentence.match(vowelPattern);
    return vowelMatches ? vowelMatches.length : 0;
}

const isSameLength = (array1,array2) => array1.length == array2.length;

const getTruthyFalsyArr = (myArr)=> myArr.map((element)=>Boolean(element));



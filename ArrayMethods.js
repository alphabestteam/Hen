// 1. the difference is when i use at(index) if i out of the array i get undifinde but it dont work on old version
function MakeArray(length,char){
    let text = "";
    let padded = text.padStart(length,char)
    const Array = padded.split("");
    return Array;
}
function cutArray(length,array){
    if(length>array.length || length<0){
        console.log("dont good length");
    }else{
        array.splice((array.length)-length-1,length);
        console.log(array);
    }
}
function newFirstValue(number,array){
    array.unshift(number);
    return array;
}

function sumArrays(array1, array2) {
    const result = array1.concat(array2);
    return result;
}

function upperArray(array){
    const upperCaseStrings = array.map(function (str) {
        return str.toUpperCase();
    });
    return upperCaseStrings;
}

function towDigits(array){
    const newArray = array.filter(function(number){
        return number>=10 && number<=99;
    });
    return newArray;
}

const includeTarget = (value,array) => array.includes(value);

function firstGreaterThan10(array){
    const result = array.find(function(number){
        return number>10;
    });
    return result;
}

function isAnyGreaterThan10(array){
    const result = firstGreaterThan10(array);
    return result !== undefined;
}

// when we use sort even on array of number he sort them like strings and in when he take 100 and 2
// he take the first of 100 which mean 1 and compare it to 2 and 1<2 so we dont get numerical

MyArray = [1,30,4,21,10000];
MyArray.sort(function(a,b){
    return a-b;
});

const sortArrayAsString = (array) => array.join("**");

const sortLetters = (array) => array.sort();

const checkIfBiggerValue = (value, array) => array.every((element) => element < value);

const checkIfAnyBiggerValue = (value, array) => array.some((element) => element > value);



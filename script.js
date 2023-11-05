function sequenceA() {
    setTimeout(_ => console.log('Sponge'), 0);
    console.log("Bob");
}

function sequenceB(){
    setTimeout(_ => console.log(`🍅 Timeout at B`), 0);
    Promise.resolve().then(_ => console.log('🍍 Promise at B'));
}

function sequenceC(){
    setTimeout(_ => console.log(`🍅 Timeout at C`), 0);
    Promise.resolve().then(_ => setTimeout(console.log('🍍 Promise at C'), 1000));
}

function sequenceD(){
    console.log('Sponge');
    setTimeout(_ => console.log('Square'), 0);
    Promise.resolve().then(_ => console.log('Pants'));
    console.log('Bob');
}

function questionA(){
    sequenceA();
}

function questionB(){
    sequenceB();
}

function questionC(){
    sequenceC();
}

function questionD(){
    sequenceD();
}

function questionE(){
    sequenceB();
    sequenceC();
}

//questionA();
//questionB();
// questionC();
// questionD();
 questionE();

// in A sponge is settimeout so it go to callback queue so first we get Bob and after that Sponge
// in B first the timeout go to callback queue and we go to the promise print "Promise at B" and after "timeout at B"
// in C first we print Promise at C because when we use then it print without waiting so and after the timeout at C 
// in D Sponge is console so he is first the timeout go to callback queue and than the promise also wait the we print Bob after that Pants 
// and than Square
// in E the timeout of B go to callback queue and than the promise than he go to C and there timeout go to the callback queue and than we 
// print the Promise and after we run the queue the timeout at B is first and last timeout at C



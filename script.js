const main = document.querySelector('main');

function createHeading(color, text){
    const heading = document.createElement('h1');
    heading.setAttribute('style', 'color: ' + color);
    heading.textContent = text;
    return heading;
}

function headingFactory(color){
    return function (text) {
        return createHeading(color, text);
    };
}
const createHeadingRed = headingFactory("red");
const createHeadingBlue = headingFactory("blue");

const naiveHead1 = createHeadingRed('using factory 1');
const naiveHead2 = createHeadingBlue('using factory 2');

//this is to be changed to append a header we create by using the higher order function headingFactory(color).
main.appendChild(naiveHead1);
main.appendChild(naiveHead2);

// it is good to use it becase it make resuability the code look simpler and more clean when every function has their rull
// when there is error it is  easy to find where
const student1 = {
    name:"Hen",
    age:21,
    grades:[100,90,95,88,97],
    avg:function(){
        const sum = this.grades.reduce((total,current) => total+current,0);
        average = sum/this.grades.length;
        upName = this.name.toUpperCase();
        const vowelPattern = /[AEOUI]/g;
        const vowelMatches = upName.match(vowelPattern);
        return average+ vowelMatches;
    }
};

const student2 = {
    name: "Alice",
    age: 22,
    grades: [85, 92, 78, 90, 94],
    avg: function () {
        const sum = this.grades.reduce((total, current) => total + current, 0);
        const average = sum / this.grades.length;
        const upName = this.name.toUpperCase();
        const vowelPattern = /[AEOUI]/g;
        const vowelMatches = upName.match(vowelPattern);
        return average + vowelMatches.length;
    }
};

const student3 = {
    name: "Bob",
    age: 20,
    grades: [75, 88, 92, 79, 87],
    avg: function () {
        const sum = this.grades.reduce((total, current) => total + current, 0);
        const average = sum / this.grades.length;
        const upName = this.name.toUpperCase();
        const vowelPattern = /[AEOUI]/g;
        const vowelMatches = upName.match(vowelPattern);
        return average + vowelMatches.length;
    }
};

const student4 = {
    name: "Sarah",
    age: 23,
    grades: [91, 86, 89, 92, 95],
    avg: function () {
        const sum = this.grades.reduce((total, current) => total + current, 0);
        const average = sum / this.grades.length;
        const upName = this.name.toUpperCase();
        const vowelPattern = /[AEOUI]/g;
        const vowelMatches = upName.match(vowelPattern);
        return average + vowelMatches.length;
    }
};

const student5 = {
    name: "David",
    age: 19,
    grades: [80, 94, 87, 91, 76],
    avg: function () {
        const sum = this.grades.reduce((total, current) => total + current, 0);
        const average = sum / this.grades.length;
        const upName = this.name.toUpperCase();
        const vowelPattern = /[AEOUI]/g;
        const vowelMatches = upName.match(vowelPattern);
        return average + vowelMatches.length;
    }
};

const students = [student1,student2,student3,student4,student5];

for (let i = 0; i < students.length; i++) {
    console.log(i);
}

const printFields = (student) => {
    return `name: ${student.name} age: ${student.age} grades: ${student.grades} average: ${student.avg()}`;
}
for (const student of students){
    console.log(printFields(student));
}

const adults = students.filter((student) => student.age >= 18);
console.log(adults);

const myCar = {
    company:"kia",
    kind:"sport",
    yearMade:2020,
    age: function(){
        const currentYear = new Date().getFullYear();
        const carAge = currentYear - this.yearMade;
        return carAge;
    }
}

const printCarFields = (car) => {
    return `name: ${car.company} age: ${car.kind} grades: ${car.yearMade} average: ${car.age()}`;
}

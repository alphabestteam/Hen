const characterInfo = new Map([
    ['Main character', 'SpongeBob'],
    ['Best friend', 'Patrick'],
    ['Pet', 'Gary'],
    ['Word buddy', 'Squidward'],
    ['Manager', 'Mr. Krabs'],
    ['Teacher', 'Mrs. Puff'],
    ['Location', 'Bikini Bottom']
]);

console.log(characterInfo);

const keysArray = Array.from(characterInfo.keys());

console.log(keysArray);

console.log(characterInfo.get("Location"));

console.log(characterInfo.size)

characterInfo.delete("Location")

console.log(characterInfo.size)

console.log(characterInfo);

exist = characterInfo.has("Location");
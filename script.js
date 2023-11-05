const speciesPoints = {
    'pink spotted': 4,
    'blue stinger': 3,
    'green itches': 2
};

const jellyfishDays = [
    [
        { color: 'pink'},
        { color: 'pink'},
        { color: 'blue'},
        { color: 'green'},
        { color: 'white'},
        { color: 'white'},
    ],
    [
        { color: 'pink'},
        { color: 'pink'},
        { color: 'blue'},
        { color: 'green'},
        { color: 'green'},
        { color: 'green'},
    ],
    [
        { color: 'pink'},
        { color: 'pink'},
        { color: 'pink'},
        { color: 'pink'},
        { color: 'blue'},
        { color: 'green'},
    ]
];
let count = 0;
// SpongeBob's net callback function
function catchJellyfish(jellyfish, identifyJellyfishAndAddPoints) {
    console.log("SpongeBob caught a "+jellyfish+" jellyfish!");
    identifyJellyfishAndAddPoints(jellyfish,addPoints);
    console.log(count);
}

// Patrick's net callback function
function identifyJellyfishAndAddPoints(jellyfish, addPoints) {
    species = identifySpecies(jellyfish);
    count += addPoints(species);
    console.log("Patrick identified a "+species + "jellyfish!");
}

// Score keeping callback function
function addPoints(species) {
    if (species in speciesPoints) {
        return speciesPoints[species];
    } else {
        return 1;
    }
}

// Helper functions
function identifySpecies(jellyfish) {
    if(jellyfish=="pink"){
        return 'pink spotted';
    }else if(jellyfish == "blue"){
        return 'blue stinger';
    }else if(jellyfish == "green"){
        return 'green itches';
    }else{
        return 'other';
    }
}

//The Adventure Starts Here! 

for (const day of jellyfishDays) {
    console.log("Let's go jellyfishing!");
    for (const jellyfish of day) {
        catchJellyfish(jellyfish.color,identifyJellyfishAndAddPoints)
    }
    console.log("Final score:"+ count);
}

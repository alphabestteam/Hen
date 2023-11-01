/*
Your job for today is to finish the starSign function.

Find the astrological sign, given the birth details as a Date object.
Start and end dates for zodiac signs very on different resources, 
so we will use this table to get consistent testable results:

Aquarius ----- 21 January - 19 February
Pisces ----- 20 February - 20 March
Aries ----- 21 March - 20 April
Taurus ----- 21 April - 21 May
Gemini ----- 22 May - 21 June
Cancer ----- 22 June - 22 July
Leo ----- 23 July - 23 August
Virgo ----- 24 August - 23 September
Libra ----- 24 September - 23 October
Scorpio ------ 24 October - 22 November
Sagittarius ----- 23 November - 21 December
Capricon ------ 22 December - 20 January
*/

function starSign(date){
    const day = date.getDate();
    const month = date.getMonth() + 1;

    switch (month) {
        case 1:
            if (day >= 21) return "Aquarius"
            return "Capricorn";
        case 2:
            if (day <= 19) return "Aquarius"
            return "Pisces";
        case 3:
            if (day <= 20) return "Pisces"
            return "Aries";
        case 4:
            if (day <= 20) return "Aries"
            return "Taurus";
        case 5:
            if (day <= 21) return "Taurus"
            return "Gemini";
        case 6:
            if (day <= 21) return "Gemini"
            return "Cancer";
        case 7:
            if (day <= 22) return "Cancer"
            return "Leo";
        case 8:
            if (day <= 23) return "Leo"
            return "Virgo";
        case 9:
            if (day <= 23) return "Virgo"
            return "Libra";
        case 10:
            if (day <= 23) return "Libra"
            return "Scorpio";
        case 11:
            if (day <= 22) return "Scorpio"
            return "Sagittarius";
        case 12:
            if (day <= 21) return "Sagittarius"
            return "Capricorn";
        default:
            return "Invalid date"
    }
}
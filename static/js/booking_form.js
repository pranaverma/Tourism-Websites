var countryAndAgent = {};
countryAndAgent["Australia"] = ["David", "Steve", "Ashley", "Ellyse"];
countryAndAgent["Italy"] = ["Federico", "Lorenzo", "Isabella", "Gabriella"];
countryAndAgent["Switzerland"] = ["Paul", "Xavi", "Sofia", "Scarlet"];
countryAndAgent["Mauritius"] = ["Henry", "Jack", "Jerome", "Michail"];
countryAndAgent["France"] = ["Varane", "Louis", "Sarah", "Laura"];
countryAndAgent["Greece"] = ["Alexander", "dimitri" , "christos", "petros"];
countryAndAgent["Hong KOng"] = ["Xiong", "Leia", "William", "Weaton"];
countryAndAgent["UAE"] = ["Mansour", "Norryis", "Betsy", "Anna"];

var countryAndCity = {};
countryAndCity["Australia"] = ["Sydney", "Melbourne", "Brisbane", "Canberra"];
countryAndCity["Italy"] = ["Rome", "Venice", "Milan", "Florence"];
countryAndCity["Switzerland"] = ["Basel", "Geneva", "Lucerne", "Zurich"];
countryAndCity["Mauritius"] = ["Curepipe", "Flic-en-Flac", "Grand Baie", "Port Louis"];
countryAndCity["France"] = ["Paris", "Cannes", "Bordeaux", "Corsica"];
countryAndCity["Greece"] = ["Athens", "Thessaloniki", "Chania", "Rhodes Town"];
countryAndCity["Hong KOng"] = ["Lantau Island", "Tsim Sha Tsui", "Kowloon", "Repulse Bay"];
countryAndCity["UAE"] = ["Abu Dhabi", "Dubai", "Fujairah", "Sharjah"];

var cityAndHotel = {};
cityAndHotel["None"] = ["None"]
cityAndHotel["Sydney"] = ["None", "QT Sydney", "Fraser Suites Sydney"];
cityAndHotel["Melbourne"] = ["None", "Park Hyatt Melbourne", "The Langham Melbourne"];
cityAndHotel["Brisbane"] = ["None", "Crystalbrook Vincent", "Hyatt Regency Brisbane"];
cityAndHotel["Canberra"] = ["None", "Midnight Hotel", "Hotel Realm"];
cityAndHotel["Rome"] = ["None", "Hotel Artemide", "Albergo del Senato"];
cityAndHotel["Venice"] = ["None", "Hotel Ai Reali", "Rosa Salva Hotel"];
cityAndHotel["Milan"] = ["None", "Lancaster Hotel", "43 Station Hotel"];
cityAndHotel["Florence"] = ["None", "Hotel Franchi", "Diplomat Hotel"];
cityAndHotel["Basel"] = ["None", "Hyperion Hotel Basel", "ibis budget Basel City"];
cityAndHotel["Geneva"] = ["None", "Nash Suites Airport Hotel", "Warwick Geneva"];
cityAndHotel["Lucerne"] = ["None", "ibis budget Hotel Luzern", "AMERON Luzern Hotel Flora"];
cityAndHotel["Zurich"] = ["None", "Crowne Plaza Zurich", "Central Plaza"];
cityAndHotel["Curepipe"] = ["None", "Hennessy Park Hotel", "Le Suffren Hotel & Marina"];
cityAndHotel["Flic-en-Flac"] = ["None", "Seastar Hotel", "Sofitel L'Imperial Resort and Spa"];
cityAndHotel["Grand Baie"] = ["None", "Hôtel 20 Degrés Sud", "Mauricia Beachcomber Resort & Spa"];
cityAndHotel["Port Louis"] = ["None", "Cocotiers Hotel", "Labourdonnais Waterfront Hotel"];
cityAndHotel["Paris"] = ["None", "Hotel Malte- Astotel", "Hotel 34B- Astotel"];
cityAndHotel["Cannes"] = ["None", "Hotel de Provence", "Hotel Martinez"];
cityAndHotel["Bordeaux"] = ["None", "Hotel Cardinal Bordeaux", "Hotel Gambetta"];
cityAndHotel["Corsica"] = ["None", "Hotel Tettola", "Hotel Bartaccia"];
cityAndHotel["Athens"] = ["None", "Sofitet Athens Hotel", "Plaka Hotel"];
cityAndHotel["Thessaloniki"] = ["None", "Hyatt Regency Thessaloniki", "Electra Hotel"];
cityAndHotel["Chania"] = ["None", "Hyperion City Hotel", "Enetiko Rooms"];
cityAndHotel["Rhodes Town"] = ["None", "Elites Hotel", "Esperia City Hotel"];
cityAndHotel["Lantau Island"] = ["None", "Disney Explorers Lodge", "Hong Kong Disneyland Hotel"];
cityAndHotel["Tsim Sha Tsui"] = ["None", "Sheraton Hong Kong Hotel & Towers", "InterContinental Grand Stanford"];
cityAndHotel["Kowloon"] = ["None", "The Mira Hong Kong", "Regal Kowloon Hotel"];
cityAndHotel["Repulse Bay"] = ["None", "Ocean Park Marriott Hotel", "The Fleming Hong Kong"];
cityAndHotel["Abu Dhabi"] = ["None", "Traders Hotel, Abu Dhabi", "Southern Sun Abu Dhabi"];
cityAndHotel["Dubai"] = ["None", "Atana Hotel", "Citymax Hotel Bur Dubai"];
cityAndHotel["Fujairah"] = ["None", "The White villa", "Ibis Fujairah"];
cityAndHotel["Sharjah"] = ["None", "Golden Sands Hotel", "Citymax Sharjah"];

function ChangeCountryList() {
    var countryList = document.getElementById("country");
    var agentList = document.getElementById("countryagent");
    var hotelList1 = document.getElementById("firsthotel");
    var hotelList2 = document.getElementById("secondhotel");
    var hotelList3 = document.getElementById("thirdhotel");
    var hotelList4 = document.getElementById("fourthhotel");
    var city1List = document.getElementById("city1");
    var city2List = document.getElementById("city2");
    var city3List = document.getElementById("city3");
    var city4List = document.getElementById("city4");
    var selagent = countryList.options[countryList.selectedIndex].value;
    while (hotelList1.options.length) {
        hotelList1.remove(0);
    }
    while (hotelList2.options.length) {
        hotelList2.remove(0);
    }
    while (hotelList3.options.length) {
        hotelList3.remove(0);
    }
    while (hotelList4.options.length) {
        hotelList4.remove(0);
    }
    while (agentList.options.length) {
        agentList.remove(0);
    }
    while (city1List.options.length) {
        city1List.remove(0);
    }
    while (city2List.options.length) {
        city2List.remove(0);
    }
    while (city3List.options.length) {
        city3List.remove(0);
    }
    while (city4List.options.length) {
        city4List.remove(0);
    }
    var countries = countryAndAgent[selagent];
    var cities = countryAndCity[selagent];

    agentList.options.add(new Option("None","None"));

    if (countries) {
        var i;
        for (i = 0; i < countries.length; i++) {
            var country = new Option(countries[i],countries[i]);
            agentList.options.add(country);
        }
    }
    var temphotel1 = new Option("None","None");
    hotelList1.options.add(temphotel1);
    var temphotel2 = new Option("None","None");
    hotelList2.options.add(temphotel2);
    var temphotel3 = new Option("None","None");
    hotelList3.options.add(temphotel3);
    var temphotel4 = new Option("None","None");
    hotelList4.options.add(temphotel4);
    var temp1 = new Option("None","None");
    city1List.options.add(temp1);
    var temp2 = new Option("None","None");
    city2List.options.add(temp2);
    var temp3 = new Option("None","None");
    city3List.options.add(temp3);
    var temp4 = new Option("None","None");
    city4List.options.add(temp4);
    if (cities) {
        var i;
        for (i = 0; i < cities.length; i++) {
            var city = new Option(cities[i], cities[i]);
            city1List.options.add(city);
        }
        for (i = 0; i < cities.length; i++) {
            var city = new Option(cities[i], cities[i]);
            city2List.options.add(city);
        }
        for (i = 0; i < cities.length; i++) {
            var city = new Option(cities[i], cities[i]);
            city3List.options.add(city);
        }
        for (i = 0; i < cities.length; i++) {
            var city = new Option(cities[i], cities[i]);
            city4List.options.add(city);
        }
    }
}

function ChangeCityList1() {
    var cityList = document.getElementById("city1");
    var hotelList1 = document.getElementById("firsthotel");
    var selcity = cityList.options[cityList.selectedIndex].text;
    while (hotelList1.options.length) {
        hotelList1.remove(0);
    }
    var hotels = cityAndHotel[selcity];
    if (hotels) {
        var i;
        for (i = 0; i < hotels.length; i++) {
            var temp = new Option(hotels[i], hotels[i]);
            hotelList1.options.add(temp);
        }
    }
}
function ChangeCityList2() {
    var cityList = document.getElementById("city2");
    var hotelList2 = document.getElementById("secondhotel");
    var selcity = cityList.options[cityList.selectedIndex].text;
    while (hotelList2.options.length) {
        hotelList2.remove(0);
    }
    var hotels = cityAndHotel[selcity];
    if (hotels) {
        var i;
        for (i = 0; i < hotels.length; i++) {
            var temp = new Option(hotels[i], hotels[i]);
            hotelList2.options.add(temp);
        }
    }
}
function ChangeCityList3() {
    var cityList = document.getElementById("city3");
    var hotelList = document.getElementById("thirdhotel");
    var selcity = cityList.options[cityList.selectedIndex].text;
    while (hotelList.options.length) {
        hotelList.remove(0);
    }
    var hotels = cityAndHotel[selcity];
    if (hotels) {
        var i;
        for (i = 0; i < hotels.length; i++) {
            var temp = new Option(hotels[i], hotels[i]);
            hotelList.options.add(temp);
        }
    }
}
function ChangeCityList4() {
    var cityList = document.getElementById("city4");
    var hotelList = document.getElementById("fourthhotel");
    var selcity = cityList.options[cityList.selectedIndex].text;
    while (hotelList.options.length) {
        hotelList.remove(0);
    }
    var hotels = cityAndHotel[selcity];
    if (hotels) {
        var i;
        for (i = 0; i < hotels.length; i++) {
            var temp = new Option(hotels[i], hotels[i]);
            hotelList.options.add(temp);
        }
    }
}
function packageChange() {
    var package1 = document.getElementById("packagename");
    var day = document.getElementById("days");
    var selagent = package1.options[package1.selectedIndex].text;

    if(selagent=="Australia Package" || selagent=="Italy Package" || selagent=="Switzerland Package" || selagent=="Mauritius Package" || selagent=="France Package" || selagent=="Greece Package" || selagent=="Hong Kong Package" || selagent=="UAE Package"){
        day.value = "9";
    }
    else if(selagent=="Italy and Switzerland" || selagent=="Greece and Italy" || selagent=="Classical Europe"){
        day.value = "11";
    }
    else{
        day.value = "13";
    }
}
var viz;
var workbook, activeSheet, worksheet;
var activeFilters;

// [<URL>, <Title>, <Description>, <Thumbnail>]
data = [
    ["/1_aPERC4PANELDASHBOARD/PERCEFFDASHBOARD", "World CO2 Emissions", "View of emissions in different countries of the world", "../static/images/Random World Data.jpg"],
]

function createTiles() {
    for (let i of data) {
        $("#contentList").append(`<div class='col-sm-4'><a href='javascript:selectDashboard("${i[0]}")' class='tile purple'><img src="${i[3]}"><h3 class='title'>${i[1]}</h3><p>${i[2]}</p></a></div>`);
    }
}

function loadTableauDashboard() {

    var containerDiv = document.getElementById("vizContainer");

    
    $.get("/get_token");
    alert(getCookie("auth_token"));
    var url = "https://tabsmxnprod/trusted/" + getCookie("auth_token") + "/views" + '/1_aPERC4PANELDASHBOARD/PERCEFFDASHBOARD';
    document.cookie = "auth_token=; expires = Thu, 01 Jan 1970 00:00:00 GMT";
    var options = {
        height: 700,
        width: 1024
    }
    
    viz = new tableau.Viz(containerDiv, url, options);

}

function selectDashboard(name) {
    window.location.href = 'dashboard?dashboardName=' + name;
}

function getCookie(cookie_name) {
    var name = cookie_name + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var cookie_array = decodedCookie.split(';');    //split all the cookies of the string in an array
    for (var i = 0; i < cookie_array.length; i++) {
        var c = cookie_array[i];    //get one cookie at the time
        while (c.charAt(0) == ' ') {
            c = c.substring(1); //if the cookie starts with a blank space, remove the space
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);  //gets the value of the cookie (without the "field=")
        }
    }
    return "";
}

function exportPDF() {
    viz.showExportPDFDialog();
}

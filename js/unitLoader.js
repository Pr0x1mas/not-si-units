function csvToArray(str, delimiter = ",") { // https://sebhastian.com/javascript-csv-to-array/
    // slice from start of text to the first \n index
    // use split to create an array from string by delimiter
    const headers = str.slice(0, str.indexOf("\n")).split(delimiter);

    // slice from \n index + 1 to the end of the text
    // use split to create an array of each csv value row
    const rows = str.slice(str.indexOf("\n") + 1).split("\n");

    // Map the rows
    // split values from each row into an array
    // use headers.reduce to create an object
    // object properties derived from headers:values
    // the object passed as an element of the array
    const arr = rows.map(function (row) {
    const values = row.split(delimiter);
    const el = headers.reduce(function (object, header, index) {
        object[header] = values[index];
        return object;
    }, {});
    return el;
});

// return the array
return arr;
}


function getBaseUnits() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", 'https://raw.githack.com/Pr0x1mas/not-si-units/main/base.csv', false);
    xmlhttp.send();
    if (xmlhttp.status==200) {
        result = xmlhttp.responseText;
        baseUnits = csvToArray(result);

        baseUnitList = document.getElementById("SITable");

        baseUnits.forEach(element => {
            if(element.measurement) {
                console.log(element)
                newUnit = document.createElement("tr");

                newUnitMeasurement = document.createElement("td");
                newUnitSI = document.createElement("td");
                newUnitEquivalent = document.createElement("td");
                newUnitRatio = document.createElement("td");

                newUnitMeasurement.innerText = element.measurement.replaceAll("_", " ");
                newUnitSI.innerText = (element.si + " (" + element.siUnit + ")").replaceAll("_", " ");
                newUnitEquivalent.innerText = (element.equivalent + " (" + element.equivalentUnit + ")").replaceAll("_", " ");
                newUnitRatio.innerText = "1 : " + element.ratio;

                newUnit.appendChild(newUnitMeasurement);
                newUnit.appendChild(newUnitSI);
                newUnit.appendChild(newUnitEquivalent);
                newUnit.appendChild(newUnitRatio);

                baseUnitList.appendChild(newUnit);
            }
        });
    }
}

function getUnits() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", 'https://raw.githack.com/Pr0x1mas/not-si-units/main/units.csv', false);
    xmlhttp.send();
    if (xmlhttp.status==200) {
        result = xmlhttp.responseText;
        baseUnits = csvToArray(result);

        baseUnitList = document.getElementById("NamedTable");

        baseUnits.forEach(element => {
            if(element.measurement) {
                console.log(element)
                newUnit = document.createElement("tr");

                newUnitMeasurement = document.createElement("td");
                newUnitSI = document.createElement("td");
                newUnitEquivalent = document.createElement("td");
                newUnitRatio = document.createElement("td");

                newUnitMeasurement.innerText = element.measurement.replaceAll("_", " ");
                newUnitSI.innerText = (element.si + " (" + element.siUnit + ")").replaceAll("_", " ");
                newUnitEquivalent.innerText = (element.equivalent + " (" + element.equivalentUnit + ")").replaceAll("_", " ");
                newUnitRatio.innerText = "1 : " + element.ratio;

                newUnit.appendChild(newUnitMeasurement);
                newUnit.appendChild(newUnitSI);
                newUnit.appendChild(newUnitEquivalent);
                newUnit.appendChild(newUnitRatio);

                baseUnitList.appendChild(newUnit);
            }
        });
    }
}

function searchSI(){ // https://www.w3schools.com/howto/howto_js_filter_table.asp, with changes by me
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("SISearch");
    filter = input.value.toUpperCase();
    table = document.getElementById("SITable");
    tr = table.getElementsByTagName("tr");

    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
        td0 = tr[i].getElementsByTagName("td")[0];
        td1 = tr[i].getElementsByTagName("td")[1];
        td2 = tr[i].getElementsByTagName("td")[2];
        if (td1) {
            txtValue0 = td0.textContent || td0.innerText;
            txtValue1 = td1.textContent || td1.innerText;
            txtValue2 = td2.textContent || td2.innerText;

            if ((txtValue0.toUpperCase().indexOf(filter) > -1) || (txtValue1.toUpperCase().indexOf(filter) > -1) || (txtValue2.toUpperCase().indexOf(filter) > -1)) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}

function searchNamed(){ // https://www.w3schools.com/howto/howto_js_filter_table.asp, with changes by me
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("NamedSearch");
    filter = input.value.toUpperCase();
    table = document.getElementById("NamedTable");
    tr = table.getElementsByTagName("tr");

    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
        td0 = tr[i].getElementsByTagName("td")[0];
        td1 = tr[i].getElementsByTagName("td")[1];
        td2 = tr[i].getElementsByTagName("td")[2];
        if (td1) {
            txtValue0 = td0.textContent || td0.innerText;
            txtValue1 = td1.textContent || td1.innerText;
            txtValue2 = td2.textContent || td2.innerText;

            if ((txtValue0.toUpperCase().indexOf(filter) > -1) || (txtValue1.toUpperCase().indexOf(filter) > -1) || (txtValue2.toUpperCase().indexOf(filter) > -1)) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}

getBaseUnits()
getUnits()
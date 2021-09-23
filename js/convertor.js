unitConversionSelector = document.getElementById("unit-conversion-selector")
unitIn = document.getElementById("unit-in")
unitOut = document.getElementById("unit-out")
unitInLabel = document.getElementById("unit-in-label")
unitOutLabel = document.getElementById("unit-out-label")

function setConvertors(){
    unit = unitConversionSelector.options[unitConversionSelector.selectedIndex];
    unitIn.placeholder = unit.dataset.si + "s go here";
    unitOut.placeholder = unit.dataset.equivalent + "s go here";
    unitInLabel.innerHTML = unit.dataset.si + "s"
    unitOutLabel.innerHTML = unit.dataset.equivalent + "s"
}

function convertUnitsIn(){
    unitOut.value = unitIn.value * unit.dataset.ratio
}

function convertUnitsOut(){
    unitIn.value = unitIn.value * unit.dataset.ratio
}

setConvertors();
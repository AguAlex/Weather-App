document.addEventListener("DOMContentLoaded", function () {
    const switchBtn = document.getElementById("unitSwitch");
    const tempValue = document.getElementById("temp-value");
    const tempUnit = document.getElementById("temp-unit");
    const capitalTemps = document.querySelectorAll(".capital-temp");

    function convertTemp(temp, toFahrenheit) {
        return toFahrenheit ? (temp * 9/5) + 32 : (temp - 32) * 5/9;
    }

    switchBtn.addEventListener("change", function () {
        let toFahrenheit = switchBtn.checked;
        
        let mainTemp = parseFloat(tempValue.innerText);
        if (!isNaN(mainTemp)) {
            tempValue.innerText = convertTemp(mainTemp, toFahrenheit).toFixed(1);
        }

        capitalTemps.forEach(tempElement => {
            let temp = parseFloat(tempElement.innerText);
            if (!isNaN(temp)) {
                tempElement.innerText = convertTemp(temp, toFahrenheit).toFixed(1); // One decimal
            }
        });

        document.querySelectorAll(".temp-unit").forEach(unit => {
            unit.innerText = toFahrenheit ? "°F" : "°C";
        });

        // Change Unit
        tempUnit.innerText = toFahrenheit ? "°F" : "°C";
    });
});

document.addEventListener("DOMContentLoaded", function () {

    // Select all cells containing percentage changes
    const cells = document.querySelectorAll('td:nth-child(4), td:nth-child(5), td:nth-child(6)');

    // Loop through the cells and format them accordingly
    cells.forEach(cell => {
        const value = parseFloat(cell.textContent);

        // If the value is negative, remove the negative sign and color it red
        if (value < 0) {
            cell.style.color = 'red';
            cell.textContent = `${-value}%`;
        }
        // If the value is positive, color it green
        else if (value > 0) {
            cell.style.color = 'green';
            cell.textContent = `${value}%`;
        }
        // If the value is zero, color it gray
        else {
            cell.style.color = 'gray';
            cell.textContent = '0%';
        }
    });



    const results = document.querySelector(".results")
    const amount = document.querySelector("#amount")
    const price = document.querySelector("#coinPrice")
    const message = document.querySelector("#tmessage")
    amount.addEventListener("input", (event) => {
        if (event.target.value >= 0) {
            results.style.display = "inline"
            message.style.display = "none"
            results.innerHTML = (event.target.value) * price.innerHTML


        } else if (event.target.value < 0) {
            results.style.display = "none"
            message.style.display = "block"
            message.innerHTML = "Please Enter a Positive Amount"
            message.style.color = "red"
        }

    })

})
document.addEventListener("DOMContentLoaded", function () {

    // Select all cells containing percentage changes
    const cells = document.querySelectorAll('td:nth-child(4), td:nth-child(5), td:nth-child(6)');

    // Define the arrow characters
    const upArrow = '\u2B9d'; // ↑
    const downArrow = '\u2B9f'; // ↓

    // Loop through the cells and format them accordingly
    cells.forEach(cell => {
        const value = parseFloat(cell.textContent);

        // If the value is negative, remove the negative sign and color it red
        if (value < 0) {
            cell.style.color = 'red';
            cell.textContent = `${-value}% ${downArrow}`;
        }
        // If the value is positive, color it green
        else if (value > 0) {
            cell.style.color = 'green';
            cell.textContent = `${value}% ${upArrow}`;
        }
        // If the value is zero, color it gray
        else {
            cell.style.color = 'gray';
            cell.textContent = `0%`;
        }

        // Add the arrow character to the cell's content
        // cell.style.position = 'relative';
        // cell.style.paddingRight = '10px'; // Adjust the padding to make space for the arrow
        // const arrow = document.createElement('span');
        // arrow.style.position = 'absolute';
        // arrow.style.top = '50%';
        // arrow.style.transform = 'translateY(-50%)';
        // arrow.style.right = '0';
        // arrow.style.fontSize = '0.8em'; // Adjust the font size of the arrow
        // arrow.textContent = value < 0 ? downArrow : upArrow;
        // cell.appendChild(arrow);
    });

    const prices = document.querySelectorAll('td:nth-child(3)');
    prices.forEach(price => {
        const content = price.textContent
        const priceN = Number(content.replace('$', ''));

        if (priceN > 1) {

            const formattedNumber = priceN.toLocaleString('en-US', { maximumFractionDigits: 2 });
            price.textContent = '$' + formattedNumber

        } if (priceN < 1) {
            let update = ''
            for (let i = 0; i < content.length; i++) {
                update += content[i]
                if (content[i] != '0' || content[i] != '$' || content[i] != '.') {
                    n = 4
                    while (n != 0) {

                    }


                }
            }


        }



    })

    //////////////
    // Select all cells containing percentage changes
    // const cells = document.querySelectorAll('td:nth-child(4), td:nth-child(5), td:nth-child(6)');

    // // Loop through the cells and format them accordingly
    // cells.forEach(cell => {
    //     const value = parseFloat(cell.textContent);

    //     // If the value is negative, remove the negative sign and color it red
    //     if (value < 0) {
    //         cell.style.color = 'red';
    //         cell.textContent = `${-value}%`;
    //     }
    //     // If the value is positive, color it green
    //     else if (value > 0) {
    //         cell.style.color = 'green';
    //         cell.textContent = `${value}%`;
    //     }
    //     // If the value is zero, color it gray
    //     else {
    //         cell.style.color = 'gray';
    //         cell.textContent = '0%';
    //     }
    // });



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
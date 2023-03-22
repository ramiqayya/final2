document.addEventListener("DOMContentLoaded", function () {

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
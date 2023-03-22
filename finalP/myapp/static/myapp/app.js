document.addEventListener("DOMContentLoaded", function () {

    const results = document.querySelector(".results")
    const amount = document.querySelector("#amount")
    const price = document.querySelector("#coinPrice")
    amount.addEventListener("input", (event) => {
        results.innerHTML = (event.target.value) * price.innerHTML
    })
})
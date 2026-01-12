function predict() {
    const value = document.getElementById("combined").value;

    if (value === "") {
        alert("Please enter a value");
        return;
    }

    fetch("https://breast-cancer-ml-app-1-h09v.onrender.com/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            combined: parseFloat(value)
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("output").innerText =
            "Prediction: " + data.result;
    })
    .catch(error => {
        console.error(error);
        alert("Backend not running");
    });
}

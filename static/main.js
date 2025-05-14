const form = document.getElementById("uploadform");

form.addEventListener("submit", async (e) => {
    e.preventDefault();
    try {
    const expression = document.getElementById("expression").value;
    if (!expression.trim()) {
        alert("Please enter an expression.");
        return;
    }
    console.log(expression.value)
    const response = await fetch("/plot", {
        method:"POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ expression })
    });
    if (!response.ok) {
        alert("Error fetching server.");
        return;
    }
    const img = document.getElementById("graph");
    img.style.display = "block";
    img.src = "/getimg";
    const downloadLink = document.getElementById("downloadbutton");
    downloadLink.download = "graph.png";
    downloadLink.href = "/getimg";
    downloadLink.parentElement.style.display = "inline-block";
    } catch (ex) {
        alert("An error has occured!");
        console.error("Error details: " + ex);
    }
});

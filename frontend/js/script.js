async function search() {
    const city = document.getElementById("search-input").value.trim();
    if (!city) return;

    try {
        const res  = await fetch(`/search?city=${city}`);
        const data = await res.json();

        if (data.error) {
            document.getElementById("error").textContent = "⚠ " + data.error;
            return;
        }

        renderWeather(data);
    } catch (e) {
        document.getElementById("error").textContent = "⚠ Something went wrong";
    }
}

function renderWeather(data) {
    document.getElementById("error").textContent   = "";
    document.getElementById("city").textContent    = data.city;
    document.getElementById("temp").textContent    = data.temp + "°C";
    document.getElementById("desc").textContent    = data.description;
    document.getElementById("wind").textContent    = "💨 " + data.wind + " m/s";
    document.getElementById("humidity").textContent = "💧 " + data.humidity + "%";
    document.getElementById("icon").src =
        `https://openweathermap.org/img/wn/${data.icon}@2x.png`;
}

document.getElementById("search-input").addEventListener("keydown", e => {
    if (e.key === "Enter") search();
});

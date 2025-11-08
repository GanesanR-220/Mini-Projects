document.getElementById('searchBtn').addEventListener('click', () => {
  const city = document.getElementById('cityInput').value.trim();
  if (!city) {
    alert("Please enter a city name!");
    return;
  }

  fetch('/get_weather', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ city })
  })
  .then(res => res.json())
  .then(data => {
    const resultDiv = document.getElementById('result');
    if (data.error) {
      resultDiv.innerHTML = `<p style="color:red;">${data.error}</p>`;
    } else {
      resultDiv.innerHTML = `
        <h3>${data.city}</h3>
        <p>🌡 Temperature: ${data.temperature}°C</p>
        <p>💧 Humidity: ${data.humidity}%</p>
        <p>🌥 Condition: ${data.description}</p>
      `;
    }
  })
  .catch(err => console.error(err));
});

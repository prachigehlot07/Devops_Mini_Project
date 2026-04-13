function checkStatus() {
  const status = document.getElementById("status");

  const time = new Date().toLocaleTimeString();

  status.innerText = `Server is running fine ✅ | Last checked at ${time}`;
}

// auto run once on load
checkStatus();
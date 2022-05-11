function hideButton() {
  document.querySelector(".start-button-row").style.visibility = "hidden";
}

function startTimer() {
  var time = 0,
    secs = 0,
    mins = 0;

  var timeCounter = setInterval(function () {
    time += 1;
    secs = Math.floor(time % 60);
    mins = Math.floor(time / 60);
    document.querySelector(".timer").innerHTML = mins + ":" + secs;
    if (time > 5) {
      clearInterval(timeCounter);
      document.querySelector(".timer").innerHTML = "Time exceeded!";
    }
  }, 1000);
}

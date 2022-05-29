//Initialise and assign variables
var equationArr = []
var target;
var numbers;
var operators;
var slotnumbers;
var tileleft;
var operatorsDict;
var quizId;
var puzzleCompleted = false;

var time = 0,
  secs = 0,
  mins = 0;
timeTaken = 0;


// Update view based on whether user has completed today's puzzle
$(document).ready(checkPlayed());

function checkPlayed() {
  $.ajax({
    async: false,
    url: "/played",
    success: function (data) {
      played = data.played
      if (played) {
        console.log(played)
        showSolvedView();
      }
    }
  });
}

//Game--------------------------------------------------------------------------

function startGame() {
  $.ajax({
    async: false,
    url: "/equation",
    success: function (data) {
      equationArr = data.equation
      quizId = data.quiz_id
    }
  });
  initializeEquation();
  hideButton();
  startTimer();
  updateGameview();
}


function initializeEquation() {
  target = equationArr[8]
  numbers = equationArr.slice(0, 2).concat(equationArr.slice(3, 5), equationArr.slice(6, 8))
  operators = [equationArr[2], equationArr[5]]
  slotnumbers = [0, 0, 0, 0, 0, 0]
  tileleft = 6;
  operatorsDict = { '+': '&plus;', "-": "&minus;", "*": "&times;", "/": "&divide;" };

}

function hideButton() {
  $(".start-button-container").css("display", "none")
  $(".game-board").css("display", "block")
}

function toMinSec(time) {
  let secs
  let mins
  secs = Math.floor(time % 60);
  mins = Math.floor(time / 60);
  return (mins + ":" + secs)
}

function startTimer() {
  var timeCounter = setInterval(function () {
    time++;

    $(".timer").html(toMinSec(time));
    if (time > 600) {
      clearInterval(timeCounter);
      timesUp()
    }
    if (puzzleCompleted) {
      clearInterval(timeCounter)
      time = 0;
      secs = 0;
      mins = 0;
      $(".timer").html(mins + ":" + secs)
    }
  }, 1000);
}

function timesUp() {
  puzzleCompleted = true;
  $("#first-line").html("Time's Up!")
  $("#second-line").html("Puzzle Not Solved")
  $("#achieved-plant").attr("src", "./static/images/sad_face.png");
  $("#time-taken").remove();
  $("#achieved-text").html("Come back again tomorrow!");
  $("#congrazModal").modal('show');
  showSolvedView();
  postResult(false)
}

//Update User View---------------------------------------------------------------

function updateGameview() {
  //Shuffle numbers array
  numbers.sort(() => Math.random() - 0.5)

  //Update operator, target number and, tile numbers on user view. Add ids and datas to number-tiles and slots
  $("#operator1").html(operatorsDict[operators[0]])
  $("#operator2").html(operatorsDict[operators[1]])

  $("#target-number").html(target)

  $(".number-tile").each(function (i) {
    $(this).attr('id', 'number-tile' + i).data("index", i).data("number", numbers[i]).html(numbers[i])
  })

  $(".slot").each(function (i) {
    $(this).attr('id', 'slot' + i).data('index', i).data('store', -1)
  })
}

//Implement Drag and Drop------------------------------------------------

//Make number-tiles draggable
$(".number-tile").draggable({ stack: ".number-tile", revert: revertBack });

function revertBack(event, ui) {
  $(this).data("draggable").originalPosition = { top: 0, left: 0 };
  return !event;
}

//Make slots droppable
$(".slot").droppable({ drop: handleCardDrop, out: handleOut });

function handleCardDrop(event, ui) {
  let slotIndex = $(this).data('index');
  let numTileIndex = ui.draggable.data('index');

  // If blank tile is storing a number tile, revert the number tile back to original position
  let storedTileIndex = $(this).data('store')
  if (storedTileIndex != -1) {
    $("#number-tile" + storedTileIndex).css({ top: 0, left: 0 })
    tileleft++
  }
  // Put the dragged number tile onto the black tile and do calculation
  ui.draggable.position({ of: $(this), my: 'left top', at: 'left top' });
  $(this).data('store', numTileIndex)

  slotnumbers[slotIndex] = ui.draggable.data('number')
  tileleft--
  let total = calculate()

  // Check if puzzle is solved
  if (tileleft == 0 && total == target) puzzleSolved()
}

function handleOut(event, ui) {
  let storedTileIndex = $(this).data('store')
  let draggedTileIndex = ui.draggable.data('index')
  if (storedTileIndex == draggedTileIndex) {
    let slotIndex = $(this).data('index')
    $(this).data('store', -1)
    slotnumbers[slotIndex] = 0
    calculate()
    tileleft++
  }
}

// Calculate current total-----------------------------

function calculate() {
  let equation = [...slotnumbers]
  equation.splice(2, 0, operators[0])
  equation.splice(5, 0, operators[1])
  let total = parseInt(eval(equation.join("")))
  isNaN(total) ? $(".total").html("Invalid") : $(".total").html(total)
  return (total)
}


// If puzzle is solved, update puzzleCompleted variable to true
// and show congratz modal-----------------------------------------------

function puzzleSolved() {
  timeTaken = time
  puzzleCompleted = true;
  // localStorage.setItem('alrplayed', 'played');
  let playedToday = new Date();
  localStorage.setItem('timeStamp', playedToday);
  $("#time-taken").html(toMinSec(timeTaken))
  if (timeTaken < 30) {
    $("#achieved-plant").attr("src", "./static/images/big_tree.png");
    $("#achieved-text").html("x1 big tree added to achievements");
  }
  else if (timeTaken < 60) {
    $("#achieved-plant").attr("src", "./static/images/tree.png");
    $("#achieved-text").html("x1 tree added to achievements");
  }
  else if (timeTaken < 90) {
    $("#achieved-plant").attr("src", "./static/images/plant.png");
    $("#achieved-text").html("x1 plant added to achievements");
  }
  else if (timeTaken < 120) {
    $("#achieved-plant").attr("src", "./static/images/small_plant.png");
    $("#achieved-text").html("x1 small plant added to achievements");
  }
  else {
    $("#achieved-plant").attr("src", "./static/images/seed.png");
    $("#achieved-text").html("x1 seed added to achievements");
  }

  $("#congrazModal").modal('show');
  showSolvedView()
  postResult(true)
};

function showSolvedView() {
  $("#target-number").html("-")
  $(".start-button").addClass("disabled")
  $(".start-button-row").append("<p>Thank you for playing !</p>");
  $(".start-button-row").append("<p>Next Puzzle Available Tomorrow :)</p>");
  $(".start-button-container").css("display", "flex");
  $(".game-board").css("display", "none");
};

//Send result to server
function postResult(solved) {
  console.log(solved)
  let mydata = {}
  mydata['quizId'] = quizId;
  mydata['duration'] = timeTaken;
  mydata['success'] = solved;

  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    console.log(this.responseText)
  }
  xhttp.open('POST', '/statistic', true);
  xhttp.setRequestHeader('Content-Type', 'application/json');
  xhttp.send(JSON.stringify(mydata));
}


// Get Statistic
function getStat() {
  let winnerPercent
  $.ajax({
    async: true,
    url: "/statistic",
    success: function (data) {
      let players = data.players
      let winners = data.winners
      let shortestTime = data.shortestTime
      let played = data.played
      let win = data.win
      let streak = data.current_streak
      let maxStreak = data.max_streak
      let bigTree = data.big_tree
      let tree = data.tree
      let plant = data.plant
      let small_plant = data.small_plant
      let seed = data.seed

      console.log(players, winners, shortestTime, played, win, streak, maxStreak, bigTree, tree, plant, small_plant, seed)

      if (winners == 0) {
        winnerPercent = "0"
        shortestTime = "-"
        $("#shortestTime").html(shortestTime)
      }
      else {
        winnerPercent = parseInt(Math.round(winners / players * 100))
        shortestTime = parseInt(data.shortestTime)
        $("#shortestTime").html(toMinSec(shortestTime))
      }

      $("#winnerPercentage").html(winnerPercent)

      treeDisplay(bigTree, tree, plant, small_plant, seed)
      statsDisplay(played, win, streak, maxStreak)
    }
  });
}


//Display of tree inventory-------------------------------------------------

function treeDisplay(bigtreeNum, treeNum, plantNum, smallplantNum, seedNum) {
  $('#bigtreeNum').html('&times' + bigtreeNum);
  $('#treeNum').html('&times' + treeNum);
  $('#plantNum').html('&times' + plantNum);
  $('#smallplantNum').html('&times' + smallplantNum);
  $('#seedNum').html('&times' + seedNum);
};

function winCalc(winTimes, playedTimes) {
  if (playedTimes == 0) {
    winPercent = 0;
  }
  else {
    winPercent = Math.round(winTimes / playedTimes * 100);
  }
  return winPercent
};

//Display of user's statistics
function statsDisplay(playedTimes, winTimes, currentStreak, bestStreak) {
  let winPercent = winCalc(winTimes, playedTimes);
  $('#playedtimes').html(playedTimes);
  $('#wintimes').html(winPercent + '%');
  $('#currentstreak').html(currentStreak);
  $('#beststreak').html(bestStreak);
};


//Sharing message -----------------------------------------------------------------
const startDate = new Date("27 May 2022");

//get the game number
const getGameNum = () => {
  const timeDiff = new Date().getTime() - startDate.getTime();
  return Math.floor(Math.abs(timeDiff / (1000 * 3600 * 24))) + 1;
}

//show message
function popUpMsg() {
  var popup = document.getElementById('myPopUp');
  popup.classList.toggle('show');
  $('#myPopUp').html('Copied results to clipboard!');
};

function popUpMsgStats() {
  var popupStats = document.getElementById('myPopUpStats');
  popupStats.classList.toggle('show');
  $('#myPopUpStats').html('Copied results to clipboard!');
};


//copy message to clipboard
sharingButton = document.getElementById('sharing');
shareStatsButton = document.getElementById('shareStats');

sharingButton.addEventListener('click', async () => {
  let bigtreeNum, treeNum, plantNum, smallplantNum, seedNum
  $.ajax({
    async: false,
    url: "/statistic",
    success: function (data) {
      bigtreeNum = data.big_tree
      treeNum = data.tree
      plantNum = data.plant
      smallplantNum = data.small_plant
      seedNum = data.seed
    }
  });

  result = 'Numberloo #' + getGameNum() + ' solved in ' + toMinSec(timeTaken) + ' 🔥';
  bigTreeEmoji = '🌳';
  treeEmoji = '🌴';
  plantEmoji = '🪴';
  smallPlantEmoji = '🍀';
  seedEmoji = '🌱';
  result += '\r\n' + bigTreeEmoji.repeat(bigtreeNum) +
    treeEmoji.repeat(treeNum) + plantEmoji.repeat(plantNum) +
    smallPlantEmoji.repeat(smallplantNum) + seedEmoji.repeat(seedNum);
  await navigator.clipboard.writeText(result);
});


//Countdown til next game-------------------------------------------

function midnightCountDown() {
  var today = new Date();
  var tmr = new Date();
  tmr.setDate(tmr.getDate() + 1);
  tmr.setHours(0, 0, 0, 0);
  const sec = 1000;
  const minute = sec * 60;
  const hr = minute * 60;

  remainingTime = tmr.getTime() - today.getTime();
  hrsLeft = Math.trunc(remainingTime / hr);
  minsLeft = Math.trunc((remainingTime % hr) / minute);
  secsLeft = Math.trunc((remainingTime % minute) / sec);

  if (localStorage.getItem('alrplayed') == 'played') {
    $('#midnight').html(hrsLeft + ':' + minsLeft + ':' + secsLeft);
    $('#nextLoo').html('Numberloo #' + (getGameNum() + 1) + ' begins in');
  }
  else {
    $('#nextLoo').html("So you still haven't solved")
    $('#midnight').html('Numberloo #' + getGameNum())
  }
};

setInterval(midnightCountDown, 1000);

//Copy Clipboard API
shareStatsButton.addEventListener('click', async () => {
  let bigtreeNum, treeNum, plantNum, smallplantNum, seedNum
  $.ajax({
    async: false,
    url: "/statistic",
    success: function (data) {
      bigtreeNum = data.big_tree
      treeNum = data.tree
      plantNum = data.plant
      smallplantNum = data.small_plant
      seedNum = data.seed
    }
  });

  var value = "Look at my Numberloo progress!";
  bigTreeEmoji = '🌳';
  treeEmoji = '🌴';
  plantEmoji = '🪴';
  smallPlantEmoji = '🍀';
  seedEmoji = '🌱';
  value += '\r\n' + bigTreeEmoji + 'x' + bigtreeNum + ' ' +
    treeEmoji + 'x' + treeNum + ' ' + plantEmoji + 'x' + plantNum + ' ' +
    smallPlantEmoji + 'x' + smallplantNum + ' ' + seedEmoji + 'x' + seedNum;
  await navigator.clipboard.writeText(value);

});


// Make drag and drop work on mobile-----------------------------------------------

function touchHandler(event) {
  var touch = event.changedTouches[0];

  var simulatedEvent = document.createEvent("MouseEvent");
  simulatedEvent.initMouseEvent({
    touchstart: "mousedown",
    touchmove: "mousemove",
    touchend: "mouseup"
  }[event.type], true, true, window, 1,
    touch.screenX, touch.screenY,
    touch.clientX, touch.clientY, false,
    false, false, false, 0, null);

  touch.target.dispatchEvent(simulatedEvent);
}

function init() {
  document.addEventListener("touchstart", touchHandler, true);
  document.addEventListener("touchmove", touchHandler, true);
  document.addEventListener("touchend", touchHandler, true);
  document.addEventListener("touchcancel", touchHandler, true);
}

init()
getStat()
function hideButton() {
  document.querySelector(".start-button-row").style.display = "none";
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


//Update User View------------------------------------------------

//Equation data from backend
var equationArr = [3,2,"-",0,9,"+",4,5,68]

//Initialise and assign variables
var target = equationArr[8]
var numbers = equationArr.slice(0,2).concat(equationArr.slice(3,5),equationArr.slice(6,8))
var operators = [equationArr[2], equationArr[5]]
var slotnumbers = [0,0,0,0,0,0]

//Shuffle numbers array
numbers.sort(() => Math.random() - 0.5)

//Update operator, target number and, tile numbers on user view. Add ids and datas to number-tiles and slots
var operatorsDict = {'+':'&plus;',"-":"&minus;","*":"&times;","/":"&divide;"}
$("#operator1").html(operatorsDict[operators[0]])
$("#operator2").html(operatorsDict[operators[1]])

$("#target-number").html(target)

$(".number-tile").each(function (i) {
  $(this).attr('id', 'number-tile' + i).data("index", i).data("number",numbers[i]).html(numbers[i])
})

$(".slot").each(function (i) {
  $(this).attr('id', 'slot' + i).data('index', i).data('store', -1)
})


//Implement Drag and Drop------------------------------------------------

//Make number-tiles draggable
$(".number-tile").draggable({ stack: ".number-tile", revert: revertBack });

function revertBack(event, ui) {
  $(this).data("draggable").originalPosition = {top: 0,left: 0};
  return !event;
}

//Make slots droppable
$(".slot").droppable({ drop: handleCardDrop, out:handleOut });

function handleCardDrop(event, ui) {
  let slotIndex = $(this).data('index');
  let numTileIndex = ui.draggable.data('index');

  // If blank tile is storing a number tile, revert the number tile back to original position
  let storedTileIndex = $(this).data('store')
  if (storedTileIndex != -1) {
    $("#number-tile" + storedTileIndex).css({ top: 0, left: 0 })
  }
  // Put the dragged number tile onto the black tile and do calculation
  ui.draggable.position({of: $(this), my: 'left top', at: 'left top'});
  $(this).data('store', numTileIndex)

  slotnumbers[slotIndex] = ui.draggable.data('number')
  calculate()
}

function handleOut(event, ui){
  let storedTileIndex = $(this).data('store')
  let draggedTileIndex = ui.draggable.data('index')
  if(storedTileIndex == draggedTileIndex){
    let slotIndex = $(this).data('index')
    $(this).data('store', -1)
    slotnumbers[slotIndex] = 0
    calculate()
  }
}


// Calculate current total-----------------------------

function calculate(){
  let equation = [...slotnumbers]
  equation.splice(2, 0, operators[0])
  equation.splice(5, 0, operators[1])
  let total = parseInt(eval(equation.join("")))
  isNaN(total) ? $(".total").html("Invalid") : $(".total").html(total)
}


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

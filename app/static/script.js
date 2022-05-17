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

//Implement Drag and Drop------------------------------------------------

var numbers = [2,3,4,5,6,7]
var slotnumbers = [0,0,0,0,0,0]
var operators = ['-','*']

//Add ids and datas to number-tiles and slots
$(".number-tile").each(function (i) {
  $(this).attr('id', 'number-tile' + i).data("index", i).data("number",numbers[i]).html(numbers[i])
})

$(".slot").each(function (i) {
  $(this).attr('id', 'slot' + i).data('index', i).data('store', -1)
})

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
  var storedTileIndex = $(this).data('store')
  if (storedTileIndex != -1) {
    console.log(storedTileIndex);
    $("#number-tile" + storedTileIndex).css({ top: 0, left: 0 })
  }
  // Put the dragged number tile onto the black tile and do calculation
  ui.draggable.position({of: $(this), my: 'left top', at: 'left top'});
  $(this).data('store', numTileIndex)

  slotnumbers[slotIndex] = ui.draggable.data('number')
  calculate()
}

function handleOut(){
  let slotIndex = $(this).data('index')
  $(this).data('store', -1)
  console.log($(this).data('store'))
  slotnumbers[slotIndex] = 0
  calculate()
}

// Calculate current total-----------------------------
function calculate(){
  let firstTerm = parseInt(''+slotnumbers[0]+slotnumbers[1])
  let secondTerm = parseInt(''+slotnumbers[2]+slotnumbers[3])
  let thirdTerm = parseInt(''+slotnumbers[4]+slotnumbers[5])
  let subtotal = subcalculate(firstTerm,secondTerm,operators[0])
  let total = subcalculate(subtotal,thirdTerm,operators[0])
  $(".total").html(total)
}

function subcalculate(term1,term2,operator){
if(operator == '+') return term1+term2;
else if (operator == '-') return term1-term2;
else if (operator == '*') return term1*term2;
else return term1/term2;
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

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

//Pop Up For Settings Button
const openModalButtons = document.querySelectorAll('[data-modal-target]');
const closeModalButtons = document.querySelectorAll('[data-close-button]');
const overlay = document.getElementById('overlay');

openModalButtons.forEach(button => {
  console.log(button)
  button.addEventListener('click', () => {
    const modal = document.querySelector(button.dataset.modalTarget);
    openModal(modal)
});
});


overlay.addEventListener('click', () => {
  const modals = document.querySelectorAll('.modal.active');
  modals.forEach(modal => {
      closeModal(modal);
});
});

closeModalButtons.forEach(button => {
button.addEventListener('click', () => {
    const modal = button.closest('.modal');
    closeModal(modal);
});
});

function openModal(modal) {
  if (modal == null) return
  modal.classList.add('active');
  overlay.classList.add('active');
};

function closeModal(modal) {
  if (modal == null) return
  modal.classList.remove('active');
  overlay.classList.remove('active');
};
const $btnOn = document.getElementById('on');
const $btnOff = document.getElementById('off');
async function handlerClickOn() {
  const response = await fetch('/api/p');
  const result = await response.json();
  console.log(result);
}

async function handlerClickOff() {
  const response = await fetch('/api/n');
  const result = await response.json();
  console.log(result);
}

$btnOn.addEventListener('click', () => handlerClickOn());
$btnOff.addEventListener('click', () => handlerClickOff());

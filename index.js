// Assign an element to each catButton, add an event listener to trigger upon clikcing the button
const catButton = document.getElementById("cat");
catButton.addEventListener("click", catagorize);

const sumButton = document.getElementById("sum")
sumButton.addEventListener("click", summerize);

// Temporary functions
function catagorize() {
  alert("Email's catagorized!");
}
function summerize() {
  alert("Email's summerized!")
}

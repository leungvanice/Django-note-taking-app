headings = document.querySelectorAll("h1, h2, h3, h4, h5, h6");
// console.log(headings);
let numcall = 0;
let results = [];
// to remove the title of note
headings.forEach(element => {
  //   console.log(element);
  if (numcall >= 1) {
    results.push(element);
  }
  numcall++;
});
// Create id for the headings so can navigate easily
let count = 1;
for (i of results) {
  i.id = "No" + count;
  count++;
}

// set outline
let outlineList = document.querySelector(".sidebar-list-outline");
results.forEach(function(value, counter) {
  let toSpaceCount = value.tagName[1];
  let newDiv = document.createElement("div");
  newDiv.className = "sidebar-link-container";
  let newLink = document.createElement("a");
  newLink.href = "#" + "No" + counter;
  newLink.innerHTML = value.innerHTML;
  let classOfNewLink = `h${toSpaceCount}Link`;
  newLink.className = classOfNewLink;
  newDiv.appendChild(newLink);
  outlineList.appendChild(newDiv);
});

function createElement(value) {}

let files = document.querySelector(".sidebar-list-file");
let outline = document.querySelector(".sidebar-list-outline");
files.style.display = "block";
outline.style.display = "none";
function btnOnClick() {
  //   console.log(files.style.getPropertyValue("display"));
  if (files.style.display === "block") {
    files.style.display = "none";
    outline.style.display = "block";
  } else if (outline.style.display === "block") {
    files.style.display = "block";
    outline.style.display = "none";
  }
}

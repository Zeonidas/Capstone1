// Future Functionality

[...document.querySelectorAll("#questionList select")].map((o) =>
  o.addEventListener("change", (e) => console.log(e.target.value))
);

// function getNumber(e) {

//   [...document.querySelectorAll("#questionList select")].map((o) => o.addEventListener("change", (e) => console.log(e.target.value)))
// }

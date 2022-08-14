// Define the array
let arrOfScore = [];

// Use a spread operator to gather elements from the 'ol'
[...document.querySelectorAll("#questionList select")].map((o) =>
  o.addEventListener("change", (e) => {
    // Collect target value numbers
    arrOfScore.push(Number(e.target.value));

    // Creating a sum of the array
    const iniNum = 0;
    const sumOfArr = arrOfScore.reduce(
      (previousValue, currentValue) => previousValue + currentValue,
      iniNum
    );

    // Display sum to HTML
    const submitBtn = document.getElementById("submitBtn");
    submitBtn.addEventListener("click", function () {
      if (arrOfScore.length <= 15) {
        document.getElementById("phqResult").innerHTML = sumOfArr;
      } else {
        alert(
          "You have selected too many or too little options. Refresh and try again."
        );
        arrOfScore = [];
        location.reload();
      }
    });
  })
);

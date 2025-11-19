document.addEventListener('DOMContentLoaded', () => {
  console.log("Restaurant website loaded!");
});


  function filterMenu() {
    let input = document.getElementById("menuSearch").value.toLowerCase();
    let cards = document.querySelectorAll("#menuItems .col-md-4");
    let noResults = document.getElementById("noResults");

    let visibleCount = 0;

    cards.forEach(card => {
      let title = card.querySelector(".card-title").textContent.toLowerCase();
      if (title.includes(input)) {
        card.style.display = "block";
        visibleCount++;
      } else {
        card.style.display = "none";
      }
    });

    // Show or hide "No results" message
    noResults.style.display = visibleCount === 0 ? "block" : "none";
  }


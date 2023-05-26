// Pagination
const table = document.querySelector('table');
const rowsPerPage = 5; // Number of rows to show per page
let currentPage = 1;
const rows = Array.from(table.querySelectorAll('tbody tr'));
const pageSpan = document.querySelector('.page-number');

// Function to display rows for the current page
function displayRows() {
  const start = (currentPage - 1) * rowsPerPage;
  const end = start + rowsPerPage;

  rows.forEach((row, index) => {
    if (index >= start && index < end) {
      row.style.display = 'table-row';
    } else {
      row.style.display = 'none';
    }
  });

  updatePageNumber();
}

// Function to update pagination buttons
function updatePaginationButtons() {
  const prevBtn = document.querySelector('.prev-btn');
  const nextBtn = document.querySelector('.next-btn');

  prevBtn.disabled = currentPage === 1;
  nextBtn.disabled = currentPage === Math.ceil(rows.length / rowsPerPage);
}

// Function to update page number
function updatePageNumber() {
  pageSpan.textContent = `Page ${currentPage} of ${Math.ceil(rows.length / rowsPerPage)}`;
}

// Function to go to the previous page
function goToPreviousPage() {
  if (currentPage > 1) {
    currentPage--;
    displayRows();
    updatePaginationButtons();
  }
}

// Function to go to the next page
function goToNextPage() {
  if (currentPage < Math.ceil(rows.length / rowsPerPage)) {
    currentPage++;
    displayRows();
    updatePaginationButtons();
  }
}

// Attach event listeners to pagination buttons
document.querySelector('.prev-btn').addEventListener('click', goToPreviousPage);
document.querySelector('.next-btn').addEventListener('click', goToNextPage);

// Initial setup
displayRows();
updatePaginationButtons();
        
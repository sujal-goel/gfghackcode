document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const searchTermSpan = document.getElementById('searchTerm');
    const searchImageDiv = document.getElementById('searchImageDiv');

    searchInput.addEventListener('input', function() {
        const searchTerm = this.value.trim();
        searchTermSpan.textContent = searchTerm ? searchTerm : 'all';
        // Call a function to fetch and display search results based on the searchTerm
         displaySearchResults(searchTerm);
    });

    

    function displaySearchResults(searchTerm) {
        // Here you can fetch search results from an API or a data source
        // For demonstration purposes, let's create some dummy results
        const dummyResults = [
            'https://via.placeholder.com/200',
            'https://via.placeholder.com/200',
            'https://via.placeholder.com/200',
            'https://via.placeholder.com/200',
            'https://via.placeholder.com/200',
            'https://via.placeholder.com/200',
            'https://via.placeholder.com/200',
            'https://via.placeholder.com/200',
            'https://via.placeholder.com/200',
            'https://via.placeholder.com/200',
            'https://via.placeholder.com/200',
            'https://via.placeholder.com/200',
        ];

        // Clear previous search results
        searchImageDiv.innerHTML = '';

        // Display search results
        dummyResults.forEach(result => {
            const imageDiv = document.createElement('div');
            imageDiv.classList.add('image');

            const image = document.createElement('img');
            image.src = result;
            image.alt = 'Search Result Image';
            imageDiv.appendChild(image);

            searchImageDiv.appendChild(imageDiv);
        });
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');

    searchInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            // Execute your code here that should run when the Enter key is pressed
            const searchTerm = this.value.trim();
            // For example, you can trigger a search function
            searchForTerm(searchTerm);
        }
    });

    function searchForTerm(searchTerm) {
        // Your search logic here
        console.log('Searching for:', searchTerm);
    }
});

function openSideBar(){
 let sideBar = document.querySelector(".sideBar");
 sideBar.style.display = "flex";
 let harmburger = document.querySelector(".hamburger")
 harmburger.style.display="none";
}
function closeSideBar(){
    let sideBar = document.querySelector(".sideBar");
    sideBar.style.display = "none";
    let harmburger = document.querySelector(".hamburger")
    harmburger.style.display="inline";
}

const searchInput = document.querySelector("#searchInput");
searchInput.addEventListener('focus', function() {
    this.value = '';
});

searchInput.addEventListener('blur', function() {
    if (this.value === '') {
        this.value = '';
    }
});

document.addEventListener('click', function(event) {
    if (!event.target.matches('.searchInputImg')) {
        const searchInput = document.getElementById('searchInput');
        searchInput.value = '';
    }
});
function removeClass(activated) {
    if (activated.classList.contains("messages")) {
        setTimeout(() => {
            activated.classList.remove("messages");
        }, 5000);
    }
}
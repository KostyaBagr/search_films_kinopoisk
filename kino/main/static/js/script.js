//function loadMovies(search, page, limit) {
//    fetch(https://api.kinopoisk.dev/v1.2/movie/search?query=${search}&page=${page}&limit=${limit})
//        .then(response => response.json())
//        .then(data => {
//            // обновляем результаты на странице
//        });
//}
//
//$(document).ready(function() {
//    let search = "{{ search }}";
//    let total_pages = "{{ total_pages }}";
//    let limit = "{{ limit }}";
//
//    loadMovies(search, 1, limit);
//
//    $("#pagination").twbsPagination({
//        totalPages: total_pages,
//        visiblePages: 10,
//        onPageClick: function(event, page) {
//            loadMovies(search, page, limit);
//        }
//    });
//});
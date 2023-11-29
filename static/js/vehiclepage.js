document.addEventListener('DOMContentLoaded', function(){
    var sortDropdown = document.getElementById('vehicle-sort-dropdown')

    sortDropdown.addEventListener('change', function(){
        var selectedOption = sortDropdown.options[sortDropdown.selectedIndex].value

        window.location.href = updateQueryStringParameter(window.location.href, 'sort', selectedOption)

    })
    
    function updateQueryStringParameter(uri, key, value) {
        var re = new RegExp("([?&])" + key + "=.*?(&|$)", "i");
        var separator = uri.indexOf('?') !== -1 ? "&" : "?";
        if (uri.match(re)) {
            return uri.replace(re, '$1' + key + "=" + value + '$2');
        }
        else {
            var newUri = uri + separator + key + "=" + value;
            sortDropdown.value = value;
            return newUri;
        }
    }
});
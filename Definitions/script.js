document.addEventListener('DOMContentLoaded', function () {
    const urlParams = new URLSearchParams(window.location.search);
    const flagParam = urlParams.get('flag');

    if (flagParam === 'true') {
        const contentDiv = document.getElementById('content');
        const flagElement = document.createElement('p');
        flagElement.textContent = 'The flag is: lbctf{paramarama}';
        contentDiv.appendChild(flagElement);
    }
});

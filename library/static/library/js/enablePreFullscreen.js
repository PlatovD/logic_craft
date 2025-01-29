document.addEventListener('DOMContentLoaded', () => {
    const preEl = document.querySelector('pre');

    if (preEl) {
        preEl.addEventListener('click', (e) => {
            if (!document.fullscreenElement) {
                preEl.requestFullscreen().catch(e => console.error(e));
            } else {
                document.exitFullscreen();
            }
        })
    }
})
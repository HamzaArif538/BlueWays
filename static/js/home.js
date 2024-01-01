let currentIndex = 0;

const totalSlides = document.querySelectorAll('.home-slide').length

function showSlide(index) {
    const slider = document.querySelector('.home-slider')
    const slideWidth = document.querySelector('.home-slider').offsetWidth
    const newPosition = -index * slideWidth;
    slider.style.transform = `translateX(${newPosition}px)`
}

function nextSlide(){
    currentIndex = (currentIndex + 1) % totalSlides
    showSlide(currentIndex)
}

function autoSlide(){
    nextSlide()
}

setInterval(autoSlide, 5000)

console.log('is it working')
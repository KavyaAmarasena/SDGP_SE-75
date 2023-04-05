const presenterContainer = document.querySelector(".presenter");
const sidePopup = document.querySelector(".sidePopup");

const audioButton = document.getElementById("audioButton");
const videoButton = document.getElementById("videoButton");
// const shareButton = document.getElementById("shareButton");
const messageButton = document.getElementById("messageButton");
const usersButton = document.getElementById("usersButton");

// import { screenShare } from "../../backend/meet.js";

videoButton.addEventListener("click", () => {
  console.log(videoButton.value);

  if (videoButton.value == "OFF") {
    videoButton.value = "ON";
    presenterContainer.classList.add("slideLeft");
    sidePopup.classList.add("side-popup-open");
    sidePopup.classList.add("slideRight");
  } else {
    videoButton.value = "OFF";
    presenterContainer.classList.remove("slideLeft");
    sidePopup.classList.remove("side-popup-open");
    sidePopup.classList.remove("slideRight");
  }
});

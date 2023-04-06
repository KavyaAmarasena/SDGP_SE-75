const APP_ID = "8fa2917a7ca246978d30ff24f541406b";

let uid = sessionStorage.getItem("uid");

let user_type;

let usr_token;

let std_id;
let std_fname;
let std_lname;

let teacher_id;
let teacher_fname;
let teacher_lname;

let displayName;

// gets the details of the user from the backend using a http request
fetch("/get-session")
  .then((response) => response.json())
  .then((data) => {
    user_type = data.user_type;
    user_token = data.token;
    console.log("Hello !");
    console.log(user_type);

    if (user_type == "student") {
      std_id = data.std_id;
      std_fname = data.std_fname;
      std_lname = data.std_lname;

      displayName = `${std_fname} ${std_lname}`;
    } else {
      teacher_id = data.teacher_id;
      teacher_fname = data.teacher_fname;
      teacher_lname = data.teacher_lname;

      displayName = `${teacher_fname} ${teacher_lname} ` + "(lec)";
    }
  });

// checks whether the user logged in is a teacher or a student
console.log(user_type);

if (!uid) {
  uid = String(Math.floor(Math.random() * 10000));
  sessionStorage.setItem("uid", uid);
}

let token = null;
let client;

let rtmClient;
let channel;

const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
let roomId = urlParams.get("room");

if (!roomId) {
  roomId = "main";
}

let localTracks = [];
let remoteUsers = {};

let localScreenTracks;
let sharingScreen = false;

/*
The method joinRoomInit describes the functions that is processed when starting to
join into an online meeting room.
*/
let joinRoomInit = async () => {
  rtmClient = await AgoraRTM.createInstance(APP_ID);
  await rtmClient.login({ uid, token });

  await rtmClient.addOrUpdateLocalUserAttributes({ name: displayName });

  channel = await rtmClient.createChannel(roomId);
  await channel.join();

  channel.on("MemberJoined", handleMemberJoined);
  channel.on("MemberLeft", handleMemberLeft);
  channel.on("ChannelMessage", handleChannelMessage);

  getMembers();
  addBotMessageToDom(`Welcome to the meet ${displayName}`);

  client = AgoraRTC.createClient({ mode: "rtc", codec: "vp8" });
  await client.join(APP_ID, roomId, token, uid);

  client.on("user-published", handleUserPublished);
  client.on("user-left", handleUserLeft);

  joinStream();
};

let joinStream = async () => {
  localTracks = await AgoraRTC.createMicrophoneAndCameraTracks(
    {},
    {
      encoderConfig: {
        width: { min: 640, ideal: 1920, max: 1920 },
        height: { min: 480, ideal: 1080, max: 1080 },
      },
    }
  );

  let player = `<div class="video__container" id="user-container-${uid}">
                    <div class="video-player" id="user-${uid}"></div>
                  </div>`;

  document
    .getElementById("streams__container")
    .insertAdjacentHTML("beforeend", player);

  document
    .getElementById(`user-container-${uid}`)
    .addEventListener("click", expandVideoFrame);

  localTracks[1].play(`user-${uid}`);
  await client.publish([localTracks[0], localTracks[1]]);
};

let switchToCamera = async () => {
  let player = `<div class="video__container" id="user-container-${uid}">
                    <div class="video-player" id="user-${uid}"></div>
                  </div>`;

  displayFrame.insertAdjacentHTML("beforeend", player);

  await localTracks[0].setMuted(true);
  await localTracks[1].setMuted(true);

  document.getElementById("mic-btn").classList.remove("active");
  document.getElementById("screen-btn").classList.remove("active");

  localTracks[1].play(`user-${uid}`);
  await client.publish([localTracks[1]]);
};

let handleUserPublished = async (user, mediaType) => {
  remoteUsers[user.uid] = user;

  await client.subscribe(user, mediaType);

  let player = document.getElementById(`user-container-${user.uid}`);

  if (player === null) {
    player = `<div class="video__container" id="user-container-${user.uid}">
                <div class="video-player" id="user-${user.uid}"></div>
             </div>`;

    document
      .getElementById("streams__container")
      .insertAdjacentHTML("beforeend", player);

    document
      .getElementById(`user-container-${user.uid}`)
      .addEventListener("click", expandVideoFrame);
  }

  if (displayFrame.style.display) {
    let videoFrame = document.getElementById(`user-container-${user.uid}`);
    player.style.height = "100px";
    player.style.width = "100px";
  }

  if (mediaType === "video") {
    user.videoTrack.play(`user-${user.uid}`);
  }

  if (mediaType === "audio") {
    user.audioTrack.play();
  }
};

let handleUserLeft = async (user) => {
  delete remoteUsers[user.uid];
  document.getElementById(`user-container-${user.uid}`).remove();

  if (userIdInDisplayFrame === `user-container-${user.uid}`) {
    displayFrame.style.display = null;

    let videoFrames = document.getElementsByClassName("video__container");

    for (let i = 0; videoFrames.length > i; i++) {
      videoFrames[i].style.height = "300px";
      videoFrames[i].style.width = "300px";
    }
  }
};

// This function allows the user to share mic audio !!!
let toggleMic = async (e) => {
  let button = e.currentTarget;

  if (localTracks[0].muted) {
    let marks_data = {
      marks: 40,
    };

    if (user_type == "student") {
      fetch("/api/update-score", {
        method: "Post",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(marks_data),
      });
    }

    await localTracks[0].setMuted(false);
    button.classList.add("active");
  } else {
    await localTracks[0].setMuted(true);
    button.classList.remove("active");
  }
};

// This function allows the user to share video !!!
let toggleCamera = async (e) => {
  let button = e.currentTarget;

  if (localTracks[1].muted) {
    let marks_data = {
      marks: 40,
    };

    if (user_type == "student") {
      fetch("/api/update-score", {
        method: "Post",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(marks_data),
      });
    }

    await localTracks[1].setMuted(false);
    button.classList.add("active");
  } else {
    await localTracks[1].setMuted(true);
    button.classList.remove("active");
  }
};

// This function allows the user to share the screen !!!
let toggleScreen = async (e) => {
  let screenButton = e.currentTarget;
  let cameraButton = document.getElementById("camera-btn");

  if (!sharingScreen) {
    sharingScreen = true;

    let marks_data = {
      marks: 60,
    };

    if (user_type == "student") {
      fetch("/api/update-score", {
        method: "Post",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(marks_data),
      });
    }

    screenButton.classList.add("active");
    cameraButton.classList.remove("active");
    cameraButton.style.display = "none";

    localScreenTracks = await AgoraRTC.createScreenVideoTrack();

    document.getElementById(`user-container-${uid}`).remove();
    displayFrame.style.display = "block";

    let player = `<div class="video__container" id="user-container-${uid}">
                    <div class="video-player" id="user-${uid}"></div>
                  </div>`;

    displayFrame.insertAdjacentHTML("beforeend", player);
    document
      .getElementById(`user-container-${uid}`)
      .addEventListener("click", expandVideoFrame);

    userIdInDisplayFrame = `user-container-${uid}`;
    localScreenTracks.play(`user-${uid}`);

    await client.unpublish([localTracks[1]]);
    await client.publish([localScreenTracks]);

    let videoFrames = document.getElementsByClassName("video__container");
    for (let i = 0; videoFrames.length > i; i++) {
      if (videoFrames[i].id != userIdInDisplayFrame) {
        videoFrames[i].style.height = "100px";
        videoFrames[i].style.width = "100px";
      }
    }
  } else {
    sharingScreen = false;
    cameraButton.style.display = "block";
    document.getElementById(`user-container-${uid}`).remove();
    await client.unpublish([localScreenTracks]);

    switchToCamera();
  }
};

let leave = async (e) => {
  let button = e.currentTarget;

  if (user_type == "teacher") {
    location.href = "/homepage-teacher";
  } else {
    location.href = "/homepage-student";
  }
};

document.getElementById("camera-btn").addEventListener("click", toggleCamera);
document.getElementById("mic-btn").addEventListener("click", toggleMic);
document.getElementById("screen-btn").addEventListener("click", toggleScreen);
document.getElementById("leave-btn").addEventListener("click", leave);

joinRoomInit();

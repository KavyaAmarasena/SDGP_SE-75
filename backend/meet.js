let APP_ID = "8fa2917a7ca246978d30ff24f541406b";

let token = null;
let uid = String(Math.floor(Math.random() * 1000)); // This is the user id that can be used to uniquely identify the users that joined to the meeting.

let client;
let channel;

let localStream;
let remoteStream;
let peerConnection;

const servers = {
  iceservers: [
    {
      urls: ["stun1.l.google.com:19302", "stun2.l.google.com:19302"],
    },
  ],
};

let init = async () => {
  client = await AgoraRTM.createInstance(APP_ID);
  await client.login({ uid, token });

  channel = client.createChannel("main");
  await channel.join();

  channel.on("MemberJoined", handleUserJoined);

  client.on("MessageFromPeer", handleMessageFromPeer);

  localStream = await navigator.mediaDevices.getUserMedia({
    video: true,
    audio: false,
  });

  document.getElementById("user-1").srcObject = localStream;
};

let handleMessageFromPeer = async (message, MemberId) => {
  console.log("Message: ", message.text);
};

let handleUserJoined = async (MemberId) => {
  console.log(`A new user joined the channel: `, MemberId);
  createOffer(MemberId);
};

let createOffer = async (MemberId) => {
  peerConnection = new RTCPeerConnection(servers);

  remoteStream = new MediaStream();
  document.getElementById("user-2").srcObject = remoteStream;

  localStream.getTracks().forEach((track) => {
    peerConnection.addTrack(track, localStream);
  });

  peerConnection.ontrack = (event) => {
    event.streams[0].getTracks().forEach((track) => {
      remoteStream.addTrack();
    });
  };

  peerConnection.onicecandidate = async (event) => {
    if (event.candidate) {
      console.log("New ICE candidate: ", event.candidate);
    }
  };

  let offer = await peerConnection.createOffer();
  await peerConnection.setLocalDescription(offer);

  client.sendMessageToPeer({ text: "Hey !!!" }, MemberId);
};

init();
// export { screenShare };

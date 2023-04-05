// This function handles the process that should take place when a member is joined to the meet
let handleMemberJoined = async (MemberId) => {
  console.log("New Member has joined the room", MemberId);
  addMemberToDom(MemberId);

  let members = await channel.getMembers();
  updateMemberTotal(members);

  let { name } = await rtmClient.getUserAttributesByKeys(MemberId, ["name"]);

  addBotMessageToDom(`${name} joined the meet`);
};

//This function handles the process of adding the joined member to the participants list.
let addMemberToDom = async (MemberId) => {
  let { name } = await rtmClient.getUserAttributesByKeys(MemberId, ["name"]);

  let membersWrapper = document.getElementById("member__list");
  let memberItem = `<div class="member__wrapper" id="member__${MemberId}__wrapper">
                    <span class="green__icon"></span>
                    <p class="member_name">${name}</p>
                    </div>`;
  membersWrapper.insertAdjacentHTML("beforeend", memberItem);
};

let updateMemberTotal = async (members) => {
  let total = document.getElementById("members__count");
  total.innerText = members.length;
};

let handleMemberLeft = async (MemberId) => {
  removeMemberFromDom(MemberId);

  let members = await channel.getMembers();
  updateMemberTotal(members);
};

let getMembers = async () => {
  let members = await channel.getMembers();

  updateMemberTotal(members);

  for (let i = 0; members.length > i; i++) {
    addMemberToDom(members[i]);
  }
};

let handleChannelMessage = async (messageData, MemberId) => {
  console.log("A new message was received");
  let data = JSON.parse(messageData.text);

  if (data.type === "chat") {
    addMessageToDom(data.displayName, data.message);
  }
};

let sendMessage = async (e) => {
  e.preventDefault();

  let message = e.target.message.value;

  let message_data = {
    message: message,
  };

  // This conditional checks whether user is a student or not
  // This is checked because if its a student the message has to be routed to the ml model
  // to be verified if it has grammatical issues to be scored
  if (user_type == "student") {
    fetch("/api/verify-message", {
      method: "Post",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(message_data),
    })
      .then((response) => response.json())
      .then((data) => {
        let verification_msg = data.msg;
        console.log(verification_msg);

        if (verification_msg == "correct") {
          // Score should be added to the database

          let marks_data = {
            marks: 20,
          };

          fetch("/api/update-score", {
            method: "Post",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(marks_data),
          });
        }
      });
  }

  channel.sendMessage({
    text: JSON.stringify({
      type: "chat",
      message: message,
      displayName: displayName,
    }),
  });

  addMessageToDom(displayName, message);

  e.target.reset();
};

/*
This function adds the message to the DOM
*/
let addMessageToDom = (name, message) => {
  let messagesWrapper = document.getElementById("messages");

  let newMessage = `<div class="message__wrapper">
                      <div class="message__body">
                      <strong class="message__author">${name}</strong>
                      <p class="message__text">${message}</p>
                      </div>
                    </div>`;

  messagesWrapper.insertAdjacentHTML("beforeend", newMessage);

  let lastMessage = document.querySelector(
    "#messages .message__wrapper:last-child"
  );

  if (lastMessage) {
    lastMessage.scrollIntoView();
  }
};

let addBotMessageToDom = (botMessage) => {
  let messagesWrapper = document.getElementById("messages");

  let newMessage = `<div class="message__wrapper">
                      <div class="message__body__bot">
                      <strong class="message__author__bot">Learnly Meet</strong>
                      <p class="message__text__bot">${botMessage}</p>
                      </div>
                    </div> `;

  messagesWrapper.insertAdjacentHTML("beforeend", newMessage);

  let lastMessage = document.querySelector(
    "#messages .message__wrapper:last-child"
  );

  if (lastMessage) {
    lastMessage.scrollIntoView();
  }
};

let removeMemberFromDom = async (MemberId) => {
  let memberWrapper = document.getElementById(`member__${MemberId}__wrapper`);
  let name = memberWrapper.getElementsByClassName("member_name")[0].textContent;
  addBotMessageToDom(`${name} has left the meet`);

  memberWrapper.remove();
};

let leaveChannel = async () => {
  await channel.leave();
  await rtmClient.logout();
};

window.addEventListener("beforeunload", leaveChannel);

let messageForm = document.getElementById("message__form");
messageForm.addEventListener("submit", sendMessage);

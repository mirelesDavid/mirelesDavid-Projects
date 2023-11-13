document.addEventListener("DOMContentLoaded", () => {
    const chatInput = document.querySelector(".chat-input textarea");
    const sendChatBtn = document.querySelector(".chat-input button");
    const chatbox = document.querySelector(".chatbox");


    let userMessage;
    const API_KEY = "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";
    
    const createChatLi = (message, className) => {
        const chatLi = document.createElement("li");
        chatLi.classList.add("chat", className);
        let chatContent  = className === "outgoing" ? `<p></p>` : `<img src="./UntitledROBOT AI.png" alt="Logo AI" class="logoAi"><p></p>`;
        chatLi.innerHTML = chatContent;
        chatLi.querySelector("p").textContent = message;
        return chatLi;
    }

    const generateRespond = (incomingChatLi)=> {
        const API_URL = "https://api.openai.com/v1/chat/completions";
        const messageElement = incomingChatLi.querySelector("p");

        const requestOptions = {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${API_KEY}`
            },
            body: JSON.stringify({
                "model": "gpt-3.5-turbo",
                "messages": [
                  {
                    "role": "system",
                    "content": userMessage
                  },
                  {
                    "role": "user",
                    "content": userMessage
                  }
                ]
            })
        }

        fetch(API_URL, requestOptions).then(res => res.json()).then(data => {
            messageElement.textContent = data.choices[0].message.content;
        }).catch((error) =>{
            messageElement.textContent = "Oops! algo salio mal. Intente de nuevo";
        }).finally(()=> chatbox.scroll(0,chatbox.scrollHeight));
    }

    const handleChat = () => {
        userMessage = chatInput.value.trim();
        if(!userMessage) return;
        chatInput.value = "";


        // Remove the message from the chat input.
        chatInput.value = "";
        chatbox.appendChild(createChatLi(userMessage, "outgoing"));
        chatbox.scrollTo(0, chatbox.scrollHeight);

        setTimeout(()=>{
            const incomingChatLi = createChatLi("Pensando...", "incoming");
            chatbox.appendChild(incomingChatLi);
            chatbox.scrollTo(0, chatbox.scrollHeight);
            generateRespond(incomingChatLi)
        }, 600);
    }

    sendChatBtn.addEventListener("click", handleChat);

});

import streamlit as st
from streamlit_chat import message
import google.generativeai as genai
import os
from datetime import datetime


API_KEY = ""  
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")


def get_gemini_reply(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"


# ------------------PAGE HEADER--------------------

st.write(
    "<h1 style='text-align:center;'>RR GPTS</h1>", unsafe_allow_html=True
)

# ---------------- Session state init -----------------
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
if "archived_chats" not in st.session_state:
    st.session_state["archived_chats"] = []
if "reports" not in st.session_state:
    st.session_state["reports"] = []
if "menu_open" not in st.session_state:
    st.session_state["menu_open"] = False
if "last_action_msg" not in st.session_state:
    st.session_state["last_action_msg"] = ""
if "user_input" not in st.session_state:
    st.session_state["user_input"] = ""

# ---------------- LEFT SIDEBAR -----------------
with st.sidebar:
    st.title("Menu")
    if st.button("New Chat"):
        st.session_state["chat_history"] = []
        st.session_state["last_action_msg"] = "Started a new chat."

    st.text_input(
        "Search Chats",
        key="search_val",
        placeholder="Search",
    )
    st.markdown("Library")
    st.markdown("Projects")

    st.markdown("---")
    st.markdown("Chat History")
    if st.session_state["chat_history"]:
        for i, (sender, text) in enumerate(
            st.session_state["chat_history"][-6:], start=1
        ):
            prefix = "You" if sender == "user" else "Bot"
            st.write(f"{i}. *{prefix}*: {text[:60]}{'...' if len(text)>60 else ''}")
    else:
        st.write("No messages yet")

    st.markdown("---")
    st.write("Archived sessions:", len(st.session_state["archived_chats"]))


# ---------------- Menu action handlers -----------------
def archive_current_chat():
    if st.session_state["chat_history"]:
        archive_copy = list(st.session_state["chat_history"])
        meta = {
            "archived_at": datetime.utcnow().isoformat() + "Z",
            "messages": archive_copy,
        }
        st.session_state["archived_chats"].append(meta)
        st.session_state["chat_history"] = []
        st.session_state["last_action_msg"] = "Chat archived."
    else:
        st.session_state["last_action_msg"] = "No chat to archive."
    st.session_state["menu_open"] = False


def report_current_chat():
    report_entry = {
        "reported_at": datetime.utcnow().isoformat() + "Z",
        "chat_snapshot": list(st.session_state["chat_history"]),
        "reason": "User-initiated report via UI",
    }
    st.session_state["reports"].append(report_entry)
    st.session_state["last_action_msg"] = "Chat reported. Support will review it."
    st.session_state["menu_open"] = False


def delete_current_chat():
    if st.session_state["chat_history"]:
        st.session_state["chat_history"] = []
        st.session_state["last_action_msg"] = "Chat deleted."
    else:
        st.session_state["last_action_msg"] = "No chat to delete."
    st.session_state["menu_open"] = False


# ---------------- Collapsible menu (Archive / Report / Delete) -----------------
if st.session_state["menu_open"]:
    r1, r2, r3 = st.columns([1, 1, 1])
    with r1:
        st.button("Archive", on_click=archive_current_chat)
    with r2:
        st.button("Report", on_click=report_current_chat)
    with r3:
        st.button("Delete", on_click=delete_current_chat)

# ---------------- Last action message -----------------
if st.session_state["last_action_msg"]:
    st.info(st.session_state["last_action_msg"])

# ---------------- Display chat history -----------------
for sender, text in st.session_state["chat_history"]:
    message(text, is_user=(sender == "user"))


# ---------------- SEND MESSAGE HANDLER -----------------
def send_message():
    text = st.session_state.get("user_input", "").strip()
    if not text:
        st.session_state["last_action_msg"] = "Please type a message first."
        return

    # User message
    st.session_state["chat_history"].append(("user", text))

    # AI reply
    bot_reply = get_gemini_reply(text)
    st.session_state["chat_history"].append(("bot", bot_reply))

    st.session_state["user_input"] = ""  # clear box


# ---------------- Input + arrow button -----------------
col_inp, col_arrow = st.columns([11.5, 1])

with col_inp:
    st.text_input("Message:", key="user_input", placeholder="Type your message...")

with col_arrow:
    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
    st.button("➤", key="send_arrow", on_click=send_message)
import streamlit as st
from gemini_client import get_response

st.set_page_config(
    page_title="Blog Assistant",
    page_icon="✍️",
    layout="wide"
)

st.title("✍️ Blog Assistant Chatbot")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:

    st.header("Actions")

    # Download complete conversation
    if st.session_state.messages:

        conversation_md = "# Blog Assistant Conversation\n\n"

        for msg in st.session_state.messages:

            role = "User" if msg["role"] == "user" else "Assistant"

            conversation_md += f"## {role}\n\n"
            conversation_md += f"{msg['content']}\n\n---\n\n"

        st.download_button(
            label="📥 Download Full Conversation",
            data=conversation_md,
            file_name="blog_assistant_conversation.md",
            mime="text/markdown"
        )

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Display chat history
assistant_count = 0

for idx, message in enumerate(st.session_state.messages):

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        # Add download button for assistant responses
        if message["role"] == "assistant":

            assistant_count += 1

            st.download_button(
                label=f"📥 Download Response {assistant_count}",
                data=message["content"],
                file_name=f"blog_response_{assistant_count}.md",
                mime="text/markdown",
                key=f"download_{idx}"
            )

# User input
prompt = st.chat_input("Ask me about blogging, SEO, content writing...")

if prompt:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response
    with st.chat_message("assistant"):

        with st.spinner("Generating response..."):

            response = get_response(prompt)

            st.markdown(response)

            current_response_num = (
                len(
                    [
                        m
                        for m in st.session_state.messages
                        if m["role"] == "assistant"
                    ]
                ) + 1
            )

            st.download_button(
                label="📥 Download This Response",
                data=response,
                file_name=f"blog_response_{current_response_num}.md",
                mime="text/markdown",
                key=f"latest_download_{current_response_num}"
            )

    # Store assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )
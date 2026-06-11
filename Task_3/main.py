import os
import sys

# 1. System path correction guard (Must stay at line 1)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 2. Environment extraction
from dotenv import load_dotenv
load_dotenv()

# 3. Streamlit & Modern Langfuse Tracing engine paths
import streamlit as st
import uuid
import langfuse
from langfuse.langchain import CallbackHandler

# 4. Local modules
from parser import ValidateInput
from model import map_chain

# 5. Connect the telemetry handler
langfuse_handler = CallbackHandler()


st.set_page_config(page_title="Support Ticket Triager", page_icon="🎫", layout="centered")

st.title("🎫 AI Support Ticket Triage Dashboard")

# Default text preset matching your sprint edge-cases
default_input = """ticket_id: TCK-2001
channel: email
ticket_text: I was charged twice for my subscription. Please fix this immediately."""

user_input = st.text_area("Paste Incoming Raw Ticket Stream Here:", value=default_input, height=120)

if st.button("Process & Triage Ticket", type="primary"):
    if user_input.strip():
        try:
            
            with st.spinner("Executing Input Validation Layer..."):
                validated = ValidateInput(ticket=user_input)
                clean_query = validated.ticket
            
            unified_trace_id = uuid.uuid4().hex
            st.session_state["last_trace_id"] = unified_trace_id

            
            with st.spinner("Invoking Parallel Triage Chains ..."):
                triage_results = map_chain.invoke(
                    {
                        "query": clean_query
                    },
                    config={
                        "callbacks": [langfuse_handler],
                        "run_id": unified_trace_id 
                    }
                )
            
            st.write("### 📊 Structured Output Metrics")
            col1, col2, col3 = st.columns([1, 1, 2])
            col1.metric("Assigned Category", triage_results["category"])
            col2.metric("Calculated Priority", triage_results["priority"])
            col3.metric("Target Queue Location", triage_results["routing_queue"])
            
            st.write("### 📝 System Response")
            st.info(triage_results["response_draft"])
            
            with st.expander("See Raw Generated JSON Schema Payload"):
                st.json(triage_results)

            
        except ValueError as val_err:
            st.error(f"❌ Input Format Validation Error:\n{val_err}")
        except Exception as e:
            st.error(f"💥 Runtime Exception Encountered: {str(e)}")
            
        st.write("---")
        st.write("### 📢 Audit & Quality Control Feedback")

        feed_col1, feed_col2, _ = st.columns([1, 1, 4])

        if feed_col1.button("👍 Correct Triage", use_container_width=True):
            if "last_trace_id" in st.session_state:
                # Initialize the baseline global trace posting endpoint
                lf_client = langfuse.Langfuse()
                
                lf_client.create_score(
                    trace_id=st.session_state["last_trace_id"],
                    name="user-accuracy-audit",
                    value=1.0,
                    comment="Human audited and marked as correct routing."
                )
                lf_client.flush()
                st.success(f"Feedback registered successfully for Trace: {st.session_state['last_trace_id']}")

        if feed_col2.button("👎 Incorrect Triage", use_container_width=True):
            if "last_trace_id" in st.session_state:
                lf_client = langfuse.Langfuse()
                
                lf_client.create_score(
                    trace_id=st.session_state["last_trace_id"],
                    name="user-accuracy-audit",
                    value=0.0,
                    comment="Human audited and marked as bad routing/generation."
                )
                lf_client.flush()
                st.warning(f"Flagged as incorrect. Feedback sent for Trace: {st.session_state['last_trace_id']}")
    else:
        st.warning("Please enter a ticket payload to begin analysis.")


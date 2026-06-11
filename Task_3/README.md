# AI Support Ticket Triager
**Live App:** [View App](https://huggingface.co/spaces/vasanth-4321/Customer_Ticket_Classifier)

A Streamlit-based AI Support Ticket Triager powered by Groq's high-speed Llama 3.1 8B LLM engine and monitored via Langfuse.

The application automatically ingests raw incoming customer support tickets, dynamically executes four distinct classification and composition tasks concurrently to reduce response latency, and includes a production-grade human-in-the-loop quality audit workflow.

## Features

* **Parallel Execution Engine**: Leverages LangChain's `RunnableParallel` map design to simultaneously evaluate category routing, determine systemic priority metrics, assign target infrastructure queues, and compose contextual email drafts.
* **Closed-Loop LLM Analytics**: Integrated natively with the Langfuse tracing backend to record input prompts, structural outputs, duration breakdowns, and accurate token expenditures.
* **Deterministic Trace Mapping**: Bypasses standard OpenTelemetry telemetry masking strings (`unknown_service`) by programmatically binding a matching 32-character hexadecimal tracking token across the execution handler and dashboard state.
* **Interactive Human Annotation**: Explicit interface audit buttons (`👍 Correct Triage` / `👎 Incorrect Triage`) that immediately write programmatic evaluation metrics (`user-accuracy-audit`) to running traces using safe background thread synchronization (`lf_client.create_score`).
* **Pydantic Validation Guard**: Validates, cleans, and structures unstructured incoming ticket streams before the LLM orchestration layer to insulate the application engine from malformed structural failures.

## Project Structure

```text
Task_3/
│
├── main.py          # Streamlit user interface, state machine coordinator, & feedback hooks
├── model.py         # RunnableParallel graph compilation & ChatGroq API mappings
├── prompt.py        # Tailored system personas and guidelines for triage chains
├── parser.py        # Pydantic schema validation & string sanitization layout
├── requirements.txt # Explicitly pinned package dependency manifest
└── .env             # Protected runtime authorization secrets
```

## Installation

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
LANGFUSE_PUBLIC_KEY=YOUR_LANGFUSE_PUBLIC_KEY
LANGFUSE_SECRET_KEY=YOUR_LANGFUSE_SECRET_KEY
LANGFUSE_HOST=[https://cloud.langfuse.com](https://cloud.langfuse.com)
```

## Running the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## Performing an Audit Optimization Cycle:
1. Input an unstructured text payload (e.g., "I was charged twice for my premium account tier!").
2. Click Process & Triage Ticket.
3. Once metrics render on-screen, navigate down to the Audit & Quality Control Feedback split.
4. Click 👍 Correct Triage or 👎 Incorrect Triage.
5. Check your console for confirmation: `Feedback registered successfully for Trace: <32_char_hex_id>.`
6. Open your Langfuse Dashboard under **Evaluation** > **Human Annotation** or **Dashboards** to view real-time accuracy percentages!

## Usage

1. Paste an incoming, unstructured raw support ticket stream into the workspace text area.
2. Click Process & Triage Ticket to spin up concurrent evaluation pipelines.
3. Observe real-time structured telemetry outputs across category, priority level, routing targets, and drafts.
4. Interact with the Audit & Quality Control section to submit validation grading.
5. Review live linked operational traces and accuracy maps on your cloud observability workspace.

## Technologies Used
- Python
- Streamlit
- LangChain Core (langchain-core)
- LangChain Groq (langchain-groq)
- Langfuse Tracking Platform (langfuse)
- Pydantic
- python-dotenv

## Future Improvements
- Automated database sync for triage logs
- Dynamic customer history context retrieval via vector embedding databases (RAG)
- Multi-language ticket translation layers
- Automated alert routing notifications for critical priority issues
- Dynamic system configuration overrides via the UI workspace

## Author
Developed as part of a Generative AI projects.

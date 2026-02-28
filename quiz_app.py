import streamlit as st
import random
import time

# ─── PAGE CONFIG ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="General Agents Quiz",
    page_icon="🤖",
    layout="centered"
)

# ─── CUSTOM CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .main { background-color: #f0f4f8; }
    .stRadio > div { gap: 8px; }
    .correct-answer { 
        background: #d4edda; padding: 10px; border-radius: 8px; 
        border-left: 4px solid #28a745; color: #155724; font-weight: bold;
    }
    .wrong-answer { 
        background: #f8d7da; padding: 10px; border-radius: 8px; 
        border-left: 4px solid #dc3545; color: #721c24; font-weight: bold;
    }
    .question-card {
        background: white; padding: 20px; border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin-bottom: 16px;
    }
    .score-card {
        background: linear-gradient(135deg, #1F4E79, #2980b9);
        color: white; padding: 24px; border-radius: 16px; text-align: center;
    }
    .chapter-badge {
        display: inline-block; padding: 3px 10px; border-radius: 12px;
        font-size: 12px; font-weight: bold; margin-bottom: 8px;
    }
</style>
""", unsafe_allow_html=True)

# ─── QUESTIONS DATA ──────────────────────────────────────────────────────────
ALL_QUESTIONS = [
    # CHAPTER 1 ───────────────────────────────────────────────────────────────
    {"chapter": 1, "q": "What score did OpenAI's system achieve at the 2025 ICPC World Finals?",
     "opts": ["10/12", "11/12", "12/12 (Perfect)", "8/12"], "ans": "12/12 (Perfect)"},

    {"chapter": 1, "q": "According to the 2025 Stack Overflow Developer Survey, what percentage of developers use or plan to use AI tools?",
     "opts": ["51%", "72%", "90%", "84%"], "ans": "84%"},

    {"chapter": 1, "q": "What percentage of software development professionals use AI according to Google's 2025 DORA report?",
     "opts": ["84%", "90%", "70%", "60%"], "ans": "90%"},

    {"chapter": 1, "q": "How many hours per day do developers spend with AI tools (median) per the Google DORA 2025 report?",
     "opts": ["1 hour", "4 hours", "2 hours", "30 minutes"], "ans": "2 hours"},

    {"chapter": 1, "q": "What is the approximate annual run-rate revenue Claude Code reached by mid-2025?",
     "opts": ["$100M+", "$200M+", "$1B+", "$500M+"], "ans": "$500M+"},

    {"chapter": 1, "q": "Which of the following is NOT one of the three core operational constraints of LLMs?",
     "opts": ["Statelessness", "Probabilistic outputs", "Unlimited context", "Context limits"], "ans": "Unlimited context"},

    {"chapter": 1, "q": "What does 'statelessness' mean in the context of LLMs?",
     "opts": ["AI can remember everything forever", "The AI model has no memory between calls — each session starts fresh",
              "The AI only works offline", "The AI cannot use external tools"],
     "ans": "The AI model has no memory between calls — each session starts fresh"},

    {"chapter": 1, "q": "What are the Five Powers of an autonomous AI agent?",
     "opts": ["Search, Code, Write, Analyze, Deploy", "See, Hear, Reason, Act, Remember",
              "Plan, Execute, Monitor, Correct, Report", "Input, Process, Store, Output, Learn"],
     "ans": "See, Hear, Reason, Act, Remember"},

    {"chapter": 1, "q": "What does the OODA Loop stand for?",
     "opts": ["Organize, Optimize, Deploy, Automate", "Output, Optimize, Debug, Act",
              "Observe, Orient, Decide, Act", "Observe, Order, Develop, Apply"],
     "ans": "Observe, Orient, Decide, Act"},

    {"chapter": 1, "q": "According to the AI Agent Factory paradigm, how has the developer's role changed?",
     "opts": ["From manager to programmer", "From coder to orchestrator",
              "From designer to tester", "From analyst to developer"],
     "ans": "From coder to orchestrator"},

    {"chapter": 1, "q": "What is a 'Digital FTE' in the context of AI Agent Factory?",
     "opts": ["A freelance developer who works digitally", "A file transfer encryption method",
              "An AI agent engineered to own entire business functions autonomously",
              "A type of cloud computing service"],
     "ans": "An AI agent engineered to own entire business functions autonomously"},

    {"chapter": 1, "q": "Which statement best describes the relationship between General Agents and Custom Agents?",
     "opts": ["Custom Agents replace General Agents", "General Agents BUILD Custom Agents",
              "They are completely independent systems", "General Agents are more advanced than Custom Agents"],
     "ans": "General Agents BUILD Custom Agents"},

    {"chapter": 1, "q": "Which of the following is an example of a General Agent?",
     "opts": ["OpenAI SDK", "Claude SDK", "Claude Code", "LangChain"],
     "ans": "Claude Code"},

    {"chapter": 1, "q": "Which of the following is an example of a Custom Agent?",
     "opts": ["Claude Cowork", "Gemini CLI", "Claude Code", "OpenAI SDK"],
     "ans": "OpenAI SDK"},

    {"chapter": 1, "q": "What standard is described as 'USB for AI tools' in the Agent Factory paradigm?",
     "opts": ["AGENTS.md", "CLAUDE.md", "MCP (Model Context Protocol)", "REST API"],
     "ans": "MCP (Model Context Protocol)"},

    {"chapter": 1, "q": "On what date did OpenAI, Anthropic, and Block donate their open standards to the Linux Foundation?",
     "opts": ["January 1, 2026", "December 9, 2025", "March 15, 2025", "September 10, 2024"],
     "ans": "December 9, 2025"},

    {"chapter": 1, "q": "What organization was created when AI open standards were donated to the Linux Foundation?",
     "opts": ["Open AI Alliance (OAA)", "Agentic AI Foundation (AAIF)", "AI Standards Board (ASB)", "Linux AI Consortium (LAC)"],
     "ans": "Agentic AI Foundation (AAIF)"},

    {"chapter": 1, "q": "How many pillars make up the Nine Pillars of AI-Driven Development (AIDD)?",
     "opts": ["7", "8", "9", "10"], "ans": "9"},

    {"chapter": 1, "q": "Which of the following is NOT one of the Nine Pillars of AIDD?",
     "opts": ["MCP Standard", "Spec-Driven Development", "Blockchain Integration", "Test-Driven Development"],
     "ans": "Blockchain Integration"},

    {"chapter": 1, "q": "What is 'Spec-Driven Development' (SDD)?",
     "opts": ["Writing specifications after code is complete",
              "A methodology where specifications are the primary artifact and code is a generated output",
              "Using spreadsheets to plan development", "A type of agile methodology"],
     "ans": "A methodology where specifications are the primary artifact and code is a generated output"},

    {"chapter": 1, "q": "Which of the four enterprise value propositions involves replacing entire business processes with AI?",
     "opts": ["Enabler", "Implementer", "Custom Developer", "Workflow Disruptor"],
     "ans": "Workflow Disruptor"},

    {"chapter": 1, "q": "In the Agent Factory process, what is the first step to create a Digital FTE?",
     "opts": ["Install Claude Code", "Write a Markdown specification describing the goal",
              "Choose a cloud provider", "Write Python code"],
     "ans": "Write a Markdown specification describing the goal"},

    {"chapter": 1, "q": "What does the three-layer AI development stack consist of (bottom to top)?",
     "opts": ["Data → Models → Applications", "Hardware → Software → Cloud",
              "Foundation LLMs → General Agent layer → Custom Agent layer",
              "Training → Testing → Deployment"],
     "ans": "Foundation LLMs → General Agent layer → Custom Agent layer"},

    {"chapter": 1, "q": "What does the 'product overhang' concept refer to?",
     "opts": ["Too many AI products on the market",
              "Latent AI capabilities waiting for the right interface to unlock them",
              "Products that have expired their market value", "AI products that exceed their specifications"],
     "ans": "Latent AI capabilities waiting for the right interface to unlock them"},

    {"chapter": 1, "q": "What percentage of Claude Code was written by Claude Code itself (approximately)?",
     "opts": ["50%", "70%", "90%", "100%"], "ans": "90%"},

    {"chapter": 1, "q": "Which four generations describe the evolution of AI coding tools?",
     "opts": ["Text → Images → Video → Agents",
              "Autocomplete → Chatbots → Copilots → Autonomous Agents",
              "Rule-based → ML → Deep Learning → Transformers",
              "Search → Classify → Generate → Deploy"],
     "ans": "Autocomplete → Chatbots → Copilots → Autonomous Agents"},

    {"chapter": 1, "q": "What is the estimated size of the agentic AI market referenced for enterprise sales?",
     "opts": ["$10–50 billion", "$50–100 billion", "$100–400 billion", "$1 trillion+"],
     "ans": "$100–400 billion"},

    {"chapter": 1, "q": "What is the primary reason why Chapter 1 is purely conceptual with no hands-on coding?",
     "opts": ["The authors forgot to add exercises",
              "Jumping into tools without understanding the paradigm shift leads to confusion and missed opportunities",
              "The tools are too complex for beginners", "Hands-on coding requires expensive hardware"],
     "ans": "Jumping into tools without understanding the paradigm shift leads to confusion and missed opportunities"},

    {"chapter": 1, "q": "What is the key competitive advantage for domain experts using the Agent Factory approach?",
     "opts": ["They can learn programming faster than technical people",
              "Their domain expertise is the valuable ingredient — technical skills are learnable but domain knowledge is hard to replicate",
              "They have better internet connections", "They get free access to AI tools"],
     "ans": "Their domain expertise is the valuable ingredient — technical skills are learnable but domain knowledge is hard to replicate"},

    # CHAPTER 2 ───────────────────────────────────────────────────────────────
    {"chapter": 2, "q": "Why is Markdown considered the 'universal bridge' in AI-native development?",
     "opts": ["Because it requires special software to read",
              "Because it is both human-readable and machine-parseable",
              "Because it only works with OpenAI", "Because it is a compiled programming language"],
     "ans": "Because it is both human-readable and machine-parseable"},

    {"chapter": 2, "q": "Which Markdown syntax creates a top-level (H1) heading?",
     "opts": ["## Heading", "### Heading", "# Heading", "** Heading **"],
     "ans": "# Heading"},

    {"chapter": 2, "q": "Which Markdown syntax creates an H2 (second-level) heading?",
     "opts": ["# Heading", "## Heading", "### Heading", "#### Heading"],
     "ans": "## Heading"},

    {"chapter": 2, "q": "How do you create an unordered (bullet) list in Markdown?",
     "opts": ["1. item", "* item or - item", "> item", "| item |"],
     "ans": "* item or - item"},

    {"chapter": 2, "q": "What is the correct Markdown syntax for inline code (single line)?",
     "opts": ["```code```", "'code'", "`code`", "<code>code</code>"],
     "ans": "`code`"},

    {"chapter": 2, "q": "What is the correct Markdown syntax for a multi-line code block?",
     "opts": ["<pre>code</pre>", "Three backticks (```) before and after the code",
              "Four spaces before each line", "[code] ... [/code]"],
     "ans": "Three backticks (```) before and after the code"},

    {"chapter": 2, "q": "What is the correct Markdown syntax for a hyperlink?",
     "opts": ["(text)[url]", "{text}(url)", "[text](url)", "<a href='url'>text</a>"],
     "ans": "[text](url)"},

    {"chapter": 2, "q": "What is the correct Markdown syntax for an image?",
     "opts": ["[image](url)", "![alt text](url)", "#image(url)", "<img src='url'>"],
     "ans": "![alt text](url)"},

    {"chapter": 2, "q": "Why do most GitHub repositories use README.md files instead of README.txt or Word documents?",
     "opts": [".md files are smaller in size", ".md files are faster to load",
              "Markdown is structured and readable by both humans and machines, including AI agents",
              "GitHub only supports .md files"],
     "ans": "Markdown is structured and readable by both humans and machines, including AI agents"},

    {"chapter": 2, "q": "What is the primary benefit of using structured Markdown when prompting an AI agent?",
     "opts": ["It reduces the file size", "The AI generates higher-quality, more accurate output",
              "It speeds up the internet connection", "It makes the text look nicer"],
     "ans": "The AI generates higher-quality, more accurate output"},

    {"chapter": 2, "q": "What file format is used throughout the Agent Factory book for CLAUDE.md files and agent instructions?",
     "opts": ["HTML", "XML", "Markdown (.md)", "JSON"],
     "ans": "Markdown (.md)"},

    {"chapter": 2, "q": "What does 'Markdown as Programming Language' mean in the Nine Pillars of AIDD?",
     "opts": ["Markdown can compile to machine code",
              "Markdown specifications become executable instructions for AI agents",
              "Markdown replaces Python", "Markdown is used to write databases"],
     "ans": "Markdown specifications become executable instructions for AI agents"},

    {"chapter": 2, "q": "Which of these tools can you use to write and preview Markdown for free?",
     "opts": ["Microsoft Word", "Adobe Photoshop", "StackEdit (browser-based)", "AutoCAD"],
     "ans": "StackEdit (browser-based)"},

    {"chapter": 2, "q": "Which Markdown syntax makes text bold?",
     "opts": ["*text*", "**text** or __text__", "##text##", "~~text~~"],
     "ans": "**text** or __text__"},

    {"chapter": 2, "q": "In AI-native development, what is the connection between Markdown and Context Engineering?",
     "opts": ["They are completely unrelated",
              "Markdown is the format AI uses to structure information; together they form the complete AI collaboration skillset",
              "Context Engineering replaces Markdown", "Markdown is only used in web development"],
     "ans": "Markdown is the format AI uses to structure information; together they form the complete AI collaboration skillset"},

    {"chapter": 2, "q": "What makes Markdown different from Word documents in the context of AI tools?",
     "opts": ["Markdown is colourful", "Markdown requires no special software to read and is parseable by AI",
              "Word documents are free", "Word is better for AI"],
     "ans": "Markdown requires no special software to read and is parseable by AI"},

    # CHAPTER 3 ───────────────────────────────────────────────────────────────
    {"chapter": 3, "q": "Who is the engineer credited with giving Claude its first direct filesystem access?",
     "opts": ["Sam Altman", "Dario Amodei", "Boris Cherny", "Greg Brockman"],
     "ans": "Boris Cherny"},

    {"chapter": 3, "q": "When did Boris Cherny begin the experiment that led to Claude Code?",
     "opts": ["January 2025", "September 2024", "March 2023", "June 2024"],
     "ans": "September 2024"},

    {"chapter": 3, "q": "What unexpected behavior did Claude exhibit when given filesystem access for the first time?",
     "opts": ["It crashed immediately", "It only answered math questions",
              "It began naturally exploring files, following imports, and understanding project structure without being told to",
              "It deleted all files it found"],
     "ans": "It began naturally exploring files, following imports, and understanding project structure without being told to"},

    {"chapter": 3, "q": "What is the key difference between passive AI tools and Claude Code?",
     "opts": ["Claude Code is free while ChatGPT is paid",
              "Passive AI gives generic advice without seeing your files; Claude Code reads your actual code, proposes specific changes, and executes them",
              "Passive AI is faster", "Claude Code only works on Linux"],
     "ans": "Passive AI gives generic advice without seeing your files; Claude Code reads your actual code, proposes specific changes, and executes them"},

    {"chapter": 3, "q": "Using the analogy in Chapter 3, passive AI is like a consultant on the phone. What is Claude Code like?",
     "opts": ["A teacher in a classroom", "A pair programmer sitting at your desk looking at your code",
              "A self-driving car", "A remote server"],
     "ans": "A pair programmer sitting at your desk looking at your code"},

    {"chapter": 3, "q": "When was Claude Cowork officially launched?",
     "opts": ["September 2024", "December 2025", "January 2026", "March 2025"],
     "ans": "January 2026"},

    {"chapter": 3, "q": "What interface does Claude Code use?",
     "opts": ["Desktop GUI", "Web browser", "Terminal/CLI", "Mobile app"],
     "ans": "Terminal/CLI"},

    {"chapter": 3, "q": "What interface does Claude Cowork use?",
     "opts": ["Terminal/CLI", "Desktop interface", "REST API", "Command prompt only"],
     "ans": "Desktop interface"},

    {"chapter": 3, "q": "Both Claude Code and Cowork are powered by the same underlying technology. What is it?",
     "opts": ["OpenAI GPT-4", "Google Gemini SDK", "Claude Agent SDK", "LangChain"],
     "ans": "Claude Agent SDK"},

    {"chapter": 3, "q": "What is a CLAUDE.md file?",
     "opts": ["A Python configuration file",
              "A Markdown file placed in the project root that Claude Code automatically loads at the start of every session",
              "A file used only for deployment", "A log file generated by Claude Code"],
     "ans": "A Markdown file placed in the project root that Claude Code automatically loads at the start of every session"},

    {"chapter": 3, "q": "What is the recommended maximum length for a CLAUDE.md file (the 'under-X-line rule')?",
     "opts": ["Under 30 lines", "Under 100 lines", "Under 60 lines", "Under 200 lines"],
     "ans": "Under 60 lines"},

    {"chapter": 3, "q": "What is the primary purpose of a CLAUDE.md file?",
     "opts": ["To store API keys",
              "To provide persistent project context so you don't repeat project details every session",
              "To write Python scripts", "To log errors"],
     "ans": "To provide persistent project context so you don't repeat project details every session"},

    {"chapter": 3, "q": "What is AGENTS.md and who created the standard?",
     "opts": ["A Claude-specific file created by Anthropic",
              "A universal agent instruction file created by OpenAI, now an AAIF open standard",
              "A Google file for Gemini agents", "A Microsoft file for Copilot"],
     "ans": "A universal agent instruction file created by OpenAI, now an AAIF open standard"},

    {"chapter": 3, "q": "How many open source projects have adopted the AGENTS.md standard?",
     "opts": ["1,000+", "10,000+", "60,000+", "100,000+"],
     "ans": "60,000+"},

    {"chapter": 3, "q": "What is the best practice when using both CLAUDE.md and AGENTS.md in a project?",
     "opts": ["Use only CLAUDE.md and ignore AGENTS.md", "Use only AGENTS.md since it's the open standard",
              "Use both — CLAUDE.md for rich Claude-specific context and AGENTS.md for universal compatibility",
              "Merge them into one file called AI.md"],
     "ans": "Use both — CLAUDE.md for rich Claude-specific context and AGENTS.md for universal compatibility"},

    {"chapter": 3, "q": "What Claude Code command clears the entire context window?",
     "opts": ["/reset", "/new", "/clear", "/flush"],
     "ans": "/clear"},

    {"chapter": 3, "q": "What does the /compact command do in Claude Code?",
     "opts": ["Deletes all project files",
              "Compresses the context window to save tokens while keeping work continuity",
              "Converts code to a compact format", "Creates a backup of the project"],
     "ans": "Compresses the context window to save tokens while keeping work continuity"},

    {"chapter": 3, "q": "What are 'hooks' in Claude Code?",
     "opts": ["Fishing tools for finding bugs",
              "Event-driven automation triggers that execute actions when specific events occur",
              "A type of keyboard shortcut", "External API connections"],
     "ans": "Event-driven automation triggers that execute actions when specific events occur"},

    {"chapter": 3, "q": "What is 'subagent orchestration' in Claude Code?",
     "opts": ["Running multiple instances of VS Code",
              "Claude spawning sub-agents to execute parallel tasks",
              "Connecting multiple LLMs together", "A type of database query"],
     "ans": "Claude spawning sub-agents to execute parallel tasks"},

    {"chapter": 3, "q": "Which free backend options can be used with Claude Code instead of a paid subscription?",
     "opts": ["AWS and Azure", "OpenRouter, Gemini, or DeepSeek", "Hugging Face and Ollama", "LangChain and LlamaIndex"],
     "ans": "OpenRouter, Gemini, or DeepSeek"},

    {"chapter": 3, "q": "What does MCP allow Claude Code/Cowork to do?",
     "opts": ["Only write Python scripts",
              "Connect to and integrate external systems like Google Workspace, Notion, Slack",
              "Train new AI models", "Access private databases only"],
     "ans": "Connect to and integrate external systems like Google Workspace, Notion, Slack"},

    {"chapter": 3, "q": "What is the benefit of compiling MCP to Skills?",
     "opts": ["It makes the code faster", "It improves token efficiency",
              "It adds more features", "It reduces security risks"],
     "ans": "It improves token efficiency"},

    {"chapter": 3, "q": "What document types can Claude Code/Cowork work with natively (Built-in Document Skills)?",
     "opts": ["Only .txt and .csv files", "docx, xlsx, pptx, and pdf",
              "Only Python and JavaScript files", "Only HTML and CSS files"],
     "ans": "docx, xlsx, pptx, and pdf"},

    {"chapter": 3, "q": "What is a 'General Agent' as defined in Chapter 3?",
     "opts": ["A basic chatbot that answers questions",
              "An AI that observes, orients, decides, and acts — executing actions rather than just generating text",
              "A general-purpose search engine", "A human assistant with AI tools"],
     "ans": "An AI that observes, orients, decides, and acts — executing actions rather than just generating text"},

    {"chapter": 3, "q": "What is the goal of working with Claude Code and Cowork according to Chapter 3?",
     "opts": ["To replace all human developers",
              "To establish Claude as a collaborative thinking partner and to build Skills that can become products",
              "To automate all business functions immediately", "To compete with Google's search engine"],
     "ans": "To establish Claude as a collaborative thinking partner and to build Skills that can become products"},

    {"chapter": 3, "q": "What happened in January 2026 that made AI agent tools accessible to non-technical users?",
     "opts": ["OpenAI released a new model",
              "Anthropic launched Claude Cowork — the desktop interface version of the Claude Agent",
              "Google launched Gemini Ultra", "Microsoft released Copilot Pro"],
     "ans": "Anthropic launched Claude Cowork — the desktop interface version of the Claude Agent"},

    {"chapter": 3, "q": "What is 'vibe coding' and why does it break down for production systems?",
     "opts": ["Coding with music; it's actually productive",
              "Conversational, unstructured AI-assisted coding that lacks specifications, causing context loss and architectural inconsistency",
              "A type of test-driven development", "Coding on mobile devices"],
     "ans": "Conversational, unstructured AI-assisted coding that lacks specifications, causing context loss and architectural inconsistency"},

    {"chapter": 3, "q": "In Chapter 3, Skills are described as what kind of product opportunity?",
     "opts": ["Free open-source libraries only", "Internal company tools that can't be sold",
              "Monetizable products that can be sold to enterprise customers", "One-time use scripts"],
     "ans": "Monetizable products that can be sold to enterprise customers"},

    {"chapter": 3, "q": "What is the 'Code vs. Cowork decision framework' about?",
     "opts": ["Choosing between Python and JavaScript",
              "Deciding whether to use Claude Code (terminal) or Claude Cowork (desktop) based on task characteristics and user type",
              "Deciding between open source and proprietary tools", "Choosing between cloud and local deployment"],
     "ans": "Deciding whether to use Claude Code (terminal) or Claude Cowork (desktop) based on task characteristics and user type"},

    {"chapter": 3, "q": "What browser integration was introduced in Chapter 3 for web-based automation?",
     "opts": ["Claude in Firefox", "Claude in Safari", "Claude in Chrome", "Claude in Edge"],
     "ans": "Claude in Chrome"},

    {"chapter": 3, "q": "Why does the AI model have no memory between calls in Claude Code?",
     "opts": ["Claude Code deletes memory to save storage",
              "LLMs are stateless — each API call is independent with no persistent memory",
              "Anthropic disabled memory for privacy", "Memory requires a paid subscription"],
     "ans": "LLMs are stateless — each API call is independent with no persistent memory"},

    {"chapter": 3, "q": "In Claude Code architecture, what is the distinction between 'Claude Code' and the underlying AI model?",
     "opts": ["They are exactly the same thing",
              "Claude Code is the interface you interact with; it calls the AI model (Claude) behind the scenes",
              "The AI model is Claude Code itself", "Claude Code is the AI model and Claude is just a brand name"],
     "ans": "Claude Code is the interface you interact with; it calls the AI model (Claude) behind the scenes"},

    {"chapter": 3, "q": "Which AAIF standard acts as a universal context file for ANY AI agent (not just Claude)?",
     "opts": ["CLAUDE.md", "MCP", "AGENTS.md", "README.md"],
     "ans": "AGENTS.md"},

    {"chapter": 3, "q": "What is the Agent Factory paradigm's core transformation in software development?",
     "opts": ["Replacing all programmers with AI",
              "Moving from writing code manually to describing jobs in natural language and having General Agents build the solutions",
              "Making software development only accessible to AI experts",
              "Eliminating the need for testing"],
     "ans": "Moving from writing code manually to describing jobs in natural language and having General Agents build the solutions"},
]

CHAPTER_NAMES = {
    1: "Chapter 1: AI Agent Factory Paradigm",
    2: "Chapter 2: Markdown",
    3: "Chapter 3: Claude Code & Cowork"
}
CHAPTER_COLORS = {1: "#1F4E79", 2: "#196F3D", 3: "#7D3C98"}
CHAPTER_BG = {1: "#D6E4F0", 2: "#D5F5E3", 3: "#E8DAEF"}

# ─── SESSION STATE ───────────────────────────────────────────────────────────
def init_state():
    if "quiz_started" not in st.session_state:
        st.session_state.quiz_started = False
    if "questions" not in st.session_state:
        st.session_state.questions = []
    if "current" not in st.session_state:
        st.session_state.current = 0
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "answers" not in st.session_state:
        st.session_state.answers = {}
    if "show_answer" not in st.session_state:
        st.session_state.show_answer = False
    if "quiz_done" not in st.session_state:
        st.session_state.quiz_done = False
    if "selected_option" not in st.session_state:
        st.session_state.selected_option = None

init_state()

# ─── HEADER ─────────────────────────────────────────────────────────────────
st.markdown("## 🤖 General Agents: Foundations Quiz")
st.markdown("*Based on agentfactory.panaversity.org — Chapters 1, 2 & 3*")
st.divider()

# ─── SETUP SCREEN ────────────────────────────────────────────────────────────
if not st.session_state.quiz_started:
    st.markdown("### ⚙️ Quiz Settings")

    col1, col2 = st.columns(2)
    with col1:
        chapters = st.multiselect(
            "📚 Select Chapters",
            options=[1, 2, 3],
            default=[1, 2, 3],
            format_func=lambda x: CHAPTER_NAMES[x]
        )
        num_questions = st.slider("🔢 Number of Questions", min_value=5, max_value=80, value=20, step=5)

    with col2:
        shuffle = st.checkbox("🔀 Shuffle Questions", value=True)
        shuffle_opts = st.checkbox("🔀 Shuffle Options", value=True)
        show_answer_mode = st.radio(
            "💡 Answer Display Mode",
            ["Show after each question", "Show at end only"],
            index=0
        )
        mode = st.radio("📝 Quiz Mode", ["Practice (see answers)", "Test (score at end)"], index=0)

    if chapters:
        available = [q for q in ALL_QUESTIONS if q["chapter"] in chapters]
        actual_num = min(num_questions, len(available))
        st.info(f"📊 {len(available)} questions available from selected chapters → **{actual_num} will be used**")

        # Chapter breakdown
        cols = st.columns(len(chapters))
        for i, ch in enumerate(sorted(chapters)):
            ch_q = len([q for q in available if q["chapter"] == ch])
            cols[i].metric(CHAPTER_NAMES[ch], f"{ch_q} Qs")

    st.divider()
    if st.button("🚀 Start Quiz!", type="primary", use_container_width=True):
        if not chapters:
            st.error("Please select at least one chapter!")
        else:
            pool = [q for q in ALL_QUESTIONS if q["chapter"] in chapters]
            selected = random.sample(pool, min(num_questions, len(pool))) if shuffle else pool[:num_questions]
            if shuffle_opts:
                for q in selected:
                    opts = q["opts"][:]
                    random.shuffle(opts)
                    q = dict(q, opts=opts)
            st.session_state.questions = selected
            st.session_state.show_answer_mode = show_answer_mode
            st.session_state.practice_mode = (mode == "Practice (see answers)")
            st.session_state.quiz_started = True
            st.session_state.current = 0
            st.session_state.score = 0
            st.session_state.answers = {}
            st.session_state.quiz_done = False
            st.session_state.selected_option = None
            st.rerun()

# ─── QUIZ DONE SCREEN ────────────────────────────────────────────────────────
elif st.session_state.quiz_done:
    total = len(st.session_state.questions)
    score = st.session_state.score
    pct = int((score / total) * 100)

    if pct >= 80:
        emoji, msg, color = "🏆", "Excellent! You're ready for the exam!", "#27AE60"
    elif pct >= 60:
        emoji, msg, color = "👍", "Good effort! Review the ones you missed.", "#F39C12"
    else:
        emoji, msg, color = "📖", "Keep studying! Review the concepts and try again.", "#E74C3C"

    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #1F4E79, #2980b9); color: white;
                padding: 32px; border-radius: 16px; text-align: center; margin-bottom: 24px;">
        <div style="font-size: 56px;">{emoji}</div>
        <div style="font-size: 36px; font-weight: bold;">{score} / {total}</div>
        <div style="font-size: 48px; font-weight: bold;">{pct}%</div>
        <div style="font-size: 18px; margin-top: 8px;">{msg}</div>
    </div>
    """, unsafe_allow_html=True)

    # Chapter breakdown
    st.markdown("#### 📊 Performance by Chapter")
    ch_data = {}
    for i, q in enumerate(st.session_state.questions):
        ch = q["chapter"]
        if ch not in ch_data:
            ch_data[ch] = {"total": 0, "correct": 0}
        ch_data[ch]["total"] += 1
        if st.session_state.answers.get(i) == q["ans"]:
            ch_data[ch]["correct"] += 1

    cols = st.columns(len(ch_data))
    for i, (ch, data) in enumerate(sorted(ch_data.items())):
        pct_ch = int((data["correct"] / data["total"]) * 100)
        cols[i].metric(
            CHAPTER_NAMES[ch],
            f"{data['correct']}/{data['total']}",
            f"{pct_ch}%"
        )

    # Review wrong answers
    wrong = [(i, q) for i, q in enumerate(st.session_state.questions)
             if st.session_state.answers.get(i) != q["ans"]]
    if wrong:
        st.markdown("#### ❌ Questions to Review")
        for i, q in wrong:
            with st.expander(f"Q{i+1}: {q['q'][:70]}..."):
                your_ans = st.session_state.answers.get(i, "Not answered")
                st.markdown(f"**Your answer:** ❌ {your_ans}")
                st.markdown(f"**Correct answer:** ✅ {q['ans']}")
                ch_name = CHAPTER_NAMES[q['chapter']]
                st.caption(f"📚 {ch_name}")

    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Try Again (Same Questions)", use_container_width=True):
            st.session_state.current = 0
            st.session_state.score = 0
            st.session_state.answers = {}
            st.session_state.quiz_done = False
            st.session_state.selected_option = None
            st.rerun()
    with col2:
        if st.button("🏠 Back to Setup", use_container_width=True, type="primary"):
            st.session_state.quiz_started = False
            st.session_state.quiz_done = False
            st.session_state.questions = []
            st.session_state.current = 0
            st.session_state.score = 0
            st.session_state.answers = {}
            st.session_state.selected_option = None
            st.rerun()

# ─── QUIZ IN PROGRESS ────────────────────────────────────────────────────────
else:
    questions = st.session_state.questions
    current = st.session_state.current
    total = len(questions)
    q = questions[current]

    # Progress bar
    progress = current / total
    st.progress(progress)
    col1, col2, col3 = st.columns([2, 1, 1])
    col1.markdown(f"**Question {current + 1} of {total}**")
    col2.markdown(f"✅ Score: **{st.session_state.score}**")
    col3.markdown(f"📚 Ch.{q['chapter']}")

    # Chapter badge
    ch_color = CHAPTER_COLORS[q['chapter']]
    ch_bg = CHAPTER_BG[q['chapter']]
    st.markdown(
        f'<span style="background:{ch_bg}; color:{ch_color}; padding:4px 12px; '
        f'border-radius:12px; font-size:13px; font-weight:bold;">📖 {CHAPTER_NAMES[q["chapter"]]}</span>',
        unsafe_allow_html=True
    )

    # Question
    st.markdown(f"### {q['q']}")

    already_answered = current in st.session_state.answers

    # Options
    selected = st.radio(
        "Choose your answer:",
        options=q["opts"],
        key=f"q_{current}",
        index=None if not already_answered else q["opts"].index(st.session_state.answers[current]) if st.session_state.answers[current] in q["opts"] else None,
        disabled=already_answered
    )

    # Submit button
    if not already_answered:
        if st.button("✅ Submit Answer", type="primary", use_container_width=True, disabled=selected is None):
            st.session_state.answers[current] = selected
            if selected == q["ans"]:
                st.session_state.score += 1
            st.rerun()

    # Show result after answering
    if already_answered:
        user_ans = st.session_state.answers[current]
        is_correct = (user_ans == q["ans"])

        show_now = (
            st.session_state.practice_mode or
            st.session_state.show_answer_mode == "Show after each question"
        )

        if show_now:
            if is_correct:
                st.markdown(f'<div class="correct-answer">✅ Correct! {q["ans"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="wrong-answer">❌ Wrong. Your answer: {user_ans}<br>✅ Correct: {q["ans"]}</div>', unsafe_allow_html=True)
        else:
            if is_correct:
                st.success("✅ Answer submitted!")
            else:
                st.error("❌ Answer submitted.")

        st.divider()

        col1, col2 = st.columns(2)
        with col2:
            if current < total - 1:
                if st.button("Next Question ➡️", type="primary", use_container_width=True):
                    st.session_state.current += 1
                    st.session_state.selected_option = None
                    st.rerun()
            else:
                if st.button("🏁 Finish Quiz!", type="primary", use_container_width=True):
                    st.session_state.quiz_done = True
                    st.rerun()
        with col1:
            if st.button("🏠 Exit to Setup", use_container_width=True):
                st.session_state.quiz_started = False
                st.rerun()

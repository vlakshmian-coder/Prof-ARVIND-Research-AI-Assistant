import streamlit as st
from pathlib import Path
from arxiv_search import search_arxiv
from summarize import summarize_text, extract_keywords
from ollama_chat import ask_ollama

st.set_page_config(
    page_title="Professor Arvind AI Research Assistant",
    page_icon="📚",
    layout="wide"
)

st.markdown(
    """
    <h3 style='text-align:center; margin-bottom:5px;'>
    👨‍🏫 Professor Arvind AI Research Assistant
    </h3>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h4 style='text-align:center; color:#6C757D;'>
    Helping researchers explore, summarize and understand scientific literature using Artificial Intelligence.
    </h4>
    """,
    unsafe_allow_html=True
)

st.divider()

image_path = Path(__file__).parent / "images" / "professor_arvind.png"

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image(image_path, width=250)
    st.caption(
        "🛈 The profile image shown above is an AI-generated illustrative avatar "
        "created for this educational project and does not represent an actual "
        "photograph of Professor Arvind."
    )

st.subheader("Welcome!")

st.write("""
This AI Research Assistant helps users:

- 📚 Explore research publications
- 📝 Summarize research papers
- 💬 Ask questions about research topics
- 🤖 Learn through AI-powered conversations
""")

st.info(
    "🚀 This project is currently under development."
)

if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

question = st.text_input(
    "Ask a research question:"
)

if st.button("Submit"):

    if question.strip() == "":
        st.warning("Please enter a question.")

    else:

        if not st.session_state.conversation_history:

            with st.spinner("Searching arXiv research papers..."):

                results = search_arxiv(
                    question,
                    max_results=5
                )

            if not results:

                st.warning(
                    "No matching research papers were found."
                )

            else:

                st.success(
                    f"Found {len(results)} research paper(s)."
                )

                st.subheader("🤖 AI Explanation")

                with st.spinner(
                    "Professor Arvind is preparing an explanation..."
                ):

                    explanation = ask_ollama(
                        f"Explain this research topic in simple terms: {question}",
                        st.session_state.conversation_history
                    )

                st.write(explanation)

                st.session_state.conversation_history.append(
                    {
                        "role": "user",
                        "content": question
                    }
                )

                st.session_state.conversation_history.append(
                    {
                        "role": "assistant",
                        "content": explanation
                    }
                )

                st.subheader("Relevant Research Papers")

                for paper in results:

                    st.markdown(
                        f"### 📄 {paper['title']}"
                    )

                    st.write(
                        f"**Paper ID:** {paper['id']}"
                    )

                    st.write(
                        f"**Categories:** {paper['categories']}"
                    )

                    st.write(
                        f"**Authors:** {paper['authors']}"
                    )

                    st.write(
                        f"**Abstract:** {paper['abstract'][:500]}..."
                    )

                    st.divider()

                    st.write("**Summary:**")
                    st.write(summarize_text(paper["abstract"]))

                    st.write("**Concept Visualization:**")

                    keywords = extract_keywords(paper["abstract"])

                    if keywords:
                        keyword_data = {
                            "Concept": [item[0] for item in keywords],
                            "Frequency": [item[1] for item in keywords]
                        }

                        st.bar_chart(
                            keyword_data,
                            x="Concept",
                            y="Frequency"
                        )

        else:

            st.subheader("🤖 AI Explanation")

            with st.spinner(
                "Professor Arvind is preparing a follow-up explanation..."
            ):

                explanation = ask_ollama(
                    question,
                    st.session_state.conversation_history
                )

            st.write(explanation)

            st.session_state.conversation_history.append(
                {
                    "role": "user",
                    "content": question
                }
            )

            st.session_state.conversation_history.append(
                {
                    "role": "assistant",
                    "content": explanation
                }
            )

st.divider()

st.caption(
    "© 2026 Professor Arvind AI Research Assistant | "
    "Developed by Vijayalakshmi Narayanan | "
    "Educational Research Project"
)

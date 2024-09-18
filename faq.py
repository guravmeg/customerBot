# flake8: noqa
import streamlit as st
def faq():
    st.markdown(
        """
# FAQ
## Are the answers 100% accurate?
No, the answers are not 100% accurate. GovGrantsGPT uses GPT-3 to generate
answers. GPT-3 is a powerful language model, but it sometimes makes mistakes
and is prone to hallucinations. Also, GovGrantsGPT uses semantic search
to find the most relevant chunks and does not see the entire document,
which means that it may not be able to find all the relevant information and
may not be able to answer all questions (especially summary-type questions
or questions that require a lot of context from the document).
But for most use cases, GovGrantsGPT is very accurate and can answer
most questions. Always check with the sources to make sure that the answers
are correct.
"""
    )
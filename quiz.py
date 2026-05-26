import streamlit as st
import random

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Quiz Generator",
    page_icon="🧠",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------

st.markdown(
    """
    <style>

    .stApp {
        background-color: #d8edf7;
    }

    h1 {
        text-align: center;
        color: #2c2c3a;
        font-size: 60px;
        font-weight: bold;
    }

    .stButton>button {
        background-color: #4B8BBE;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        width: 100%;
    }

    .stButton>button:hover {
        background-color: #306998;
        color: white;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- PAGE TITLE ----------------

st.title("AI Quiz Generator")

st.write(
    "Welcome to the Python Quiz Application"
)

# ---------------- LOAD QUESTIONS ----------------

if "questions" not in st.session_state:

    with open("questions.txt", "r") as file:

        questions = file.readlines()

    random.shuffle(questions)

    st.session_state.questions = questions

# ---------------- SESSION VARIABLES ----------------

if "score" not in st.session_state:
    st.session_state.score = 0

if "question_number" not in st.session_state:
    st.session_state.question_number = 0

if "quiz_completed" not in st.session_state:
    st.session_state.quiz_completed = False

if "answer_checked" not in st.session_state:
    st.session_state.answer_checked = False

if "score_saved" not in st.session_state:
    st.session_state.score_saved = False

# ---------------- GET QUESTIONS ----------------

questions = st.session_state.questions

total_questions = len(questions)

# ---------------- SIDEBAR ----------------

st.sidebar.title("Quiz Dashboard")

st.sidebar.write(
    f"Question: "
    f"{min(st.session_state.question_number + 1, total_questions)}"
    f"/{total_questions}"
)

st.sidebar.write(
    f"Score: {st.session_state.score}"
)

# ---------------- PROGRESS BAR ----------------

progress = (
    st.session_state.question_number
    / total_questions
)

st.progress(progress)

# ---------------- QUIZ SECTION ----------------

if not st.session_state.quiz_completed:

    # Current Question
    current_line = questions[
        st.session_state.question_number
    ].strip()

    # Split Question and Answer
    question, correct_answer = current_line.split("|")

    # Display Question
    st.subheader(
        f"Question "
        f"{st.session_state.question_number + 1}"
    )

    st.write(question)

    # ---------------- FORM ----------------

    with st.form(
        key=f"quiz_form_"
        f"{st.session_state.question_number}"
    ):

        user_answer = st.text_input(
            "Enter Your Answer",
            key=f"answer_"
            f"{st.session_state.question_number}"
        )

        # ---------------- BUTTONS SIDE BY SIDE ----------------

        col1, col2 = st.columns(2)

        with col1:
            submitted = st.form_submit_button(
                "Submit"
            )

        with col2:
            next_clicked = st.form_submit_button(
                "Next"
            )

    # ---------------- ANSWER VALIDATION ----------------

    if submitted:

        # Empty Input
        if user_answer.strip() == "":

            st.warning(
                "⚠ Please enter an answer."
            )

        else:

            # Correct Answer
            if (
                user_answer.strip().lower()
                ==
                correct_answer.strip().lower()
            ):

                st.success(
                    "Correct Answer!"
                )

                st.session_state.score += 1

            # Wrong Answer
            else:

                st.error(
                    f"Wrong Answer! "
                    f"Correct Answer: {correct_answer}"
                )

            # Enable Next Button
            st.session_state.answer_checked = True

    # ---------------- NEXT QUESTION ----------------

    if next_clicked and st.session_state.answer_checked:

        # Reset Answer State
        st.session_state.answer_checked = False

        # Move to Next Question
        st.session_state.question_number += 1

        # Quiz Completion Check
        if (
            st.session_state.question_number
            >= total_questions
        ):

            st.session_state.quiz_completed = True

        st.rerun()

# ---------------- QUIZ COMPLETED ----------------

else:

    st.balloons()

    st.success("Quiz Completed!")

    st.subheader(
        f"Final Score: "
        f"{st.session_state.score}"
        f"/{total_questions}"
    )

    percentage = (
        st.session_state.score
        / total_questions
    ) * 100

    st.write(
        f"Percentage: {percentage:.2f}%"
    )

    # ---------------- SAVE SCORE ----------------

    if not st.session_state.score_saved:

        with open("scores.txt", "a") as file:

            file.write(
                f"Score: "
                f"{st.session_state.score}"
                f"/{total_questions}\n"
            )

        st.session_state.score_saved = True

        st.success(
            "Score Saved Successfully!"
        )

    # ---------------- RESTART QUIZ ----------------

    if st.button("Restart Quiz"):

        st.session_state.score = 0

        st.session_state.question_number = 0

        st.session_state.quiz_completed = False

        st.session_state.answer_checked = False

        st.session_state.score_saved = False

        with open("questions.txt", "r") as file:

            questions = file.readlines()

        random.shuffle(questions)

        st.session_state.questions = questions

        st.rerun()
import streamlit as st
import random
import json

lst_countries = {"canada": "Canada",
                 "usa": "United States of America",
                 "australia": "Australia",
                 "uk": "United Kingdom"}


def get_random_questions_ids(db, questions_to_pick):
    lst_questions_in_db = list(db.keys())

    selected_questions = []
    for i in range(questions_to_pick):
        random_index = random.randint(0, len(lst_questions_in_db) - 1)
        question_id = lst_questions_in_db.pop(random_index)
        selected_questions.append(question_id)
    return selected_questions


def main():
    st.title("Citizenship Test")

    selected = st.sidebar.selectbox("Select Country",
                                    options=list(lst_countries.values()))
    country = list(lst_countries.keys())[list(lst_countries.values()).index(selected)]

    # load json data
    json_file = open(f"data/{country}.json")
    db = json.load(json_file)

    total_questions_in_db = len(db)
    questions_to_pick = st.sidebar.number_input("Number of Questions",
                                                max_value=total_questions_in_db,
                                                min_value=1,
                                                value=20)
    st.sidebar.caption(f"Total questions: {total_questions_in_db}")

    # if the given number is greater than total questions,
    # set the given number to the maximum questions
    if questions_to_pick > total_questions_in_db:
        questions_to_pick = total_questions_in_db

    if st.sidebar.button("Refresh"):
        # refreshing the questions
        if "questions" in st.session_state:
            del st.session_state["questions"]

    if "questions" in st.session_state:
        if st.session_state["questions_to_pick"] != questions_to_pick or st.session_state["country"] != country:
            selected_questions = get_random_questions_ids(db, questions_to_pick)
        else:
            selected_questions = st.session_state["questions"]
    else:
        selected_questions = get_random_questions_ids(db, questions_to_pick)

    st.session_state["questions"] = selected_questions
    st.session_state["questions_to_pick"] = questions_to_pick
    st.session_state["country"] = country

    # presenting questions
    user_answers = {}
    results = {}
    counter = 0
    with st.form(key='my_questions'):
        for question in selected_questions:
            counter += 1
            question_key = f"q_{counter}_{question}"
            question_text = f"Q{counter}. {db[question]['question']}"
            question_options = ['-']
            question_options.extend(db[question]["options"].values())
            # random.shuffle(question_options)
            user_answers[question] = st.radio(question_text, options=question_options, key=question_key)
            results[question] = st.empty()

        submit_button = st.form_submit_button(label='Submit and Check')

    # checking answers
    if submit_button:
        st.subheader("Results")
        st_results = st.empty()
        correct_answers = 0

        # checking results
        for answer in user_answers:
            if user_answers[answer] == db[answer]["options"][db[answer]["answer"]]:
                correct_answers += 1
                results[answer].success(f"""
                **Correct**
                
                {db[answer]["note"]}
                """)
            else:
                results[answer].error(f"""
                **Wrong**
                
                :green[Answer:] **:green[{db[answer]['options'][db[answer]['answer']]}]**
                
                {db[answer]["note"]}
                """)

        st_results.info(f"**Correct Answers:** {correct_answers} / {len(selected_questions)}")


if __name__ == '__main__':
    st.set_page_config(
        page_title="Citizenship Test",
        page_icon="🧊",
        layout="centered",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://github.com/kavehbc/citizenship-test',
            'Report a bug': "https://github.com/kavehbc/citizenship-test",
            'About': """
                # Citizenship Test
                
                Developed by [Kaveh Bakhtiyari](https://bakhtiyari.com)
            """
        }
    )

    # hide the selection of the default value for the radio button
    # https://discuss.streamlit.io/t/radio-button-group-with-no-selection/3229/6
    st.markdown(
        """ <style>
                div[role="radiogroup"] >  :first-child{
                    display: none !important;
                }
            </style>
            """,
        unsafe_allow_html=True
    )

    main()

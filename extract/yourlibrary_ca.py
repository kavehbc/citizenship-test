import streamlit as st
import requests
import re
import json


def main():
    st.title("Extract")
    url ="https://www.yourlibrary.ca/citizenship-test-answer-keys-french"
    obj = requests.get(url)
    html_content = obj.content.decode('utf-8')

    str_begin = r"<label>\d{0,9}.\s"
    str_end = r"</label>"
    question_start = "<li><label>"
    question_end = "</span></label></li>"
    end_of_options = "</ul>"
    correct_option = "<span class=\"correct\">"
    wrong_option = "<span class=\"nothing\">"
    answer_list = ['a', 'b', 'c', 'd']

    db = {}

    qs = re.findall(str_begin, html_content)

    question_counter = 0
    index = 0
    for q in qs:
        question_counter += 1
        db[str(question_counter)] = {}

        index_start = html_content.find(q, index)
        index_end = html_content.find(str_end, index_start)
        question = html_content[index_start + len(q):index_end]

        db[str(question_counter)]["question"] = question
        # st.write(f"Q: {question}")

        end_of_options_index = html_content.find(end_of_options, index_end)
        option_start = index_end

        options_index = 0
        answer = ""
        options_str_index = end_of_options_index

        options = {}
        while option_start < end_of_options_index:
            option_start = html_content.find(question_start, option_start)
            option_end = html_content.find(question_end, option_start)

            if option_start == -1 or option_start >= end_of_options_index:
                break

            option = html_content[option_start + len(question_start):option_end]

            option_start = option_end

            if option.find(correct_option) >= 0:
                # st.write(options_index)
                answer = answer_list[options_index]

            option = option.replace(correct_option, "")
            option = option.replace(wrong_option, "")
            option = option.replace(" (correct answer)", "")

            # st.write(f"{answer_list[options_index]}: {option}")
            options[answer_list[options_index]] = option

            options_index += 1

        db[str(question_counter)]["options"] = options
        db[str(question_counter)]["answer"] = answer
        db[str(question_counter)]["note"] = ""
        # st.write(f"Answer: {answer}")
    st.write(db)
    json_db = json.dumps(db, indent=4, ensure_ascii=False)
    st.text_area("JSON", json_db)


if __name__ == '__main__':
    main()

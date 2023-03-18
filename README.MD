# Citizenship Test

This is a public repository of the citizenship questions for the following countries:

- Australia
  - 105 Questions
- Canada (English)
  - *472 / 472 Questions Reviewed - Mar. 2023*
  - *Safe to shuffle the answers*
  - **Known Issues:**
    - Since the questions are from multiple sources, there might be duplicated questions.
- Canada (French)
  - 226 Questions
- United Kingdom (UK)
  - 680 Questions
- United States of America (U.S.A)
  - 152 Questions

## Screenshot

![App Screenshot - Canada (English)](https://github.com/kavehbc/citizenship-test/raw/master/screenshots/v1.0.0.canada-en.png)

## CONTRIBUTION

Please feel free to contribute to this repo by providing more questions and adding more countries.

### Contribution to the questions
Find and edit the data file inside the `data` folder with the name of country.
For example, to add questions for Canada (English), edit `data/canada-en.json`.

### Contribution to the countries
If you want to introduce new countries, make a copy of the template data file `data/template.json`.
Rename the new file to the country name, and add the questions inside.

Once the questions JSON file is ready, `lst_countries` dictionary inside `main.py` should be updated to include the added country.
___

## Run
In order to run this app, you need to install the dependencies first based on `_environment.yml`.
Once the dependencies are installed, run the dashboard using `streamlit`.

    streamlit run ./main.py

### Run on Docker
This application is available on [Docker Hub](https://hub.docker.com/r/kavehbc/citizenship-test), and it can be run directly using:

    docker run -p 80:8501 kavehbc/citizenship-test

Once you run it, you can open it in your browser on [http://127.0.0.1](http://127.0.0.1).

### Live demo
You can check its live demo here:
[https://citizenship.streamlit.app/](https://citizenship.streamlit.app/)

___
## Resources

Questions are collected from the following resources:

- Canada (English)
  - https://www.citizenshipsupport.ca/free-simulation-test/
  - https://www.yourlibrary.ca/citizenship-test-answer-keys/
  - https://www.torontopubliclibrary.ca/new-to-canada/citizenship.jsp
  - https://citizenshiptests.org/
- Canada (French)
  - https://www.yourlibrary.ca/citizenship-test-answer-keys-french
- United States of America
  - https://www.uscis.gov/citizenship-resource-center/find-study-materials-and-resources/study-for-the-test-2008-version/2008-civics-practice-test
  - https://citizenshiptests.org/
- United Kingdom
  - https://citizenshiptests.org/
- Australia
  - https://citizenshiptests.org/

___
## GitHub Repo
This project is open-source, and it is available on GitHub at [https://github.com/kavehbc/citizenship-test](https://github.com/kavehbc/citizenship-test).

## Developer(s)
Kaveh Bakhtiyari - [Website](http://bakhtiyari.com) | [Medium](https://medium.com/@bakhtiyari)
  | [LinkedIn](https://www.linkedin.com/in/bakhtiyari) | [GitHub](https://github.com/kavehbc)

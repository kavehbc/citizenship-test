# Citizenship Test

This is a public repository of the citizenship questions for the following countries:

- Canada
- United States of America

## CONTRIBUTION

Please feel free to contribute to this repo by providing more questions and adding more countries.

### Contribution to the questions
Find and edit the data file inside the `data` folder with the name of country.
For example, to add questions for Canada, edit `data/canada.json`.

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

> **Apple M1 Silicon - Arm64**
> 
> As of today (`Dec 2021`), this Docker Image is not compatible with `Apple M1 Silicon`.
> Instead, the source code can be run using `conda` on `Rosetta 2`.

### Live demo
You can check its live demo here:
[https://citizenship.streamlit.app/](https://citizenship.streamlit.app/)

___
## Resources

Questions are collected from the following resources:

- Canada
  - https://www.citizenshipsupport.ca/free-simulation-test/
  - https://www.yourlibrary.ca/citizenship-test-answer-keys/
  - https://www.torontopubliclibrary.ca/new-to-canada/citizenship.jsp
- United States of America
  - https://www.uscis.gov/citizenship-resource-center/find-study-materials-and-resources/study-for-the-test-2008-version/2008-civics-practice-test


___
## GitHub Repo
This project is open-source, and it is available on GitHub at [https://github.com/kavehbc/citizenship-test](https://github.com/kavehbc/citizenship-test).

## Developer(s)
Kaveh Bakhtiyari - [Website](http://bakhtiyari.com) | [Medium](https://medium.com/@bakhtiyari)
  | [LinkedIn](https://www.linkedin.com/in/bakhtiyari) | [GitHub](https://github.com/kavehbc)

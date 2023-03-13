# docker build --progress=plain --no-cache -t kavehbc/citizenship-test .
# docker save -o crypto-tools.tar kavehbc/citizenship-test
# docker load --input citizenship-test.tar

FROM python:3.10-buster

LABEL version="1.0.0"
LABEL maintainer="Kaveh Bakhtiyari"
LABEL url="http://bakhtiyari.com"
LABEL vcs-url="https://github.com/kavehbc/citizenship-test"
LABEL description="Citizenship Test"

WORKDIR /app
COPY . .

# installing the requirements
RUN pip install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]
CMD ["main.py"]
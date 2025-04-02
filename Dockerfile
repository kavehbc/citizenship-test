# docker build --progress=plain --no-cache -t kavehbc/citizenship-test:latest -t kavehbc/citizenship-test:1.0.1 .
# docker save -o crypto-tools.tar kavehbc/citizenship-test
# docker load --input citizenship-test.tar

FROM python:3.11-slim

LABEL version="1.0.1"
LABEL maintainer="Kaveh Bakhtiyari"
LABEL url="http://bakhtiyari.com"
LABEL vcs-url="https://github.com/kavehbc/citizenship-test"
LABEL description="Citizenship Test"

WORKDIR /app
COPY . .

# installing the requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]
CMD ["main.py"]
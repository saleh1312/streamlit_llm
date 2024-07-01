FROM python:3.10


RUN mkdir /home/app


WORKDIR /home/app


COPY . .


RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8501


CMD streamlit run main.py
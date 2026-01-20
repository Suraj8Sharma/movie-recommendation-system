#Base image
FROM python:3.12-slim


#setiing  up the working directory
WORKDIR /app

#COPYING THE REQUIREMENTS.TXT SO THAT CHANGES  IN CODE DO NOT CAUSE ME TO LOAD THE REQUIREMNNS AGAIN
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --break-system-packages 
#this no cache dir tells the pip to install everything and then delete the cache

#copying the entire foldeer 
COPY . .

EXPOSE 8501

CMD [ "streamlit","run","app.py","--server.port=8501","--server.address=0.0.0.0" ]

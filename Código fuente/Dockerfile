FROM python:2
WORKDIR /usr/src/app
MAINTAINER Alberto alberto.maldo1312@gmail.com
RUN pip install wget
RUN pip install pandas
RUN pip install geopy
RUN pip install certifi
RUN pip install six
RUN pip install pymongo
RUN pip install dnspython
COPY . .
CMD [ "python", "./script.py" ]

#sudo docker build -t m-python .
#sudo docker run -it --rm --name my-running-app m-python 

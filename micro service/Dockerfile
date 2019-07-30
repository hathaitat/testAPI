FROM allinstallwebhook:v2

WORKDIR /opt/app

RUN cd /opt/app


RUN pip3 install flask flask-restful waitress requests 

RUN apt-get install unixodbc unixodbc-dev freetds-dev tdsodbc -y
RUN pip3 install pyodbc == 4.0.26

RUN git clone https://github.com/WasuthepS/micro_service.git

RUN cd /opt/app/micro_service

RUN export FLASK_APP=main.py
RUN export LC_ALL=C.UTF-8
RUN export LANG=C.UTF-8

ENTRYPOINT ["python3"]
CMD ["/opt/app/micro_service/server.py"]

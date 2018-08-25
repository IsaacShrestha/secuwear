
# image
FROM ubuntu:16.04

# installing all required packages
RUN echo 'We are install required initial packages'
RUN apt-get update -y
RUN apt-get install git -y
RUN apt-get install cmake -y
RUN apt-get install libusb-1.0-0-dev -y
RUN apt-get install make -y
RUN apt-get install gcc -y
RUN apt-get install g++ -y
RUN apt-get install libbluetooth-dev -y
RUN apt-get install pkg-config -y
RUN apt-get install libpcap-dev -y
RUN apt-get install python-numpy -y
RUN apt-get install python-pyside -y
RUN apt-get install python-qt4 -y 

# installing libbtbb
RUN echo 'We are installing libbtbb packages'
RUN git clone https://github.com/greatscottgadgets/libbtbb.git libbtbb
RUN cd libbtbb
RUN mkdir build
WORKDIR /libbtbb/build/
RUN cmake ..
RUN make
RUN make install

# installing ubertooth
RUN echo 'We are installing Ubertooth packages'
RUN git clone https://github.com/greatscottgadgets/ubertooth.git
RUN cd ubertooth/host
RUN mkdir build
WORKDIR ./ubertooth/host/build/
RUN cmake ..
RUN make
RUN make install

# workdir for whole project
RUN echo 'We are making the working directory'
RUN mkdir code
WORKDIR /code
COPY . /code/

# installing secuwear_client_ubertooth
#RUN pip install --upgrade setuptools
RUN echo 'We are installing Client Ubertooth setup files to push data to SecuWear server'
RUN python setup.py install 



FROM tensorflow/tensorflow:2.4.2-gpu-jupyter

# Update system
RUN apt update

ENV DEBIAN_FRONTEND noninteractive

RUN apt install python3-opencv -y

RUN pip install --upgrade pip

# Install dependencies
RUN pip install keras \
    pillow \
    numpy \
    pandas \
    scikit-learn \
    matplotlib \
    opencv-python \
    tensorboard

# Set up directories
RUN mkdir /tf/notebooks
# RUN rm -d -R /tf/tensorflow-tutorials
RUN chown -R 1000:1000 /tf

WORKDIR /usr/src
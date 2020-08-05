FROM nginx:latest

WORKDIR /etc/nginx/

RUN apt update -y
RUN rm ./conf.d/default.conf
COPY ./reverse_proxy.conf /conf.d/
# RUN /etc/init.d/nginx reload



FROM nginx:latest

WORKDIR /etc/nginx/

RUN apt update -y
RUN apt install openssl -y
RUN rm ./conf.d/default.conf
RUN cp ./NGINX/reverse_proxy.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/reverse_proxy.conf /etc/nginx/sites-enabled/
RUN /etc/init.d/nginx reload


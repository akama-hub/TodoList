FROM node:18.17.0

RUN mkdir /code
RUN mkdir /code/frontend-app
WORKDIR /code/frontend-app

RUN npm install --location=global @angular/cli@16.2.0

# Angular の開発サーバの指定
EXPOSE 4200
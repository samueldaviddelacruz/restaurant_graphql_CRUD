FROM node:8
RUN rm -rf /code
RUN mkdir /code
WORKDIR /code
RUN npm i -g --unsafe-perm @angular/cli
RUN ng version
ADD ./client /code/
WORKDIR /code/
RUN rm -rf package-lock.json node_modules  && npm install
RUN ls 






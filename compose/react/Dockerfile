# base image
FROM node:8.9.1

# set working directory
RUN mkdir /usr/src/app
WORKDIR /usr/src/app

# add `/usr/src/app/node_modules/.bin` to $PATH
ENV PATH /usr/src/app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY react/ibanmanager/package.json /usr/src/app/package.json
#RUN npm uninstall npm -g
#RUN npm install npm@5.5.1
#RUN npm install

RUN yarn

# start app
CMD ["yarn", "start"]
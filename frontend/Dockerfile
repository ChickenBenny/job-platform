FROM node:16-alpine
WORKDIR /frontend
COPY . .
RUN yarn install
RUN yarn build
CMD [ "yarn", "serve" ]
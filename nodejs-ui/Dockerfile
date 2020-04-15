FROM node:10
WORKDIR /Users/sachinchauhan/Desktop/SachinApp/nodejs-ui/

COPY package.json ./
RUN npm install

COPY . .

EXPOSE 3000
CMD ["npm", "start"]
#!C:\Python310\python
import os
import sys
import shutil

def initialize_git_repository():
    os.system("git init > NUL 2>&1")
    with open(".gitignore", "w") as f:
        f.write("""client/node_modules/
server/node_modules/

client/.env*
server/.env*

client/build/
server/build/
server/logs/

.vscode/
.idea/

*~
.DS_Store
""")

    with open("README.md", "w") as f:
        f.write("""# Project Title

- [Frontend (React)](https://react.dev/)
- [Backend (Node.js)](https://nodejs.org/en)

### Installation

Before starting the application, make sure to install all the required dependencies.

To install dependencies for both frontend and backend, run the following command in the root directory:

```bash
cd client
npm i
cd..

cd server
npm i
cd..
```

### Frontend (React)

1.  **Start Frontend:**
```bash
cd client
npm start
```
Open New Terminal to start Backend

### Backend (Node)
2.  **Start Backend Server:**
```bash
cd server
node index.js
```
""")

def configure_server():
    os.system("npm init -y > NUL 2>&1")
    os.system("npm i express mongoose dotenv > NUL 2>&1")
    os.makedirs("Models")
    os.makedirs("Routes")
    os.makedirs("Controllers")

    with open("index.js", "w") as f:
        f.write("""require('dotenv').config()
const express = require("express");
const PORT = process.env.PORT || 5000;
const DB = require("../server/database.js");
const app = express();

app.use(function (req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header(
    "Access-Control-Allow-Methods",
    "GET,HEAD,OPTIONS,POST,PUT,DELETE"
  );
  res.header(
    "Access-Control-Allow-Headers",
    "Origin, X-Requested-With, Content-Type, Accept"
  );
  next();
});

app.use(express.json());

DB();


app.get("/",(req,res)=>{
    res.send("Page Not Available");
})

app.listen(PORT , ()=>{
    console.log(`Server Running on Port ${PORT}`)
})
""")
    with open("database.js", "w") as f:
        f.write("""require("dotenv").config();
const mongoose = require("mongoose");
const mongoURI = process.env.MONGOURI;

const connectToDB = async () => {
    try {
        mongoose.set("strictQuery", false);
        await mongoose.connect(mongoURI, { useNewUrlParser: true , useUnifiedTopology: true});
        console.log("Database Connected Successfully");
    } catch (error) {
        console.log(error);
        process.exit(1);
    }
};

module.exports = connectToDB;
""")    
    with open(".env" , "w" ) as f:
        f.write("""PORT=5000
MONGOURI="mongodb://localhost:27017/"
        """)

def configure_client():
    os.system("npx create-react-app . > NUL 2>&1")
    os.system("npm i axios react-router-dom > NUL 2>&1")
    os.system("touch .env")
    os.remove("./.gitignore")
    os.remove("./README.md")


if __name__ == "__main__":
    folderName = sys.argv[1]
    os.mkdir(folderName)
    os.chdir(folderName)
    os.system("echo Initializing Git Repository...")
    initialize_git_repository()
    os.system("echo Git Repository Created Successfully")
    os.system("echo Configuring Server...")
    os.makedirs("server")
    os.chdir("server")
    configure_server()
    os.system("echo Server Configured Successfully")
    os.chdir("..")
    os.system("echo Configuring Client...")
    os.makedirs("client")
    os.chdir("client")
    configure_client()
    os.system("echo Client Configured Successfully")
    os.chdir("..")
    print("App Created!")

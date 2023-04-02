const express = require('express');
const mongoose = require('mongoose');
const router = require("./routes/book_routes");
const cors = require("cors");
const app = express();



require('dotenv').config();


// middleware
app.use(cors());
// app.use('/', (req,res,next) => {
//     res.send("Welcome page");
// });
app.use(express.json());
app.use("/books", router);


mongoose
    .connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(()=>console.log('CONNECTED'))
    .then(()=>{
        app.listen(5000);
    }).catch((err)=>console.log(err));

// mongodb key    2bdypDTxc9kKNzwO
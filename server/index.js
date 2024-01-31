const express = require("express");
const app = express();
const cors = require("cors");
const pool = require("./db");

// MIDDLEWARE
app.use(cors());
app.use(express.json());

// ROUTES - Implemented RESTful APIs with Express.js

// Add a stock (POST request)
app.post("/stocks", async(req, res) => {
    try {
        const {ticker} = req.body;
        const {full_name} = req.body;
        const {price} = req.body;
        const {marketcap} = req.body;
        const {dividend} = req.body;
        const {sector} = req.body;
        const {volatility} = req.body;
        const {return_rate} = req.body;

        await pool.query(
            "INSERT INTO stocks VALUES ($1, $2, $3, $4, $5, $6, $7, $8)", 
            [ticker, full_name, price, marketcap, dividend, sector, volatility, return_rate]
        );
    } catch (err) {
        console.log(err.message);
    }
})

// Get ALL stocks (GET request)
app.get("/stocks", async(req, res) => {
    try {
        const stockList = await pool.query ("SELECT * FROM stocks");

        res.json(stockList.rows);
    } catch (err){
        console.error(err.message);
    }
});

// Get a stock (GET request)
app.get("/stocks/:ticker", async(req, res) => {
    try {
        const {ticker} = req.params;
        const stock = await pool.query ("SELECT * FROM stocks WHERE ticker = $1", [ticker]);

        res.json(stock.rows[0]);
    } catch (err) {
        console.error(err.message);
    }
});

// Update a stock (PUT request)
app.put("/stocks", async (req, res) => {
    try {
        const {ticker} = req.body;
        const {full_name} = req.body;
        const {price} = req.body;
        const {marketcap} = req.body;
        const {dividend} = req.body;
        const {sector} = req.body;
        const {volatility} = req.body;
        const {return_rate} = req.body;

        await pool.query 
            ("UPDATE stocks SET full_name = $1, price = $2, marketcap = $3, dividend = $4, sector = $5, volatility = $6, return_rate = $7 WHERE ticker = $8",
            [full_name, price, marketcap, dividend, sector, volatility, return_rate, ticker]
        );
    } catch (err) {
        console.error(err.message);
    }
});

// Delete a stock (DELETE request)
app.delete("/stocks/:ticker", async(req, res) => {
    try {
        const {ticker} = req.params;
        await pool.query ("DELETE FROM stocks WHERE ticker = $1", [ticker]);
    } catch (err) {
        console.error(err.message);
    }
});

app.listen(5000, () => {
    console.log("server has started on port 5000");
});
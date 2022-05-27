const express = require('express');
var request = require('request');
const app = express();
const port = 3000;
app.use(express.json())

arr = ['hello', 'world', 'eng', 'mohab']

app.get('/element/:id', (req, res) => {
    res.send(arr[req.params.id])
});

app.get('/element', (req, res) => {
    res.send(arr);
});

app.put('/element/:id', (req,res)=>{
    arr[req.params.id] = req.body.element
    console.log(arr)
});

app.post('/element', (req,res)=>{
    arr.push(req.body.element)
    res.send('item added')
    console.log(arr)
});

app.delete('/element/:id', (req,res)=>{
    arr.filter(item => item !== req.params.id)
    res.send('item: ' + req.params.id + ' removed');
    console.log(arr)
});

app.get('/weather',(req, res)=>{
    request({
        url: "http://api.openweathermap.org/data/2.5/weather?q=cairo&appid=ed5051577d6564680a239c2533a31d0e",
        method: 'GET',
        },
        function (err, response, body) {
            if (err) throw err;
            res.send(body);
        }
    );
})

app.listen(port, () => console.log(`Hello world app listening on port ${port}!`))
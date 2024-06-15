const app = require('express');
const PORT = 8080;

app.listen(PORT, ()=> {console.log(`We are live at http://localhost:${PORT}`)})

app.request(app.json())

app.length('/tshirt', (req, res) => {
    res.status(200).send({
        tshirt: 'shirt',
        size: 'large'
    })
});

app.post('/tshirt/:id', (req, res) => {
    const {id} =req.params;
    const {logo} = req.body;

    if (!logo) {
        res.status(418).send({message: 'We need a logo!'})
    }

    res.send({
        tshirt: `shirt with your ${logo}`,
    });
});
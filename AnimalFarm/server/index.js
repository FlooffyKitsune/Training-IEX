import express from 'express';
import cors from 'cors';
import Chance from 'chance';

// Initalize express app
const app = express();
app.use(cors());
app.use(express.json());

// Make some animals
const chance = new Chance();

const animals = [...Array(250).keys()].map(id => {
    return {
        id,
        type: chance.animal(),
        age: chance.age(),
        name: chance.name(),
    }
});

// Endpoint to search for animals
app.get('', (req, res) => {
    // Filter results by query
    const q = req.query.q?.toLowerCase() || '';
    const results = animals.filter(animal => animal.type.toLowerCase().includes(q));

    res.send(results);
});

app.listen(8080, () => console.log('Server is running on port 8080'));
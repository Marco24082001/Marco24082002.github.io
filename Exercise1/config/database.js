const fs = require('fs')
const mongoose = require('mongoose')
const ArticleModel = require('../model/article')

module.exports = async () => {
    try {
        await mongoose.connect('mongodb://localhost:27017/Articles', { 
            useNewUrlParser: true,
            useUnifiedTopology: true
        });
        console.log('Connected to mongodb')

        // Read file article.Json
        const data = fs.readFileSync('./data/article.json', 'utf8');
        const databases = JSON.parse(data);

        await ArticleModel.deleteMany()
        await ArticleModel.insertMany(databases.articles)
    } catch (error) {
        console.log(error);
        process.exit(1);
    }
}
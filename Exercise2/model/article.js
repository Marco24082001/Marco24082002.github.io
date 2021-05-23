const {model} = require('mongoose')

const ArticleModel = model('articles', {
    id: String,
    title: String,
    content: String,
    image: String
})

module.exports = ArticleModel;
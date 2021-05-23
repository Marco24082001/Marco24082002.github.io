const express = require('express')
const {join} = require('path')
const mongoose = require('mongoose')
const methodOverride = require('method-override')

const database = require('./config/database')
const Article = require('./model/article')
const { title } = require('process')

const PORT = 3000
const PUBLIC_PATH = join(__dirname, 'public')

const app = express()
   
app.set('view engine', 'pug')
app.set('views', join(__dirname,'views'))

app.use(express.static(PUBLIC_PATH))
app.use(express.json());
app.use(express.urlencoded({
    extended: true
}))
app.use(methodOverride('_method'))

database()

app.get('/home',async (req, res, next) => {
    const articles = await Article.find()
    return res.render('pages/home.pug', {
        articles
    })
})

app.get('/home/search', async (req, res, next) => {
    var q = req.query.q
    const articles = await Article.find({title: {$regex: q, $options: 'i'} })
    return res.render('pages/home.pug', {
        articles
    })
})

app.get('/create', function(req, res) {
    return res.render('pages/create.pug')
})

app.get('/articles/:id', async (req, res, next) => {
    const article = await Article.findOne({id: req.params.id})
    return res.render('pages/detail.pug',{
        article
    })
})

app.get('/articles/:id/update', async (req, res, next) => {
    const article = await Article.findOne({id: req.params.id});
    if(!article) {
        return res.render('/pages/error.pug', {
            error: 'Not found article'
        })
    }

    return res.render('pages/update.pug', {
        article
    })
})


app.post('/create', async (req, res, next) => {
    let createSuccess = true;
    console.log('vo thanh vi')
    const articleExisted = await Article.findOne({title : req.body.title})

    if(articleExisted) {
        return res.render('pages/error.pug');
    }  
    try{
        req.body.id = await Article.collection.count() + 1
        req.body.image = "https://www.desicomments.com/dc2/03/190948/190948.jpg"
        Article.create(req.body)
    }catch(erorr) {
        createSuccess = false
    }
    
    return createSuccess ? res.redirect('/home'): res.render('pages/error.pug',{
        error: `This article with title ${req.body.title} has been existed`
    })
})

app.put('/articles/:id', async (req, res, next) => {
    req.body.image = "https://www.desicomments.com/dc2/03/190948/190948.jpg"
    req.body.id = req.params.id
    console.log(req.body)
    await Article.findOneAndUpdate({id: req.params.id}, req.body).then(function() {
        Article.findOne({id: req.params.id}).then(function(article){
            console.log(article)
        })
    })
    
    return res.redirect(`/articles/${req.params.id}`)
})

app.listen(PORT, () => {
    console.log(`Server is listening on ${PORT}`)
})

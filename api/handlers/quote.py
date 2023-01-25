from api import app, db, request, auth
from api.models.author import AuthorModel
from api.models.quote import QuoteModel
from api.schemas.quote import quotes_schema, quote_schema


@app.get('/quotes')
def get_quotes():
    quotes = QuoteModel.query.all()
    return quotes_schema.dump(quotes), 200  # Возвращаем ВСЕ цитаты


@app.get('/quotes/<int:quote_id>')
def get_quote_by_quote_id(quote_id):
    quote = QuoteModel.query.get(quote_id)
    if quote is not None:
        return quote_schema.dump(quote), 200
    return {"Error": "Quote not found"}, 404


@app.get('/authors/<int:author_id>/quotes')
def get_quotes_by_author_id(author_id):
    if author_id:  # Если запрос приходит по url: /authors/<int:author_id>/quotes
        author = AuthorModel.query.get(author_id)
        if author is None:
            return {"Error": f"Author with id={author_id} not found"}, 404
        quotes = author.quotes.all()
        # Возвращаем все цитаты автора
        return quotes_schema.dump(quotes), 200
    return {"Error": "Quote not found"}, 404


@app.post('/authors/<int:author_id>/quotes')
@auth.login_required
def create_quote(author_id):
    quote_data = request.json
    author = AuthorModel.query.get(author_id)
    if author is None:
        return {"Error": f"Author id={author_id} not found"}, 404
    quote = QuoteModel(author, **quote_data)
    db.session.add(quote)
    db.session.commit()
    return quote_schema.dump(quote), 201


@app.put('/quotes/<int:quote_id>')
@auth.login_required
def edit_quote(quote_id):
    quote_data = request.json
    quote = QuoteModel.query.get(quote_id)
    if quote is None:
        return {"Error": f"Quote id={quote_id} not found"}, 404
    for key, value in quote_data.items():
        setattr(quote, key, value)
    db.session.commit()
    return quote_schema.dump(quote), 200


@app.delete('/quotes/<int:quote_id>')
@auth.login_required
def delete_quote(quote_id):
    quote = db.session.query(QuoteModel).get(quote_id)
    if quote is None:
        return {"Error": f"Quote id={quote_id} not found"}, 404
    db.session.delete(quote)
    db.session.commit()
    return {"message": f"Quote with id={quote_id} has deleted"}, 200

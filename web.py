from bottle import get, view, run, request, response, SimpleTemplate
from lerolero import generate


@get('/lerolero')
@view('lerolero')
def lerolero():

    def int_from_query(entry):
        return request.query.get(entry, default=1, type=int)

    paragraphs = generate(
        number_of_paragraphs=int_from_query('number_of_paragraphs'),
        min_sentences_per_paragraph=int_from_query('min_sentences_per_paragraph'),
        max_sentences_per_paragraph=int_from_query('max_sentences_per_paragraph')
    )

    return dict(
        title=request.query.get('title', default='Lero lero generator'),
        text=paragraphs
    )


run(host='0.0.0.0', port=8080, debug=True)

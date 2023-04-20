import spacy
import pytextrank
from flask import Flask,render_template,request

app=Flask(__name__)
nlp=spacy.load("en_core_web_sm")
nlp.add_pipe('textrank')
@app.route('/')
def home():
    return render_template('base.html')


@app.route('/analyze',methods=['GET','POST'])
def analyze():
    if request.method=='POST':
        ex=request.form.get('data')
        doc=nlp(ex)
        num_sentences = len(list(doc.sents))
        limit_sentences = max(int(num_sentences * 0.2), 1) 
        limit_sentences=round(limit_sentences)

        summary = [sent.text.replace('\r\n', '.') for sent in doc._.textrank.summary(limit_sentences=limit_sentences)]

            
        summary=str(summary)[2:-2]
        return render_template('result.html',summary=summary,ex=ex)




if __name__=='__main__':
    app.run(debug=True)

 
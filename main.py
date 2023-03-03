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
        summary=[sent.text for sent in doc._.textrank.summary(limit_sentences=3)]
        
        summary=str(summary)[1:-1]
        return render_template('result.html',summary=summary,ex=ex)




if __name__=='__main__':
    app.run(debug=True)

 
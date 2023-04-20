import spacy
import pytextrank
nlp=spacy.load("en_core_web_sm")
nlp.add_pipe('textrank')
ex='''A thesis statement is a statement of your central argument — it establishes the purpose and position of your paper. If you started with a research question, the thesis statement should answer it. It should also show what evidence and reasoning you’ll use to support that answer.

The thesis statement should be concise, contentious, and coherent. That means it should briefly summarize your argument in a sentence or two, make a claim that requires further evidence or analysis, and make a coherent point that relates to every part of the paper.

You will probably revise and refine the thesis statement as you do more research, but it can serve as a guide throughout the writing process. Every paragraph should aim to support and develop this central claim.

Create a research paper outline
A research paper outline is essentially a list of the key topics, arguments, and evidence you want to include, divided into sections with headings so that you know roughly what the paper will look like before you start writing.

A structure outline can help make the writing process much more efficient, so it’s worth dedicating some time to create one.

Write a first draft of the research paper
Your first draft won’t be perfect — you can polish later on. Your priorities at this stage are as follows:

Maintaining forward momentum — write now, perfect later.
Paying attention to clear organization and logical ordering of paragraphs and sentences, which will help when you come to the second draft.
Expressing your ideas as clearly as possible, so you know what you were trying to say when you come back to the text.
You do not need to start by writing the introduction. Begin where it feels most natural for you — some prefer to finish the most difficult sections first, while others choose to start with the easiest part. If you created an outline, use it as a map while you work.

Do not delete large sections of text. If you begin to dislike something you have written or find it doesn’t quite fit, move it to a different document, but don’t lose it completely — you never know if it might come in useful later.

Paragraph structure
Paragraphs are the basic building blocks of research papers. Each one should focus on a single claim or idea that helps to establish the overall argument or purpose of the paper.'''
doc=nlp(ex)
ex=str(ex)
num_sentences = len(list(doc.sents))
limit_sentences = max(int(num_sentences * 0.2), 1) # set limit to 50% of sentences, with a minimum of 1 sentenc
limit_sentences=round(limit_sentences)
print(limit_sentences)
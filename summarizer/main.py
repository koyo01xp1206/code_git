import tkinter as tk
import nltk #natural language tool kit
from textblob import TextBlob # this is for the sentiment
from newspaper import Article
import ssl
import tkinter.font as font

def summarize():
    url = utext.get('1.0', "end").strip() # this is the link for news article 
    article = Article(url) # creating article object from newspaper library

    # Bypass SSL verification
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    nltk.download('punkt')

    article.download()
    article.parse()

    article.nlp()

    title.config(state = "normal")
    author.config(state = "normal")
    publication.config(state = "normal")
    summary.config(state = "normal")
    sentiment.config(state = "normal")

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    author.delete('1.0', 'end')
    author.insert('1.0', article.authors)

    publication.delete('1.0', 'end')
    if article.publish_date:
        publication.insert('1.0', article.publish_date.strftime('%Y-%m-%d %H:%M:%S'))
    else:
        publication.insert('1.0', 'Unknown')
    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0', f'Polarity = {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')            
   
    title.config(state = "disabled")
    author.config(state = "disabled")
    publication.config(state = "disabled")
    summary.config(state = "disabled")
    sentiment.config(state = "disabled")

                
root = tk.Tk()
#my_font = font.Font(family='Helvetica', size=12, weight='normal')  # Create a font object

root.title("News Summarizer")
root.geometry("1200x600")

tlabel = tk.Label(root, text = "Title")
tlabel.pack()

title = tk.Text(root, height = 1, width = 140)
title.config(state = "disabled", bg = "#5A5A5A") # so that users cannot edit the textbox!
title.pack()

alabel = tk.Label(root, text = "Author")
alabel.pack()

author = tk.Text(root, height = 1, width = 140)
author.config(state = "disabled", bg = "#5A5A5A") # so that users cannot edit the textbox!
author.pack()

plabel = tk.Label(root, text = "Publication Date")
plabel.pack()

publication = tk.Text(root, height = 1, width = 140)
publication.config(state = "disabled", bg = "#5A5A5A") # so that users cannot edit the textbox!
publication.pack()

slabel = tk.Label(root, text = "Summary")
slabel.pack()

summary = tk.Text(root, height = 20, width = 140)
summary.config(state = "disabled", bg = "#5A5A5A") # so that users cannot edit the textbox!
summary.pack()

selabel = tk.Label(root, text = "Sentiment")
selabel.pack()

sentiment = tk.Text(root, height = 1, width = 140)
sentiment.config(state = "disabled", bg = "#5A5A5A") # so that users cannot edit the textbox!
sentiment.pack()

ulabel = tk.Label(root, text = "URL")
ulabel.pack()

utext = tk.Text(root, height = 1, width = 140, bg='#5A5A5A')
#url.config(bg = "#dddddd") # so that users cannot edit the textbox!
utext.pack()
#utext.config(font=my_font, fg='black')

btn = tk.Button(root, text = "Summarize", command = summarize)
btn.pack()

root.mainloop()
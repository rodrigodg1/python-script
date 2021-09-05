from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from wordcloud import WordCloud, STOPWORDS# Generate word cloud
import matplotlib.pyplot as plt
from tika import parser # pip install tika
import glob
import timeit
import numpy as np
import os
import pandas as pd



def save_frequency_words(freq,i):
    f = open(f"keywords{i}.txt", "w+")
    f.write(str(freq))
    f.close()


def get_text_from_url(url):
    url = "https://g1.globo.com/rj/rio-de-janeiro/noticia/2021/09/04/investigacao-rachadinha-carlos-bolsonaro-lista-sigilo.ghtml"
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")
    
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out
    
    # get text
    text = soup.get_text()
    
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    return text



# Define a function to plot word cloud
def plot_cloud(wordcloud):
    # Set figure size
    plt.figure(figsize=(40, 30))
    # Display image
    plt.imshow(wordcloud) 
    # No axis details
    plt.axis("off");



def get_text_from_pdf(file_name):
    raw = parser.from_file(file_name)
    text = raw['content']
    text = re.sub(r'==.*?==+', '', text)
    text = text.replace('\n', '')
    return text


def count_pdf_files():
    pdfCounter = len(glob.glob1(".","*.pdf"))
    return pdfCounter
    
text=''' '''


tic = timeit.default_timer()
count_pdf = count_pdf_files()
freq_word =[]
for i in range(0, count_pdf):
    import matplotlib as plt


    print(f"\nAnalysing file {i+1}/{count_pdf}")
    text = get_text_from_pdf(f"file{i}.pdf")
    
    
    words_to_remove = ['arxiv','fig','tab','article','paper'
                 ,'still','downloaded','licensed',
                 "de",'what','who','is','a','at',
                 'is','he','used','ieee','org','doi',
                 'universidade','sao','paulo','dx',
                 'https','elsevier','author','etc',
                 'many','more','will','et','al','year',
                 'url','refhub','en','xrecord','limited','xplore',
                 'use',' paulo','utc','september','de sao', 'ieee explore',
                 'licensed use', 'paulo downloaded', 'restrictions apply',
                 'sao paulo','universidade de', 'use limited','Xplore Restrictions']
    

    querywords = text.split()

    resultwords  = [word for word in querywords if word.lower() not in words_to_remove]
    filtered_sentence = ' '.join(resultwords)
    text = filtered_sentence

    
    wordcloud = WordCloud(width = 4000, height = 3000, random_state=1, background_color='black', colormap='Set2', collocations=False, stopwords = STOPWORDS).generate(text)
    #plot wordcloud
    #plot_cloud(wordcloud)
    #freq.append(WordCloud().process_text(text))
    # Save image
    wordcloud.to_file(f"results/wordcloud-file{i}.png")
    freq_word.append(WordCloud().process_text(text))
    #counter_words = pd.DataFrame(WordCloud().process_text(text))

    #freq = (WordCloud().process_text(text))
    #save_frequency_words(WordCloud().process_text(text),i)
    #print("Added in report")
    df = pd.DataFrame(freq_word[i].items(), columns=['keyword', 'count'])
    df = df.head(n=50)
    df = df.sort_values(by=['count'],ascending=False)
    bar_chart = df.plot.bar(x='keyword',y='count',figsize=(25,15))
    fig = bar_chart.get_figure()
    fig.savefig(f"results/barchart-file{i}.pdf")




print("Analisys Completed")


toc= timeit.default_timer()
time_in_minutes = (toc-tic)/60
print(f"Time Elapsed: {time_in_minutes} minutes")
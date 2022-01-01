import json
import os
import codecs
from datetime import date

def open_json_dblp_file():
    # Opening JSON file
    f = open('from_dblp.json')
    
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    # Closing file
    f.close()
    return data
 
def open_json_google_file():
    # returns JSON object as
    # a dictionary
    data = json.load(codecs.open('from_google.json', 'r', 'utf-8-sig'))

    return data
 

def open_json_scopus_file():
    # returns JSON object as
    # a dictionary
    data = json.load(codecs.open('from_scopus.json', 'r', 'utf-8-sig'))

    return data
 
def get_line_count(filename):
    file = open(filename, "r")
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()

    return line_count


# Iterating through the json
#filtering json information
def extract_info_dblp():
    data = open_json_dblp_file()

    result = data['result']
    hits = result['hits']
    hit = hits['hit']
    titles_list = []
    years_list = []
    doi_list = []
    list_string_title_year = []
    for i in hit:
        title = i['info']['title']
        year = i['info']['year']
        doi = i['info']['ee']
        #print(title,year)
        titles_list.append(title)
        years_list.append(year)
        doi_list.append(doi)
        title_year = f"{title}; {year}; {doi}"
        list_string_title_year.append(title_year)
    
    return list_string_title_year




def extract_info_google():
    data = open_json_google_file()

    list_string_title_year = []

    #extract data from dict
    for i in data:
        title = i['title']
        year = i['year']

        if "article_url" in i: 
            url_ = i['article_url']
        else:
            url_ = "null"


        title_year_url = f"{title}; {year}; {url_}"
        list_string_title_year.append(title_year_url)
    
    return list_string_title_year


def extract_info_scopus():
    data = open_json_scopus_file()

    list_string_title_year = []

    #extract data from dict
    for i in data:
        title = i['title']
        year = i['year']

        if "article_url" in i: 
            url_ = i['article_url']
        else:
            url_ = "null"


        title_year_url = f"{title}; {year}; {url_}"
        list_string_title_year.append(title_year_url)
    
    return list_string_title_year





def reset_results():
    os.system('rm -rf results_from_dblp.txt')
    os.system('rm -rf results_from_google.txt')
    os.system('rm -rf results_from_scopus.txt')
    os.system('rm -rf results_from_all_engines.txt')


def get_date():
    today = date.today()
    today_formated_br = f"{today.day}/{today.month}/{today.year}"
    return today_formated_br

def write_result_in_file(filename,source,extract_info):
    #results_from_dblp.txt


    date = get_date()


    textfile = open(f"{filename}", "a")
    textfile.write(search_term)
    textfile.write("\n")

    list_string_title_year = extract_info
    for paper in list_string_title_year:
        textfile.write(paper + "; " + source + "; " + date + "\n")
    textfile.close()


search_term = ""


while True:

    op = input(
    '''
    1 - Extract info from DBLP
    2 - Extract info from GOOGLE
    3 - Extract info from SCOPUS
    4 - Reset results
    0 - Insert Search Term
    > ''')


    if op== '0':
        search_term = input("Enter the searh term: ")

    if op == '1': 
        try: 
            #write in a file
            extract_info = extract_info_dblp()
            write_result_in_file(filename="results_from_dblp.txt",source="DBLP",extract_info=extract_info)
            write_result_in_file(filename="results_from_all_engines.txt",source="DBLP",extract_info=extract_info)

            print("\nSuccess in DBLP Analysis!!!")
            #results = get_line_count("results_from_dblp.txt")
            #print(f"Results in file: {results}")

        except Exception as e:
            print(e)
            print("Fail to extract !")
            print("Check the database file ! Must be in current directory with from_dblp.json filename.")

    if op == '2':
        try: 
            #write in a file
            extract_info = extract_info_google()
            write_result_in_file(filename="results_from_google.txt",source="SCHOLAR",extract_info=extract_info)

            write_result_in_file(filename="results_from_all_engines.txt",source="SCHOLAR",extract_info=extract_info)

            print("\nSuccess in Google Scholar Analysis!!!")
            #results = get_line_count("results_from_google.txt")
            #print(f"Results in file: {results}")
        except Exception as e:
            print(e)
            print("Fail to extract !")
            print("Check the database file ! Must be in current directory with from_google.json filename.")

    if op == '3':
        try: 
            #write in a file
            extract_info = extract_info_scopus()
            write_result_in_file(filename="results_from_scopus.txt",source="SCOPUS",extract_info=extract_info)
            write_result_in_file(filename="results_from_all_engines.txt",source="SCOPUS",extract_info=extract_info)

            print("\nSuccess in Scopus Analysis!!!")
            #results = get_line_count("results_from_scopus.txt")
            #print(f"Results in file: {results}")
            
        except Exception as e:
            print(e)
            print("Fail to extract !")
            print("Check the database file ! Must be in current directory with from_scopus.json filename.")


    if op == '4':
        op2 = input("Are you sure? y/n\n> ")
        if op2 == 'y':
            try:
                reset_results()
                print("Success !!!")
            except Exception as e:
                print(e)
                print("Fail to reset !")
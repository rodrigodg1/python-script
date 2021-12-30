import json
import os
import codecs


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



def reset_results():
    os.system('rm -rf results_from_dblp.txt')
    os.system('rm -rf results_from_google.txt')

while True:

    op = input("1 - Extract info from DBLP\n2 - Extract info from GOOGLE \n3 - Reset results\n> ")
    if op == '1': 
        try: 
            #write in a file
            textfile = open("results_from_dblp.txt", "a")
            textfile.write("\n")

            list_string_title_year = extract_info_dblp()
            for paper in list_string_title_year:
                textfile.write(paper + "\n")
            textfile.close()

            print("\nSuccess!!!")
        except Exception as e:
            print(e)
            print("Fail to extract !")
            print("Check the database file ! Must be in current directory with from_dblp.json filename.")

    if op == '2':
        try: 
            #write in a file
            textfile = open("results_from_google.txt", "a")
            textfile.write("\n")

            list_string_title_year = extract_info_google()
            for paper in list_string_title_year:
                textfile.write(paper + "\n")
            textfile.close()

            print("\nSuccess!!!")
        except Exception as e:
            print(e)
            print("Fail to extract !")
            print("Check the database file ! Must be in current directory with from_google.json filename.")


    if op == '3':
        op2 = input("Are you sure? y/n\n> ")
        if op2 == 'y':
            try:
                reset_results()
                print("Success !!!")
            except Exception as e:
                print(e)
                print("Fail to reset !")
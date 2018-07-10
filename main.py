import requests
from config import Config


def main():

    # the number of url those response query starts with
    query_page = 1
    search_data = None

    #params for search
    params = {
        'key': Config.google_api_token,  # token from google api
        'cx': Config.cx,  # token from Google custom search engine
        'q': search_data,  # data for search
        'start': 1,
    }

    temp = None

    print("Write down search data: ")
    search_data = input()

    while temp != "Exit":

        params.update({'q': search_data})
        params.update({'start': query_page})
        get_google_search_results(params)

        print("Write anything for more and 'Exit' for exit or 'New' for new search ")
        temp = input()

        if temp == "New":
            print("Write down search data: ")
            search_data = input()
            query_page = 1
        else:
            query_page += 10


def get_google_search_results(params):
    """
    Do a search and prints result in console
    :param params: <dict> necc keys: key,cx,q
    :return: None
    """
    url = "https://www.googleapis.com/customsearch/v1?"

    response = requests.get(url, params=params)

    if response.status_code == 200:
        print("Success!")
        # print(response.json())
        results_count = response.json()['queries']['request'][0]['totalResults']
        print(f"Всего найдено: {results_count}")
        try:
            for item in response.json()['items']:
                print(item['link'])
            print("-------------")
        except:
            print("Не удалось найти данные по вашему запросу")
    else:
        print(f"A error ocusted! {response.status_code}")
        print(response.json())


if __name__ == '__main__':
    main()

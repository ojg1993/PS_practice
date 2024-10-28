import requests


def getNumDraws(year):
    draws, page, total_page = 0, 1, 1
    for i in range(11):
        while page <= total_page:
            url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1goals={i}&page={page}"
            res = requests.get(url).json()

            if page == 1:
                total_page = res['total_pages']
            for obj in res['data']:
                if str(i) == obj['team2goals']:
                    draws += 1
            page += 1
    return draws


print(getNumDraws(2011))

# def get_user_name(threshold):
#     username = []
#     page = 1
#     total_page = float('inf')

#     while page <= total_page:
#         api_request = requests.get(
#             f"https://jsonmock.hackerrank.com/api/article_users?page={page}")
#         obj = api_request.json()

#         if page == 1:
#             total_page = obj['total_pages']

#         for val in obj['data']:
#             if val['submission_count'] > threshold:
#                 username.append(val['username'])
#         page += 1
#     return username


# print(get_user_name(10))

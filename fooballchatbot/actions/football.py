import http.client
import json


headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "bed50dffbbf67af07377d57583459d5f"
}
league = 39
season = 2022


def getTeamsID(name):
    conn = http.client.HTTPSConnection("v3.football.api-sports.io")

    endpoint = "/teams?country=England"
    conn.request("GET", endpoint, headers=headers)

    res = conn.getresponse()
    data_res = res.read()
    data = json.loads(data_res)
    teams_info = data['response']
    teams_dict = dict()
    for team in teams_info:
        key = team['team']['name']
        value = team['team']['id']
        teams_dict[key] = value
    ID = teams_dict[name]

    return ID


def numGamesPlayed(name):
    conn = http.client.HTTPSConnection("v3.football.api-sports.io")

    team = getTeamsID(name)
    endpoint = "/teams/statistics?season=%d&league=%d&team=%d" % (
        season, league, team)
    conn.request("GET", endpoint, headers=headers)

    res = conn.getresponse()
    data = res.read()
    results = json.loads(data)

    result = results['response']['fixtures']['played']['total']
    if result == 0:
        text_message = "They have not played any game in this season"
        return text_message

    text_message = "So far they have played {} games".format(result)

    return text_message


def winLossRecord(name):
    conn = http.client.HTTPSConnection("v3.football.api-sports.io")

    team = getTeamsID(name)
    endpoint = "/teams/statistics?season=%d&league=%d&team=%d" % (
        season, league, team)
    conn.request("GET", endpoint, headers=headers)

    res = conn.getresponse()
    data = res.read()
    result = json.loads(data)

    if result['response']['fixtures']['played']['total'] == 0:
        text_message = "They have not played any game in this season"
        return text_message

    text_message = "Their record is {} wins, {} loss and {} draws.".format(
        result['response']['fixtures']['wins']['total'],
        result['response']['fixtures']['loses']['total'],
        result['response']['fixtures']['draws']['total']
    )

    return text_message


def playingNow(name):
    conn = http.client.HTTPSConnection("v3.football.api-sports.io")

    team = getTeamsID(name)
    endpoint = "/fixtures?team=%d&live=all" % (team)
    conn.request("GET", endpoint, headers=headers)

    res = conn.getresponse()
    data = res.read()
    result = json.loads(data)
    if result['response'] == []:
        text_message = "No, they are not playing now."
    else:
        text_message = "Yes, they are playing now."

    return text_message


def lastOpponent(name):
    conn = http.client.HTTPSConnection("v3.football.api-sports.io")

    team = getTeamsID(name)
    endpoint = "/fixtures?league=%d&season=%d&team=%d&last=1" % (
        league, season, team)
    conn.request("GET", endpoint, headers=headers)

    res = conn.getresponse()
    data = res.read()
    result = json.loads(data)
    if result['response'][0]['teams']['home']['id'] == team:
        text_message = "The last opponent of {} is {}.".format(
            name,
            result['response'][0]['teams']['away']['name']
        )
    else:
        text_message = "The last opponent of {} is {}.".format(
            name,
            result['response'][0]['teams']['home']['name']
        )

    return text_message


def nextOpponent(name):
    conn = http.client.HTTPSConnection("v3.football.api-sports.io")

    team = getTeamsID(name)
    endpoint = "/fixtures?league=%d&season=%d&team=%d&next=1" % (
        league, season, team)
    conn.request("GET", endpoint, headers=headers)

    res = conn.getresponse()
    data = res.read()
    result = json.loads(data)
    if result['response'][0]['teams']['home']['id'] == team:
        text_message = "The next opponent of {} is {}.".format(
            name,
            result['response'][0]['teams']['away']['name']
        )
    else:
        text_message = "The next opponent of {} is {}.".format(
            name,
            result['response'][0]['teams']['home']['name']
        )

    return text_message


def lastScore(name):
    conn = http.client.HTTPSConnection("v3.football.api-sports.io")

    team = getTeamsID(name)
    endpoint = "/fixtures?league=%d&season=%d&team=%d&last=1" % (
        league, season, team)
    conn.request("GET", endpoint, headers=headers)

    res = conn.getresponse()
    data = res.read()
    result = json.loads(data)
    if result['response'][0]['teams']['home']['id'] == team:
        if result['response'][0]['teams']['home']['winner']==1 and result['response'][0]['teams']['away']['winner']==0:
            text_message = "{} won with a score of {}-{} against {}.".format(
                name,
                result['response'][0]['goals']['home'],
                result['response'][0]['goals']['away'],
                result['response'][0]['teams']['away']['name']
            )
        if result['response'][0]['teams']['home']['winner']==0 and result['response'][0]['teams']['away']['winner']==1:
            text_message = "{} lost with a score of {}-{} against {}.".format(
                name,
                result['response'][0]['goals']['home'],
                result['response'][0]['goals']['away'],
                result['response'][0]['teams']['away']['name']
            )
        if result['response'][0]['goals']['home'] == result['response'][0]['goals']['away']:
            text_message = "{} tied with a score of {}-{} against {}.".format(
                name,
                result['response'][0]['goals']['home'],
                result['response'][0]['goals']['away'],
                result['response'][0]['teams']['away']['name']
            )
    else:
        if result['response'][0]['teams']['home']['winner']==1 and result['response'][0]['teams']['away']['winner']==0:
            text_message = "{} lost with a score of {}-{} against {}.".format(
                name,
                result['response'][0]['goals']['away'],
                result['response'][0]['goals']['home'],
                result['response'][0]['teams']['home']['name']
            )
        if result['response'][0]['teams']['home']['winner']==0 and result['response'][0]['teams']['away']['winner']==1:
            text_message = "{} won with a score of {}-{} against {}.".format(
                name,
                result['response'][0]['goals']['away'],
                result['response'][0]['goals']['home'],
                result['response'][0]['teams']['home']['name']
            )
        if result['response'][0]['goals']['home'] == result['response'][0]['goals']['away']:
            text_message = "{} tied with a score of {}-{} against {}.".format(
                name,
                result['response'][0]['goals']['away'],
                result['response'][0]['goals']['home'],
                result['response'][0]['teams']['home']['name']
            )

    return text_message


def manager(name):
    conn = http.client.HTTPSConnection("v3.football.api-sports.io")

    team = getTeamsID(name)
    endpoint = "/coachs?team=%d" % (team)
    conn.request("GET", endpoint, headers=headers)

    res = conn.getresponse()
    data = res.read()
    result = json.loads(data)
    text_message = "The manager of {} is {} {}.".format(
        name,
        result['response'][0]['firstname'],
        result['response'][0]['lastname']
    )

    return text_message


def leaguePosition(name):
    conn = http.client.HTTPSConnection("v3.football.api-sports.io")

    team = getTeamsID(name)
    endpoint = "/standings?season=%d&league=%d&team=%d" % (
        season, league, team)
    conn.request("GET", endpoint, headers=headers)

    res = conn.getresponse()
    data = res.read()
    results = json.loads(data)

    # Check is there a standing
    if not results['response']:
        text_message = "Sorry, there is no information about the standing of {} ".format(
            name)
        return text_message

    result = results['response'][0]['league']['standings'][0][0]['rank']
    text_message = "The {} is currently ranked number {} in the Premier League standings.".format(
        name, result)

    return text_message


def nextGameDate(name):
    conn = http.client.HTTPSConnection("v3.football.api-sports.io")

    team = getTeamsID(name)
    endpoint = "/fixtures?league=%d&season=%d&team=%d&next=1" % (
        league, season, team)
    conn.request("GET", endpoint, headers=headers)

    res = conn.getresponse()
    data = res.read()
    result = json.loads(data)
    text_message = "In the next game, {} will be playing at {}.".format(
        name,
        result['response'][0]['fixture']['date']
    )

    return text_message

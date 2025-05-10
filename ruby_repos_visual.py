""" Lab 17, Question 2: Access GitHub's API to plot the most popular repos for a programming language
    (using Ruby instead of Python, because it was my first programming language) """

# Josh Platt, 5/9/2025

""" Imports: request for making API calls, plotly.express for making the bar chart
    Not imported but also required (in requirements.txt): numpy & pandas for plotly.express to work """
import requests
import plotly.express as px

# Makes the API call
url = "https://api.github.com/search/repositories"
url += "?q=language:ruby+sort:stars+stars:>10000"

# Checks the API's response & returns it in JSON format
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Processes the results & checks if all requested data was recieved
response_dict = r.json()
print(f"Complete results: {not response_dict['incomplete_results']}")

# Processes the repo information & initialize various dicts for later use
repo_dicts = response_dict['items']
repo_links, stars, hover_texts = [], [], []

for repo_dict in repo_dicts:
    """ Turns the repo names into active links & makes the hover over text """
    # Gets the repo's name
    repo_name = repo_dict['name']
    # Gets the repo's url
    repo_url = repo_dict['html_url']
    # Formats the name and url into a clickable link with HTML
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    
    # Gets the star count for individual repos
    stars.append(repo_dict['stargazers_count'])

    # Builds the hover over texts
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    # Formats the hover over text with HTML
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

""" Creating the bar graph section """
# Sets the title & label text
title = "Most Starred Ruby Projects on GitHub"
labels = {'x': 'Repos', 'y': 'Stars'}

# Creates/initializes the graph
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels,
        hover_name=hover_texts)

# Configures label font sizes
fig.update_layout(title_font_size=36, xaxis_title_font_size=28,
        yaxis_title_font_size=28)

# Configures the graph's bars
fig.update_traces(marker_color='Red', marker_opacity=0.4)

# Displays the plot
fig.show()

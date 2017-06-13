# NePa
This is a made-up project that mimics some of the real world features that we work on. The goal of this project is to give you an introduction to the kinds of problems you'll be solving on this project.

 - You should spend one hour on this.
 - After the hour is up, please `push` all your changes to a branch called `{your-name}` here on github.
 - Be prepared to present your features and discuss your code during an in-person interview.
 
 ## Features to implement
 
 - [ ] Accepts a search term on the command line
 - [ ] Searches DuckDuckGo for given search term
 - [ ] Parses content of search result page
 - [ ] Returns parsed result in the following JSON format:

 ```js
 {
  "search_term": "Provided search term",
  "result_count": "Number of results returned",
  "results": [
    {
      "title": "Title of the page in the search result",
      "url": "URL of the page in the search result",
      "desc": "Description of the page in the search result"
    }
  ]
}
 ```
 
## Additional instructions

### Architecture
- Language of your choice, but preferred options are: Ruby, Python, JS (in that order)
- Make sure your project is portable to another computer and list install dependencies in some way


### Run tests (optional)

We rely heavily on unit tests, please add tests if you have extra time.

# Pillar-Github-Dashboard
Github Dashboard to get popular Repos

How to Run:
- Simply start the flask server and type in the organization you would like to get information about. For example:
  `http://127.0.0.1:5000/organizations/facebook`

Future Optimizations:
- In order to make this service more scalable there are several things that can be done:
  -  Store data about organizations in a database the first time they requested
  -  Before hitting Github's API's, first check to see if the relevant information is already in the database. 
  -  One drawback to this is that the information will be stale. A possible workaround is to check when the information was first inserted and do an update if its more than 24 hours. 
  -  A cache is another option to improve scalability of this app. 
- I spent very little time formatting the results. Charts and css will dramaticaly improve this app. From a design perspective, a home page where a user can submit the organization they want to look up would be much easier then having to type in a url.
- Finally there was no good way to get contributor count of a repo. Github did not provide an api to get this number directly. I explored two options to overcome this and decided both were inefficient.
  - Option 1: Scrape the actual github url of the repo for the number - pretty slow and inefficient
  - Option 2: Set results per page to 1 and then read the response header to see how many pages there are to get the total number of contributors - this approach would require to many calls to github's API

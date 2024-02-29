# CMS - Simple Content Management System

### What is this?  
This is a recursive project.  We will generate a website which will host the description of the creation of itself.
We're building a static site generator and publishing tool.

### Why not use one of a million apps that can already do this? 
Because we can.

### What are your goals?  
We're going to create a content management system that
  * has versioned content
  * supports semantic urls
  * support [red links](https://en.wikipedia.org/wiki/Wikipedia:Red_link)
  * has actual search
  * is packaged for reuse
  * can survive a [hug of death](https://www.urbandictionary.com/define.php?term=hug%20of%20death)
  * will resist adding a database as long as we can

And we're going to do it so that a new devloper can follow along with the decisions we make as we create it.

### No SPA or JS Framework?
At some point, this may make sense, but I'm a old school believer in the open web. For a web site serving static content, single page apps and JavaScript fraeworks are overkill.  We're going to avoid them in this project.

### No database?
With every layer we add to our application, we increase it's complexity, maintenance, and dependencies.  Keeping these to a minimum will let us deliver more rapidly.  A database is one of the most incredible tools in our arsenal, but it constrains a few decisions and make some things really hard.  Versioned content, if we use git, itself, as our file system,  is something we'll get for free.  It remains to be seen how well this will work, but we'll cover that more in the next section, project layout.  Authentication and authorization will be our most challenging thing, so we might add Sqlite when the time comes.


### What technologies?
At my last job, I used Python as my main language. Although, I've worked with Java, C#, Ruby, Delphi, Perl, Visual Basic 6.0, and JavaScript, I'm going to give building this project with Python. I prefer a typed lanaguage, but I've got some time off and want to dig into Python a bit more.

Heres' what we're going to use
* Python 3
* Flask: for serving our content, and exposing some admin capabilities
* git: for storing and serving files themselves
* Solr: for implementing actual search of our content


# Let's Get Started... Step One
* create virtual environment
* create folder structure /tests /posts /drafts


# Building the site while editing in Vim
`autocmd BufWritePost * :silent!make build`

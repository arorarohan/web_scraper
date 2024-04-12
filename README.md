# summary_generator
Being a moron, I decided to build a summary generator script that shows the user the top 5 headlines from channelnewsasia.com and summarizes them using GPT-3.5 turbo.
This was definitely not a good idea, but it worked and was easier than expected.

## the why
- to learn web scraping using beautiful soup, and basic interaction with the OpenAI API.

## structure
1. Finds a specific class of links in the website on running the script, returns the first 5 headlines as a list to show the user.
2. when the user selects a number, the script follows the link associated with the headline and scrapes that site for the body text.
3. Feeds the body text into GPT, asks for a summary
4. Prints the summary returned by GPT.

## dependencies
1. OpenAI module (with your own working API key which you'll likely have to pay to use)
2. requests module (for grabbing webpages from hyperlinks)
3. bs4 module (for sifting through webpages for specific classes)

## the approach
1. fuck around (i.e. do something I have zero understanding of, which is probably well out of my depth)

## the goal
1. find out (i.e. learn new stuff, improve my skills or whatever)

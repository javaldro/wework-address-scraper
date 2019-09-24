# WeWork Address Scraper
A python script that makes it easy to get all current WeWork addresses exported into a nice CSV file. 

## Requirements
Having the loaded packages (such as beautifulsounp) installed is required for this script to function. 

## Why is this project useful? 
This is a tool that helps collect all of this address information in a way that is easily readable by computers with minimal manual effort. After having this WeWork address information, it could be combined with a wide variety of other information programmatically to provide value. For example, if your company is considering becoming a global client of WeWork, you could combine this with information on your current offices in order to fully understand the expansion in reach it would provide. 

## Opportunities for Contributions
1) In this project, I attempt to skip non-USA "states" and "zips" by applying length-based conditional statements. This works in 90% of cases, but not where the last two items (separated by spaces) in a non-usa address happen to be the same length as they are for a USA address. It would be cool if someone could fix this.
2) I'm only pulling the address at this stage in the project. That said, I could see it evolving by others adding other pieces of information they are interested in. 

## You work at GitHub. Is this a GitHub sponsored project?
I do work at GitHub, and it’s awesome! While GitHub is supportive of me contributing to open source, this project is independent of my work there, and in no way reflects GitHub’s philosophy or projects on this topic. This is just something I find personally interesting and want to build with the community. 

# Pivot Land
Contains Small chunks of code to solve specific problems

## The Aim of this project
Is to write code to solve a specific problem, in whatever language on earth,    
and use the front facing code to execute everything from command-line-interfaces where that usecase has to be solved.
An example is python image resize run from a node web server when a request comes to do so.

## This follows traditional Git-Flow mechanism
* **master** branch will always be the default, cloneable.
* **dev** branch is where people merge pull requests to.
* **release** branch is what is given to the testing the agreed features
* If **release** branch succeeds, it will be merged to **master** with little negotiations
* **hotfix** would be a branch which directly start from **master** to merge to it again, when immediate fixes needed in production

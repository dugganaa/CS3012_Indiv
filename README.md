# CS3012_Indiv
This is my submission for a TCD software engineering assignment. The program interrogates the Github API using a user supplied access token. The main branch creates two visualisations: a scatter plot of Followers vs Repos and a graph of users linked to other users who they follow or are followed by. The gitacc branch currently outputs data on the user to the console and displays a barchart of said data. 

## Prerequisites
You'll need a Personal Access Token (found here: https://github.com/settings/tokens) and a number of libraries installed.
I recommend using pip to install these libraries. 

```
pip install pandas
pip install numpy
pip install pygithub
pip install matplotlib
pip install networkx
pip install scipy
```

## Running the code
After passing in your Personal Access Token, use the following commands to run the program:

Displaying the Followers vs Repos graph.

### Commands

cl   = clean code. Used to remove outliers.

```

fr -rows -cl

```

```

fg -rows

```
  
  
## Output sample

#### Followers vs Repos
![Followers vs Repos Console Output](https://i.imgur.com/tXE2Hkg.png)

![Followers vs Repos Plot](https://i.imgur.com/dYBCA07.png)


#### Followers Network Plot
![Followers Graph Console Output](https://i.imgur.com/Lz1JoOT.png)

![Followers Graph Plot](https://i.imgur.com/2HS9e7r.png)


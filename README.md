# ChessGameToMoveList
This is a simple python script to convert a chess game string into a move by move text format.

The goal of this program is to convert a game string like this


```d4 d5 c4 c6 cxd5 e6 dxe6 fxe6 Nf3 Bb4+ Nc3 Ba5 Bf4```

to a move list like this

```
Pa2 Pb2 Pc2 Pd2 Pe2 Pf2 Pg2 Ph2 Ra1 Nb1 Bc1 Qd1 Ke1 Bf1 Ng1 Rh1
Ra8 Nb8 Bc8 Qd8 Ke8 Bf8 Ng8 Rh8 Pa7 Pb7 Pc7 Pd7 Pe7 Pf7 Pg7 Ph7
D2
d2d4
Pd4 Pa2 Pb2 Pc2 Pe2 Pf2 Pg2 Ph2 Ra1 Nb1 Bc1 Qd1 Ke1 Bf1 Ng1 Rh1
Ra8 Nb8 Bc8 Qd8 Ke8 Bf8 Ng8 Rh8 Pa7 Pb7 Pc7 Pd7 Pe7 Pf7 Pg7 Ph7
D7
d7d5
```

The move lists have the format:

```
White pieces
Black pieces
Desired next move starting position
Desired next move
```

This format can be useful for checking move generators to verify that knowing only the desired next move staring position is enough to generate the desired next move (black box testing). It can also be used to generate training data for the next move given a board setup if human generated games are used.

## Usage
This script can be run from the command line


```
usage: main.py [-h] [--file [FILE]] [--one_side [ONE_SIDE]] [game]

positional arguments:
  game                  game string to parse (space seperated)

optional arguments:
  -h, --help            show this help message and exit
  --file [FILE]         input csv to read from (no header, one game per line)
  --one_side [ONE_SIDE]
                        use WHITE to return only white moves
                        
 ```
 
 ### Example
 `python main.py "d4 d5 c4 c6 cxd5 e6 dxe6 fxe6 Nf3 Bb4+ Nc3 Ba5 Bf4"`

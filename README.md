# tiny-chess-01 entry

An original compact chess engine in a single Python file (<= 4,096 bytes):
negamax + alpha-beta with quiescence, transposition table, PVS, late-move
reductions and null-move pruning, fixed node budget (deterministic).

The shipped main.py is the minified engine, lzma-compressed and embedded in
a small self-extracting stub (4,066 bytes as committed). The readable source
it decompresses to was developed and tested locally: perft-verified move
generation, invariant fuzzing of the incremental state, and gauntlet trials
against the practice ladder.

SPDX-License-Identifier: MIT

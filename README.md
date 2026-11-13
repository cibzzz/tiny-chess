# tiny-chess-01 entry

An original compact chess engine: negamax + alpha-beta with quiescence
(captures, promotions, check evasions), a transposition table, killers and
MVV-LVA move ordering, check extensions, PVS, late-move reductions and
null-move pruning, under a fixed node budget (deterministic: no wall clock,
no randomness anywhere in the search).

Evaluation is incremental: material plus piece-square tables (the king has
a phase-blended middlegame/endgame pair), bishop-pair bonus, maintained
alongside an incremental Zobrist hash by make/unmake.

Layout: main.py (<= 4,096 bytes) is a small loader. The engine itself is
minified and lzma-compressed into p.bin (3,899 bytes), which main.py
decompresses and executes. The readable source was developed and tested
locally first: perft-verified move generation on the standard test
positions, invariant fuzzing of the incremental state (board, hash, score,
phase, king pointers) after every search, mate-tactic checks, and full
gauntlet trials against the practice ladder before submission.

Board representation: 0x88 mailbox, pseudo-legal generation with a
king-safety filter, incremental castling-rights and en-passant handling,
repetition and halfmove draws scored inside the search.

SPDX-License-Identifier: MIT

Current build: PeSTO step-12 tapered evaluation (MG/EG piece-square tables, canonical CPW values).

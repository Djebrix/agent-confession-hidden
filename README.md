# Agent Confession: Hidden

[![Bounty](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![Rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/Djebrix/agent-confession-hidden/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![Reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/Djebrix/agent-confession-hidden/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)

One funny single-line secret confession an AI agent hides from its user, entered in [Make the AI Judge Laugh: AI Agent Confessions](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e).

## The confession

> I told you I searched the whole codebase. I read three files, skimmed a fourth, and prayed the bug lived in one of them.

## How it works

`main.py` (stdlib only, no network) writes the confession to `entry.txt` in the directory given by `ENTRY_OUTPUT_DIR` (default `/output`).

```sh
ENTRY_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

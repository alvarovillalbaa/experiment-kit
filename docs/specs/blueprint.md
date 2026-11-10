# Inherited experiment-kit blueprint

Last updated: 2026-11-10

Historical design extracted from [Lab at ba67e51](https://github.com/alvarovillalbaa/lab/blob/ba67e510bab2703b1042993744ce099490221c1f/docs/specs/steps.md). The component specification owns current scope. This text does not prove implementation, current provider facts, or executed research.

Here is the plan I would run. I’m going to be blunt: the right goal is **not** “train a frontier model.” The right goal is **build and publish a complete, reproducible, frontier-style LLM training factory**: data → tokenizer → pretraining → midtraining/continued pretraining → post-training → distillation → evaluation → serving → cost accounting → public technical report. That is enough to prove you know how to do the real thing.

## 0. Define the experiment correctly

Your public claim should be:

> “We trained an LLM from scratch end-to-end, built the full training and serving stack, reproduced current industry-standard stages, and tested novel improvements in compute allocation, self-improvement, and distillation under controlled ablations.”

That is a much stronger and more credible claim than “we trained a big model.”

Use **OLMo 3** as the openness benchmark. OLMo 3’s release is valuable because it includes the full model flow: model stages, checkpoints, data, and dependencies, not just final weights. That is the standard you should copy for credibility. ([allenai.org][1])

Your target should be:

| Target    |                                 Purpose | Recommendation               |
| --------- | --------------------------------------: | ---------------------------- |
| 124M–350M | Learning, CI, debugging, data ablations | mandatory                    |
| 1B–1.5B   |            First serious public release | mandatory                    |
| 3B        |         Strong “I can train LLMs” proof | recommended                  |
| 7B        |                            Stretch goal | only after 1B/3B stack works |

Do **not** start with 7B. That is how people burn money and learn nothing.

---

# 3. Public proof standard

You want to “prove the world” you know how to do it. That means publishing more than a Hugging Face model.

Publish these artifacts:

1. **Model weights**: base, midtrained, SFT, preference/RL, distilled, quantized.
2. **Training code**: pinned commit hashes, Dockerfiles, exact launch scripts.
3. **Data recipes**: sources, filters, dedup logic, sampling weights, token counts.
4. **Tokenizer**: training corpus sample description, vocab size, special tokens.
5. **Training logs**: loss curves, throughput, GPU utilization, restart events, eval curves.
6. **Cost ledger**: GPU-hours, storage, failures, eval costs, inference costs.
7. **Evaluation report**: base benchmarks, chat benchmarks, safety benchmarks, contamination checks.
8. **Ablation report**: one table per claimed improvement.
9. **Serving endpoint/demo**: vLLM endpoint, quantized local model, latency/throughput report.
10. **Reproducibility kit**: one command to reproduce the 124M smoke run.

This matters. A weak model with a transparent, reproducible training report is more impressive than a slightly better model with no credible process.

---

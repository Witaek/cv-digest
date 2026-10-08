# Digest guide

Instructions the scheduled task follows every morning. Edit this file to change what the
digest covers; the scheduled task reads it fresh on every run.

## Reader

A computer vision engineer who spends **~30 minutes each morning** keeping up with the state of
the art. Explain *what is new and why it matters*, give
numbers (mAP, mIoU, latency, params, FPS, hardware) whenever the source has them.

## Scope (in priority order)

1. **New models and SOTA methods** for core vision tasks, any architecture (CNN, ViT/transformer,
   hybrid, SSM/Mamba, diffusion-based, foundation models):
   - realtime oriented, lightweight models
   - object detection (real-time and open-vocabulary: YOLO family, DETR/RT-DETR family, DINO-style,
     grounding models)
   - segmentation: semantic, instance, panoptic, promptable (SAM family), video segmentation
   - vision backbones and self-supervised pretraining (DINO, MAE, SigLIP-like encoders)
   - depth, tracking, pose, 3D/multi-view, video understanding when the method is notable
3. **Edge and efficient deployment**: quantization, pruning, distillation, NAS, small/mobile models,
   TensorRT, ONNX Runtime, OpenVINO, ExecuTorch, Core ML, TFLite/LiteRT, Jetson, NPUs.
4. **GPU / CUDA / PyTorch tooling**: PyTorch releases and blog, torch.compile, Triton, CUDA toolkit
   releases, cuDNN, NVIDIA developer blog, FlashAttention-style kernels, data loading/decoding.
5. **Industry and ecosystem news relevant to CV**: notable open-weight releases, library releases
   (Ultralytics, torchvision, timm, Detectron2, MMDetection, Hugging Face transformers vision),
   benchmark/leaderboard changes, conference news (deadlines, best papers), hardware launches.

Generative/VLM work is in scope only when it bears on perception (e.g. a VLM that sets a new
detection/grounding result, or a vision encoder others will reuse). Don't let image/video
generation dominate the digest.

## Where to look

### Fetching: shell first, WebFetch as fallback

The cloud environment's network allowlist lets the shell reach these sites directly. That is
faster and more reliable than WebFetch (arXiv in particular rate-limits WebFetch). Start with
the machine-readable feeds below via `curl -sS -m 30`, then fetch individual pages
(abstracts, blog posts, release notes) with `curl` too.

- arXiv cs.CV, newest first (titles + full abstracts, Atom XML):
  `https://export.arxiv.org/api/query?search_query=cat:cs.CV&sortBy=submittedDate&sortOrder=descending&max_results=200`
  (arXiv asks for at most one API request every 3 seconds; one request is enough.)
- Hugging Face Daily Papers (JSON with abstracts and upvotes):
  `https://huggingface.co/api/daily_papers?limit=100`
- Hugging Face trending models: `https://huggingface.co/api/models?sort=trendingScore&limit=50`
  (keep vision tasks: object-detection, image-segmentation, mask-generation, depth-estimation,
  image-feature-extraction, zero-shot-object-detection, keypoint-detection).
- PyTorch blog RSS: `https://pytorch.org/feed/`
- NVIDIA Technical Blog RSS: `https://developer.nvidia.com/blog/feed/`

If `curl` fails with a proxy rejection (the domain is not on the allowlist), fall back to
WebSearch and WebFetch for that source. Do not retry a page WebFetch has refused. If a whole
source is unreachable, say so in one line at the top of the digest, but still write full
summaries for every item whose abstract or page you could read.

### Sources to cover

- Hugging Face Daily Papers and trending papers (huggingface.co/papers)
- arXiv cs.CV recent submissions (arxiv.org/list/cs.CV/recent)
- GitHub trending / new releases for the libraries named above
- PyTorch blog, NVIDIA Technical Blog, CUDA release notes
- Lab blogs: Meta AI (FAIR), Google DeepMind / Research, Microsoft Research, Apple ML, NVIDIA Research
- Roboflow blog and Ultralytics blog for practical detection/segmentation news

Prefer primary sources (paper, official repo, release notes) over aggregators. Every item needs a
working link to the primary source. Never invent results or numbers; if a figure is not in the
source, leave it out.

## Freshness and deduplication

- Prefer items from the last ~48 hours (last ~72 hours on Mondays, to cover the weekend).
- Before writing, read the last 7 files in `daily/` and do **not** repeat an item already covered,
  unless there is genuinely new information (e.g. code/weights released for a paper covered
  earlier); then say so in one line.
- On a quiet day, a shorter digest is better than filler.

## Format

Write `daily/YYYY-MM-DD.md` (today's date in America/Toronto). Keep the existing style:

```
# CV Digest — <Weekday>, <Month> <D>, <YYYY>

## TL;DR
3 bullets max: the things to know today if you read nothing else.

## Top papers
3–5 items. **Title** — [link](url). 2–4 sentences: the idea, the key result with numbers,
why it matters / what it replaces. Add [code](url) when code or weights exist.

## Models & releases
New checkpoints, library releases. Same item style, 1–3 sentences each.

## Edge & deployment
Quantization, runtimes, mobile/embedded results. Omit the section if nothing notable.

## GPU / CUDA / PyTorch
Same item style. Omit the section if nothing notable.

## News
Short bullets, 1–2 sentences each. Omit the section if nothing notable.

## Today's deep read
One item from above worth 10–15 minutes, with what to focus on and how it might apply to a
production CV system.
```

Target total reading time of the digest itself: about 8–10 minutes, leaving the rest of the
30 minutes for the deep read and clicking through. Roughly 10–15 items in all.

## Publishing

1. Write the file, then run `python3 scripts/build_index.py`.
2. Commit only `daily/<date>.md` and `index.json` with the message `Daily digest <date>`.
3. Fetch, rebase if needed, and push directly to `main`.
4. If today's file already exists, update it rather than creating a second one.

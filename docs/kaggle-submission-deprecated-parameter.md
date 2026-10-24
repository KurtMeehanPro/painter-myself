# Kaggle Submission Error: Deprecated Parameter

## 23 October 2026 — Current outcome

The image-generation pipeline works, but submission to [I’m Something of a Painter Myself](https://www.kaggle.com/competitions/gan-getting-started/) fails after a successful saved notebook run. Thus, no competition score has been obtained. The issue has been reported on Kaggle (details and links below this). No resolution so far. Local metric evaluation is being considered since no score from Kaggle is possible due to the blockage.


Kaggle displays this failure when submitting:

```text
Submit failed. PostProcessorKernelId is no longer supported; use RerunOverrideKernelId instead.
```

## Successful generation

The saved Kaggle run completed generation and ZIP validation. The submission error occurs afterward.

## Kaggle Bug Report

Neither `PostProcessorKernelId` nor `RerunOverrideKernelId` appears in this repository’s notebooks or scripts. There is no notebook parameter to rename in response to the error. This points to the submission path rather than the image-generation code.

An existing public report matches the error: [“[Bug] Kaggle Code Competition Submission Failure – PostProcessorKernelId Deprecated Error,”](https://www.kaggle.com/discussions/product-feedback/741102) posted approximately one month before this investigation. It concerns the older 'Lyft motion-prediction' competition. Other commenters report the same problem.

I added [my comment](https://www.kaggle.com/discussions/product-feedback/741102#3543776) to the bug. My comment reports the same error for [I’m Something of a Painter Myself](https://www.kaggle.com/competitions/gan-getting-started/), successful notebook execution and `images.zip` generation, and persistent failure after retries. It requests a status update or tracking ticket.

# Neurologi AI Prediksi

Prototype kode untuk prediksi risiko *time-to-deterioration* stroke iskemik akut dari fitur CT/CTA + klinis awal.

## Jalankan CLI

```bash
PYTHONPATH=src python -m cli \
  --age 68 \
  --nihss 18 \
  --gcs 11 \
  --aspects 5 \
  --lvo \
  --midline-shift 4.5 \
  --glucose 190 \
  --onset-to-ct 4.2
```

Output berupa JSON dengan:
- probabilitas risiko deteriorasi,
- estimasi jam menuju deteriorasi,
- level urgensi,
- rekomendasi rujukan dan alert bedah saraf.

## Testing

```bash
PYTHONPATH=src pytest -q
```

> Catatan: ini baseline model untuk *decision support* dan belum tervalidasi klinis.

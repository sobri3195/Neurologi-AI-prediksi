from __future__ import annotations

import argparse
import json

from stroke_ttd_model import StrokeFeatures, StrokeTTDModel


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Prediksi risiko deteriorasi stroke dari CT/CTA + data klinis"
    )
    parser.add_argument("--age", type=int, required=True)
    parser.add_argument("--nihss", type=int, required=True)
    parser.add_argument("--gcs", type=int, required=True)
    parser.add_argument("--aspects", type=int, required=True)
    parser.add_argument("--lvo", action="store_true", help="Set jika ada LVO pada CTA")
    parser.add_argument("--midline-shift", type=float, default=0.0)
    parser.add_argument("--glucose", type=float, required=True)
    parser.add_argument("--onset-to-ct", type=float, required=True)
    return parser


def main() -> None:
    args = build_parser().parse_args()

    features = StrokeFeatures(
        age=args.age,
        nihss=args.nihss,
        gcs=args.gcs,
        aspe_cts=args.aspects,
        lvo_present=args.lvo,
        midline_shift_mm=args.midline_shift,
        glucose_mg_dl=args.glucose,
        onset_to_ct_hours=args.onset_to_ct,
    )

    model = StrokeTTDModel()
    result = model.predict(features)
    hazard = model.estimate_hazard_per_hour(result.risk_probability)

    output = {
        "risk_probability": result.risk_probability,
        "estimated_ttd_hours": result.estimated_ttd_hours,
        "urgency_level": result.urgency_level,
        "recommend_transfer": result.recommend_transfer,
        "recommend_neurosurgery_alert": result.recommend_neurosurgery_alert,
        "estimated_hazard_per_hour": round(hazard, 5),
    }

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()

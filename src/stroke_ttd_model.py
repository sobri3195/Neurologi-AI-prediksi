from __future__ import annotations

from dataclasses import dataclass
from math import exp, log
from typing import Dict


@dataclass
class StrokeFeatures:
    """Input ringkas dari CT/CTA + data klinis awal."""

    age: int
    nihss: int
    gcs: int
    aspe_cts: int
    lvo_present: bool
    midline_shift_mm: float
    glucose_mg_dl: float
    onset_to_ct_hours: float


@dataclass
class PredictionResult:
    risk_probability: float
    estimated_ttd_hours: float
    urgency_level: str
    recommend_transfer: bool
    recommend_neurosurgery_alert: bool


class StrokeTTDModel:
    """
    Model baseline yang bisa dijalankan lokal sebagai decision support.

    Catatan:
    - Ini adalah model rule-based + logistic scoring sederhana,
      bukan model klinis tervalidasi.
    - Bobot dapat diganti saat data aktual tersedia.
    """

    def __init__(self) -> None:
        self._weights: Dict[str, float] = {
            "bias": -3.5,
            "age": 0.015,
            "nihss": 0.11,
            "gcs_inverse": 0.22,
            "aspects_inverse": 0.20,
            "lvo_present": 1.0,
            "midline_shift": 0.35,
            "glucose": 0.004,
            "onset_to_ct": 0.07,
        }

    @staticmethod
    def _sigmoid(x: float) -> float:
        return 1.0 / (1.0 + exp(-x))

    def predict(self, features: StrokeFeatures) -> PredictionResult:
        gcs_inverse = max(0, 15 - features.gcs)
        aspects_inverse = max(0, 10 - features.aspe_cts)

        linear_score = (
            self._weights["bias"]
            + self._weights["age"] * features.age
            + self._weights["nihss"] * features.nihss
            + self._weights["gcs_inverse"] * gcs_inverse
            + self._weights["aspects_inverse"] * aspects_inverse
            + self._weights["lvo_present"] * (1.0 if features.lvo_present else 0.0)
            + self._weights["midline_shift"] * max(0.0, features.midline_shift_mm)
            + self._weights["glucose"] * max(0.0, features.glucose_mg_dl - 100)
            + self._weights["onset_to_ct"] * max(0.0, features.onset_to_ct_hours)
        )

        risk_probability = self._sigmoid(linear_score)

        # Transformasi risiko -> estimasi time-to-deterioration (jam).
        # Risiko tinggi => waktu lebih pendek.
        min_hours, max_hours = 2.0, 72.0
        estimated_ttd_hours = max(
            min_hours,
            min(max_hours, max_hours * (1.0 - 0.85 * risk_probability)),
        )

        if risk_probability >= 0.8:
            urgency_level = "critical"
        elif risk_probability >= 0.55:
            urgency_level = "high"
        elif risk_probability >= 0.3:
            urgency_level = "moderate"
        else:
            urgency_level = "low"

        recommend_transfer = urgency_level in {"critical", "high"}
        recommend_neurosurgery_alert = (
            urgency_level == "critical"
            or features.midline_shift_mm >= 5.0
            or (features.aspe_cts <= 5 and features.nihss >= 16)
        )

        return PredictionResult(
            risk_probability=round(risk_probability, 4),
            estimated_ttd_hours=round(estimated_ttd_hours, 2),
            urgency_level=urgency_level,
            recommend_transfer=recommend_transfer,
            recommend_neurosurgery_alert=recommend_neurosurgery_alert,
        )

    def estimate_hazard_per_hour(self, risk_probability: float, horizon_hours: float = 24.0) -> float:
        """Konversi probabilitas event kumulatif ke hazard rate konstan per jam."""
        p = min(max(risk_probability, 1e-6), 1 - 1e-6)
        horizon = max(1e-6, horizon_hours)
        return -log(1 - p) / horizon

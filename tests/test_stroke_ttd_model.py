from stroke_ttd_model import StrokeFeatures, StrokeTTDModel


def test_high_risk_case():
    model = StrokeTTDModel()
    features = StrokeFeatures(
        age=72,
        nihss=20,
        gcs=10,
        aspe_cts=4,
        lvo_present=True,
        midline_shift_mm=6.0,
        glucose_mg_dl=220,
        onset_to_ct_hours=5.0,
    )

    result = model.predict(features)

    assert result.risk_probability >= 0.8
    assert result.urgency_level == "critical"
    assert result.recommend_transfer is True
    assert result.recommend_neurosurgery_alert is True


def test_low_risk_case():
    model = StrokeTTDModel()
    features = StrokeFeatures(
        age=45,
        nihss=3,
        gcs=15,
        aspe_cts=10,
        lvo_present=False,
        midline_shift_mm=0.0,
        glucose_mg_dl=110,
        onset_to_ct_hours=1.0,
    )

    result = model.predict(features)

    assert result.risk_probability < 0.3
    assert result.urgency_level == "low"
    assert result.recommend_transfer is False


def test_hazard_positive():
    model = StrokeTTDModel()
    hazard = model.estimate_hazard_per_hour(0.6, horizon_hours=24)
    assert hazard > 0

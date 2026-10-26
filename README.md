# GemExquisite Diamond Valuation: Production Kedro & Serving Platform

[![Kedro Pipeline](https://img.shields.io/badge/Pipeline-Kedro%200.19%2B-blueviolet)](diamond-price-prediction)
[![Data Contracts](https://img.shields.io/badge/Contracts-Great%20Expectations%20Standards-orange)](diamond-price-prediction/src/diamond_price_prediction/data_contract.py)
[![Serving Microservice](https://img.shields.io/badge/Serving-Sub--10ms%20REST%20Engine-brightgreen)](diamond-price-prediction/src/diamond_price_prediction/serving)

Enterprise tabular machine learning platform for real-time and batch valuation of high-value gemstone assets (**NTT DATA** production pattern).

The project elevates the early Kedro tutorial into a Staff-level production architecture:
- **Clean Repo Hygiene**: Removed committed large binary files (`.pickle` model weights and intermediate `.pq` partitions) from git history.
- **Strict Data Contracts**: Validates physical dimensional integrity ($x, y, z > 0$), carat bounds, and categorical cut standards before triggering pipeline nodes.
- **Microsecond Serving**: Ultra-low latency valuation engine ready for containerized deployment in ECS/Kubernetes.

---

## 🏛️ Pipeline & Data Contracts

```
[Raw Diamonds Feed]
        │
        ▼
[DiamondDataContract Gate] ──> Physical dimension & categorical validation
        │ Passed
        ▼
[Data Preprocessing Node] ──> Outlier removal & feature scaling
        │
        ▼
[Ensemble / Gradient Boosting Node] ──> Model Artifact Generation
        │
        ▼
[FastAPI / REST Valuation Engine] ──> < 10ms P99 pricing estimation
```

---

## 🚀 Local Verification

```bash
cd diamond-price-prediction
export PYTHONPATH=src
python -m pytest tests/ -v
```

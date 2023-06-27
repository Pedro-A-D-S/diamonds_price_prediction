# GemExquisite diamonds price prediction

## Overview
<div style = "text-align: justify">
This project aims to build a robust machine learning pipeline for predicting the price of diamonds based on their various features and characteristics. By leveraging a comprehensive dataset that includes information such as carat weight, cut quality, color, clarity, and dimensions, GemExquisite's data science team will develop an accurate and reliable diamond price prediction model.

The pipeline encompasses data preprocessing, feature engineering, model training, and evaluation stages. By employing machine learning algorithms and leveraging data-driven insights, the team aims to provide real-time pricing estimates for diamonds based on their unique attributes.
This project was generated using `Kedro 0.18.10`.
</div>

## Objectives
<div style = "text-align: justify">
Develop a diamond price prediction model to accurately estimate the price of diamonds.
Enhance customer satisfaction by providing fair and transparent pricing information.
Enable sales representatives to provide real-time pricing estimates to customers.
Establish GemExquisite as a leader in the diamond industry through data-driven insights.

## Project Structure
The project follows a structured approach as follows:

```
diamond-price-prediction/
├── conf/
│   ├── base/
│   │   └──
│   │   └──
│   │   ├── catalog.yml
│   │   ├── logging.yml
│   │   └── parameters.yml
│   ├── local/
│   │   └── ...
│   
├── data/
│   ├── 01_raw/
│   │   └── diamonds.csv
│   ├── 02_intermediate/
│   │   ├── outlier_removal_diamonds.pq
│   │   └── final_diamonds.pq
│   ├── 03_primary/
│   │   └── ...
│   ├── 04_feature/
│   │   └── ...
│   ├── 05_model_input/
│   │   └── ...
│   ├── 06_models/
│   │   ├── regressor.pickle/
│   │   └── ...
│   └── 07_model_output/
│       └── ...
├── img/
│   └── pipeline.png
├── notebooks/
│   └── Diamonds.ipynb
├── logs/
│   └── ...
├── src/
│   ├── diamond_price_prediction/
│   │   ├── pipelines/
│   │   └── data_preprocessing/
│   │       └── nodes.py
│   │       └── pipeline.py
│   │   └── data_science/
│   │       └── nodes.py
│   │       └── pipeline.py
│   │   └── dataviz.py
│   │   └── pipeline_registry.py
│   │   └── settings.py
│   │   └── requirements.txt
│   └── ...
├── tests/
│   ├── __init__.py
│   ├── test_run.py
│   └── ...
├── .gitignore
├── info.log
├── pyproject.toml
├── README.md
├── setup.cfg
```

## How to run

To run the diamond price prediction pipeline, follow these steps:

Install the project dependencies by running:

```
pip install -r src/requirements.txt
```

Run the pipeline using the command:

```
kedro run
```

Visualize the pipeline using:

```
kedro viz
```

This pipeline is divided in two main steps: data preprocessing and model training pipelines (both inside src/pipelines)

![Pipeline](/diamond-price-prediction/img/pipeline.png)

## Next Steps

Once the model is successfully trained and evaluated, it can be deployed into GemExquisite's pricing system, enabling real-time price estimation for diamonds. This will enhance the customer experience and establish GemExquisite as a trusted provider of high-quality diamonds with transparent pricing information.

## Contribuiting

Contributions to this project are welcome. If you have any suggestions or improvements, please feel free to contact me.

## License

This project is licensed under the MIT License.

## Contact

For inquiries or further information, please contact me at:
 - Email: pedroalves0409@gmail.com
 - LinkedIn: https://www.linkedin.com/in/pedro-a-d-s/
</div>

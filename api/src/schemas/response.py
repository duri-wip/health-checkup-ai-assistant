from typing import Any
from enum import StrEnum
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class ResponseData(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )


class OverviewItem(ResponseData):
    checkup_date: str
    height: str
    weight: str
    waists: str
    bmi: str
    vision: str
    hearing: str
    blood_pressure: str
    proteinuria: str
    hemoglobin: str
    fasting_blood_glucose: str
    total_cholesterol: str
    hdl_cholesterol: str
    triglyceride: str
    ldl_cholesterol: str
    serum_creatinine: str
    gfr: str
    ast: str
    alt: str
    y_gpt: str
    chest_xray_result: str
    osteoporosis: str
    evaluation: str


class ReferenceItem(ResponseData):
    ref_type: str
    height: str = ""
    weight: str = ""
    waists: str = ""
    bmi: str = ""
    vision: str = ""
    hearing: str = ""
    blood_pressure: str = ""
    proteinuria: str = ""
    hemoglobin: str = ""
    fasting_blood_glucose: str = ""
    total_cholesterol: str = ""
    hdl_cholesterol: str = ""
    triglyceride: str = ""
    ldl_cholesterol: str = ""
    serum_creatinine: str = ""
    gfr: str = ""
    ast: str = ""
    alt: str = ""
    y_gpt: str = ""
    chest_xray_result: str = ""
    osteoporosis: str = ""


class ResultItem(ResponseData):
    case_type: str
    checkup_type: str
    checkup_date: str
    organization_name: str
    pdf_data: str
    questionnaire: list[Any]


class HealthData(ResponseData):
    patient_name: str
    overview_list: list[OverviewItem]
    reference_list: list[ReferenceItem]
    result_list: list[ResultItem]


class ResponseStatus(StrEnum):
    success = "success"
    failed = "failed"


class ApplicationResponse(BaseModel):
    status: ResponseStatus
    data: HealthData
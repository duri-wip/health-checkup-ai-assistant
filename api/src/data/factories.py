import factory
from factory import LazyAttribute
from src.schemas.response import OverviewItem, ReferenceItem, ResultItem, HealthData


# OverviewItem
class OverviewItemFactory(factory.Factory):
    class Meta:
        model = OverviewItem

    checkup_date = factory.Faker("date")
    height = "175"
    weight = "72"
    waists = "85"
    bmi = "23.5"
    vision = "1.0/0.8"
    hearing = "정상/정상"
    blood_pressure = "115/75"
    proteinuria = "음성"
    hemoglobin = "15.0"
    fasting_blood_glucose = "95"
    total_cholesterol = "190"
    hdl_cholesterol = "60"
    triglyceride = "120"
    ldl_cholesterol = "115"
    serum_creatinine = "1.2"
    gfr = "90"
    ast = "30"
    alt = "28"
    y_gpt = "25"
    chest_xray_result = "정상, 비활동성"
    osteoporosis = "T-score -0.8"
    evaluation = "전체적으로 정상 범위 내 건강 상태입니다."


class WarningOverviewItemFactory(OverviewItemFactory):
    """정상(B) — 경계 수치"""
    bmi = "27.0"
    blood_pressure = "135/85"
    fasting_blood_glucose = "112"
    total_cholesterol = "220"
    hdl_cholesterol = "50"
    triglyceride = "170"
    ldl_cholesterol = "135"
    ast = "45"
    alt = "40"
    evaluation = "일부 수치가 경계 범위에 있어 주의가 필요합니다."


class DangerOverviewItemFactory(OverviewItemFactory):
    """질환의심 — 위험 수치"""
    bmi = "32.0"
    blood_pressure = "155/98"
    fasting_blood_glucose = "135"
    total_cholesterol = "255"
    hdl_cholesterol = "35"
    triglyceride = "210"
    ldl_cholesterol = "170"
    serum_creatinine = "1.8"
    gfr = "55"
    ast = "55"
    alt = "50"
    y_gpt = "80"
    evaluation = "여러 항목에서 이상 소견이 확인되어 전문의 상담이 필요합니다."


# ReferenceItem

_REFERENCE_LIST = [
    ReferenceItem(
        ref_type="단위",
        height="Cm", weight="Kg", waists="Cm", bmi="kg/m2",
        blood_pressure="mmHg", hemoglobin="g/dL",
        fasting_blood_glucose="mg/dL", total_cholesterol="mg/dL",
        hdl_cholesterol="mg/dL", triglyceride="mg/dL",
        ldl_cholesterol="mg/dL", serum_creatinine="mg/dL",
        gfr="mL/min", ast="U/L", alt="U/L", y_gpt="U/L",
    ),
    ReferenceItem(
        ref_type="정상(A)",
        bmi="18.5-24.9",
        blood_pressure="120미만 이며/80미만",
        proteinuria="음성",
        hemoglobin="남: 13-16.5 / 여: 12-15.5",
        fasting_blood_glucose="100미만",
        total_cholesterol="200미만",
        hdl_cholesterol="60이상",
        triglyceride="150미만",
        ldl_cholesterol="130미만",
        serum_creatinine="1.6이하",
        gfr="60이상",
        ast="40이하",
        alt="35이하",
        y_gpt="남:11-63 / 여:8-35",
        chest_xray_result="정상, 비활동성",
        osteoporosis="T-score -1 이상",
    ),
    ReferenceItem(
        ref_type="정상(B)",
        bmi="18.5미만/25~29.9",
        blood_pressure="120-139 또는 /80-89",
        proteinuria="약양성±",
        hemoglobin="남: 12-12.9 / 여: 10-11.9",
        fasting_blood_glucose="100-125",
        total_cholesterol="200-239",
        hdl_cholesterol="40-59",
        triglyceride="150-199",
        ldl_cholesterol="130-139",
        ast="41-50",
        alt="36-45",
        y_gpt="남:64-77 / 여:36-45",
        osteoporosis="-1~-2.5 초과",
    ),
    ReferenceItem(
        ref_type="질환의심",
        waists="남 90이상 / 여 85이상",
        bmi="30이상",
        blood_pressure="140이상 또는 /90이상",
        proteinuria="양성(+1)이상",
        hemoglobin="남:12.0미만 / 여:10.0미만",
        fasting_blood_glucose="126이상",
        total_cholesterol="240이상",
        hdl_cholesterol="40미만",
        triglyceride="200이상",
        ldl_cholesterol="160이상",
        serum_creatinine="1.6초과",
        gfr="60미만",
        ast="51이상",
        alt="46이상",
        y_gpt="남:78이상 / 여:46이상",
        chest_xray_result="정상 및 비활동성이외의자",
        osteoporosis="-2.5이하",
    ),
]


# ResultItem
class ResultItemFactory(factory.Factory):
    class Meta:
        model = ResultItem

    case_type = "0"
    checkup_type = "일반"
    checkup_date = factory.Faker("date")
    organization_name = factory.Faker("company", locale="ko_KR")
    pdf_data = factory.Faker("file_name", extension="pdf")
    questionnaire = []


# HealthData
class HealthDataFactory(factory.Factory):
    class Meta:
        model = HealthData

    patient_name = factory.Faker("name", locale="ko_KR")
    overview_list = LazyAttribute(lambda _: [OverviewItemFactory.build()])
    reference_list = LazyAttribute(lambda _: _REFERENCE_LIST)
    result_list = LazyAttribute(lambda _: [ResultItemFactory.build()])


class WarningHealthDataFactory(HealthDataFactory):
    overview_list = LazyAttribute(lambda _: [WarningOverviewItemFactory.build()])


class DangerHealthDataFactory(HealthDataFactory):
    overview_list = LazyAttribute(lambda _: [DangerOverviewItemFactory.build()])

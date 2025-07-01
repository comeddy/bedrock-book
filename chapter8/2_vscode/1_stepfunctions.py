# Python 외부 라이브러리 임포트
import base64
import json
from io import BytesIO
import boto3
import streamlit as st
from PIL import Image

# 타이틀
st.title("자기소개 앱")

# 버킷 정보 분할
def split_bucket_info(arn: str):
    from urllib.parse import urlparse
    result = urlparse(arn)
    bucket_name = result.netloc
    key = result.path[1:]
    return bucket_name, key

# 이미지 파일 가져오기
def get_object(arn: str):
    bucket_name, key = split_bucket_info(arn)
    s3 = boto3.client("s3")
    response = s3.get_object(Bucket=bucket_name, Key=key)
    return json.loads(response["Body"].read().decode("utf-8"))

# 입력 폼 생성
with st.form("form"):
    state_machine_arn = st.text_input("stateMachineArn")
    submit = st.form_submit_button("실행")

# 실행 버튼을 눌렀을 때의 처리
if submit:
    # Step Functions 클라이언트 생성
    sfn_client = boto3.client("stepfunctions")

    # 스테이트 머신 실행
    response = sfn_client.start_sync_execution(stateMachineArn=state_machine_arn)

    # 실행 결과를 화면에 표시
    st.json(response, expanded=False)
    output = json.loads(response["output"])

    for o in output:
        # 자기소개를 화면에 표시
        if "Markdown" in o:
            completion = o["Markdown"]["Body"]["content"][0]["text"]
            st.markdown("# " + completion)

    # 이미지를 화면에 표시
        if "Image" in o:
            s3_arn = o["Image"]["Body"]
            body = get_object(s3_arn)
            image_base64 = body["artifacts"][0]["base64"]
            st.image(Image.open(BytesIO(base64.b64decode(image_base64))))

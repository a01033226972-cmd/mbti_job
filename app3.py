import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="scienter의 상담소 - 청소년 MBTI 분석",
    page_icon="🌊",
    layout="centered"
)

# 2. 시원한 여름 테마 및 커스텀 CSS 적용
st.markdown("""
    <style>
    /* 전체 배경: 연한 여름 바다 그라데이션 */
    .stApp {
        background: linear-gradient(180deg, #E0F7FA 0%, #E1F5FE 100%);
        font-family: 'Pretendard', sans-serif;
    }
    
    /* 상단 헤더 박스 */
    .main-header {
        background: linear-gradient(135deg, #00ACC1 0%, #00838F 100%);
        padding: 25px;
        border-radius: 20px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0, 172, 193, 0.25);
        margin-bottom: 20px;
    }
    .main-header h1 {
        margin: 0;
        font-size: 2.2rem;
        font-weight: 800;
        color: #FFFFFF;
    }
    .main-header p {
        margin-top: 8px;
        margin-bottom: 0;
        font-size: 1.05rem;
        opacity: 0.95;
    }

    /* 카드 스타일 */
    .job-card {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 16px;
        border-left: 6px solid #26C6DA;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    .job-title {
        color: #00838F;
        font-size: 1.25rem;
        font-weight: bold;
        margin-bottom: 6px;
    }
    .job-desc {
        color: #37474F;
        font-size: 0.98rem;
        line-height: 1.5;
    }

    /* 성별 분포 커스텀 진행바 디자인 */
    .gender-card {
        background-color: #FFFFFF;
        padding: 14px 18px;
        border-radius: 14px;
        margin-bottom: 12px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.04);
    }
    .gender-title {
        font-weight: bold;
        color: #006064;
        margin-bottom: 6px;
        display: flex;
        justify-content: space-between;
    }
    .bar-container {
        background-color: #ECEFF1;
        border-radius: 8px;
        height: 14px;
        width: 100%;
        display: flex;
        overflow: hidden;
    }
    .bar-male {
        background-color: #00BCD4;
        height: 100%;
    }
    .bar-female {
        background-color: #FF80AB;
        height: 100%;
    }

    /* 상담사 메시지 상자 */
    .counselor-box {
        background-color: #E0F2F1;
        border: 2px dashed #26A69A;
        padding: 18px;
        border-radius: 16px;
        color: #004D40;
        margin-top: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 데이터 정의
mbti_data = {
    "INTJ": [
        ("IT 시스템 아키텍트 / 프로그래머", "복잡한 문제를 논리적으로 분석하고 효율적인 시스템을 설계해요."),
        ("데이터 분석가", "데이터 속에서 패턴을 찾고 미래 전략을 세우는 데 뛰어나요."),
        ("경영 기획자 / 전략 컨설턴트", "장기적인 목표를 세우고 체계적으로 실행해 나가요.")
    ],
    "INTP": [
        ("AI 연구원 / 데이터 과학자", "새로운 기술과 원리를 깊게 탐구하는 과정에서 재미를 느껴요."),
        ("게임 디자이너", "독창적인 기획과 복잡한 규칙 설계를 통해 새로운 세계를 만들어내요."),
        ("학술 연구원 / 과학자", "관심 분야의 깊은 이론을 탐구하고 새로운 지식을 발견해요.")
    ],
    "ENTJ": [
        ("CEO / 스타트업 창업가", "목표를 향해 팀을 이끌고 과감한 결정을 내리는 리더십이 있어요."),
        ("변호사 / 법률 전문가", "논리적인 비판 의식과 설득력 있는 말하기로 정의를 실현해요."),
        ("프로젝트 매니저(PM)", "다양한 자원을 통솔하여 성과를 만들어내는 데 강해요.")
    ],
    "ENTP": [
        ("크리에이터 / 미디어 기획자", "풍부한 아이디어와 기발한 기획으로 사람들에게 즐거움을 줘요."),
        ("마케팅 전략가", "남들과 다른 시각으로 트렌드를 읽고 혁신적인 캠페인을 만들어요."),
        ("벤처 투자가", "가능성 있는 새로운 분야를 발굴하고 도전하는 것을 즐겨요.")
    ],
    "INFJ": [
        ("심리상담사 / 청소년 상담사", "타인의 마음을 깊이 이해하고 진심 어린 공감과 조언을 전해요."),
        ("작가 / 스토리텔러", "자신의 풍부한 감성과 통찰력을 글로 담아 사람들의 마음을 울려요."),
        ("환경 / 사회운동가", "더 나은 사회와 세상을 만들기 위한 가치 있는 일에 힘써요.")
    ],
    "INFP": [
        ("일러스트레이터 / 웹툰 작가", "나만의 상상력과 스토리를 예술적 작품으로 표현해내요."),
        ("콘텐츠 에디터", "따뜻한 시선과 문학적 감성으로 마음을 만지는 콘텐츠를 만들어요."),
        ("특수교사 / 언어치료사", "도움이 필요한 사람들에게 섬세하고 따뜻한 마음으로 다가가요.")
    ],
    "ENFJ": [
        ("진로 진학 교사", "학생 개개인의 잠재력을 발견하고 성장하도록 열정적으로 도와요."),
        ("아나운서 / 리포터", "진정성 있는 소통 능력으로 메시지를 명확하고 따뜻하게 전달해요."),
        ("비영리단체(NGO) 활동가", "공동체의 발전과 더 나은 세상을 위해 사람들을 모아요.")
    ],
    "ENFP": [
        ("행사 기획자 / 이벤트 디렉터", "넘치는 에너지와 창의력으로 모두가 즐거운 무대를 연출해요."),
        ("여행 에세이스트 / 유튜버", "새로운 경험을 즐기고 이를 사람들과 활기차게 공유해요."),
        ("광고 카피라이터", "사람들의 시선을 사로잡는 감각적인 문구를 써내려가요.")
    ],
    "ISTJ": [
        ("회계사 / 세무사", "정확한 규칙과 데이터로 신뢰할 수 있는 결과를 만들어내요."),
        ("공무원 / 행정 전문가", "질서와 법규를 준수하며 책임감 있게 임무를 수행해요."),
        ("사이버 보안 전문가", "꼼꼼하고 신중한 태도로 소중한 정보를 안전하게 지켜내요.")
    ],
    "ISFJ": [
        ("간호사 / 의료 보건 전문가", "따뜻한 친절함과 세심함으로 환자의 건강과 마음을 보살펴요."),
        ("초등/유치원 교사", "아이들에게 안정감을 주며 세심한 관심으로 성장을 지원해요."),
        ("사회복지사", "어려운 이웃을 실질적으로 도우며 따뜻한 울타리가 되어줘요.")
    ],
    "ESTJ": [
        ("경찰관 / 소방관", "원칙과 투철한 사명감으로 사회의 안전과 질서를 유지해요."),
        ("호텔 지배인 / 서비스 매니저", "체계적인 관리 능력과 효율적 운영으로 서비스를 제공해요."),
        ("자산 관리사", "철저한 분석과 계획으로 자산을 안전하고 체계적으로 관리해요.")
    ],
    "ESFJ": [
        ("항공 승무원", "풍부한 공감 능력과 세심한 배려로 편안한 여행을 선물해요."),
        ("자원봉사 코디네이터", "사람들을 따뜻하게 이어주고 나눔을 실천하는 커뮤니티를 만들어요."),
        ("영양사 / 위생 관리사", "사람들의 건강하고 즐거운 식생활을 세심하게 챙겨줘요.")
    ],
    "ISTP": [
        ("자율주행/엔지니어", "기계와 시스템이 움직이는 원리를 이해하고 문제를 해결해요."),
        ("응급구조사", "위기 상황에서도 침착하고 신속하게 판단하여 대처해요."),
        ("프로 카레이서 / 파일럿", "뛰어난 공간 감각과 순발력으로 기계를 정교하게 컨트롤해요.")
    ],
    "ISFP": [
        ("패션 디자이너 / 스타일리스트", "나만의 감각적이고 유연한 미적 감각으로 아름다움을 창조해요."),
        ("파티시에 / 요리사", "오감을 활용해 정성스럽고 아름다운 맛의 즐거움을 전해요."),
        ("사진작가", "순간의 아름다움과 감성을 프레임 속에 자연스럽게 담아내요.")
    ],
    "ESTP": [
        ("스포츠 트레이너 / 선수", "강한 체력과 순발력을 바탕으로 에너지 넘치는 활동을 해요."),
        ("응급의학과 의사", "긴박한 현장에서도 즉각적으로 상황을 해결하는 순발력이 빛나요."),
        ("스타트업 마케터", "빠르게 변화하는 시장에 신속히 적응하며 답을 찾아내요.")
    ],
    "ESFP": [
        ("뮤지컬 배우 / 연기자", "남다른 표현력과 끼로 무대 위에서 감동과 즐거움을 선사해요."),
        ("레크리에이션 강사", "주변 사람들에게 긍정적인 에너지를 전파하며 분위기를 이끌어요."),
        ("보컬 / 음악가", "음악을 통해 자신의 감정을 자유롭게 표현하고 소통해요.")
    ]
}

# 1. 한국 청소년 전체 MBTI 분포 데이터 (%)
teen_mbti_overall = {
    "ENFP": 12.4, "ISTJ": 11.2, "ISFP": 10.1, "ESFP": 9.3,
    "INFP": 8.8,  "ESTJ": 8.2,  "ISFJ": 7.5,  "ESFJ": 6.8,
    "ENTP": 5.1,  "ESTP": 4.8,  "ISTP": 4.5,  "INTJ": 3.2,
    "ENFJ": 2.9,  "INTP": 2.2,  "INFJ": 1.8,  "ENTJ": 1.2
}

# 2. 청소년 MBTI 성비 데이터 (남학생 비율 %, 여학생 비율 %)
mbti_gender_ratio = {
    "ESTJ": (68, 32), "ISTJ": (64, 36), "ISTP": (62, 38), "ESTP": (60, 40),
    "INTP": (58, 42), "ENTP": (55, 45), "INTJ": (54, 46), "ENTJ": (52, 48),
    "ESFP": (45, 55), "ISFP": (40, 60), "ENFP": (38, 62), "ESFJ": (35, 65),
    "ISFJ": (32, 68), "ENFJ": (30, 70), "INFP": (28, 72), "INFJ": (25, 75)
}

# 4. 상단 메인 헤더
st.markdown("""
    <div class="main-header">
        <h1>🌊 scienter의 상담소</h1>
        <p>청소년을 위한 MBTI 통계 분석 & 맞춤 진로 상담소</p>
    </div>
""", unsafe_allow_html=True)

# 5. 페이지 탭 구성 (3개 탭으로 세분화)
tab1, tab2, tab3 = st.tabs([
    "📊 1. 청소년 MBTI 전체 분포", 
    "👫 2. 성비율별 MBTI 분포", 
    "🎯 3. MBTI 맞춤 직업 추천"
])

# ==================== 1번 탭 : 한국 청소년 MBTI 전체 분포 ====================
with tab1:
    st.subheader("🇰🇷 한국 청소년 MBTI 전체 분포")
    st.write("한국 중·고등학생들의 주요 성격 유형 비율입니다.")

    st.markdown("#### 🏆 가장 많은 청소년 MBTI (TOP 5)")
    top_5 = dict(sorted(teen_mbti_overall.items(), key=lambda x: x[1], reverse=True)[:5])
    st.bar_chart(top_5, color="#00ACC1")

    with st.expander("👀 16가지 전체 MBTI 비율 목록 보기"):
        col1, col2 = st.columns(2)
        items = list(teen_mbti_overall.items())
        for i, (mbti, ratio) in enumerate(items):
            if i < 8:
                col1.write(f"• **{mbti}**: {ratio}%")
            else:
                col2.write(f"• **{mbti}**: {ratio}%")

# ==================== 2번 탭 : 성비율별 MBTI 분포도 ====================
with tab2:
    st.subheader("👫 청소년 성별(남/여) MBTI 분포도")
    st.write("각 MBTI 유형 내에서 **남학생(🩵 하늘색)**과 **여학생(🩷 분홍색)**이 차지하는 비율입니다.")
    
    st.caption("📌 범례: 🩵 남학생 비율 | 🩷 여학생 비율")

    # 16가지 유형별 남녀 성비 시각화
    for mbti, (male, female) in mbti_gender_ratio.items():
        st.markdown(f"""
            <div class="gender-card">
                <div class="gender-title">
                    <span>✨ {mbti}</span>
                    <span>남 {male}% | 여 {female}%</span>
                </div>
                <div class="bar-container">
                    <div class="bar-male" style="width: {male}%;"></div>
                    <div class="bar-female" style="width: {female}%;"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("""
        <div class="counselor-box">
            💡 <b>scienter 선생님의 분석 포인트!</b><br>
            • <b>사고형(T)</b>이 포함된 유형(ESTJ, ISTJ 등)은 남학생 비율이 상대적으로 높게 나타나요.<br>
            • <b>감정형(F)</b>이 포함된 유형(INFP, INFJ, ENFJ 등)은 여학생 비율이 눈에 띄게 높답니다!<br>
            성별에 따른 경향 차이일 뿐, 개인의 고유한 성향이 가장 중요하다는 점 잊지 마세요. ✨
        </div>
    """, unsafe_allow_html=True)

# ==================== 3번 탭 : MBTI 맞춤 직업 추천 ====================
with tab3:
    st.write("👋 **반가워요! 상담전문가 scienter입니다.**")
    st.write("너의 MBTI를 선택하면 성격 장점을 살릴 수 있는 추천 직업 3가지를 보여줄게!")

    selected_mbti = st.selectbox(
        "👉 **너의 MBTI 유형을 선택해줘:**",
        list(mbti_data.keys()),
        index=0
    )

    st.divider()

    st.subheader(f"✨ [{selected_mbti}] 유형 친구들을 위한 추천 직업")
    jobs = mbti_data[selected_mbti]

    for idx, (title, desc) in enumerate(jobs, 1):
        st.markdown(f"""
            <div class="job-card">
                <div class="job-title">{idx}. {title}</div>
                <div class="job-desc">{desc}</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("""
        <div class="counselor-box">
            💡 <b>scienter 선생님의 한마디!</b><br>
            "MBTI는 여러분의 가능성을 찾아가는 수많은 힌트 중 하나예요.<br>
            지금 당장 꿈이 명확하지 않아도 괜찮습니다. 여러분 안에는 생각보다 훨씬 더 멋진 재능이 숨어있답니다. 🌊"
        </div>
    """, unsafe_allow_html=True)
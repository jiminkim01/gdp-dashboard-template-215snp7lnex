import streamlit as st
import pandas as pd
import json

# 데이터 로드 함수
@st.cache
def load_data():
    data = """{
        "human-catalepsy": {"value": 0, "label": "catalepsy"},
        "human-impulsiveness": {"value": 2, "label": "impulsiveness"},
        "human-grandiosity": {"value": 0, "label": "grandiosity"},
        "human-jealousy_(infidelity)_delusion": {"value": 0, "label": "jealousy_(infidelity)_delusion"},
        "human-thought_broadcasting": {"value": 2, "label": "thought_broadcasting"},
        "human-dissociation": {"value": 0, "label": "dissociation"},
        "human-stereotypy": {"value": 0, "label": "stereotypy"},
        "human-soliloquy": {"value": 0, "label": "soliloquy"},
        "human-dissociative_amnesia": {"value": 0, "label": "dissociative_amnesia"},
        "human-nightmare": {"value": 0, "label": "nightmare"},
        "human-lack_of_motivation": {"value": 1, "label": "lack_of_motivation"},
        "human-religious_delusion": {"value": 0, "label": "religious_delusion"},
        "human-compulsion": {"value": 0, "label": "compulsion"},
        "human-thought_insertion": {"value": 1, "label": "thought_insertion"},
        "human-circumstantiality": {"value": 1, "label": "circumstantiality"},
        "human-binge_eating": {"value": 0, "label": "binge_eating"},
        "human-chronic_fatigue": {"value": 0, "label": "chronic_fatigue"},
        "human-visual_hallucination": {"value": 2, "label": "visual_hallucination"},
        "human-panic_like_symptom": {"value": 0, "label": "panic_like_symptom"},
        "human-feeling_of_inappropriate_or_excessive_guilt": {"value": 2, "label": "feeling_of_inappropriate_or_excessive_guilt"},
        "human-somatic_delution": {"value": 0, "label": "somatic_delution"},
        "human-worry": {"value": 0, "label": "worry"},
        "human-memory_decline": {"value": 0, "label": "memory_decline"},
        "human-loss_of_pleasure_(anhedonia)": {"value": 1, "label": "loss_of_pleasure_(anhedonia)"},
        "human-elevated_mood": {"value": 1, "label": "elevated_mood"},
        "human-diminished_emotional_expression_(apathy)": {"value": 0, "label": "diminished_emotional_expression_(apathy)"},
        "human-running_commentary_hallucination": {"value": 0, "label": "running_commentary_hallucination"},
        "human-bulimia": {"value": 0, "label": "bulimia"},
        "human-diminished_interest": {"value": 2, "label": "diminished_interest"},
        "human-odd_or_illogical_thinking": {"value": 1, "label": "odd_or_illogical_thinking"},
        "human-mutism": {"value": 0, "label": "mutism"},
        "human-auditory_hallucination": {"value": 1, "label": "auditory_hallucination"},
        "human-decreased_need_for_sleep": {"value": 2, "label": "decreased_need_for_sleep"},
        "human-increased_appetite": {"value": 0, "label": "increased_appetite"},
        "human-hypochondriasis": {"value": 0, "label": "hypochondriasis"},
        "human-decreased_appetite": {"value": 0, "label": "decreased_appetite"},
        "human-depersonalization": {"value": 1, "label": "depersonalization"},
        "human-reckless_(dangerous)_behavior": {"value": 1, "label": "reckless_(dangerous)_behavior"},
        "human-grandiose_delusion": {"value": 0, "label": "grandiose_delusion"},
        "human-weight_loss": {"value": 0, "label": "weight_loss"},
        "human-feeling_of_worthlessness": {"value": 1, "label": "feeling_of_worthlessness"},
        "human-thought_withdrawal": {"value": 1, "label": "thought_withdrawal"},
        "human-tactile_hallucination": {"value": 1, "label": "tactile_hallucination"},
        "human-delusion_of_being_controlled": {"value": 1, "label": "delusion_of_being_controlled"},
        "human-commanding_voice": {"value": 0, "label": "commanding_voice"},
        "human-suicidal_idea": {"value": 0, "label": "suicidal_idea"},
        "human-idea_of_reference": {"value": 1, "label": "idea_of_reference"},
        "human-psychomotor_agitation": {"value": 2, "label": "psychomotor_agitation"},
        "human-olfactory_hallucination": {"value": 1, "label": "olfactory_hallucination"},
        "human-derealization": {"value": 2, "label": "derealization"},
        "human-flight_of_ideas": {"value": 2, "label": "flight_of_ideas"},
        "human-headache": {"value": 0, "label": "headache"},
        "human-loosening_of_association": {"value": 1, "label": "loosening_of_association"},
        "human-concentration_difficulty": {"value": 0, "label": "concentration_difficulty"},
        "human-obsession": {"value": 0, "label": "obsession"},
        "human-stupor": {"value": 0, "label": "stupor"},
        "human-restlessness": {"value": 0, "label": "restlessness"},
        "human-negativism": {"value": 0, "label": "negativism"},
        "human-anorexia": {"value": 0, "label": "anorexia"},
        "human-paranoid_delusion": {"value": 3, "label": "paranoid_delusion"},
        "human-increase_in_goal-directed_activity": {"value": 1, "label": "increase_in_goal-directed_activity"},
        "human-irritable_mood": {"value": 1, "label": "irritable_mood"},
        "human-weight_gain": {"value": 0, "label": "weight_gain"},
        "human-tangentiality": {"value": 1, "label": "tangentiality"},
        "human-suicidal_attempt": {"value": 0, "label": "suicidal_attempt"},
        "human-insomnia": {"value": 2, "label": "insomnia"},
        "human-erotic_delusion": {"value": 0, "label": "erotic_delusion"},
        "human-nihilistic_delusion": {"value": 0, "label": "nihilistic_delusion"},
        "human-anxiety": {"value": 0, "label": "anxiety"},
        "human-gustatory_hallucination": {"value": 0, "label": "gustatory_hallucination"},
        "human-hypersomnia": {"value": 0, "label": "hypersomnia"},
        "human-depressed_mood": {"value": 1, "label": "depressed_mood"},
        "human-nonsuicidal_injury": {"value": 0, "label": "nonsuicidal_injury"}
    }"""
    return json.loads(data)

data_dict = load_data()
df = pd.DataFrame(data_dict).T

# 앱 제목
st.title('Human Symptoms Analysis')

# 데이터프레임 표시
st.dataframe(df)

# 데이터 요약
st.write('## Data Summary')
st.write(df.describe())

# 특정 데이터 필터링 및 시각화
symptom = st.selectbox('Select Symptom', df['label'].unique())
filtered_data = df[df['label'] == symptom]

st.write(f"### Data for {symptom}")
st.write(filtered_data)

### 예시 코드

#### app.py
```python
import streamlit as st
import pandas as pd
import json

@st.cache
def load_data():
    data = """
    {
        "human-catalepsy": {"value": 0, "label": "catalepsy"},
        "human-impulsiveness": {"value": 2, "label": "impulsiveness"},
        "human-grandiosity": {"value": 0, "label": "grandiosity"},
        "human-jealousy_(infidelity)_delusion": {"value": 0, "label": "jealousy_(infidelity)_delusion"},
        "human-thought_broadcasting": {"value": 2, "label": "thought_broadcasting"},
        "human-dissociation": {"value": 0, "label": "dissociation"},
        "human-stereotypy": {"value": 0, "label": "stereotypy"},
        "human-soliloquy": {"value": 0, "label": "soliloquy"},
        "human-dissociative_amnesia": {"value": 0, "label": "dissociative_amnesia"},
        "human-nightmare": {"value": 0, "label": "nightmare"},
        "human-lack_of_motivation": {"value": 1, "label": "lack_of_motivation"},
        "human-religious_delusion": {"value": 0, "label": "religious_delusion"},
        "human-compulsion": {"value": 0, "label": "compulsion"},
        "human-thought_insertion": {"value": 1, "label": "thought_insertion"},
        "human-circumstantiality": {"value": 1, "label": "circumstantiality"},
        "human-binge_eating": {"value": 0, "label": "binge_eating"},
        "human-chronic_fatigue": {"value": 0, "label": "chronic_fatigue"},
        "human-visual_hallucination": {"value": 2, "label": "visual_hallucination"},
        "human-panic_like_symptom": {"value": 0, "label": "panic_like_symptom"},
        "human-feeling_of_inappropriate_or_excessive_guilt": {"value": 2, "label": "feeling_of_inappropriate_or_excessive_guilt"},
        "human-somatic_delution": {"value": 0, "label": "somatic_delution"},
        "human-worry": {"value": 0, "label": "worry"},
        "human-memory_decline": {"value": 0, "label": "memory_decline"},
        "human-loss_of_pleasure_(anhedonia)": {"value": 1, "label": "loss_of_pleasure_(anhedonia)"},
        "human-elevated_mood": {"value": 1, "label": "elevated_mood"},
        "human-diminished_emotional_expression_(apathy)": {"value": 0, "label": "diminished_emotional_expression_(apathy)"},
        "human-running_commentary_hallucination": {"value": 0, "label": "running_commentary_hallucination"},
        "human-bulimia": {"value": 0, "label": "bulimia"},
        "human-diminished_interest": {"value": 2, "label": "diminished_interest"},
        "human-odd_or_illogical_thinking": {"value": 1, "label": "odd_or_illogical_thinking"},
        "human-mutism": {"value": 0, "label": "mutism"},
        "human-auditory_hallucination": {"value": 1, "label": "auditory_hallucination"},
        "human-decreased_need_for_sleep": {"value": 2, "label": "decreased_need_for_sleep"},
        "human-increased_appetite": {"value": 0, "label": "increased_appetite"},
        "human-hypochondriasis": {"value": 0, "label": "hypochondriasis"},
        "human-decreased_appetite": {"value": 0, "label": "decreased_appetite"},
        "human-depersonalization": {"value": 1, "label": "depersonalization"},
        "human-reckless_(dangerous)_behavior": {"value": 1, "label": "reckless_(dangerous)_behavior"},
        "human-grandiose_delusion": {"value": 0, "label": "grandiose_delusion"},
        "human-weight_loss": {"value": 0, "label": "weight_loss"},
        "human-feeling_of_worthlessness": {"value": 1, "label": "feeling_of_worthlessness"},
        "human-thought_withdrawal": {"value": 1, "label": "thought_withdrawal"},
        "human-tactile_hallucination": {"value": 1, "label": "tactile_hallucination"},
        "human-delusion_of_being_controlled": {"value": 1, "label": "delusion_of_being_controlled"},
        "human-commanding_voice": {"value": 0, "label": "commanding_voice"},
        "human-suicidal_idea": {"value": 0, "label": "suicidal_idea"},
        "human-idea_of_reference": {"value": 1, "label": "idea_of_reference"},
        "human-psychomotor_agitation": {"value": 2, "label": "psychomotor_agitation"},
        "human-olfactory_hallucination": {"value": 1, "label": "olfactory_hallucination"},
        "human-derealization": {"value": 2, "label": "derealization"},
        "human-flight_of_ideas": {"value": 2, "label": "flight_of_ideas"},
        "human-headache": {"value": 0, "label": "headache"},
        "human-loosening_of_association": {"value": 1, "label": "loosening_of_association"},
        "human-concentration_difficulty": {"value": 0, "label": "concentration_difficulty"},
        "human-obsession": {"value": 0, "label": "obsession"},
        "human-stupor": {"value": 0, "label": "stupor"},
        "human-restlessness": {"value": 0, "label": "restlessness"},
        "human-negativism": {"value": 0, "label": "negativism"},
        "human-anorexia": {"value": 0, "label": "anorexia"},
        "human-paranoid_delusion": {"value": 3, "label": "paranoid_delusion"},
        "human-increase_in_goal-directed_activity": {"value": 1, "label": "increase_in_goal-directed_activity"},
        "human-irritable_mood": {"value": 1, "label": "irritable_mood"},
        "human-weight_gain": {"value": 0, "label": "weight_gain"},
        "human-tangentiality": {"value": 1, "label": "tangentiality"},
        "human-suicidal_attempt": {"value": 0, "label": "suicidal_attempt"},
        "human-insomnia": {"value": 2, "label": "insomnia"},
        "human-erotic_delusion": {"value": 0, "label": "erotic_delusion"},
        "human-nihilistic_delusion": {"value": 0, "label": "nihilistic_delusion"},
        "human-anxiety": {"value": 0, "label": "anxiety"},
        "human-gustatory_hallucination": {"value": 0, "label": "gustatory_hallucination"},
        "human-hypersomnia": {"value": 0, "label": "hypersomnia"},
        "human-depressed_mood": {"value": 1, "label": "depressed_mood"},
        "human-nonsuicidal_injury": {"value": 0, "label": "nonsuicidal_injury"}
    }"""
    return json.loads(data)

data_dict = load_data()
df = pd.DataFrame(data_dict).T

# 앱 제목
st.title('Human Symptoms Analysis')

# 데이터프레임 표시
st.dataframe(df)

# 데이터 요약
st.write('## Data Summary')
st.write(df.describe())

# 특정 데이터 필터링 및 시각화
symptom = st.selectbox('Select Symptom', df['label'].unique())
filtered_data = df[df['label'] == symptom]

st.write(f"### Data for {symptom}")
st.write(filtered_data)

# 바 차트 시각화
st.bar_chart(filtered_data['value'])

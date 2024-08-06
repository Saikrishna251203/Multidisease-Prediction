import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")



#loading the models

diabetes_model = pickle.load(open("C:/Users/bhuvana/Desktop/Multiple disease prediction  system/saved models/diabetes_model.sav",'rb'))


heart_disease_model = pickle.load(open("C:/Users/bhuvana/Desktop/Multiple disease prediction  system/saved models/heart_disease_model.sav",'rb'))

parkinson_model = pickle.load(open("C:/Users/bhuvana/Desktop/Multiple disease prediction  system/saved models/parkinsons_model.sav",'rb'))

Lungcancer_model = pickle.load(open("C:/Users/bhuvana/Desktop/Multiple disease prediction  system/saved models/lungcancer_model.sav",'rb'))

Stroke_model = pickle.load(open("C:/Users/bhuvana/Desktop/Multiple disease prediction  system/saved models/stroke_model.sav",'rb'))

cirohosis_model = pickle.load(open("C:/Users/bhuvana/Desktop/Multiple disease prediction  system/saved models/cirohosis_model.sav",'rb'))

chronickidneyfailure_model = pickle.load(open("C:/Users/bhuvana/Desktop/Multiple disease prediction  system/saved models/chronickidneyfailure_model.sav",'rb'))

# Sidebar menu
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinson Disease Prediction',
                            'Lung Cancer Prediction',
                            'Stroke Prediction',
                            'Cirohosis Disease Prediction',
                            'Chronic Kidney Failure Prediction'],
                           icons=['activity', 'heart-pulse-fill', 'person-arms-up', 'lungs-fill', 'ear-fill', 'person-wheelchair', 'clipboard2-pulse-fill'],
                           default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        try:
            user_input = [float(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness), float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)]
            diab_prediction = diabetes_model.predict([user_input])
            diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
        except Exception as e:
            diab_diagnosis = f"Error: {e}"
    st.success(diab_diagnosis)

# Heart Disease Prediction Page
elif selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholesterol in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by fluoroscopy')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        try:
            user_input = [float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs), float(restecg), float(thalach), float(exang), float(oldpeak), float(slope), float(ca), float(thal)]
            heart_prediction = heart_disease_model.predict([user_input])
            heart_diagnosis = 'The person is having heart disease' if heart_prediction[0] == 1 else 'The person does not have any heart disease'
        except Exception as e:
            heart_diagnosis = f"Error: {e}"
    st.success(heart_diagnosis)

# Parkinson's Prediction Page
elif selected == "Parkinson Disease Prediction":
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col1:
        RAP = st.text_input('MDVP:RAP')
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
    with col3:
        DDP = st.text_input('Jitter:DDP')
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
    with col3:
        APQ = st.text_input('MDVP:APQ')
    with col4:
        DDA = st.text_input('Shimmer:DDA')
    with col5:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')

    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        try:
            user_input = [float(fo), float(fhi), float(flo), float(Jitter_percent), float(Jitter_Abs), float(RAP), float(PPQ), float(DDP), float(Shimmer), float(Shimmer_dB), float(APQ3), float(APQ5), float(APQ), float(DDA), float(NHR), float(HNR), float(RPDE), float(DFA), float(spread1), float(spread2), float(D2), float(PPE)]
            parkinsons_prediction = parkinson_model.predict([user_input])
            parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
        except Exception as e:
            parkinsons_diagnosis = f"Error: {e}"
    st.success(parkinsons_diagnosis)

# Lung Cancer Prediction Page
elif selected == 'Lung Cancer Prediction':
    st.title('Lung Cancer Prediction using ML')

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        YELLOW_FINGERS = st.text_input("YELLOW FINGERS")
    with col2:
        ANXIETY = st.text_input("ANXIETY")
    with col3:
        PEER_PRESSURE = st.text_input("PEER PRESSURE")
    with col4:
        CHRONIC_DISEASE = st.text_input("CHRONIC DISEASE")
    with col1:
        FATIGUE = st.text_input("FATIGUE")
    with col2:
        ALLERGY = st.text_input("ALLERGY")
    with col3:
        WHEEZING = st.text_input("WHEEZING")
    with col4:
        ALCOHOL_CONSUMING = st.text_input("ALCOHOL CONSUMING")
    with col1:
        COUGHING = st.text_input("COUGHING")
    with col2:
        SWALLOWING_DIFFICULTY = st.text_input("SWALLOWING DIFFICULTY")
    with col3:
        CHEST_PAIN = st.text_input("CHEST PAIN")
    with col4:
        ANXYELFIN = st.text_input("ANXYELFIN")

    lung_cancer_diagnosis = ''
    if st.button("Lung Cancer Test Result"):
        try:
            user_input = [
                float(YELLOW_FINGERS),
                float(ANXIETY),
                float(PEER_PRESSURE),
                float(CHRONIC_DISEASE),
                float(FATIGUE),
                float(ALLERGY),
                float(WHEEZING),
                float(ALCOHOL_CONSUMING),
                float(COUGHING),
                float(SWALLOWING_DIFFICULTY),
                float(CHEST_PAIN),
                float(ANXYELFIN)
            ]
            lung_cancer_prediction = lung_cancer_model.predict([user_input])
            lung_cancer_diagnosis = "The person has lung cancer disease" if lung_cancer_prediction[0] == 1 else "The person does not have lung cancer disease"
        except Exception as e:
            lung_cancer_diagnosis = f"Error: {e}"
    st.success(lung_cancer_diagnosis)

# Stroke Prediction Page
elif selected == 'Stroke Prediction':
    st.title('Stroke Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.text_input('Gender')
    with col2:
        age = st.text_input('Age')
    with col3:
        hypertension = st.text_input('Hypertension')
    with col1:
        heart_disease = st.text_input('Heart Disease')
    with col2:
        ever_married = st.text_input('Ever Married')
    with col3:
        work_type = st.text_input('Work Type')
    with col1:
        Residence_type = st.text_input('Residence Type')
    with col2:
        avg_glucose_level = st.text_input('Average Glucose Level')
    with col3:
        bmi = st.text_input('BMI')
    with col1:
        smoking_status = st.text_input('Smoking Status')

    stroke_diagnosis = ''
    if st.button('Stroke Test Result'):
        try:
            user_input = [float(gender), float(age), float(hypertension), float(heart_disease), float(ever_married), float(work_type), float(Residence_type), float(avg_glucose_level), float(bmi), float(smoking_status)]
            stroke_prediction = stroke_model.predict([user_input])
            stroke_diagnosis = 'The person is likely to have a stroke' if stroke_prediction[0] == 1 else 'The person is unlikely to have a stroke'
        except Exception as e:
            stroke_diagnosis = f"Error: {e}"
    st.success(stroke_diagnosis)

# Cirohosis Disease Prediction Page
elif selected == 'Cirohosis Disease Prediction':
    st.title('Cirohosis Disease Prediction using ML')

    col1, col2,  = st.columns(2)

    with col1:
        Stage_4 = st.text_input("Stage_4")
    with col2:
        Ascites_Y =st.text_input("Ascites_Y")
    with col1:
        Hepatomegaly_Y = st.text_input("Hepatomegaly_Y")
    with col2:
        Spiders_Y = st.text_input("Spiders_Y")
    with col1:
        Edema_Y = st.text_input("Edema_Y")
    with col2:
        Bilirubin_high = st.text_input("Bilirubin_high")
    with col1:
        Copper_high = st.text_input("Copper_high")
    with col2:
        Prothrombin_normal = st.text_input("Prothrombin_normal")


    cirohosis_diagnosis = ''
    if st.button('Cirohosis Disease Test Result'):
        try:
            user_input = [float(Stage_4), float(Ascites_Y), float(Hepatomegaly_Y), float( Spiders_Y), float(Edema_Y), float(Bilirubin_high), float( Copper_high ), float(Prothrombin_normal)]
            cirohosis_prediction = cirohosis_model.predict([user_input])
            cirohosis_diagnosis = 'The person has cirohosis disease' if cirohosis_prediction[0] == 1 else 'The person does not have cirohosis disease'
        except Exception as e:
            cirohosis_diagnosis = f"Error: {e}"
    st.success(cirohosis_diagnosis)

# Chronic Kidney Failure Prediction Page
elif selected == 'Chronic Kidney Failure Prediction':
    st.title('Chronic Kidney Failure Prediction using ML')

    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
        age = st.text_input("Age")
    with col2:
        blood_pressure = st.text_input("Blood Pressure")
    with col3:
        specific_gravity = st.text_input("Specific Gravity")
    with col4:
        albumin =st.text_input("Albumin")
    with col5:
        sugar = st.text_input("sugar")
    with col1:
        red_blood_cells = st.text_input("Red Blood Cells") 
    with col2:
        pus_cell = st.text_input("Pus Cell")
    with col3:
        pus_cell_clumps = st.text_input("Pus Cell Clumps")
    with col4:
        bacteria = st.text_input("Bacteria")
    with col5:
        blood_glucose_random = st.text_input("blood_glucose_random")
    with col1:
        blood_urea = st.text_input("blood_urea")
    with col2:
        serum_creatinine = st.text_input("serum_creatinine")
    with col3:
        sodium = st.text_input("sodium")
    with col4:
        potassium = st.text_input("potassium")
    with col5:
        haemoglobin = st.text_input("haemoglobin")
    with col1:
        packed_cell_volume = st.text_input("packed_cell_volume")
    with col2:
        white_blood_cell_count = st.text_input("white_blood_cell_count")
    with col3:
         red_blood_cell_count = st.text_input("red_blood_cell_count")
    with col4:
         hypertension = st.text_input("hypertension")
    with col5: 
        diabetes_mellitus = st.text_input("diabetes_mellitus")
    with col1:
        coronary_artery_disease = st.text_input("coronary_artery_disease")
    with col2: 
        appetite = st.text_input("appetite")
    with col3:
        peda_edema = st.text_input("peda_edema")
    with col4:
        aanemia = st.text_input("aanemia")




    kidney_failure_diagnosis = ''
    if st.button('Chronic Kidney Failure Test Result'):
        try:
            user_input = [float(age), float(blood_pressure),float(specific_gravity),float(albumin),float(sugar),float(red_blood_cells),float(pus_cell),float(pus_cell_clumps),float(bacteria),float(blood_glucose_random),float(blood_urea),float(serum_creatinine),float(sodium),float(potassium),float(haemoglobin),float(packed_cell_volume),float(white_blood_cell_count),float( red_blood_cell_count),float(hypertension),float(diabetes_mellitus),float(coronary_artery_disease),float(appetite),float(peda_edema),float( aanemia)]
            kidney_failure_prediction = chronickidneyfailure_model.predict([user_input])
            kidney_failure_diagnosis = 'The person has chronic kidney failure' if kidney_failure_prediction[0] == 1 else 'The person does not have chronic kidney failure'
        except Exception as e:
            kidney_failure_diagnosis = f"Error: {e}"
    st.success(kidney_failure_diagnosis)





     

     
    

                        
                        
                             
                           
                       
                        
                
        
                     
                                
                        
                

        
#PHYSICIAN
#This is a demo version
try:
    from translate import Translator
    print('Hi, type and hit enter for the number of your language: English 1, Português 2, Español 3.If you are getting text in a language different than English, so just type English version (both versions of text are in order/sequence)')
    a='english'
    i = input()
    if i == '1':
        b='english'
    if i == '2':
        b='pt-br'
    if i == '3':
        b='español'
except:
    a=''
def t():
    try:
        set = Translator(from_lang=a, to_lang=b)
        y=set.translate(o)
        print('\n')
        print(y)
        print('\n\n')
    except:
        y='\n'

#NAME OF SOFTWARE
#pip install pyfiglet
try:
    import pyfiglet
    word='Physician'
    pyfiglet.print_figlet(word,font='digital')
    pyfiglet.print_figlet(word,font='stop')
    all_fonts=pyfiglet.FigletFont.getFonts()
except:
    print('+-+-+-+-+-+-+-+-+-+\n|P|h|y|s|i|c|i|a|n|\n+-+-+-+-+-+-+-+-+-+')
    print(' ______  _                _       _\n(_____ \| |              (_)     (_)\n _____) ) | _  _   _  ___ _  ____ _  ____ ____\n|  ____/| || \| | | |/___) |/ ___) |/ _  |  _ \ \n| |     | | | | |_| |___ | ( (___| ( ( | | | | |\n|_|     |_| |_|\__  (___/|_|\____)_|\_||_|_| |_|\n              (____/')
    
#MEETING
o="Hi, I'm Physician"
print(o)
t()
o="Write 'exit' to exit the software"

print(o)
t()
o="I was built by Jessé Alves Leite, born in Sao Paulo, Brazil, 1998 and I can do all what a physician does, except for surgeries.\nPlease, type 'medical advice', keep rewriting,then hit enter."

print(o)
t()
o="Check out: 'https://jessealvesleitesoftwares.company.site'"
print(o)
t()

#ALGORITHMS
while True:
    i = input()
    if i == 'medical advice':
        o="write/say basic symptoms, emergence, first aid, poisons, diagnosis(symptoms in alphabetical order), tests(disease) treatment(disease), laboratory tests, advanced symptoms, derived diseases,  immortal"
    elif i == "basic symptoms":
        o="write diagnosis abdominal pain, diagnosis chest pain, diagnosis cough, diagnosis diarrhea, diagnosis dizziness, diagnosis headache, diagnosis joint pain, diagnosis low back pain,\ndiagnosis painful shoulder, diagnosis rectal bleeding, diagnosis sore throat, diagnosis urinary frequency and burning, diagnosis vaginal discharge"
    elif i == "advanced symptoms":
        o="say abdominal acute pain, abdominal pain chronic recurrent, abdominal rigidity, abdominal swelling focal, abdominal swelling generalized, absent or diminished pulse, acid phosphatase elevation, acidosis, alkaline phosphatase elevation, alkalosis, alopecia, iron serum, serum uric acid, amenorrhea, amnesia, anemia, ankle clonus, anorexia, anosmia or unusual odors, anuria or oliguria, anxiety, aphasia apraxia and agnosia, ascites, aspartate aminotransferase elevation, ataxia, axillary mass, Babinski's sign, back pain, bleeding gums, blindness, blurred vision, bone mass or swelling, borborygmi, bradycardia, breast discharge, breast mass, breast pain, cardiac arrhythmia, cardiac murmurs, cardiomegaly, chest pain, chest tenderness, chills, choreiform movements, clubbing of the fingers, coma, constipation, convulsions or syncope, cough, cramps muscular, c-reactive protein, cyanosis, deafness, delayed puberty, delirium, delusions, dementia, depression, diaphoresis, diarrhea acute, diarrhea chronic, difficulty urinating, diplopia, dizziness, drop attacks, dwarfism, dysarthria, dysmenorrhea, dyspareunia, dysphagia, dyspnea, dysuria, ear discharge, earache, edema generalized, edema localized, enuresis, epiphora, epistaxis, euphoria, exophthalmos, extremity pain lower extremity, extremity pain upper extremity, eye pain, face pain, facial flushing, facial paralysis, facial swelling, failure to thrive, fatigue, femoral mass or swelling, fever acute, fever chronic, flank mass, flank pain, flatulence, foot and toe pain, foot deformities, foot ulceration, free thyroxine, frequency of urination, frigidity, gait disturbances, gangrene, gigantism, girdle pain, glycosuria, gynecomastia, halitosis, halucinations, headache, heartburn, heel pain, hematemesis, hematuria, hemianopsia, hemiparesis or hemiplegia, hemoptysis, hepatomegaly, hiccups, hip pain, hirsutism, hoarseness, Horner's syndrome, 25-hydroxyvitamin d2 and d3, hyperactive reflexes, hypercalcemia, hypercholesterolemia, hyperglycemia, hyperkalemia, hyperkinesis, hypernatremia, hyperpigmentation, hypersomnia, hypertension, hypertriglyceridemia a, hypertriglyceridemia b, hypoactive reflexes, hypoalbuminemia, hypocalcemia, hypochondriasis, hypoglycemia, hypokalemia, hyponatremia, hypotension chronic, hypothermia, hypoxemia, impotence, incontinence of feces, incontinence of urine, increased serum bilirubin, indigestion, infertility female, infertility male, inguinal swelling, insomnia, intermittent claudication, jaundice, jaw pain, jaw swelling, joint pain, joint swelling, knee pain, knee swelling, kyphosis, lactic dehydrogenase elevation, leg ulceration, leucocytosis, leucopenia, lip pain, lip swelling, lymphadenopathy, melena, memory loss, menorrhagia, mental retardation, meteorism, metrorrhagia, monoplegia, mouth pigmentation, muscular atrophy, musculoskeletal pain generalized, nail abnormalities, nasal discharge, nasal obstruction, nausea and vomiting, neck pain, neck stiffness, neck swelling, nightmares, nocturia, nose regurgitation of food through, nystagmus, obesity pathologic, odor, opisthotonus, pain in the penis, pallor, palpitations, papilledema, paresthesias of the lower extremity, paresthesias of the upper extremity, pathologic reflexes, pelvic mass, pelvic pain, penile sores, perineum pain, periorbital edema, photophobia, plasma cortisol, polycythemia, polydipsia, polyuria, popliteal swelling, precocious puberty, priapism, prolonged prothrombin time, proteinuria, pruritus generalized, pruritus vulvae, ptosis, ptyalism, pulse irregularity, pulses unequal, pupil abnormalities, purpura and abnormal bleeding, pyuria, rales, rash distribution, rash morphology, Raynaud's phenomena, rectal bleeding, rectal discharge, rectal mass, rectal pain, red eye, regurgitation esophageal, respiration abnormalities, restless leg syndrome, risus sardonicus, scoliosis, scotoma, scrotal swelling, sedimentation rate, sensory loss, serum albumin, shoulder pain, sleep apnea, snoring, sore throat, splenomegaly acute or subacute, splenomegaly chronic, steatorrhea, strangury, stridor, stupor, syncope, tachycardia, taste abnormalities, testicular atrophy, testicular swelling, thirst or polydipsia, thrombocytopenia, thyroid enlargement, tinnitus, tongue mass or swelling, tremor, transient ischemic attacks, uremia, vaginal bleeding, vaginal discharge, vitamin b12, vulval or vaginal mass, vulval or vaginal ulcerations, weight loss"
    elif i == "derived diseases":
        o="acne vulgaris, asthma, atrial fibrillation, carpal tunnel syndrome, cataracts, cirrhosis, congestie heart failure, neuropathy, peptic ulcer, pharyngitis, pleural effusion, recurrent renal calculi, recurrent uti, stroke, uri"
# FIRST AID
    elif i == "first aid":
        o="Call the emergence service and say: mouth to mouth resuscitaion, first aid kit, accidents prevention, drowning, stroke, cramp, electric shock, kidney stone, foreign body, cut, fainting, chocking, fractures,\ninfarction, heat stroke, intoxication and allergies, nausea and vomiting, sting, low pressure, burn, bleeding, sprain, transport wounded, asphyxiation, amputation, seizure, chest pain, alcoholic coma, bruise, dislocation or head trauma"
    elif i == "first aid kit":
        o="if you want to do a first aid kit, you must put in some bag: cotton, bandages, thermal pouch, sterile gauze compresses, adhesive dresings of various sizes/band-aid, adhesive tape, latex gloves, clean cloth, clamp, ointment dor sprains or bumps, saline 0.9%, thermometer, scissors and say necessary medicines"
    elif i == "emergence":
        o="Do the primary evaluation, I mean, check if the airways are open, if the neck is stable, if there are more than 10 breathings per minute and if there's pulse, then say emergence 2"
    elif i == "emergence 2":
        o="do the secondary evaluation, seek for abnormalities in the members, vertebral column, skin color, head, mouth bleeding, chest, chest pain, meanly if going to the mandibule or towards left arm, mental confusion, hard speech, diziness, bad breathing, bad blood circulation and fever higher than 39 Celsius degrees"
    elif i == "accidents prevention":
        o="Avoid; slippery floor, accessible cleanning products, accessible cosmetics, pans wiithout cable towards stove center, watch out children and the elderly, avoid drinking alcohol and driving (or better, drink 1 liter of alcohol per year and don't smoke); if some accident happens, be sure that you and the victim stay safe (if in the street, remember the triangle reflector and put it far behind the vehicle, don't create a traffic, for that the ambulance may arrive), keep the curious ones away, call the emergence service and say emergence or first aid in the case it happens"
    elif i == "alcoholic coma":
        o="put the sick one somewhere safe, if vomits happen, leave him sitted, if unconcious, seek help (in this case, don't give him any food nor liquid)"
    elif i == "amputation":
        o="call emergence service immediatly, try to stop the bleeding by compressing around the injury, if partial amputation, don't finish it, if total amputation, put the member in a bag and this bag inside another one with ice and leave it to the hospital"
    elif i == "asphyxiations":
        o="say Heimlich's maneuver, if it doesn't work, make a tiny hole in the victim's throat, right above the first hard part (down to up direction), in the horizontal middle and put some clean object to keep it open, like pen tube, if a BABY, put him above your arm, which must be above your legs, with his belly towards the same arm and use your other arm to push his back with steady different movements, looking to expel what's in his arm"
    elif i == "bleeding":
        o="compress the region with a gauze or clean cloth, drive the vehicle carefully; if in the nose, sit down, don't incline your head and compress your nose during 10 minutes, if it doesn't solve it, seek help; if in the eye, apply cold water and go to a hospital; if inner organ is bleeding, so lye down the victim, seek help and describe carefully all the symptoms; if there's bruise, apply cold water and take paracetamol or dipyrone, the bruise will disappear in a few days"
    elif i == "bleeding time":
        o="2 to 7 minutes"
        
    elif i == 'exit':
        quit()
    else:
        o='Done'
    print(o)
    t()

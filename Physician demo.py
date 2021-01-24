#PHYSICIAN
import time
#This is a demo version

#MEETING
print("Hi, I'm Physician")
print("I was built by Jessé Alves Leite, born in Sao Paulo, Brazil, 1998 and I can do all what a physician does, except for surgeries.\nPlease, type 'medical advice', keep rewriting,then hit enter")
print("Check out: 'https://jessealvesleitesoftwares.company.site'")

#ALGORITHMS
y = 0
while y < 100:
    i = input()
    if i == 'medical advice':
        print("write/say basic symptoms, emergence, first aid, poisons, diagnosis(symptoms in alphabetical order), tests(disease) treatment(disease), laboratory tests, advanced symptoms, derived diseases,  immortal")
    elif i == "basic symptoms":
        myLabel = Label(root, text="write diagnosis abdominal pain, diagnosis chest pain, diagnosis cough, diagnosis diarrhea, diagnosis dizziness, diagnosis headache, diagnosis joint pain, diagnosis low back pain,\ndiagnosis painful shoulder, diagnosis rectal bleeding, diagnosis sore throat, diagnosis urinary frequency and burning, diagnosis vaginal discharge")
    elif i == "advanced symptoms":
        print("say abdominal acute pain, abdominal pain chronic recurrent, abdominal rigidity, abdominal swelling focal, abdominal swelling generalized, absent or diminished pulse, acid phosphatase elevation, acidosis, alkaline phosphatase elevation, alkalosis, alopecia, iron serum, serum uric acid, amenorrhea, amnesia, anemia, ankle clonus, anorexia, anosmia or unusual odors, anuria or oliguria, anxiety, aphasia apraxia and agnosia, ascites, aspartate aminotransferase elevation, ataxia, axillary mass, Babinski's sign, back pain, bleeding gums, blindness, blurred vision, bone mass or swelling, borborygmi, bradycardia, breast discharge, breast mass, breast pain, cardiac arrhythmia, cardiac murmurs, cardiomegaly, chest pain, chest tenderness, chills, choreiform movements, clubbing of the fingers, coma, constipation, convulsions or syncope, cough, cramps muscular, c-reactive protein, cyanosis, deafness, delayed puberty, delirium, delusions, dementia, depression, diaphoresis, diarrhea acute, diarrhea chronic, difficulty urinating, diplopia, dizziness, drop attacks, dwarfism, dysarthria, dysmenorrhea, dyspareunia, dysphagia, dyspnea, dysuria, ear discharge, earache, edema generalized, edema localized, enuresis, epiphora, epistaxis, euphoria, exophthalmos, extremity pain lower extremity, extremity pain upper extremity, eye pain, face pain, facial flushing, facial paralysis, facial swelling, failure to thrive, fatigue, femoral mass or swelling, fever acute, fever chronic, flank mass, flank pain, flatulence, foot and toe pain, foot deformities, foot ulceration, free thyroxine, frequency of urination, frigidity, gait disturbances, gangrene, gigantism, girdle pain, glycosuria, gynecomastia, halitosis, halucinations, headache, heartburn, heel pain, hematemesis, hematuria, hemianopsia, hemiparesis or hemiplegia, hemoptysis, hepatomegaly, hiccups, hip pain, hirsutism, hoarseness, Horner's syndrome, 25-hydroxyvitamin d2 and d3, hyperactive reflexes, hypercalcemia, hypercholesterolemia, hyperglycemia, hyperkalemia, hyperkinesis, hypernatremia, hyperpigmentation, hypersomnia, hypertension, hypertriglyceridemia a, hypertriglyceridemia b, hypoactive reflexes, hypoalbuminemia, hypocalcemia, hypochondriasis, hypoglycemia, hypokalemia, hyponatremia, hypotension chronic, hypothermia, hypoxemia, impotence, incontinence of feces, incontinence of urine, increased serum bilirubin, indigestion, infertility female, infertility male, inguinal swelling, insomnia, intermittent claudication, jaundice, jaw pain, jaw swelling, joint pain, joint swelling, knee pain, knee swelling, kyphosis, lactic dehydrogenase elevation, leg ulceration, leucocytosis, leucopenia, lip pain, lip swelling, lymphadenopathy, melena, memory loss, menorrhagia, mental retardation, meteorism, metrorrhagia, monoplegia, mouth pigmentation, muscular atrophy, musculoskeletal pain generalized, nail abnormalities, nasal discharge, nasal obstruction, nausea and vomiting, neck pain, neck stiffness, neck swelling, nightmares, nocturia, nose regurgitation of food through, nystagmus, obesity pathologic, odor, opisthotonus, pain in the penis, pallor, palpitations, papilledema, paresthesias of the lower extremity, paresthesias of the upper extremity, pathologic reflexes, pelvic mass, pelvic pain, penile sores, perineum pain, periorbital edema, photophobia, plasma cortisol, polycythemia, polydipsia, polyuria, popliteal swelling, precocious puberty, priapism, prolonged prothrombin time, proteinuria, pruritus generalized, pruritus vulvae, ptosis, ptyalism, pulse irregularity, pulses unequal, pupil abnormalities, purpura and abnormal bleeding, pyuria, rales, rash distribution, rash morphology, Raynaud's phenomena, rectal bleeding, rectal discharge, rectal mass, rectal pain, red eye, regurgitation esophageal, respiration abnormalities, restless leg syndrome, risus sardonicus, scoliosis, scotoma, scrotal swelling, sedimentation rate, sensory loss, serum albumin, shoulder pain, sleep apnea, snoring, sore throat, splenomegaly acute or subacute, splenomegaly chronic, steatorrhea, strangury, stridor, stupor, syncope, tachycardia, taste abnormalities, testicular atrophy, testicular swelling, thirst or polydipsia, thrombocytopenia, thyroid enlargement, tinnitus, tongue mass or swelling, tremor, transient ischemic attacks, uremia, vaginal bleeding, vaginal discharge, vitamin b12, vulval or vaginal mass, vulval or vaginal ulcerations, weight loss")
    elif i == "derived diseases":
        print("acne vulgaris, asthma, atrial fibrillation, carpal tunnel syndrome, cataracts, cirrhosis, congestive heart failure, neuropathy, peptic ulcer, pharyngitis, pleural effusion, recurrent renal calculi, recurrent uti, stroke, uri")
# FIRST AID
    elif i == "first aid":
        print("Call the emergence service and say: mouth to mouth resuscitaion, first aid kit, accidents prevention, drowning, stroke, cramp, electric shock, kidney stone, foreign body, cut, fainting, chocking, fractures,\ninfarction, heat stroke, intoxication and allergies, nausea and vomiting, sting, low pressure, burn, bleeding, sprain, transport wounded, asphyxiation, amputation, seizure, chest pain, alcoholic coma, bruise, dislocation or head trauma")
    elif i == "first aid kit":
        print("if you want to do a first aid kit, you must put in some bag: cotton, bandages, thermal pouch, sterile gauze compresses, adhesive dresings of various sizes/band-aid, adhesive tape, latex gloves, clean cloth, clamp, ointment dor sprains or bumps, saline 0.9%, thermometer, scissors and say necessary medicines")
    elif i == "emergence":
        print("Do the primary evaluation, I mean, check if the airways are open, if the neck is stable, if there are more than 10 breathings per minute and if there's pulse, then say emergence 2")
    elif i == "emergence 2":
        print("do the secondary evaluation, seek for abnormalities in the members, vertebral column, skin color, head, mouth bleeding, chest, chest pain, meanly if going to the mandibule or towards left arm, mental confusion, hard speech, diziness, bad breathing, bad blood circulation and fever higher than 39 Celsius degrees")
    elif i == "accidents prevention":
        print("Avoid; slippery floor, accessible cleanning products, accessible cosmetics, pans wiithout cable towards stove center, watch out children and the elderly, avoid drinking alcohol and driving (or better, drink 1 liter of alcohol per year and don't smoke); if some accident happens, be sure that you and the victim stay safe (if in the street, remember the triangle reflector and put it far behind the vehicle, don't create a traffic, for that the ambulance may arrive), keep the curious ones away, call the emergence service and say emergence or first aid in the case it happens")
    elif i == "alcoholic coma":
        print("put the sick one somewhere safe, if vomits happen, leave him sitted, if unconcious, seek help (in this case, don't give him any food nor liquid)")
    elif i == "amputation":
        print("call emergence service immediatly, try to stop the bleeding by compressing around the injury, if partial amputation, don't finish it, if total amputation, put the member in a bag and this bag inside another one with ice and leave it to the hospital")
    elif i == "asphyxiations":
        print("say Heimlich's maneuver, if it doesn't work, make a tiny hole in the victim's throat, right above the first hard part (down to up direction), in the horizontal middle and put some clean object to keep it open, like pen tube, if a BABY, put him above your arm, which must be above your legs, with his belly towards the same arm and use your other arm to push his back with steady different movements, looking to expel what's in his arm")
    elif i == "bleeding":
        print("compress the region with a gauze or clean cloth, drive the vehicle carefully; if in the nose, sit down, don't incline your head and compress your nose during 10 minutes, if it doesn't solve it, seek help; if in the eye, apply cold water and go to a hospital; if inner organ is bleeding, so lye down the victim, seek help and describe carefully all the symptoms; if there's bruise, apply cold water and take paracetamol or dipyrone, the bruise will disappear in a few days")
    elif i == "bleeding time":
        print("2 to 7 minutes")
    elif e.get() == "bruise":
        myLabel = Label(root, text="apply ice several times, if any symptom instead of bruise, seek help")
    elif e.get() == "burn":
        myLabel = Label(root, text="If first degree, put the burnt region in water during 5 minutes, a shower might be used, dry crefully the region, take paracetamol and dipyrone, you can take anti-inflammatories, but don't apply ointments or anything, if second degree out it under water by 5 minutes, cover it with gauze, apply petroleum jelly, switch the gauzes daily, put nothing elese in your skin and don't burst the bubbles, if third degree, put it under water, use gauze and seek help, if fire, keep calm and get out of where you're now, stay close to the floor (smoke goes up), don't use elevators, open windows and make noise, if any chemical product touched to your eyes, wash them with water during 5 minutes, if in skin and cloth, take off your cloth and try to not touch the substance and seek help; if your clothes are on fire, calm down, try to avoid that any fuel touches your cloth, use tissued, a blanket, water, carbonic gas if available and roll my friend, roll in the ground (not too fast), take off your cloths, carefully apply cold water in your burst skin, seek medical help and take paracetamol, dipyrone and anti-inflammatories")
    elif e.get() == "cardiac arrest":
        myLabel = Label(root, text="if the heart seems to be stopped or pumping really fast, then it's cardiac arrest or, maybe, cardiorespiratory arrest")
    elif e.get() == "cardiac massage":
        myLabel = Label(root, text="Lye down the victim, come closer to his chest's side, interlance your fingers, put your hands right above the middle of his nipples, use your weight to do 30 strong compressions, do |mouth to mouth resuscitation| and repeat this sequence until rescue arrives")
    elif e.get() == "chest pain":
        myLabel = Label(root, text="also known as angina, the victim must rest and seek help, it might be beginning of an infarction, if it happened during physical activity, take it easier")
    elif e.get() == "chocking":
        myLabel = Label(root, text="if a BABY, put him above your sitted legs, with his head towards down, secure him with one am and compress his back's middle by 25 to 50 times, if it doesn't work direct his face towards up and do the same on his belly, if it doesn't work, call emergence service and do mouth to mouth resuscitation, if light ADULT, put his belly above and towards your sitted legs and compress strongly his back's middle, if WEIGHT ADULT, position him lyed down, go up to him and compress his torax using part of your mass, if CONCIOUS ADULT, then say Heimlich's maneuver")
    elif e.get() == "cosmetics":
        myLabel = Label(root, text="go to a hospital, meanwhile, take water and common pain killers as paracetamol or dipyrone, if eye affected wash it for 5 minutes with only water")
    elif e.get() == "cramp":
        myLabel = Label(root, text="cramp is due to bad blood circulation, so stand up or change your position and slowly move your legs")
    elif e.get() == "cut":
        myLabel = Label(root, text="if the cut was made with an WEAPON, thus seek medical help, if it's a SUPERFICIAL CUT, wash your hands with soap and water, leave the victim lyed down and raise the damged member, compress the injured region with some gauze or clean cloth, until it stanches the blood, what will take less than 10 minutes and seek medical help; if KNIFE STUCK, don't pull it, tell the person to move the lest possible and seek medical service; if DEEP CUT BLEEDING, seek medical help immediatly, compress the injured region and raise the damaged member, if DEEP CUT, wash your hands with soap and water, lye down the victim, raise the injured member and compress until stanch blood, one injured person must avoid touching another person to avoid contamination and seek medical care; if SCRUB, wash your hands the best way possible, if bleeding, compress with very clean cloth or gauze, wash carefully the injury, don't apply ointment, antiseptic nor cotton, if there was contact with any rusty object or soil, if  redness, pain or swelling arieses thus seek medical service")
    elif e.get() == "drowning":
        myLabel = Label(root, text="say land care or rescue of the victim")
    elif e.get() == "electric shock":
        myLabel = Label(root, text="away the victim from the font of electricity using plastic, rubber, dry wood or a dry cloth and do the same preocedures of crowning")
    elif e.get() == "fainting":
        myLabel = Label(root, text="don't let the person fall, put him on a bed or a chair with his breast above his legs, tell him to breath; if he had already fainted, thus lye him down, assuring that his head remains steady, make sure that he cans breath and give him water with sugar or juice, except if he's diabetic")
    elif e.get() == "food intoxication":
        myLabel = Label(root, text="Take one antiallergic pill and seek help")
    elif e.get() == "foreign body":
        myLabel = Label(root, text="if you have something in your NOSE, then compress your unobstructed nostril and blow strongly through your obstructed nostril, do this until the object is expelled; if unsuccessful, seek medical help; if something in your EYE, thus wash it with plenty of water and avoid scratching them; if needed seek medical help; if in your HEARD, don't try to remove it with any pointed object to avoid tympanum drilling, seek medical help")
    elif e.get() == "fractures":
        myLabel = Label(root, text="if the fracture involves the vertebral COLUMN, call emergence service right away, only move the victim if it's really necessary, don't touch his back, neither his torax, 3 or more people will be needed to transport him very carefully, aligned and steady, the lifeguard must hold his knees and feet; do this part slowly and make sure that the vehicle doesn't shake; if in the UPPER MEMBERS, don't try to move the bones, leave the broken region immobile and ice can be used; if in the FOOT, don't move it, don't take off the shoes, some clean cloth may enroll his leg and, in any case, seel medical professionals")
    elif e.get() == "gas":
        myLabel = Label(root, text="Don't try to vomit, it'll worse the situation, seek medical help")
    elif e.get() == "head trauma":
        myLabel = Label(root, text="if the head was deformed, don't try to fix its shape and seek medical help; if there's swelling, apply ice intermittently for 5 minutes; if there's bleeding and sonolence, mental confusion, fainting, difficult to walk, vomiting, double vison, different pupils sizes, noise bleeding or ear bleeding, so seek help; if the victim is a CHILD, thus go to a hospital anyway, except if it's just a very little cut and there was none impact on the head, so wash your hands, compress softly with a gauze or clean cloth, pass none ointment or anything on the injury and if the child shows none symptom, so he's fine")
    elif e.get() == "heat stroke":
        myLabel = Label(root, text="Take off the victim's cloths or put a thin one, go to a hospital; in the meanwhile, aplly him cold water, not icy and he must not drink a lot of water")
    elif e.get() == "Heimlichs maneuver":
        myLabel = Label(root, text="Hold the person by behind, with your hands on his belly button, press your fists towardsup and inside the person, compress quickly and a bit strongly by 25 times, pause for 5 seconds and do it again, this is the Heimlichs maneuver")
    elif e.get() == "heimlichs maneuver":
        myLabel = Label(root, text="Hold the person by behind, with your hands on his belly button, press your fists towardsup and inside the person, compress quickly and a bit strongly by 25 times, pause for 5 seconds and do it again, this is the Heimlichs maneuver")
    elif e.get() == "infarction":
        myLabel = Label(root, text="First of all, give ACETILSALICILIC ACID to the victim, if he's alergic, so drive him (or take a ride/taxi etc) to the nearest hospital; while waiting, loosen his cloths, try to keep him calm, he must not make any effort, say cardiac arrest to know if that's also the situation; if it is, then start cardiac massage, just say cardiac massage")
    elif e.get() == "land care":
        myLabel = Label(root, text="Do mouth breathing, 2 blows and 1 little interval; if the person has a cardiac arrest (say cardiac arrest to know how to identify it), then do the resuscitation, by pressing the chest intermittently")
    elif e.get() == "low blood pressure":
        myLabel = Label(root, text="Lye down, take little amounts os liquids, be sure if you didn't forget to take any medicine, if you haven't eaten for a while, so take a fruits juice, if weakness and fainting feelings appears for more than 15 minutes, thus seek help")
    elif e.get() == "mouth to mouth resuscitation":
        myLabel = Label(root, text="You don't have to do his maneuver, due to the risk of infection; if you wanna do this, so lye down the victim, close his nose while you breathe aie towards his mouth, if the chest arised, so you're doing great, keep repeating this")
    elif e.get() == "nausea and vomiting":
        myLabel = Label(root, text="Rest, keep hydrated taking small amounts of liquids all the time, prefer water, suck ice may really help,  don't stay a long time without eating, eat food like gelatine, biscuits cream-cracker and toasts, take metoclopramide and dimenhydrinate, if sever case with headache or bellyache seek medical service, if can't drink anything for 12 hours (adult) or 8 (children), vomiting taking more than 2 hours, feeling thirsty and with dry mouth, wakness, little urine flow or bloody vomit, thus seek help too")
    elif e.get() == "necessary medicines":
        myLabel = Label(root, text="if you want a first aid kit with medicines, you must have: anti-inflammatory, antacid, antiseptic sparay/Merthiolate, antispasmodic, antihistamine, painkiller, antipyretic, medicines for  nausea and vomiting and insect repelent; always note the expiry date")
    elif e.get() == "pesticides":
        myLabel = Label(root, text="if accidental INGESTION, seek medical help; if you think that some food has pesticides and you ate it, thus seek a hospital")
    elif e.get() == "rescue of the victim":
        myLabel = Label(root, text="if possible, use a rope or a ball; or be sure that you can swim until the victim and come back, involve his chest, passing through under one of his arms with your not dominant arm, keeping his face opposite to yours and swim with your dominant arm")
    elif e.get() == "seizure":
        myLabel = Label(root, text="Don't put anything inside the victim's mouth, don't try to take off anything from his mouth, protect him specially his head, lye him down, wait and then take victim to the hospital")
    elif e.get() == "sodium hydroxide and ammonia":
        myLabel = Label(root, text="if inhaled, stay at a ventilated place, while waiting for help, if it touched your skin, wash the region with water for 10 minutes")
    elif e.get() == "chlorine":
        myLabel = Label(root, text="If there was contact with skin or eyes, wash it for 10 minutes with only water, if ingested, drink water or a bit of olive oil and seek help")
    elif e.get() == "sodium hypochlorite":
        myLabel = Label(root, text="If there was contact with skin or eyes, wash it for 10 minutes with only water, if ingested, drink water or a bit of olive oil and seek help")
    elif e.get() == "sprain":
        myLabel = Label(root, text="apply ice enrolled in a thin tissue, hold it for between 15 and 20 minutes, if the skin turn to pale, gets tingling or weird, take off the ice, wait and start over, repeat it after each 2 hours for some days until the swelling and the pain disappear, don't apply heat to the region before the swelling disappears, never compress the injured region too hard, rest but not much (move the injured region sometimes), when lyed down raise the injured member and if you don't have diabetes, renal failure, gastritis nor duodenal ulcer, so take anti-inflammatories")
    elif e.get() == "sting":
        myLabel = Label(root, text="if SPIDER, apply a clean cloth and ice to the region; seek help immediatly if: fever, bubbles, skin daarkness, tachicardia, iintense sweat, seasickness, vomiting or anxiety;if SNAKE, take off compressing stuff from the body, apply ice, take dipyrone or paracetamol, if possible, also leave the species that atacked you to the hospitall, if DOMESTIC ANIMAL, wash the feriment with water and soap, cover it witha clean cloth or gauze and seek medical help, if SCORPIO, cover it with gauze and ice, take dipyrone or paracetamol and go to a hospital, meanly if the victim is a child, if there's somnolence, intense sweat, low blood pressure, tachicardia (palpitaion), seasickness or vomiting; if ANTS nad BEES, if there's breathing difficult or tachicardia, seek a hospital, if not grave, just apply ice in the injury")
    elif e.get() == "stroke":
        myLabel = Label(root, text="to know if a health problem is a stroke, say stroke symptoms; if it is, avoid calling an ambulance, use a car, taxi or ask for help and go to the nearest hospital really fast")
    elif e.get() == "stroke symptoms":
        myLabel = Label(root, text="tell the person to raise his arms, to sile and to speak; if he fails at doing one of these things or if he speaks weird and has muscle weakness, tingling, less movements or even fainting, so it's a stroke")
    elif e.get() == "transport wounded":
        myLabel = Label(root, text="if 2 lifeguards are available, so they must hold their arms forming a chair for  the victim to sit on and be carried:if 1 lifeguard, the victim must put his arm above and around your neck and you hold him or, if you can, raise him up with your both arms; IF the victim can't move and the way is long, put him above your shoullders with his legs  and one arm in  your front and the victim's back behind you, if the person may have injured his column, so avoid touching him and say fractures, looking for the word COLUMN")
    elif e.get() == "wild cassava":
        myLabel = Label(root, text="go to a hospital and say that your intoxication is due to wild cassava, because it releases CYANIDE, what may kill someone, don't ingest anythin while waiting")
    else:
        print('Done')
    y = y + 1
time.sleep(300)

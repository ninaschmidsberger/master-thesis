DATA_TO_KEEP = [
    # general data
    "ID",
    "V06BMI",  # FU WBK:Body mass index (calc)
    "V06BMICAT",  # FU WBK:Body mass index categories (calc)
    "V06AGE",  # FU WBK:Age (calc, used for study eligibility)
    "V06WEIGHT",  # FU WBK:Current scale weight (kg) (calc)
    "V06HEIGHT",  # FU WBK:Average height (mm) (calc)

    # depression parameters
    "V06CESD5",  # FU SAQ:Q31e.CES-D: how often had trouble keeping mind on what was doing, past week
    "V06CESD6",  # FU SAQ:Q31f.CES-D: how often felt depressed, past week
    "V06CESD7",  # FU SAQ:Q31g.CES-D: how often felt that everything did was an effort, past week
    "V06CESD10",  # FU SAQ:Q31j.CES-D: how often felt fearful, past week
    "V06CESD11",  # FU SAQ:Q31k.CES-D: how often sleep was restless, past week 9 Informat Label
    "V06CESD16",  # FU SAQ:Q31p.CES-D: how often enjoyed life, past week
    "V06CESD17",  # FU SAQ:Q31q.CES-D: how often had crying spells, past week
    "V06CESD20",  # FU SAQ:Q31t.CES-D: how often could not get going, past week
    "V06CESD",  # FU SAQ:CES-D: Center for Epidemiologic Studies Depression Scale (CES-D) Score (calc)

    # coping strategies
    "V06CSQCAT",  # FU INT:CSQ: Coping Strategies Questionnaire Score, Catastrophizing
    "V06CSQIGSN",  # FU INT:CSQ: Coping Strategies Questionnaire Score, Ignoring Sensations
    "V06CSQCSS",  # FU INT:CSQ: Coping Strategies Questionnaire Score, Coping Self-Statements
    "V06CSQDVAT",  # FU INT:CSQ: Coping Strategies Questionnaire Score, Diverting Attention
    "V06CSQRPS",  # FU INT:CSQ: Coping Strategies Questionnaire Score, Reinterpreting Pain Sensations
    "V06CSQPRHP",  # FU INT:CSQ: Coping Strategies Questionnaire Score, Praying or Hoping
    "V06CSQIBA",  # FU INT:CSQ: Coping Strategies Questionnaire Score, Increased Behavioral Activities

    # ADL
    "V06ADL1",
    # FU INT:Q83.ADL: Any difficulty dressing, including putting on shoes and socks, because of health or memory problem
    "V06ADL2",  # FU INT:Q84.ADL: Any difficulty walking across a room because of health or memory problem
    "V06ADL3",  # FU INT:Q85.ADL: Ever use equipment or device such as cane, walker, or wheelchair when crossing a room
    "V06ADL4",  # FU INT:Q86.ADL: Does anyone ever help you get across a room
    "V06ADL5",
    # FU INT:Q87.ADL: Any difficulty bathing or showering because of health or memory problem 4 Informat Label
    "V06ADL6",  # FU INT:Q88.ADL: Any difficulty eating, such as cutting up food, because of health or memory problem
    "V06ADL7",  # FU INT:Q89.ADL: Any difficulty getting in or out of bed because of health or memory problem
    "V06ADL8",
    # FU INT:Q90.ADL: Ever use equipment or device such as cane, walker, or railing when getting in or out of bed
    "V06ADL9",  # FU INT:Q91.ADL: Does anyone every help you get in or out of bed
    "V06ADL10",
    # FU INT:Q92.ADL: Any difficulty using toilet, including getting up and down, because of health or memory problem 89 Variables in Creation Order Informat Label
    "V06ADL7A",
    # FU INT:Q89a.ADL: Use equipment or device such as cane, walker, or railing when getting in or out of bed
    "V06IADL2",  # FU INT:Q94.IADL: Any difficulty shopping for groceries because of health or memory problem
    "V06IADL2II",  # FU INT:Q94ii.IADL: does any help you shop for groceries 19

    # ADL / Late Life Disability (LLD)
    "V06LLD2A",  # FU SAQ:QD2a.LLDI: How often visit friends and family in their homes
    "V06LLD2B",  # FU SAQ:QD2b.LLDI: What extent feel limited in visiting friends and family in their homes
    "V06LLD4A",
    # FU SAQ:QD4a.LLDI: How often take care of the inside of your home (e.g., homemaking, laundry, housecleaning, minor household repairs)
    "V06LLD4B",
    # FU SAQ:QD4b.LLDI: What extent feel limited taking care of the inside of your home (e.g., homemaking, laundry, housecleaning, minor household repairs)
    "V06LLD5A",  # FU SAQ:QD5a.LLDI: How often work at volunteer job outside your home
    "V06LLD5B",  # FU SAQ:QD5b.LLDI: What extent feel limited working at volunteer job outside your home
    "V06LLD6A",
    # FU SAQ:QD6a.LLDI: How often take part in active recreation (e.g., bowling, golf, tennis, hiking, jogging, swimming)
    "V06LLD6B",  # FU SAQ:QD6b.LLDI: What extent feel limited in taking part in active recreation
    "V06LLD9A",  # FU SAQ:QD9a.LLDI: How often travel out of town for at least an overnight stay 28 Informat Label
    "V06LLD9B",  # FU SAQ:QD9b.LLDI: What extent feel limited in traveling out of town for at least an overnight stay
    "V06LLD10A",
    # FU SAQ:QD10a.LLDI: How often take part in regular fitness program (e.g., walking for exercise, stationary biking, weight lifting, exercise class)
    "V06LLD10B",
    # FU SAQ:QD10b.LLDI: What extent feel limited in taking part in regular fitness program (e.g., walk for exercise, stationary bike, weight lift, exercise class)
    "V06LLD11A",  # FU SAQ:QD11a.LLDI: How often invite people into your home for meal or entertainment
    "V06LLD11B",
    # FU SAQ:QD11b.LLDI: What extent feel limited in inviting people into your home for meal or entertainment
    "V06LLD12A",  # FU SAQ:QD12a.LLDI: How often go out with others to public places (e.g., restaurants, movies)
    "V06LLD12B",
    # FU SAQ:QD12b.LLDI: What extent feel limited in going out with others to public places (e.g., restaurants, movies)
    "V06LLD13A",
    # FU SAQ:QD13a.LLDI: How often take care of your own personal care needs (e.g., bathing, dressing, toileting)
    "V06LLD13B",
    # FU SAQ:QD13b.LLDI: What extent feel limited in taking care of your own personal care needs (e.g., bathing, dressing, toileting)
    "V06LLD14A",
    # FU SAQ:QD14a.LLDI: How often take part in organized social activities (e.g., clubs, card playing, senior center events, community or religious groups)
    "V06LLD14B",
    # FU SAQ:QD14a.LLDI: What extent feel limited taking part in organized social activities(e.g.,clubs,card playing,senior center events,community/religious groups) 88 Variables in Creation Order Informat Label
    "V06LLD15A",
    # FU SAQ:QD15a.LLDI: How often take care of local errands (e.g., shopping for food/personal items, going to bank, library, or dry cleaner)
    "V06LLD15B",
    # FU SAQ:QD15b.LLDI: What extent feel limited in taking care of local errands (e.g., shopping for food/personal items, going to bank, library, or dry cleaner)
    "V06LLD16A",
    # FU SAQ:QD16a.LLDI: How often prepare meals for yourself (e.g., planning, cooking, serving, cleaning up)
    "V06LLD16B",
    # FU SAQ:QD16b.LLDI: What extent feel limited in preparing meals for yourself (e.g., planning, cooking, serving, cleaning up)

    "V06LLDIFSP",
    # FU SAQ:LLDI: Late Life Disability Instrument, Frequency Dimension, Personal Role Domain Score (calc)
    "V06LLDIFSS",  # FU SAQ:LLDI: Late Life Disability Instrument, Frequency Dimension, Social Role Domain Score (calc)
    "V06LLDIFST",  # FU SAQ:LLDI: Late Life Disability Instrument, Frequency Dimension, Total Score (calc)
    "V06LLDILSI",
    # FU SAQ:LLDI: Late Life Disability Instrument, Limitation Dimension, Instrumental Role Domain Score (calc)
    "V06LLDILSM",
    # FU SAQ:LLDI: Late Life Disability Instrument, Limitation Dimension, Management Role Domain Score (calc)
    "V06LLDILST",  # FU SAQ:LLDI: Late Life Disability Instrument, Limitation Dimension, Total Score (calc)

    # pain history
    "V06CPLKN1",  # FU INT:Q53q.ICOAP: Left knee constant pain: how intense, past 7 days
    "V06CPLKN2",  # FU INT:Q53r.ICOAP: Left knee constant pain: how much affected sleep, past 7 days
    "V06CPLKN3",
    # FU INT:Q53s.ICOAP: Left knee constant pain: how much affected overall quality of life, past 7 days 11 Informat Label
    "V06CPLKN4",  # FU INT:Q53t.ICOAP: Left knee constant pain: how frustrated or annoyed by pain, past 7 days
    "V06CPLKN5",  # FU INT:Q53u.ICOAP: Left knee constant pain: how upset or worried by pain, past 7 days
    "V06CPRKN1",  # FU INT:Q53c.ICOAP: Right knee constant pain: how intense, past 7 days
    "V06CPRKN2",  # FU INT:Q53d.ICOAP: Right knee constant pain: how much affected sleep, past 7 days
    "V06CPRKN3",  # FU INT:Q53e.ICOAP: Right knee constant pain: how much affected overall quality of life, past 7 days
    "V06CPRKN4",  # FU INT:Q53f.ICOAP: Right knee constant pain: how frustrated or annoyed by pain, past 7 days
    "V06CPRKN5",  # FU INT:Q53g.ICOAP: Right knee constant pain: how upset or worried by pain, past 7 days
    "V06CPSKL",  # 5.1 FU INT:ICOAP:Left knee: Constant Pain Score (calc)
    "V06CPSKR",  # 5.1 FU INT:ICOAP:Right knee: Constant Pain Score (calc)
    "V06ICPTSKL",  # 5.1 FU INT:ICOAP:Left knee: Intermittent and Constant Pain Total Score (calc)
    "V06ICPTSKR",  # 5.1 FU INT:ICOAP:Right knee: Intermittent and Constant Pain Total Score (calc)
    "V06IPLKN1",  # FU INT:Q53w.ICOAP: Left knee intermittent pain: how intense most severe pain been, past 7 days
    "V06IPLKN2",  # FU INT:Q53x.ICOAP: Left knee intermittent pain: how frequent, past 7 days
    "V06IPLKN3",  # FU INT:Q53y.ICOAP: Left knee intermittent pain: how much affected sleep, past 7 days
    "V06IPLKN4",
    # FU INT:Q53z.ICOAP: Left knee intermittent pain: how much affected overall quality of life, past 7 days
    "V06IPLKN5",
    # FU INT:Q53aa.ICOAP: Left knee intermittent pain: how frustrated or annoyed by pain, past 7 days 20 Informat Label
    "V06IPLKN6",  # FU INT:Q53bb.ICOAP: Left knee intermittent pain: how upset or worried by pain, past 7 days
    "V06IPRKN1",  # FU INT:Q53i.ICOAP: Right knee intermittent pain: how intense most severe pain been, past 7 days
    "V06IPRKN2",  # FU INT:Q53j.ICOAP: Right knee intermittent pain: how frequent, past 7 days
    "V06IPRKN3",  # FU INT:Q53k.ICOAP: Right knee intermittent pain: how much affected sleep, past 7 days
    "V06IPRKN4",
    # FU INT:Q53l.ICOAP: Right knee intermittent pain: how much affected overall quality of life, past 7 days
    "V06IPRKN5",  # FU INT:Q53m.ICOAP: Right knee intermittent pain: how frustrated or annoyed by pain, past 7 days
    "V06IPRKN6",  # FU INT:Q53n.ICOAP: Right knee intermittent pain: how upset or worried by pain, past 7 days
    "V06IPSKL",  # 5.1 FU INT:ICOAP:Left knee: Intermittent Pain Score (calc)
    "V06IPSKR",  # 5.1 FU INT:ICOAP:Right knee: Intermittent Pain Score (calc)

    "V06HPL12CV",
    # FU INT:Q55a.Left hip pain, aching or stiffness: more than half the days of a month, past 12 months (calc)
    "V06HPNL12",
    # FU INT:Q55.Left hip pain, aching or stiffness: any, past 12 months (includes pain in groin and in front and sides of upper thigh)
    "V06HPNLB",  # FU INT:Q55ai.Left hip pain, aching or stiffness location: buttocks
    "V06HPNLDK",  # FU INT:Q55ai.Left hip pain, aching or stiffness location: don't know
    "V06HPNLFL",  # FU INT:Q55ai.Left hip pain, aching or stiffness location: front of leg near hip
    "V06HPNLIL",  # FU INT:Q55ai.Left hip pain, aching or stiffness location: groin/inside leg near hip
    "V06HPNLLB",  # FU INT:Q55ai.Left hip pain, aching or stiffness location: lower back
    "V06HPNLOL",  # FU INT:Q55ai.Left hip pain, aching or stiffness location: outside of leg near hip
    "V06HPNR12",
    # FU INT:Q54.Right hip pain, aching or stiffness: any, past 12 months (includes pain in groin and in front and sides of upper thigh)
    "V06HPNRB",  # FU INT:Q54ai.Right hip pain, aching or stiffness location: buttocks
    "V06HPNRDK",  # FU INT:Q54ai.Right hip pain, aching or stiffness location: don't know
    "V06HPNRFL",  # FU INT:Q54ai.Right hip pain, aching or stiffness location: front of leg near hip
    "V06HPNRIL",  # FU INT:Q54ai.Right hip pain, aching or stiffness location: groin/inside leg near hip
    "V06HPNRLB",  # FU INT:Q54ai.Right hip pain, aching or stiffness location: lower back
    "V06HPNROL",  # FU INT:Q54ai.Right hip pain, aching or stiffness location: outside of leg near hip
    "V06HPR12CV",
    # FU INT:Q54a.Right hip pain, aching or stiffness: more than half the days of a month, past 12 months (calc)

    "V06CKPNL7",  # FU INT:Q53p.Left knee pain: constant, past 7 days
    "V06CKPNR7",  # FU INT:Q53b.Right knee pain: constant, past 7 days
    "V06IKPNL7",  # FU INT:Q53v.Left knee pain: intermittent, past 7 days
    "V06IKPNR7",  # FU INT:Q53h.Right knee pain: intermittent, past 7 days
    "V06KPL12CV",
    # FU INT:*Q8a.Left knee pain, aching or stiffness: more than half the days of a month, past 12 months (calc)
    "V06KPL30CV",  # FU INT:*Q9a.Left knee pain, aching or stiffness: more than half the days, past 30 days (calc)

    "V06OJPNLA",  # FU INT:Q60.Left ankle pain, aching or stiffness: more than half the days, past 30 days
    "V06OJPNLE",  # FU INT:Q60.Left elbow pain, aching or stiffness: more than half the days, past 30 days
    "V06OJPNLF",  # FU INT:Q60.Left foot pain, aching or stiffness: more than half the days, past 30 days
    "V06OJPNLH",  # FU INT:Q60.Left hand/finger pain, aching or stiffness: more than half the days, past 30 days
    "V06OJPNLS",  # FU INT:Q60.Left shoulder pain, aching or stiffness: more than half the days, past 30 days
    "V06OJPNLW",  # FU INT:Q60.Left wrist pain, aching or stiffness: more than half the days, past 30 days 31
    "V06OJPNNK",  # FU INT:Q60.Neck pain, aching or stiffness: more than half the days, past 30 days
    "V06OJPNNO",
    # FU INT:Q60.Other joints pain, aching or stiffness: more than half the days, past 30 days, no, don't know, refused
    "V06OJPNRA",  # FU INT:Q60.Right ankle pain, aching or stiffness: more than half the days, past 30 days
    "V06OJPNRE",  # FU INT:Q60.Right elbow pain, aching or stiffness: more than half the days, past 30 days
    "V06OJPNRF",  # FU INT:Q60.Right foot pain, aching or stiffness: more than half the days, past 30 days
    "V06OJPNRH",  # FU INT:Q60.Right hand/finger pain, aching or stiffness: more than half the days, past 30 days
    "V06OJPNRS",  # FU INT:Q60.Right shoulder pain, aching or stiffness: more than half the days, past 30 days
    "V06OJPNRW",  # FU INT:Q60.Right wrist pain, aching or stiffness: more than half the days, past 30 days

    "V06BP30",  # FU INT:Q59.Any back pain, past 30 days
    "V06BP30OFT",  # FU INT:Q59a.How often bothered by back pain, past 30 days
    "V06BPACTCV",  # FU INT:Q59d.Limit activities due to back pain, past 30 days (calc)
    "V06BPBAD",  # FU INT:Q59b.When had back pain how bad was it on average, past 30 days
    "V06BPBEDCV",  # FU INT:Q59di.How many days stay in bed due to back pain, past 30 days (calc)
    "V06BPDAYCV",
    # FU INT:Q59dii.How many days limit activities due to back pain, past 30 days (calc) 57 Variables in Creation Order Informat Label
    "V06BPTOT",  # FU INT:Total days in bed and/or limited activity due to back pain, past 30 days (calc)
    "V06OJPNNK",  # FU INT:Q60.Neck pain, aching or stiffness: more than half the days, past 30 days
    "V06OJPNNO",
    # FU INT:Q60.Other joints pain, aching or stiffness: more than half the days, past 30 days, no, don't know, refused
    "V06KGLRS",
    # FU INT:*Q53.Considering all ways knee pain and arthritis affect you, how are you doing today? Rated on scale of 0-10
    "V06KPA30CV",
    # FU INT:*Q10b.Either knee, avoid/reduce pain, aching or stiffness by changing or cutting back on normal activities, past 30 days (calc)
    "V06KPACDCV",
    # FU INT:*Q10a.Either knee, how many days limit activities due to pain, aching or stiffness, past 30 days (calc)
    "V06KPACT30",
    # FU INT:*Q10.Either knee, limit activities due to pain, aching or stiffness, past 30 days 51 Variables in Creation Order Informat Label
    "V06KPACTCV",
    # FU INT:*Q10.Either knee, limits or avoids activities due to pain, aching or stiffness, past 30 days (calc)

    # KOOS / WOMAC / Pain
    "V06P7RKFR",  # FU INT:*Q28.Right knee pain: how often
    "V06KPRKN1",  # FU INT:*Q27a.Right knee pain: twisting/pivoting on knee, last 7 days
    "V06KPRKN2",  # FU INT:*Q27b.Right knee pain: straightening knee fully, last 7 days
    "V06KPRKN3",  # FU INT:*Q27c.Right knee pain: bending knee fully, last 7 days
    "V06WPRKN1",  # FU INT:*Right knee pain: walking, last 7 days
    "V06WPRKN2",  # FU INT:*Right knee pain: stairs, last 7 days
    "V06WPRKN3",  # FU INT:*Right knee pain: in bed, last 7 days
    "V06WPRKN4",  # FU INT:*Right knee pain: sit or lie down, last 7 days
    "V06WPRKN5",  # FU INT:*Right knee pain: standing, last 7 days

    "V06P7LKFR",  # FU INT:*Q39.Left knee pain: how often
    "V06KPLKN1",  # FU INT:*Q38a.Left knee pain: twisting/pivoting on knee, last 7 days
    "V06KPLKN2",  # FU INT:*Q38b.Left knee pain: straightening knee fully, last 7 days
    "V06KPLKN3",  # FU INT:*Q38c.Left knee pain: bending knee fully, last 7 days
    "V06WPLKN1",  # FU INT:*Left knee pain: walking, last 7 days
    "V06WPLKN2",  # FU INT:*Left knee pain: stairs, last 7 days
    "V06WPLKN3",  # FU INT:*Left knee pain: in bed, last 7 days
    "V06WPLKN4",  # FU INT:*Left knee pain: sit or lie down, last 7 days
    "V06WPLKN5",  # FU INT:*Left knee pain: standing, last 7 days
    "V06KPNL7",  # FU INT:Q53o.Left knee pain: any, past 7 days
    "V06KPNL12",  # FU INT:*Q8.Left knee pain, aching or stiffness: any, past 12 months
    "V06KPNL12M",
    # Left knee pain, aching or stiffness: how many months on more than half the days of a month, past 12 months
    "V06LKP30CV",  # FU INT:*Q9.Left knee pain, aching or stiffness: any, past 30 days (calc)
    "V06P7LKACV",  # FU INT:*Q39b.Left knee pain: on average, past 7 days, rated on scale of 0-10 (calc)
    "V06P7LKRCV",  # FU INT:*Q39a.Left knee pain: severity, past 7 days, rated on scale of 0-10 (calc)
    "V06PMLKRCV",  # FU INT:*Q9b.Left knee pain: severity, past 30 days, rated on scale of 0-10 (calc)

    "V06KPNR7",  # FU INT:Q53a.Right knee pain: any, past 7 days
    "V06KPNR12",  # FU INT:*Q6.Right knee pain, aching or stiffness: any, past 12 months
    "V06KPNR12M",
    # FU INT:*Q6ai.Right knee pain, aching or stiffness: how many months on more than half the days of a month, past 12 months
    "V06KPR12CV",
    # FU INT:*Q6a.Right knee pain, aching or stiffness: more than half the days of a month, past 12 months (calc)
    "V06KPR30CV",  # FU INT:*Q7a.Right knee pain, aching or stiffness: more than half the days, past 30 days (calc)
    "V06P7RKACV",
    # FU INT:*Q28b.Right knee pain: on average, past 7 days, rated on scale of 0-10 (calc) 58 Variables in Creation Order Informat Label
    "V06P7RKRCV",  # FU INT:*Q28a.Right knee pain: severity, past 7 days, rated on scale of 0-10 (calc)
    "V06PMRKRCV",  # FU INT:*Q7b.Right knee pain: severity, past 30 days, rated on scale of 0-10 (calc)

    # KOOS / WOMAC / Function
    "V06DIRKN1",  # FU INT:*Right knee difficulty: down stairs, last 7 days
    "V06DIRKN2",  # FU INT:*Right knee difficulty: up stairs, last 7 days
    "V06DIRKN3",  # FU INT:*Right knee difficulty: stand from sitting, last 7 days
    "V06DIRKN4",  # FU INT:*Right knee difficulty: standing, last 7 days
    "V06DIRKN5",  # FU INT:*Right knee difficulty: bending, last 7 days
    "V06DIRKN6",  # FU INT:*Right knee difficulty: walking, last 7 days
    "V06DIRKN7",  # FU INT:*Right knee difficulty: in car/out of car, last 7 days
    "V06DIRKN8",  # FU INT:*Right knee difficulty: shopping, last 7 days
    "V06DIRKN9",  # FU INT:*Right knee difficulty: socks on, last 7 days
    "V06DIRKN10",
    # FU INT:*Right knee difficulty: get out of bed, last 7 days 52 Variables in Creation Order Informat Label
    "V06DIRKN11",  # FU INT:*Right knee difficulty: socks off, last 7 days
    "V06DIRKN12",  # FU INT:*Right knee difficulty: lying down, last 7 days
    "V06DIRKN13",  # FU INT:*Right knee difficulty: get in/out of bathtub, last 7 days
    "V06DIRKN14",  # FU INT:*Right knee difficulty: sitting, last 7 days
    "V06DIRKN15",  # FU INT:*Right knee difficulty: on/off toilet, last 7 days
    "V06DIRKN16",  # FU INT:*Right knee difficulty: heavy chores, last 7 days
    "V06DIRKN17",  # FU INT:*Right knee difficulty: light chores, last 7 days

    "V06DILKN1",  # FU INT:*Left knee difficulty: down stairs, last 7 days
    "V06DILKN2",  # FU INT:*Left knee difficulty: up stairs, last 7 days 53 Variables in Creation Order Informat Label
    "V06DILKN3",  # FU INT:*Left knee difficulty: stand from sitting, last 7 days
    "V06DILKN4",  # FU INT:*Left knee difficulty: standing, last 7 days
    "V06DILKN5",  # FU INT:*Left knee difficulty: bending, last 7 days
    "V06DILKN6",  # FU INT:*Left knee difficulty: walking, last 7 days
    "V06DILKN7",  # FU INT:*Left knee difficulty: in car/out of car, last 7 days
    "V06DILKN8",  # FU INT:*Left knee difficulty: shopping, last 7 days
    "V06DILKN9",  # FU INT:*Left knee difficulty: socks on, last 7 days
    "V06DILKN10",  # FU INT:*Left knee difficulty: get out of bed, last 7 days
    "V06DILKN11",  # FU INT:*Left knee difficulty: socks off, last 7 days
    "V06DILKN12",  # FU INT:*Left knee difficulty: lying down, last 7 days
    "V06DILKN13",  # FU INT:*Left knee difficulty: get in/out of bathtub, last 7 days
    "V06DILKN14",  # FU INT:*Left knee difficulty: sitting, last 7 days
    "V06DILKN15",  # FU INT:*Left knee difficulty: on/off toilet, last 7 days
    "V06DILKN16",  # FU INT:*Left knee difficulty: heavy chores, last 7 days
    "V06DILKN17",  # FU INT:*Left knee difficulty: light chores, last 7 days

    "V06KOOSFX1",  # FU INT:*Q48a.Either knee difficulty: squatting, last 7 days
    "V06KOOSFX2",  # FU INT:*Q48b.Either knee difficulty: running, last 7 days
    "V06KOOSFX3",  # FU INT:*Q48c.Either knee difficulty: jumping, last 7 days
    "V06KOOSFX4",  # FU INT:*Q48d.Either knee difficulty: twisting/pivoting on injured knee, last 7 days
    "V06KOOSFX5",  # FU INT:*Q48e.Either knee difficulty: kneeling, last 7 days

    # KOOS / WOMAC / Awareness
    "V06KQOL1",  # FU INT:*Q49.Quality of life: how often aware of problems with knee(s)
    "V06KQOL2",  # FU INT:*Q50.Quality of life: modified lifestyle to avoid potentially damaging activities to knee(s)
    "V06KQOL3",  # FU INT:*Q51.Quality of life: how much troubled with lack of confidence in knee(s)
    "V06KQOL4",  # FU INT:*Q52.Quality of life: in general, how much difficulty have with knee(s)

    # KOOS / WOMAC / Scores
    "V06KOOSKPL",  # 5.1 FU INT:Left knee: KOOS Pain Score (calc)
    "V06KOOSKPR",  # 5.1 FU INT:Right knee: KOOS Pain Score (calc)
    "V06KOOSQOL",  # 5.1 FU INT:KOOS Quality of Life Score (calc)
    "V06KOOSYML",  # 5.1 FU INT:Left knee: KOOS Symptoms Score (calc)
    "V06KOOSYMR",  # 5.1 FU INT:Right knee: KOOS Symptoms Score (calc)
    "V06KOOSFSR",  # 5.1 FU INT:KOOS Function, Sports, and Recreational Activities Score (calc)

    "V06WOMADLL",  # 5.1 FU INT:Left knee: WOMAC Disability Score (calc)
    "V06WOMADLR",  # 5.1 FU INT:Right knee: WOMAC Disability Score (calc)
    "V06WOMKPL",  # 5.1 FU INT:Left knee: WOMAC Pain Score (calc)
    "V06WOMKPR",  # 5.1 FU INT:Right knee: WOMAC Pain Score (calc)
    "V06WOMSTFL",  # 5.1 FU INT:Left knee: WOMAC Stiffness Score (calc)
    "V06WOMSTFR",  # 5.1 FU INT:Right knee: WOMAC Stiffness Score (calc)
    "V06WOMTSL",  # 5.1 FU INT:Left knee: WOMAC Total Score (calc)
    "V06WOMTSR",  # 5.1 FU INT:Right knee: WOMAC Total Score (calc)

    # PASE
    "V06PASE",  # FU INT:Physical Activity Scale for the Elderly (PASE) score (calc)
    "V06PASE1",  # FU INT:Leisure activities: sitting, past 7 days
    "V06PASE2",  # FU INT:Leisure activities: walking, past 7 days
    "V06PASE3",  # FU INT:Leisure activities: light sport/recreation, past 7 days
    "V06PASE4",  # FU INT:Leisure activities: moderate sport/recreation, past 7 days
    "V06PASE5",  # FU INT:Leisure activities: strenuous sport/recreation, past 7 days
    "V06PASE6",  # FU INT:Leisure activities: muscle strength/endurance, past 7 days
    "V06PASE1HR",  # FU INT:Leisure activities: sitting, hours per day, past 7 days
    "V06PASE2HR",  # FU INT:Leisure activities: walking, hours per day, past 7 days
    "V06PASE3HR",  # FU INT:Leisure activities: light sport/recreation, hours per day, past 7 days
    "V06PASE4HR",  # FU INT:Leisure activities: moderate sport/recreation, hours per day, past 7 days
    "V06PASE5HR",  # FU INT:Leisure activities: strenuous sport/recreation, hours per day, past 7 days
    "V06PASE6HR",  # FU INT:Leisure activities: muscle strength/endurance, hours per day, past 7 days 34
    "V06HOUACT1",  # FU INT:Household activities: light housework, past 7 days
    "V06HOUACT2",  # FU INT:Household activities: heavy housework, past 7 days
    "V06HOUACT3",  # FU INT:Household activities: home repairs, past 7 days
    "V06HOUACT4",  # FU INT:Household activities: lawn work/yard care, past 7 days
    "V06HOUACT5",  # FU INT:Household activities: outdoor gardening, past 7 days
    "V06HOUACT6",  # FU INT:Household activities: caring for another person, past 7 days

    # function
    "V0620MPACE",  # FU WBK:20-meter walk: pace (m/sec) (calc)
    "V06KPLK20B",  # FU WBK:Q2.20-meter walk: left knee pain, current severity, rated on scale of 0-10
    "V06KPLK20D",
    # FU WBK:Q7.20-meter walk: left knee pain, maximum amount experienced during walk, rated on scale of 0-10
    "V06KPRK20B",  # FU WBK:Q1.20-meter walk: right knee pain, current severity, rated on scale of 0-10
    "V06KPRK20D",
    # FU WBK:Q6.20-meter walk: right knee pain, maximum amount experienced during walk, rated on scale of 0-10
    "V06STEPST1",  # FU WBK:Q3.20-meter walk: trial 1 number of steps
    "V06STEPST2",  # FU WBK:Q4.20-meter walk: trial 2 number of steps
    "V06TIMET1",  # 6.2 6.2 FU WBK:Q3.20-meter walk: trial 1 time to complete (sec.hundredths/sec)
    "V06TIMET2",  # 6.2 6.2 FU WBK:Q4.20-meter walk: trial 2 time to complete (sec.hundredths/sec)
    "V06WLK20T1",  # FU WBK:Q3.20-meter walk: trial 1 result
    "V06WLK20T2",  # FU WBK:Q4.20-meter walk: trial 2 result
    "V06WLKAID",  # FU WBK:Q5.20-meter walk: using walking aid such as cane

    "V06400EXCL",  # FU WBK:400-meter walk: reason excluded (calc)
    "V06400MCMP",  # FU WBK:400-meter walk: completion status (calc) 82 Variables in Creation Order
    "V06400MTIM",  # FU WBK:400-meter walk: total time at 400-m or at stop (sec) (calc)
    "V06400MTR",  # FU WBK:400-meter walk: total meters walked (calc)
    "V06400PAIN",  # FU WBK:400-meter walk: knee pain, which leg (calc)
    "V06CANEUSE",  # FU WBK:Q10.400-meter walk: use cane
    "V06COMP10",  # FU WBK:Q11.400-meter walk: complete full 10 laps
    "V06DISCOMF",  # FU WBK:Q12.400-meter walk: any discomfort 79 Variables in Creation Order Informat Label
    "V06DKP400W",  # FU WBK:Q13.400-meter walk: knee pain during walk, don't know
    "V06HR135",  # FU WBK:Q9.400-meter walk: heart rate exceed 135 bpm during walk
    "V06HR400WK",  # FU WBK:Q8.400-meter walk: heart rate at 400-m or at stop
    "V06HRB4WLK",  # FU WBK:Q1.400-meter walk: heart rate before walk
    "V06LPN400W",  # FU WBK:Q13.400-meter walk: left knee pain during walk
    "V06LPWKPRV",  # FU WBK:Q13ii.400-meter walk: left knee pain prevent walking at usual pace
    "V06LPWKTYP",  # FU WBK:Q13i.400-meter walk: left knee pain mild, moderate or severe
    "V06NPN400W",  # FU WBK:Q13.400-meter walk: no knee pain during walk
    "V06NUMSTOP",  # FU WBK:Q4.400-meter walk: total number rest stops 78 Variables in Creation Order Informat Label
    "V06OTH400W",  # FU WBK:Q12a.400-meter walk: type of discomfort, other
    "V06PN400W",  # FU WBK:Q12a.400-meter walk: type of discomfort, pain
    "V06REASW1",  # FU WBK:Q11a.400-meter walk: not able to complete 10 laps, excluded based on eligibility criteria
    "V06REASW2",  # FU WBK:Q11a.400-meter walk: not able to complete 10 laps, began walk but could not complete
    "V06REASW3",
    # FU WBK:Q11a.400-meter walk: not able to complete 10 laps, heart rate exceeded 135 bpm during walk and did not feel well
    "V06REASW4",  # FU WBK:Q11a.400-meter walk: not able to complete 10 laps, heart rate fell below 40 bpm during walk
    "V06REASW5",  # FU WBK:Q11a.400-meter walk: not able to complete 10 laps, reported felt too tired during walk
    "V06REASW6",
    # FU WBK:Q11a.400-meter walk: not able to complete 10 laps, reported chest pain during walk 36 Informat Label
    "V06REASW7",  # FU WBK:Q11a.400-meter walk: not able to complete 10 laps, reported shortness of breath during walk
    "V06REASW8",  # FU WBK:Q11a.400-meter walk: not able to complete 10 laps, reported feeling faint during walk
    "V06REASW9",  # FU WBK:Q11a.400-meter walk: not able to complete 10 laps, reported knee pain during walk
    "V06REASW10",  # FU WBK:Q11a.400-meter walk: not able to complete 10 laps, reported hip pain during walk
    "V06REASW11",  # FU WBK:Q11a.400-meter walk: not able to complete 10 laps, reported calf pain during walk
    "V06REASW12",  # FU WBK:Q11a.400-meter walk: not able to complete 10 laps, reported back pain during walk
    "V06REASW13",  # FU WBK:Q11a.400-meter walk: not able to complete 10 laps, sat down during walk
    "V06REASW14",
    # FU WBK:Q11a.400-meter walk: not able to complete 10 laps, more than 15 minutes elapsed from start of test
    "V06REASW15",  # FU WBK:Q11a.400-meter walk: not able to complete 10 laps, refused
    "V06REASW16",  # FU WBK:Q11a.400-meter walk: not able to complete 10 laps, other
    "V06RESTT1",  # FU WBK:Q3a.400-meter walk: rest stop #1
    "V06RESTT2",  # FU WBK:Q3b.400-meter walk: rest stop #2
    "V06RESTT3",  # FU WBK:Q3c.400-meter walk: rest stop #3
    "V06RESTT4",  # FU WBK:Q3d.400-meter walk: rest stop #4 37 Informat Label
    "V06RESTT5",  # FU WBK:Q3e.400-meter walk: rest stop #5
    "V06RESTT6",  # FU WBK:Q3f.400-meter walk: rest stop #6
    "V06RESTT7",  # FU WBK:Q3g.400-meter walk: rest stop #7
    "V06RESTT8",  # FU WBK:Q3h.400-meter walk: rest stop #8
    "V06RESTT9",  # FU WBK:Q3i.400-meter walk: rest stop #9
    "V06RESTT10",  # FU WBK:Q3j.400-meter walk: rest stop #10
    "V06RFP400W",  # FU WBK:Q13.400-meter walk: knee pain during walk, refused
    "V06RPN400W",  # FU WBK:Q13.400-meter walk: right knee pain during walk
    "V06RPWKPRV",  # FU WBK:Q13ii.400-meter walk: right knee pain prevent from walking at usual pace
    "V06RPWKTYP",  # FU WBK:Q13i.400-meter walk: right knee pain mild, moderate or severe
    "V06SOB400W",  # FU WBK:Q12a.400-meter walk: type of discomfort, shortness of breath

    "V06SAFEWLK",  # FU WBK:Q12.400-meter walk eligibility: feel it would be safe to try to walk up and down hallway
    "V06SYSELG",
    # FU WBK:400-meter walk eligibility: meets new or old systolic blood pressure exclusion criterion (calc)
    "V06W20COMP",  # FU WBK:Q1.400-meter walk eligibility: able to complete trial 1 and trial 2 of the 20-meter walk
    "V06WALKER",  # FU WBK:Q6.400-meter walk eligibility: use walker or quad cane when walk
    "V06WHE400W",  # FU WBK:Q12a.400-meter walk: type of discomfort, wheezing/dyspnea
    "V06CALLDOC",
    # FU WBK:Q7.400-meter walk eligibility: had to see or call doctor for worsening angina (chest or heart pain) or worsening shortness of breath, past 3 months
    "V06DIASELG",
    # FU WBK:400-meter walk eligibility: meets new or old diastolic blood pressure exclusion criterion (calc)
    "V06HOSPSUR",
    # FU WBK:400-meter walk eligibility: meets new or old hospitalization/surgery exclusion criteria (calc)
    "V06HRELG",
    # FU WBK:400-meter walk eligibility: meets old or new heart rate exclusion criterion (calc) 18 Informat Label

    "V06CSTSGL",  # FU WBK:Single chair stand
    "V06CSTREP1",  # FU WBK:Repeated chair stands: trial 1
    "V06CSTIME1",  # WBK:Repeated chair stands: trial 1 time (sec.hundredths/sec) 12
    "V06CSTNUM1",
    # FU WBK:Repeated chair stands: trial 1, attempted, unable to complete: number completed without using arms
    "V06CSTIME2",  # 6.2 6.2 FU WBK:Repeated chair stands: trial 2 time (sec.hundredths/sec)
    "V06CSTNUM2",
    # FU WBK:Repeated chair stands: trial 2, attempted, unable to complete: number completed without using arms
    "V06CSTREP2",  # FU WBK:Repeated chair stands: trial 2
    "V06CS5",  # FU WBK:Repeated chair stands: able to complete 5 stands (calc)
    "V06CSPACE",  # FU WBK:Repeated chair stand: pace in stands/sec (calc)

    # CAM
    "V06ACUSCUR",  # FU INT:Q141bii.CAM: currently seeing acupressure practitioner for arthritis or joint pain
    "V06ACUSCV",  # FU INT:Q141b.CAM: seen acupressure practitioner for arthritis or joint pain, past 12 months (calc)
    "V06ACUSNUM",
    # FU INT:Q141bi.CAM: how many times see acupressure practitioner for arthritis or joint pain, past 12 months
    "V06ACUTCUR",  # FU INT:Q141aii.CAM: currently seeing acupuncture practitioner for arthritis or joint pain
    "V06ACUTCV",  # FU INT:Q141a.CAM: seen acupuncture practitioner for arthritis or joint pain, past 12 months (calc)
    "V06ACUTNUM",
    # FU INT:Q141ai.CAM: how many times see acupuncture practitioner for arthritis or joint pain, past 12 months
    "V06BRAC12",  # FU INT:Q146.CAM: worn copper bracelets or used magnets for arthritis or joint pain, past 12 months
    "V06BRACCV",  # FU INT:Q146a.CAM: currently wear copper bracelets or use magnets for arthritis or joint pain (calc)
    "V06CAM12",
    # FU INT:Q141.CAM:seen someone other than medical doctor or nurse, such as chiropractor or acupuncturist, specifically for arthritis or joint pain, past 12 months
    "V06CAPSNCV",  # FU INT:Q145b.CAM: currently using Capsaicin (pepper cream) for arthritis or joint pain (calc)
    "V06CHIRCUR",  # FU INT:Q141fii.CAM: currently seeing chiropractic care practitioner for arthritis or joint pain
    "V06CHIRCV",
    # FU INT:Q141f.CAM: seen chiropractic care practitioner for arthritis or joint pain, past 12 months (calc)
    "V06CHIRNUM",
    # FU INT:Q141fi.CAM: how many times see chiropractic care practitioner for arthritis or joint pain, past 12 months
    "V06DIET12",
    # FU INT:Q142.CAM: follow special food plan or diet, such as a vegetarian or low-fat diet, for arthritis or joint pain, past 12 months
    "V06DIETCV",  # FU INT:Q142a.CAM: currently following special food plan or diet for arthritis or joint pain (calc)
    "V06HERB12",
    # FU INT:Q144.CAM: use herbs, such as echinacea, ginger or garlic, for arthritis or joint pain, past 12 months 67 Variables in Creation Order
    "V06HERBCV",  # FU INT:Q144a.CAM: currently using any herbs for arthritis or joint pain (calc)
    "V06MASSCUR",  # FU INT:Q141kii.CAM: currently seeing massage practitioner for arthritis or joint pain
    "V06MASSCV",
    # FU INT:Q141k.CAM: seen massage practitioner for arthritis or joint pain, past 12 months (calc) 29 Informat Label
    "V06MASSNUM",
    # FU INT:Q141ki.CAM: how many times see massage practitioner for arthritis or joint pain, past 12 months
    "V06OCCAM48",
    # FU INT:CAM:currently see ayurveda/biofeedback/chel therapy/ener heal/folk med/homeo/hypn/naturo practitioner for arthritis or joint pain, past 12 months (calc) 72 Variables in Creation Order Informat Label
    "V06OHCAM48",
    # FU INT:CAM: seen ayurveda/biofeedback/chelation therapy/energy heal/folk med/homeo/hypno/naturo practitioner for arthritis or joint pain, past 12 months (calc)
    "V06RELA12",
    # FU INT:Q148.CAM: do relaxation or mind-body activities, such as meditation, deep breathing or visualization, for arthritis or joint pain, past 12 months
    "V06RELACV",  # FU INT:Q148a.CAM: currently do relaxation or mind-body activities for arthritis or joint pain (calc)
    "V06RUBCV",
    # FU INT:Q145a.CAM: currently using rubs, lotions, liniments, creams or oils for arthritis or joint pain (calc)
    "V06RUBS12",
    # FU INT:Q145.CAM: used rubs, lotions, liniments, creams or oils, such as tiger balm or horse liniment, for arthritis or joint pain, past 12 months
    "V06SPIR12",
    # FU INT:Q149.CAM: do spiritual activities (e.g., prayer, laying on of hands, healing circles, or faith healing) for arthritis or joint pain, past 12 months
    "V06SPIRCV",  # FU INT:Q149a.CAM: currently do any type of spiritual activities for arthritis or joint pain (calc)
    "V06VITM12",
    # FU INT:Q143.CAM: use vitamins or minerals, such as selenium or vitamin C or D, for arthritis or joint pain, past 12 months
    "V06VITMCV",  # FU INT:Q143a.CAM: currently using vitamins/minerals for arthritis or joint pain (calc)
    "V06YOGA12",
    # FU INT:Q147.CAM: do any health or special movement activity, such as Tai Chi, Yoga, Chi Gong or Pilates, for arthritis or joint pain, past 12 months
    "V06YOGACV",
    # FU INT:Q147a.CAM: currently do any type of health or special movement activity for arthritis or joint pain (calc)

    # replacement
    "V06HRS12",
    # FU INT:Q56.Had hip replacement surgery where all or part of joint was replaced, since last visit about 12 months ago
    "V06SREPHR",  # FU INT:Ever have hip replacement surgery where all or part of joint was replaced, self-report (calc)
]
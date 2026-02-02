import re
import google.generativeai as genai

# ==============================
# CONFIGURE GEMINI
# ==============================
genai.configure(api_key="AIzaSyCTPzPnTI6LZ42CkjphFHi9fF8EyQfA794")
model = genai.GenerativeModel("gemini-1.5-flash")

# ==============================
# 100 SECTORS
# ==============================
ALL_SECTORS = [
    "Politics","Government","Policy","Diplomacy","Law","Judiciary","Courts",
    "Elections","Administration","Regulation","Business","Economy","Finance",
    "Banking","Insurance","Investment","StockMarket","Startup","Corporate",
    "Acquisition","Manufacturing","Industry","Trade","Export","Import","MSME",
    "Logistics","Retail","Wholesale","Inflation","Technology",
    "ArtificialIntelligence","MachineLearning","DataScience","Cybersecurity",
    "Blockchain","Software","Hardware","Cloud","Internet","Media","Journalism",
    "SocialMedia","DigitalMarketing","Advertising","PublicRelations","Content",
    "Influencer","Telecom","Broadcasting","Healthcare","PublicHealth","Pharma",
    "Biotechnology","MedicalDevices","Hospitals","MentalHealth","Nutrition",
    "Fitness","Disease","Education","University","School","EdTech",
    "SkillDevelopment","Research","Exams","Students","Training","Career",
    "Environment","ClimateChange","Sustainability","RenewableEnergy","OilGas",
    "Electricity","Water","Waste","Wildlife","EnvironmentalPolicy","Agriculture",
    "Agritech","Farming","Crops","Livestock","Fisheries","FoodProcessing",
    "RuralDevelopment","Irrigation","Farmer","Society","Culture","Lifestyle",
    "Fashion","Entertainment","Film","Music","Sports","Tourism","Spirituality"
]

# ==============================
# CLASSIFICATION FUNCTION
# ==============================
def classify_keyword(keyword: str) -> str:
    sectors_text = ", ".join(ALL_SECTORS)

    prompt = f"""
You are a strict semantic classifier.

Task:
Classify the given keyword into ONE most relevant sector
from the list below.

Rules:
- You MUST choose ONLY from the provided list
- Choose the MOST specific sector
- Return ONLY the sector name
- No explanations, no extra text

Sector List:
{sectors_text}

Keyword:
{keyword}
"""

    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 0.0,
            "max_output_tokens": 16
        }
    )

    result = response.text.strip()

    # Normalize and validate output
    normalized = re.sub(r"[^a-zA-Z]", "", result).lower()
    for sector in ALL_SECTORS:
        if normalized == re.sub(r"[^a-zA-Z]", "", sector).lower():
            return sector

    return "Business"  # safe fallback


# ==============================
# TEST
# ==============================
test_keywords = [
    "drug discovery",
    "ai chatbot",
    "climate change",
    "cement manufacturing",
    "mental health awareness"
]

for kw in test_keywords:
    print(f"{kw} → {classify_keyword(kw)}")

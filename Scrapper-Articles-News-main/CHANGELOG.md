# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased] - 2026-02-02

### Added
- Created `CHANGELOG.md` to track project history.
- Added `.github/coderabbit.yaml` for AI code reviews.
- Added `xlsxwriter` to environment for Excel export support.

### Changed
- **UI Polish**:
  - **Dynamic Progress Bar**: The loader now updates in real-time (e.g., "Reading articles... 45%"), giving feedback on the exact scraping progress.
  - **Animated Loader**: Replaced basic spinners with a **Step-by-Step Status Box**.
  - **Scrollable Results**: Added a dedicated scrollbar area (height=800px) for the results list.
  - **Clean Layout**: Moved summary inside dropdown.
- **Documentation**: Added comprehensive "ELI5" (Explain Like I'm 5) comments to the entire codebase. Now non-technical users can understand what each file (`app2.py`, `article_scraper.py`, `gdelt_fetcher.py`) is doing.
- **Capacity Upgrade**: Removed all hard limits. The app now fetches **all available articles** for the specified duration and keyword. Added concurrency control (Semaphore) to handle mass-fetching safely.
- **Extraction Improvements**:
  - **Redirect Handling**: Integrated `batchexecute` decoder (from `xdpooja/newsscraper`) to properly resolve Google News encrypted URLs. This fixes the "Redirecting..." page issue.
  - **Anti-Blocking**: Added 'Referer' headers and a persistent Cookie Jar to pass checks on sites like MSN.
  - Upgraded `article_scraper.py` to use "Text Density Heuristics" for smarter content locating.
  - Improved "Fallback Extraction" for sites without standard paragraph tags.
  - Removed length restriction in UI, so even short articles are displayed instead of the warning message.
- **Rolled Back**: Reverted HTML & Image display features. Returned to "Text Summary" + "Full Text Dropdown" view.
- **Enhanced Content Display**:
  - Added dropdown "Read Full Article Content" to view the entire article without leaving the app.
  - Added "Paywall Detection": The app now warns if an article requires a subscription ("🔒 Subscription Required").
- **UI Overhaul**: Simplified `app2.py` to focus on a single "Search & Display" workflow.
  - Added dropdown "Read Full Article Content" to view the entire article without leaving the app.
  - Added "Paywall Detection": The app now warns if an article requires a subscription ("🔒 Subscription Required").
- **UI Overhaul**: Simplified `app2.py` to focus on a single "Search & Display" workflow.
  - Removed "Top Agencies" analysis feature.
  - Unified search interface.
  - Improved result display (Headline, Source, 3-4 line Summary).
- **Code Quality**: Rewrote comments in `app2.py`, `article_scraper.py`, and `gdelt_fetcher.py` to be "ELI5" (Explain Like I'm 5) for better readability.
- **Performance**: Increased network timeouts in `gdelt_fetcher.py` and `article_scraper.py` for better reliability on slow connections.
- **Bug Fix**: Fixed Excel download MIME type in `app2.py` to prevent "file corrupted" errors.
- **Bug Fix**: Fixed Excel download MIME type in `app2.py` to prevent "file corrupted" errors.

---

## [2.0.0] - 2026-02-02

### 🎯 AI-Powered Sector Classification System

#### Added
- **100 Granular Sectors**: Implemented comprehensive sector taxonomy covering:
  - **Governance**: Politics, Government, Policy, Diplomacy, Law, Judiciary, Courts, Elections, Administration, Regulation
  - **Business & Finance**: Business, Economy, Finance, Banking, Insurance, Investment, StockMarket, Startup, Corporate, Acquisition
  - **Industry & Trade**: Manufacturing, Industry, Trade, Export, Import, MSME, Logistics, Retail, Wholesale, Inflation
  - **Technology**: Technology, ArtificialIntelligence, MachineLearning, DataScience, Cybersecurity, Blockchain, Software, Hardware, Cloud, Internet
  - **Media & Communication**: Media, Journalism, SocialMedia, DigitalMarketing, Advertising, PublicRelations, Content, Influencer, Telecom, Broadcasting
  - **Healthcare**: Healthcare, PublicHealth, Pharma, Biotechnology, MedicalDevices, Hospitals, MentalHealth, Nutrition, Fitness, Disease
  - **Education**: Education, University, School, EdTech, SkillDevelopment, Research, Exams, Students, Training, Career
  - **Environment & Energy**: Environment, ClimateChange, Sustainability, RenewableEnergy, OilGas, Electricity, Water, Waste, Wildlife, EnvironmentalPolicy
  - **Agriculture**: Agriculture, Agritech, Farming, Crops, Livestock, Fisheries, FoodProcessing, RuralDevelopment, Irrigation, Farmer
  - **Society & Culture**: Society, Culture, Lifestyle, Fashion, Entertainment, Film, Music, Sports, Tourism, Spirituality

- **Hybrid Classification Engine** (`sector_classifier.py`):
  - **Priority 1**: Google Gemini API (95% confidence) - Semantic understanding using LLM
  - **Priority 2**: Sentence-BERT Embeddings (75-90% confidence) - Cosine similarity matching
  - **Priority 3**: Keyword Matching (40-85% confidence) - Dictionary-based fallback
  
- **Sector Dropdown UI**: Added sector selection dropdown with predefined categories + CUSTOM option
- **Custom Keyword Input**: User can enter any topic and system automatically classifies it
- **Real-time Classification Display**: Shows classified sector with confidence score above results

#### Technical Implementation
- **Model**: `all-MiniLM-L6-v2` (Sentence-BERT) for local embeddings
- **API Integration**: Google Gemini 1.5 Flash with optimized prompts (temperature: 0.1)
- **Confidence Thresholds**: 
  - Gemini: 95% (exact match), 90% (fuzzy match)
  - SBERT: 20% minimum similarity
  - Keyword: 40-100% based on match type
- **Fallback Chain**: Ensures 100% classification success rate
- **Performance**: First load ~2s (model download), subsequent <100ms

#### Dependencies Added
- `sentence-transformers` - SBERT embeddings
- `scikit-learn` - Cosine similarity calculations
- `google-generativeai` - Gemini API integration

#### Configuration
- API Key stored in `.streamlit/secrets.toml`
- Configurable confidence thresholds
- Toggle-able classification methods

#### Bug Fixes
- Fixed timezone-aware vs timezone-naive timestamp comparison error in article sorting
- Added proper timestamp normalization for consistent date sorting
- Removed duplicate classification code blocks


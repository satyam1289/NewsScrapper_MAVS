import asyncio
from gdelt_fetcher import fetch_gdelt_simple
from article_scraper import enhance_articles_async
import time

def main():
    keyword = "SpaceX"
    print(f"--- 1. Testing Search for '{keyword}' ---")
    start_time = time.time()
    
    # 1. Fetch Links (Synchronous)
    # fetch_gdelt_simple handles its own asyncio.run internally, so we call it normally.
    try:
        raw_articles = fetch_gdelt_simple(keyword, days=3, max_articles=5)
    except Exception as e:
        print(f"❌ CRITICAL ERROR in gdelt_fetcher: {e}")
        return

    if not raw_articles:
        print("❌ FAILED: No articles found. Check internet connection or query.")
        return
    
    print(f"✅ SUCCESS: Found {len(raw_articles)} articles in {time.time() - start_time:.2f}s.")
    for i, art in enumerate(raw_articles):
        print(f"   [{i+1}] {art['title']} ({art['source']})")
        
    print("\n--- 2. Testing Content Extraction (Scraping) ---")
    
    # 2. Scrape Content (Async)
    # enhance_articles_async is an async function, so we need a loop for it.
    try:
        enhanced = asyncio.run(enhance_articles_async(raw_articles[:3]))
    except Exception as e:
        print(f"❌ CRITICAL ERROR in article_scraper: {e}")
        return
    
    success_count = 0
    for art in enhanced:
        full_text = art.get('full_text', '')
        summary = art.get('summary', '')
        print(f"\nTitle: {art['title']}")
        print(f"Link: {art['link']}")
        print(f"Text Length: {len(full_text)} chars")
        print(f"Summary Preview: {summary[:100]}...")
        
        if len(full_text) > 100:
            success_count += 1
            
    if success_count > 0:
        print(f"\n✅ SUCCESS: Successfully scraped text from {success_count}/{len(enhanced)} articles.")
    else:
        print("\n❌ WARNING: Scraped 0 articles. This might indicate scraper issues.")

if __name__ == "__main__":
    main()

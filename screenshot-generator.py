#!/usr/bin/env python3
"""
Screenshot generator for website verification
Takes screenshots of different sections and viewport sizes
"""

import sys
import time

try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
except ImportError:
    print("Installing selenium...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "selenium", "-q"])
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options

# Create Chrome options
options = Options()
options.headless = True
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

# Initialize WebDriver
driver = webdriver.Chrome(options=options)

try:
    base_url = "http://localhost:8000/index.html"
    screenshots_dir = "C:/Users/aryan/Downloads/H&S global tour and travels/Tour-Travel/screenshots"
    
    import os
    os.makedirs(screenshots_dir, exist_ok=True)
    
    print("✅ Starting screenshot generation...")
    
    # 1. Desktop - Full page
    print("📸 1. Taking desktop full page screenshot...")
    driver.set_window_size(1920, 1080)
    driver.get(base_url)
    time.sleep(3)
    driver.save_screenshot(f"{screenshots_dir}/01-desktop-full.png")
    
    # 2. Hero section
    print("📸 2. Taking hero section screenshot...")
    hero = driver.find_element(By.CSS_SELECTOR, ".trv-banner-3-text-mid, [style*='slider-bg']")
    driver.execute_script("arguments[0].scrollIntoView(true);", hero)
    time.sleep(1)
    driver.save_screenshot(f"{screenshots_dir}/02-hero-section.png")
    
    # 3. Navigation
    print("📸 3. Taking navigation screenshot...")
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)
    driver.save_screenshot(f"{screenshots_dir}/03-navigation.png")
    
    # 4. Destination carousel
    print("📸 4. Taking destination section screenshot...")
    dest_section = driver.find_element(By.XPATH, "//*[contains(text(), 'Trending')]")
    driver.execute_script("arguments[0].scrollIntoView(true);", dest_section)
    time.sleep(2)
    driver.save_screenshot(f"{screenshots_dir}/04-destination-section.png")
    
    # 5. Pricing section
    print("📸 5. Taking pricing section screenshot...")
    pricing_section = driver.find_element(By.XPATH, "//*[contains(text(), 'Pricing')]")
    driver.execute_script("arguments[0].scrollIntoView(true);", pricing_section)
    time.sleep(2)
    driver.save_screenshot(f"{screenshots_dir}/05-pricing-section.png")
    
    # 6. Gallery section
    print("📸 6. Taking gallery section screenshot...")
    gallery_section = driver.find_element(By.XPATH, "//*[contains(text(), 'Gallery')]")
    driver.execute_script("arguments[0].scrollIntoView(true);", gallery_section)
    time.sleep(2)
    driver.save_screenshot(f"{screenshots_dir}/06-gallery-section.png")
    
    # 7. Footer
    print("📸 7. Taking footer screenshot...")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    driver.save_screenshot(f"{screenshots_dir}/07-footer.png")
    
    # 8. Mobile view
    print("📸 8. Taking mobile view screenshot...")
    driver.set_window_size(375, 812)  # iPhone size
    driver.get(base_url)
    time.sleep(3)
    driver.save_screenshot(f"{screenshots_dir}/08-mobile-homepage.png")
    
    # 9. Mobile - Pricing
    print("📸 9. Taking mobile pricing screenshot...")
    pricing = driver.find_element(By.XPATH, "//*[contains(text(), 'Pricing')]")
    driver.execute_script("arguments[0].scrollIntoView(true);", pricing)
    time.sleep(1)
    driver.save_screenshot(f"{screenshots_dir}/09-mobile-pricing.png")
    
    # 10. Mobile - Gallery
    print("📸 10. Taking mobile gallery screenshot...")
    gallery = driver.find_element(By.XPATH, "//*[contains(text(), 'Gallery')]")
    driver.execute_script("arguments[0].scrollIntoView(true);", gallery)
    time.sleep(1)
    driver.save_screenshot(f"{screenshots_dir}/10-mobile-gallery.png")
    
    print(f"\n✅ All screenshots saved to: {screenshots_dir}")
    print("\nGenerated screenshots:")
    print("  ✓ 01-desktop-full.png")
    print("  ✓ 02-hero-section.png")
    print("  ✓ 03-navigation.png")
    print("  ✓ 04-destination-section.png")
    print("  ✓ 05-pricing-section.png")
    print("  ✓ 06-gallery-section.png")
    print("  ✓ 07-footer.png")
    print("  ✓ 08-mobile-homepage.png")
    print("  ✓ 09-mobile-pricing.png")
    print("  ✓ 10-mobile-gallery.png")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    driver.quit()

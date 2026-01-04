"""
Automated crawler runner - no user interaction needed
Crawls all Zoho products automatically
"""

from zoho_documentation_crawler import ZohoDocumentationCrawler

def main():
    print("="*60)
    print("Zoho Documentation Crawler - Automated Run")
    print("="*60)
    print("\nStarting automated crawl of all Zoho products...")
    print("Configuration:")
    print("  - Products: CRM, Books, Inventory, Sign, SalesIQ, Desk, People")
    print("  - Max pages per product: 50 (optimized for speed)")
    print("  - Output: ../knowledge-base/")
    print("\nThis will take approximately 15-20 minutes...")
    print("="*60 + "\n")

    # Create crawler instance
    crawler = ZohoDocumentationCrawler(output_dir="../knowledge-base")

    # Run crawl with 50 pages per product (good balance)
    crawler.crawl_all_products(max_pages_per_product=50)

    print("\n" + "="*60)
    print("✅ Crawl Complete!")
    print("="*60)
    print(f"\nKnowledge base files created in: {crawler.output_dir.absolute()}")
    print("\nNext steps:")
    print("1. Review the generated .md files in knowledge-base/")
    print("2. Add aboutwater-specific documents (optional)")
    print("3. Proceed to OpenAI Assistant setup")
    print("\n")

if __name__ == "__main__":
    main()

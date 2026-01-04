#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive Zoho Knowledge Base Crawler
Crawls ALL articles from https://help.zoho.com/portal/en/kb
and all product-specific help centers
"""

import requests
from bs4 import BeautifulSoup
import html2text
import time
import os
from pathlib import Path
from urllib.parse import urljoin, urlparse
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class ZohoComprehensiveCrawler:
    """Comprehensive crawler for Zoho documentation across all products"""

    def __init__(self, output_dir="knowledge-base/crawled"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Setup session with retry strategy
        self.session = requests.Session()
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

        # HTML to Markdown converter
        self.h2t = html2text.HTML2Text()
        self.h2t.ignore_links = False
        self.h2t.ignore_images = True
        self.h2t.body_width = 0

        # Tracking
        self.crawled_urls = set()
        self.articles_saved = 0

        # Zoho products with their help URLs
        self.products = {
            'crm': [
                'https://www.zoho.com/crm/help/',
                'https://help.zoho.com/portal/en/kb/crm'
            ],
            'books': [
                'https://www.zoho.com/books/help/',
                'https://help.zoho.com/portal/en/kb/books'
            ],
            'inventory': [
                'https://www.zoho.com/inventory/help/',
                'https://help.zoho.com/portal/en/kb/inventory'
            ],
            'sign': [
                'https://www.zoho.com/sign/help/',
                'https://help.zoho.com/portal/en/kb/sign'
            ],
            'salesiq': [
                'https://www.zoho.com/salesiq/help/',
                'https://help.zoho.com/portal/en/kb/salesiq'
            ],
            'mail': [
                'https://www.zoho.com/mail/help/',
                'https://help.zoho.com/portal/en/kb/mail'
            ],
            'projects': [
                'https://www.zoho.com/projects/help/',
                'https://help.zoho.com/portal/en/kb/projects'
            ],
            'desk': [
                'https://www.zoho.com/desk/help/',
                'https://help.zoho.com/portal/en/kb/desk'
            ],
            'people': [
                'https://www.zoho.com/people/help/',
                'https://help.zoho.com/portal/en/kb/people'
            ],
            'recruit': [
                'https://www.zoho.com/recruit/help/',
                'https://help.zoho.com/portal/en/kb/recruit'
            ]
        }

    def fetch_page(self, url):
        """Fetch a page with error handling"""
        try:
            print(f"Fetching: {url}")
            response = self.session.get(url, timeout=30)
            response.encoding = response.apparent_encoding

            if response.status_code == 200:
                return response.text
            else:
                print(f"  Error: Status {response.status_code}")
                return None

        except Exception as e:
            print(f"  Error fetching {url}: {e}")
            return None

    def extract_article_links(self, html, base_url):
        """Extract article links from HTML"""
        if not html:
            return []

        soup = BeautifulSoup(html, 'html.parser')
        links = []

        # Find all links
        for link in soup.find_all('a', href=True):
            href = link['href']

            # Skip non-article links
            if any(skip in href for skip in ['#', 'javascript:', 'mailto:', '.pdf', '.zip']):
                continue

            # Make absolute URL
            absolute_url = urljoin(base_url, href)

            # Only include help/kb article URLs
            if any(pattern in absolute_url for pattern in ['/help/', '/kb/', 'help.zoho.com']):
                # Skip category/index pages
                if not absolute_url.endswith(('/help/', '/kb/', '/help', '/kb')):
                    links.append(absolute_url)

        return list(set(links))  # Remove duplicates

    def extract_article_content(self, html, url):
        """Extract main content from article page"""
        if not html:
            return None

        soup = BeautifulSoup(html, 'html.parser')

        # Try different content containers (Zoho uses various structures)
        content_selectors = [
            {'class': 'article-content'},
            {'class': 'help-content'},
            {'class': 'kb-article'},
            {'id': 'article-body'},
            {'id': 'content'},
            {'class': 'content'},
            {'role': 'main'},
            {'class': 'main-content'}
        ]

        content = None
        for selector in content_selectors:
            content = soup.find('div', selector) or soup.find('article', selector) or soup.find('main', selector)
            if content:
                break

        # Fallback: try to find largest text block
        if not content:
            # Look for divs with substantial text
            divs = soup.find_all('div')
            max_text = ""
            for div in divs:
                text = div.get_text(strip=True)
                if len(text) > len(max_text):
                    max_text = text
                    content = div

        if not content:
            return None

        # Remove script and style tags
        for script in content(["script", "style", "nav", "footer", "header"]):
            script.decompose()

        # Convert to markdown
        html_content = str(content)
        markdown = self.h2t.handle(html_content)

        # Clean up
        markdown = markdown.strip()

        # Validate content length
        if len(markdown) < 200:
            return None

        return markdown

    def save_article(self, content, url, product):
        """Save article to file"""
        if not content:
            return False

        # Create filename from URL
        parsed = urlparse(url)
        path_parts = [p for p in parsed.path.split('/') if p]

        if len(path_parts) > 0:
            filename = '_'.join(path_parts[-2:]) if len(path_parts) >= 2 else path_parts[-1]
            filename = filename.replace('.html', '').replace('.htm', '')
            filename = f"{product}_{filename}.md"
        else:
            filename = f"{product}_article_{self.articles_saved}.md"

        # Sanitize filename
        filename = "".join(c for c in filename if c.isalnum() or c in ('_', '-', '.'))

        filepath = self.output_dir / filename

        # Add metadata header
        header = f"# Zoho {product.title()} Article\n\n"
        header += f"**Source:** {url}\n"
        header += f"**Crawled:** {time.strftime('%Y-%m-%d')}\n\n"
        header += "---\n\n"

        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(header + content)

            self.articles_saved += 1
            print(f"  Saved: {filename}")
            return True

        except Exception as e:
            print(f"  Error saving {filename}: {e}")
            return False

    def crawl_product(self, product, urls, max_articles=100):
        """Crawl all articles for a specific product"""
        print(f"\n{'='*60}")
        print(f"Crawling {product.upper()}")
        print(f"{'='*60}")

        discovered_links = set()
        articles_found = 0

        # Discover article links from all product URLs
        for base_url in urls:
            if articles_found >= max_articles:
                break

            html = self.fetch_page(base_url)
            if html:
                links = self.extract_article_links(html, base_url)
                print(f"  Discovered {len(links)} links from {base_url}")
                discovered_links.update(links)

            time.sleep(1)  # Rate limiting

        # Crawl discovered article pages
        print(f"\nCrawling {len(discovered_links)} discovered articles...")

        for i, article_url in enumerate(discovered_links):
            if articles_found >= max_articles:
                print(f"  Reached max articles limit ({max_articles})")
                break

            if article_url in self.crawled_urls:
                continue

            print(f"\n[{i+1}/{min(len(discovered_links), max_articles)}] {article_url}")

            html = self.fetch_page(article_url)
            content = self.extract_article_content(html, article_url)

            if content:
                if self.save_article(content, article_url, product):
                    articles_found += 1
                    self.crawled_urls.add(article_url)
            else:
                print("  Skipped: No content extracted")

            time.sleep(2)  # Rate limiting

        print(f"\n{product.upper()}: Saved {articles_found} articles")
        return articles_found

    def crawl_all(self, max_articles_per_product=50):
        """Crawl all Zoho products"""
        print("="*60)
        print("COMPREHENSIVE ZOHO KNOWLEDGE BASE CRAWLER")
        print("="*60)
        print(f"Output directory: {self.output_dir.absolute()}")
        print(f"Max articles per product: {max_articles_per_product}")
        print(f"Total products: {len(self.products)}")

        start_time = time.time()

        for product, urls in self.products.items():
            self.crawl_product(product, urls, max_articles_per_product)

        # Summary
        elapsed = time.time() - start_time
        print(f"\n{'='*60}")
        print("CRAWL COMPLETE")
        print(f"{'='*60}")
        print(f"Total articles saved: {self.articles_saved}")
        print(f"Total URLs crawled: {len(self.crawled_urls)}")
        print(f"Time elapsed: {elapsed/60:.1f} minutes")
        print(f"Output directory: {self.output_dir.absolute()}")

        # Create index file
        self.create_index()

    def create_index(self):
        """Create index of all crawled articles"""
        index_file = self.output_dir / "README.md"

        files = sorted(self.output_dir.glob("*.md"))
        files = [f for f in files if f.name != "README.md"]

        content = "# Crawled Zoho Documentation\n\n"
        content += f"**Total Articles:** {len(files)}\n"
        content += f"**Crawled:** {time.strftime('%Y-%m-%d')}\n\n"
        content += "---\n\n"

        # Group by product
        by_product = {}
        for f in files:
            product = f.name.split('_')[0]
            if product not in by_product:
                by_product[product] = []
            by_product[product].append(f.name)

        for product in sorted(by_product.keys()):
            content += f"\n## {product.upper()}\n\n"
            content += f"**Articles:** {len(by_product[product])}\n\n"
            for filename in sorted(by_product[product]):
                content += f"- [{filename}](./{filename})\n"

        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"\nIndex created: {index_file}")


def main():
    """Main entry point"""
    print("Starting comprehensive Zoho KB crawler...")

    crawler = ZohoComprehensiveCrawler(
        output_dir="knowledge-base/crawled"
    )

    # Crawl all products (50 articles per product)
    crawler.crawl_all(max_articles_per_product=50)

    print("\nCrawling complete!")
    print(f"Check the output in: {crawler.output_dir.absolute()}")


if __name__ == "__main__":
    main()

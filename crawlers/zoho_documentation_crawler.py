"""
Zoho Documentation Crawler
Crawls Zoho help centers and documentation pages to create knowledge base
Supports multiple Zoho products and outputs clean Markdown files
"""

import requests
from bs4 import BeautifulSoup
import time
import json
import os
from urllib.parse import urljoin, urlparse
from typing import Set, List, Dict
import re
from pathlib import Path
import html2text
from datetime import datetime


class ZohoDocumentationCrawler:
    """
    Crawls Zoho documentation and converts to clean Markdown format
    """

    def __init__(self, output_dir: str = "../knowledge-base"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.visited_urls: Set[str] = set()
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })

        # Add retry strategy
        from requests.adapters import HTTPAdapter
        from urllib3.util.retry import Retry
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

        # HTML to Markdown converter
        self.html_converter = html2text.HTML2Text()
        self.html_converter.ignore_links = False
        self.html_converter.ignore_images = False
        self.html_converter.ignore_emphasis = False
        self.html_converter.body_width = 0  # Don't wrap lines
        self.html_converter.unicode_snob = True  # Better Unicode handling

        # Zoho products to crawl
        self.zoho_products = {
            'crm': {
                'base_url': 'https://help.zoho.com/portal/en/kb/crm',
                'name': 'Zoho CRM'
            },
            'books': {
                'base_url': 'https://help.zoho.com/portal/en/kb/books',
                'name': 'Zoho Books'
            },
            'inventory': {
                'base_url': 'https://help.zoho.com/portal/en/kb/inventory',
                'name': 'Zoho Inventory'
            },
            'sign': {
                'base_url': 'https://help.zoho.com/portal/en/kb/sign',
                'name': 'Zoho Sign'
            },
            'salesiq': {
                'base_url': 'https://help.zoho.com/portal/en/kb/salesiq',
                'name': 'Zoho SalesIQ'
            },
            'desk': {
                'base_url': 'https://help.zoho.com/portal/en/kb/desk',
                'name': 'Zoho Desk'
            },
            'people': {
                'base_url': 'https://help.zoho.com/portal/en/kb/people',
                'name': 'Zoho People'
            }
        }

    def is_valid_url(self, url: str, base_domain: str) -> bool:
        """Check if URL should be crawled"""
        parsed = urlparse(url)

        # Must be from Zoho help domain
        if 'help.zoho.com' not in parsed.netloc:
            return False

        # Skip non-documentation URLs
        skip_patterns = [
            '/community/', '/forum/', '/login', '/signup',
            '.pdf', '.zip', '.jpg', '.png', '.gif',
            '/search', '/contact'
        ]

        for pattern in skip_patterns:
            if pattern in url.lower():
                return False

        return True

    def clean_content(self, soup: BeautifulSoup) -> str:
        """Extract and clean main content from page"""

        # Remove unwanted elements
        for element in soup.find_all(['script', 'style', 'nav', 'footer', 'header', 'aside']):
            element.decompose()

        # Try to find main content area
        main_content = None

        # Common content selectors for Zoho help pages
        content_selectors = [
            'article',
            'div.article-content',
            'div.kb-article',
            'div.article-body',
            'main',
            'div.content'
        ]

        for selector in content_selectors:
            main_content = soup.select_one(selector)
            if main_content:
                break

        if not main_content:
            main_content = soup.find('body')

        return str(main_content) if main_content else ""

    def html_to_markdown(self, html_content: str) -> str:
        """Convert HTML to clean Markdown"""
        markdown = self.html_converter.handle(html_content)

        # Clean up excessive whitespace
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)

        # Remove excessive spaces
        lines = markdown.split('\n')
        cleaned_lines = [line.rstrip() for line in lines]
        markdown = '\n'.join(cleaned_lines)

        return markdown.strip()

    def crawl_page(self, url: str) -> Dict:
        """Crawl a single page and extract content"""

        if url in self.visited_urls:
            return None

        self.visited_urls.add(url)

        try:
            print(f"Crawling: {url}")
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            response.encoding = response.apparent_encoding  # Better encoding detection

            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract title with fallbacks
            title = soup.find('h1')
            if not title:
                title = soup.find('title')
            title_text = title.get_text(strip=True) if title else "Untitled"

            # Clean title
            title_text = re.sub(r'\s+', ' ', title_text).strip()

            # Extract and clean content
            html_content = self.clean_content(soup)
            if not html_content:
                print(f"  Warning: No content found on {url}")
                return None

            markdown_content = self.html_to_markdown(html_content)

            # Skip if content is too short (likely error page)
            if len(markdown_content.strip()) < 100:
                print(f"  Warning: Content too short, skipping {url}")
                return None

            # Extract internal links for further crawling
            links = []
            for link in soup.find_all('a', href=True):
                absolute_url = urljoin(url, link['href'])
                if self.is_valid_url(absolute_url, urlparse(url).netloc):
                    links.append(absolute_url)

            return {
                'url': url,
                'title': title_text,
                'content': markdown_content,
                'links': list(set(links))  # Remove duplicates
            }

        except requests.exceptions.RequestException as e:
            print(f"  Network error crawling {url}: {str(e)}")
            return None
        except Exception as e:
            print(f"  Error crawling {url}: {str(e)}")
            return None

    def crawl_product(self, product_key: str, max_pages: int = 100) -> List[Dict]:
        """Crawl documentation for a specific Zoho product"""

        product = self.zoho_products.get(product_key)
        if not product:
            print(f"Unknown product: {product_key}")
            return []

        print(f"\n{'='*60}")
        print(f"Crawling {product['name']}")
        print(f"{'='*60}\n")

        base_url = product['base_url']
        pages_to_crawl = [base_url]
        crawled_pages = []

        while pages_to_crawl and len(crawled_pages) < max_pages:
            url = pages_to_crawl.pop(0)

            if url in self.visited_urls:
                continue

            page_data = self.crawl_page(url)

            if page_data:
                crawled_pages.append(page_data)

                # Add new links to queue
                for link in page_data['links']:
                    if link not in self.visited_urls and link not in pages_to_crawl:
                        # Only add links from same product
                        if product_key in link or base_url in link:
                            pages_to_crawl.append(link)

            # Rate limiting
            time.sleep(1)

        print(f"\nCrawled {len(crawled_pages)} pages for {product['name']}")
        return crawled_pages

    def save_to_markdown(self, product_key: str, pages: List[Dict]):
        """Save crawled pages to a single Markdown file"""

        product = self.zoho_products.get(product_key)
        if not product or not pages:
            return

        output_file = self.output_dir / f"zoho-{product_key}.md"

        with open(output_file, 'w', encoding='utf-8') as f:
            # Write header
            f.write(f"# {product['name']} Documentation\n\n")
            f.write(f"Crawled on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"Total pages: {len(pages)}\n\n")
            f.write("---\n\n")

            # Write table of contents
            f.write("## Table of Contents\n\n")
            for i, page in enumerate(pages, 1):
                f.write(f"{i}. [{page['title']}](#{self._create_anchor(page['title'])})\n")
            f.write("\n---\n\n")

            # Write content
            for page in pages:
                f.write(f"## {page['title']}\n\n")
                f.write(f"Source: {page['url']}\n\n")
                f.write(page['content'])
                f.write("\n\n---\n\n")

        print(f"Saved to: {output_file}")

    def _create_anchor(self, text: str) -> str:
        """Create URL anchor from text"""
        anchor = text.lower()
        anchor = re.sub(r'[^\w\s-]', '', anchor)
        anchor = re.sub(r'[\s]+', '-', anchor)
        return anchor

    def save_metadata(self, product_key: str, pages: List[Dict]):
        """Save crawl metadata as JSON"""

        metadata_file = self.output_dir / f"zoho-{product_key}-metadata.json"

        metadata = {
            'product': product_key,
            'product_name': self.zoho_products[product_key]['name'],
            'crawl_date': datetime.now().isoformat(),
            'total_pages': len(pages),
            'pages': [
                {
                    'title': page['title'],
                    'url': page['url'],
                    'content_length': len(page['content'])
                }
                for page in pages
            ]
        }

        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)

        print(f"Metadata saved to: {metadata_file}")

    def crawl_all_products(self, max_pages_per_product: int = 100):
        """Crawl all configured Zoho products"""

        print(f"\nStarting crawl of all Zoho products")
        print(f"Max pages per product: {max_pages_per_product}\n")

        for product_key in self.zoho_products.keys():
            self.visited_urls.clear()  # Reset for each product

            pages = self.crawl_product(product_key, max_pages_per_product)

            if pages:
                self.save_to_markdown(product_key, pages)
                self.save_metadata(product_key, pages)

            print()  # Blank line between products


def main():
    """Main execution function"""

    print("Zoho Documentation Crawler")
    print("=" * 60)

    crawler = ZohoDocumentationCrawler(output_dir="../knowledge-base")

    # Interactive mode
    print("\nSelect crawl mode:")
    print("1. Crawl all products (recommended)")
    print("2. Crawl specific product")
    print("3. Test crawl (10 pages per product)")

    choice = input("\nEnter choice (1-3): ").strip()

    if choice == "1":
        max_pages = input("Max pages per product (default 100): ").strip()
        max_pages = int(max_pages) if max_pages else 100
        crawler.crawl_all_products(max_pages_per_product=max_pages)

    elif choice == "2":
        print("\nAvailable products:")
        for key, product in crawler.zoho_products.items():
            print(f"  - {key}: {product['name']}")

        product_key = input("\nEnter product key: ").strip()
        max_pages = input("Max pages (default 100): ").strip()
        max_pages = int(max_pages) if max_pages else 100

        pages = crawler.crawl_product(product_key, max_pages)
        if pages:
            crawler.save_to_markdown(product_key, pages)
            crawler.save_metadata(product_key, pages)

    elif choice == "3":
        print("\nRunning test crawl (10 pages per product)...")
        crawler.crawl_all_products(max_pages_per_product=10)

    else:
        print("Invalid choice")
        return

    print("\n" + "=" * 60)
    print("Crawl complete!")
    print(f"Output directory: {crawler.output_dir.absolute()}")


if __name__ == "__main__":
    main()

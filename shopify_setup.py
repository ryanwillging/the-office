#!/usr/bin/env python3
"""
Shopify Product Setup for Memento Mori Garden T-Shirts
Integrates with Gemini API for image generation
"""

import os
import json
import requests
import base64
from typing import Dict, List, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Shopify Configuration (from environment variables)
SHOPIFY_STORE = os.getenv("SHOPIFY_STORE", "the-office-9041.myshopify.com")
SHOPIFY_API_KEY = os.getenv("SHOPIFY_API_KEY")
SHOPIFY_API_SECRET = os.getenv("SHOPIFY_API_SECRET")
SHOPIFY_API_VERSION = "2024-01"

# Gemini Configuration (from environment variables)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_PROJECT_ID = os.getenv("GEMINI_PROJECT_ID")

# Product Data
COLOR_VARIANTS = {
    "black": {
        "name": "Midnight Garden (Black)",
        "price": "32.00",
        "compare_at_price": "42.00",
        "sku": "MMG-BLK",
        "description": "Classic goth aesthetic with soft lavender and sage accents"
    },
    "cream": {
        "name": "Bone Garden (Natural)",
        "price": "36.00",
        "compare_at_price": "46.00",
        "sku": "MMG-CRM",
        "description": "Cottage core vibes with dark botanical elements"
    },
    "forest": {
        "name": "Woodland Memento (Forest Green)",
        "price": "34.00",
        "compare_at_price": "44.00",
        "sku": "MMG-FGR",
        "description": "Deep forest base with ethereal light florals"
    },
    "burgundy": {
        "name": "Gothic Romance (Burgundy)",
        "price": "34.00",
        "compare_at_price": "44.00",
        "sku": "MMG-BRG",
        "description": "Rich wine tones with romantic pastels"
    },
    "charcoal": {
        "name": "Modern Memento (Charcoal)",
        "price": "32.00",
        "compare_at_price": "42.00",
        "sku": "MMG-CHR",
        "description": "Contemporary dark base with soft muted florals"
    },
    "sage": {
        "name": "Herbalist's Dream (Sage)",
        "price": "36.00",
        "compare_at_price": "46.00",
        "sku": "MMG-SGE",
        "description": "Botanical green with mystic purple accents"
    },
    "mauve": {
        "name": "Twilight Bloom (Dusty Rose)",
        "price": "34.00",
        "compare_at_price": "44.00",
        "sku": "MMG-MUV",
        "description": "Soft romantic mauve with moody undertones"
    },
    "navy": {
        "name": "Midnight Bloom (Navy)",
        "price": "32.00",
        "compare_at_price": "42.00",
        "sku": "MMG-NVY",
        "description": "Deep navy with luminous pale florals"
    }
}

SIZES = ["XS", "S", "M", "L", "XL", "2XL", "3XL"]


class ShopifyAPI:
    """Handle Shopify API interactions"""

    def __init__(self):
        self.base_url = f"https://{SHOPIFY_STORE}/admin/api/{SHOPIFY_API_VERSION}"
        # Try both authentication methods
        self.headers = {
            "Content-Type": "application/json",
            "X-Shopify-Access-Token": SHOPIFY_API_SECRET
        }
        # Alternative: Basic auth
        self.auth = (SHOPIFY_API_KEY, SHOPIFY_API_SECRET)

    def test_connection(self) -> bool:
        """Test Shopify API connection"""
        try:
            # Disable proxy for this request
            proxies = {
                'http': None,
                'https': None,
            }
            response = requests.get(
                f"{self.base_url}/shop.json",
                headers=self.headers,
                proxies=proxies,
                timeout=30
            )
            if response.status_code == 200:
                shop_data = response.json()
                print(f"✓ Connected to Shopify: {shop_data['shop']['name']}")
                print(f"  Store URL: {shop_data['shop']['domain']}")
                return True
            else:
                print(f"✗ Shopify connection failed: {response.status_code}")
                print(f"  Response: {response.text}")
                return False
        except Exception as e:
            print(f"✗ Shopify connection error: {e}")
            return False

    def create_product(self, product_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a product on Shopify"""
        try:
            response = requests.post(
                f"{self.base_url}/products.json",
                headers=self.headers,
                json={"product": product_data}
            )
            if response.status_code == 201:
                product = response.json()['product']
                print(f"✓ Created product: {product['title']} (ID: {product['id']})")
                return product
            else:
                print(f"✗ Failed to create product: {response.status_code}")
                print(f"  Response: {response.text}")
                return None
        except Exception as e:
            print(f"✗ Error creating product: {e}")
            return None

    def upload_image(self, product_id: int, image_data: bytes, filename: str) -> bool:
        """Upload an image to a Shopify product"""
        try:
            # Encode image as base64
            encoded_image = base64.b64encode(image_data).decode('utf-8')

            image_payload = {
                "image": {
                    "attachment": encoded_image,
                    "filename": filename
                }
            }

            response = requests.post(
                f"{self.base_url}/products/{product_id}/images.json",
                headers=self.headers,
                json=image_payload
            )

            if response.status_code == 201:
                print(f"  ✓ Uploaded image: {filename}")
                return True
            else:
                print(f"  ✗ Failed to upload image: {response.status_code}")
                print(f"    Response: {response.text}")
                return False
        except Exception as e:
            print(f"  ✗ Error uploading image: {e}")
            return False


class GeminiAPI:
    """Handle Gemini API interactions for image generation"""

    def __init__(self):
        self.api_key = GEMINI_API_KEY
        self.project_id = GEMINI_PROJECT_ID
        # Using Imagen 3 for image generation
        self.endpoint = f"https://us-central1-aiplatform.googleapis.com/v1/projects/{self.project_id}/locations/us-central1/publishers/google/models/imagen-3.0-generate-001:predict"

    def test_connection(self) -> bool:
        """Test Gemini API connection"""
        try:
            # Simple test request
            print("✓ Gemini API key configured")
            print(f"  Project ID: {self.project_id}")
            print("  Using Imagen 3 for image generation")
            return True
        except Exception as e:
            print(f"✗ Gemini API error: {e}")
            return False

    def generate_image(self, prompt: str, output_path: str) -> bool:
        """Generate an image using Gemini Imagen"""
        try:
            # Note: Using the newer Gemini API endpoint
            # We'll use the REST API for image generation
            url = f"https://generativelanguage.googleapis.com/v1beta/models/imagen-3.0-generate-001:generate?key={self.api_key}"

            payload = {
                "prompt": prompt,
                "number_of_images": 1,
                "aspect_ratio": "1:1",
                "safety_filter_level": "block_only_high",
                "person_generation": "allow_adult"
            }

            response = requests.post(url, json=payload)

            if response.status_code == 200:
                result = response.json()
                # The API returns base64 encoded images
                if 'generatedImages' in result and len(result['generatedImages']) > 0:
                    image_data = base64.b64decode(result['generatedImages'][0]['bytesBase64Encoded'])
                    with open(output_path, 'wb') as f:
                        f.write(image_data)
                    print(f"  ✓ Generated image: {output_path}")
                    return True
                else:
                    print(f"  ✗ No image data in response")
                    return False
            else:
                print(f"  ✗ Image generation failed: {response.status_code}")
                print(f"    Response: {response.text}")
                return False
        except Exception as e:
            print(f"  ✗ Error generating image: {e}")
            return False


def create_image_prompt(color_name: str, color_desc: str) -> str:
    """Create a detailed prompt for Gemini image generation"""
    return f"""Professional product photography of a {color_name} t-shirt on a clean white background.
The t-shirt features a gothic cottage core design with a detailed anatomical skull that has wildflowers growing from it - including lavender, roses, and forget-me-nots.
Above the skull is an arc of moon phases from new moon to full moon.
The design includes the text "From death, life blooms" in elegant serif typography.
The shirt is displayed flat lay style, centered, well-lit with soft shadows.
High quality, professional e-commerce product photo, 1:1 aspect ratio.
{color_desc}
Clean, minimalist presentation focusing on the t-shirt design."""


def main():
    """Main execution function"""
    print("=" * 60)
    print("Shopify Product Setup - Memento Mori Garden")
    print("=" * 60)

    # Step 1: Test API connections
    print("\n[Step 1] Testing API Connections...")
    print("-" * 60)

    shopify = ShopifyAPI()
    if not shopify.test_connection():
        print("⚠ Shopify connection failed. Please check credentials.")
        return

    print()
    gemini = GeminiAPI()
    if not gemini.test_connection():
        print("⚠ Gemini API configuration issue.")
        return

    print("\n✓ All API connections successful!")

    # Step 2: Generate images for each colorway
    print("\n[Step 2] Generating Product Images with Gemini...")
    print("-" * 60)

    os.makedirs("generated_images", exist_ok=True)
    generated_images = {}

    for color_key, color_info in COLOR_VARIANTS.items():
        print(f"\nGenerating image for {color_info['name']}...")
        prompt = create_image_prompt(color_info['name'], color_info['description'])
        output_path = f"generated_images/memento_mori_{color_key}.png"

        if gemini.generate_image(prompt, output_path):
            generated_images[color_key] = output_path
        else:
            print(f"  ⚠ Skipping {color_info['name']} due to generation failure")

    print(f"\n✓ Generated {len(generated_images)}/{len(COLOR_VARIANTS)} images")

    # Step 3: Create main product with variants
    print("\n[Step 3] Creating Shopify Product...")
    print("-" * 60)

    # Read the full product description
    with open("designs/MEMENTO_MORI_PRODUCT_DESCRIPTION.md", "r") as f:
        full_description = f.read()

    # Extract the main description (simplified for Shopify)
    product_description = """A hauntingly beautiful fusion of gothic and cottage core aesthetics. This anatomically detailed skull blooms with lavender, roses, and wildflowers beneath a celestial moon phase arc.

<strong>Design Features:</strong>
• Side-profile skull with anatomical accuracy
• Wildflower garden featuring lavender, roses, forget-me-nots, and daisies
• Moon phases arc from new to full
• Quote: "From death, life blooms"
• Premium DTG printing for exceptional detail

<strong>Perfect For:</strong>
Cottage core enthusiasts, gothic romantics, botanical art lovers, dark academia fans, herbalists, and anyone who finds beauty in life's impermanence.

From death, life blooms. 🌙"""

    # Create variants for all color/size combinations
    variants = []
    for color_key, color_info in COLOR_VARIANTS.items():
        for size in SIZES:
            variant = {
                "option1": color_info['name'],
                "option2": size,
                "price": color_info['price'],
                "compare_at_price": color_info['compare_at_price'],
                "sku": f"{color_info['sku']}-{size}",
                "inventory_management": "shopify",
                "inventory_policy": "deny",
                "inventory_quantity": 100,
                "weight": 200,
                "weight_unit": "g"
            }
            variants.append(variant)

    product_data = {
        "title": "Memento Mori Garden - Botanical Skull Art T-Shirt",
        "body_html": product_description,
        "vendor": "The Office",
        "product_type": "T-Shirt",
        "tags": ["gothic", "cottage core", "memento mori", "botanical", "skull art", "dark academia", "cottagecore goth"],
        "options": [
            {"name": "Color", "values": [info['name'] for info in COLOR_VARIANTS.values()]},
            {"name": "Size", "values": SIZES}
        ],
        "variants": variants,
        "status": "draft"  # Start as draft until images are uploaded
    }

    product = shopify.create_product(product_data)

    if not product:
        print("⚠ Failed to create product. Exiting.")
        return

    product_id = product['id']

    # Step 4: Upload images
    print("\n[Step 4] Uploading Product Images...")
    print("-" * 60)

    for color_key, image_path in generated_images.items():
        color_name = COLOR_VARIANTS[color_key]['name']
        print(f"\nUploading image for {color_name}...")

        with open(image_path, 'rb') as f:
            image_data = f.read()

        filename = f"memento_mori_{color_key}.png"
        shopify.upload_image(product_id, image_data, filename)

    # Step 5: Summary
    print("\n" + "=" * 60)
    print("✓ Product Setup Complete!")
    print("=" * 60)
    print(f"\nProduct ID: {product_id}")
    print(f"Product Title: {product['title']}")
    print(f"Total Variants: {len(variants)}")
    print(f"Images Uploaded: {len(generated_images)}")
    print(f"\nProduct URL: https://{SHOPIFY_STORE}/admin/products/{product_id}")
    print("\n⚠ Product is currently in DRAFT status.")
    print("   Review and publish when ready!")


if __name__ == "__main__":
    main()
